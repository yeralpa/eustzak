import logging
import os
from random import choice

from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from data.enums import Aditza, Denbora, Modua, Pertsona
from data.exceptions import (
    AditzException,
    InvalidCombinationException,
    NotFoundException,
    NotImplementedException,
    ParseException,
)
from data.mintegia import AditzMintegia
from data.utils import mota_from_pertsonak, random_pertsonak_from_mota

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s\t%(name)s\t%(message)s")
logger = logging.getLogger(__name__)

_ALL_PERTSONAK   = [p for p in Pertsona if p not in (Pertsona.ERR, Pertsona.NONE)]
_NOR_NORI_NOR    = [Pertsona.HURA, Pertsona.HAIEK]  # valid NOR for nor-nori-nork
_MODUAK          = [m for m in Modua if m not in (Modua.ERR, Modua.NONE)]

app      = FastAPI(title="Eustzak API", version="1.0.0")
mintegia = AditzMintegia()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(ParseException,              lambda _, exc: JSONResponse(status_code=422, content={"detail": str(exc)}))
app.add_exception_handler(InvalidCombinationException, lambda _, exc: JSONResponse(status_code=422, content={"detail": str(exc)}))
app.add_exception_handler(NotFoundException,           lambda _, exc: JSONResponse(status_code=404, content={"detail": str(exc)}))
app.add_exception_handler(NotImplementedException,     lambda _, exc: JSONResponse(status_code=501, content={"detail": str(exc)}))





def _require_aditza(aditza: str) -> Aditza:
    parsed = Aditza.fromString(aditza)
    if parsed == Aditza.ERR:
        raise ParseException("aditza", aditza, "Aditza ez da topatu! Ondo idatzi al duzu?")
    return parsed

def _require_pertsonak(nor: str, nori: str, nork: str) -> tuple[Pertsona, Pertsona, Pertsona]:
    pertsonak = Pertsona.fromTuple((nor, nori, nork))
    if Pertsona.ERR in pertsonak:
        idx = list(pertsonak).index(Pertsona.ERR)
        raise ParseException("pertsona", (nor, nori, nork)[idx], "Pertsona ez da topatu! Ondo idatzi al duzu?")
    if not Pertsona.checkValid(pertsonak):
        raise InvalidCombinationException(nor, nori, nork)
    return pertsonak





def _get_form(aditza_name: str, modua: Modua, denbora: Denbora,
              nor: Pertsona, nori: Pertsona, nork: Pertsona) -> str | None:
    try:
        return mintegia.search(aditza_name, modua.name, denbora.name, nor.name, nori.name, nork.name)
    except AditzException:
        return None

def _build_table(aditza_name: str, nor_name: str, nori_name: str, nork_name: str) -> dict:
    nor  = Pertsona.fromString(nor_name)
    nori = Pertsona.fromString(nori_name)
    nork = Pertsona.fromString(nork_name)
    return {
        modua.name.lower(): {
            denbora.name.lower(): _get_form(aditza_name, modua, denbora, nor, nori, nork)
            for denbora in modua.denborak
        }
        for modua in _MODUAK
    }

def _build_full_table(aditza_name: str, mota: str) -> dict:
    def slice(modua: Modua, denbora: Denbora) -> dict:
        # Skip invalid combos
        def get(nor: Pertsona, nori: Pertsona = Pertsona.NONE, nork: Pertsona = Pertsona.NONE) -> str | None:
            return _get_form(aditza_name, modua, denbora, nor, nori, nork) if Pertsona.checkValid((nor, nori, nork)) else None

        if mota == "nor":
            return {p.nor: get(p) for p in _ALL_PERTSONAK}
        if mota == "nor-nori":
            return {nor.nor: {nori.nori: get(nor, nori=nori) for nori in _ALL_PERTSONAK} for nor in _ALL_PERTSONAK}
        if mota == "nor-nork":
            return {nor.nor: {nork.nork: get(nor, nork=nork) for nork in _ALL_PERTSONAK} for nor in _ALL_PERTSONAK}

        return {
            nor.nor: {
                nork.nork: {nori.nori: get(nor, nori, nork) for nori in _ALL_PERTSONAK}
                for nork in _ALL_PERTSONAK
            }
            for nor in _NOR_NORI_NOR
        }

    return {
        modua.name.lower(): {
            denbora.name.lower(): slice(modua, denbora) 
            for denbora in modua.denborak
        }
        for modua in _MODUAK
    }





def _random_item(pool: list[Aditza] | None = None) -> dict:
    aditza = choice(pool) if pool else Aditza.random()
    while True:
        modua  = Modua.random()
        denbora = Denbora.random()
        if denbora not in modua.denborak:
            continue
        nor, nori, nork = Pertsona.random()
        if mota_from_pertsonak(nori, nork) not in aditza.motak:
            continue
        try:
            res = mintegia.search(aditza.name, modua.name, denbora.name, nor.name, nori.name, nork.name)
        except AditzException:
            continue
        return {
            "infinitiboa": aditza.name,
            "modua":       modua.name,
            "denbora":     denbora.name,
            "nor":         nor.nor,
            "nori":        nori.nori,
            "nork":        nork.nork,
            "aditza":      res,
        }






@app.get("/conjugation")
async def conjugation(aditza: str, modua: str, denbora: str,
                      nor: str = "NONE", nori: str = "NONE", nork: str = "NONE"):
    logger.info("Requested conjugation: {} - {} {} - {} {} {}".format(aditza, modua, denbora, nor, nori, nork))
    resultado = mintegia.search(aditza, modua, denbora, nor, nori, nork)
    return {"success": True, "aditza": resultado}

@app.get("/conjugation/random")
async def conjugation_random():
    logger.info("Requested random conjugation")
    return {"success": True, **_random_item()}

@app.get("/conjugations/random")
async def conjugations_random(
    n: int = 5,
    aditzak: str | None = Query(default=None, description="Comma-separated aditz names to include"),
):
    logger.info("Requested random conjugation from aditzak: {}".format(aditzak))
    pool: list[Aditza] | None = None
    if aditzak:
        parsed = [Aditza.fromString(a.strip()) for a in aditzak.split(",")]
        pool   = [a for a in parsed if a not in (Aditza.ERR, Aditza.NONE)]
        if not pool:
            raise ParseException("aditzak", aditzak, "Aditza baliogabeak")
    items = [_random_item(pool) for _ in range(max(1, min(n, 20)))]
    return {"success": True, "items": items}

@app.get("/table")
async def table(aditza: str, nor: str, nori: str = "NONE", nork: str = "NONE"):
    logger.info("Requested table for aditza {}, (nor, nori, nork) = ({}, {}, {})".format(aditza, nor, nori, nork))
    pAditza         = _require_aditza(aditza)
    pNor, pNori, pNork = _require_pertsonak(nor, nori, nork)
    mota = mota_from_pertsonak(pNori, pNork)
    if mota not in pAditza.motak:
        raise NotImplementedException("mota", mota)
    return {
        "success":     True,
        "infinitiboa": pAditza.name,
        "nor":         pNor.nor,
        "nori":        pNori.nori,
        "nork":        pNork.nork,
        "aditzak":     _build_table(pAditza.name, pNor.name, pNori.name, pNork.name),
    }

@app.get("/table/random")
async def table_random(aditza: str | None = None):
    logger.info("Requested random table for aditza {}".format(aditza))
    pAditza         = _require_aditza(aditza) if aditza else Aditza.random()
    mota            = choice(pAditza.motak)
    nor, nori, nork = random_pertsonak_from_mota(mota)
    return await table(pAditza.name, nor.name, nori.name, nork.name)

@app.get("/meta")
async def meta():
    logger.info("Requested meta information")
    return {
        "aditzak": [
            {"value": a.name, "label": a.label, "motak": a.motak}
            for a in Aditza if a not in (Aditza.ERR, Aditza.NONE)
        ],
        "moduak": [
            {
                "value":    m.name.lower(),
                "label":    m.label,
                "denborak": [{"value": d.name.lower(), "label": d.label} for d in m.denborak],
            }
            for m in Modua if m not in (Modua.ERR, Modua.NONE)
        ],
        "pertsonak": [
            {"value": p.name, "nor": p.nor, "nori": p.nori, "nork": p.nork}
            for p in Pertsona if p not in (Pertsona.ERR, Pertsona.NONE)
        ],
    }

@app.get("/full-table")
async def full_table(aditza: str, mota: str):
    logger.info("Requested full table of aditza {}".format(aditza))
    pAditza = _require_aditza(aditza)
    if mota not in pAditza.motak:
        raise NotImplementedException("mota", mota)
    return {"success": True, "mota": mota, "aditza": pAditza.name,
            "data": _build_full_table(pAditza.name, mota)}
