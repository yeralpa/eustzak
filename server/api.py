from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from data.mintegia import AditzMintegia
from data.enums import *

app = FastAPI()
mintegia = AditzMintegia()

# Configuración necesaria para que React pueda conectar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Limitar a el dominio
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://medium.com/@abhaysingh71711/fastapi-explained-build-scalable-and-async-apis-with-python-24883f747b65

@app.get("/search")
async def search_aditza(aditza: str, modua: str, denbora: str, 
                         nor: str = "NONE", nori: str = "NONE", nork: str = "NONE"):
    try:
        resultado = mintegia.search(aditza, modua, denbora, nor, nori, nork)
        return {"success": True, "aditza": resultado}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/random")
async def random_aditza():
    try:
        aditza: Aditza = Aditza.random()

        while True:
            modua = Modua.random()
            denbora = Denbora.random()
            
            if not (modua not in [Modua.BALDINTZA, Modua.AHALERA] and denbora == Denbora.ALEGIAZKOA):
                break

        nor, nori, nork = Pertsona.random()
        
        res = mintegia.search(aditza.name, modua.name, denbora.name, nor.name, 
                                    nori.name, nork.name)
        return {"success": True, 
                "ifinitiboa": aditza.name,
                "modua": modua.name,
                "denbora": denbora.name,
                "nor": nor.name,
                "nori": nori.name,
                "nork": nork.name,
                "aditza": res} # resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/bulkRandom")
async def bulkd_random_aditza():
    try:
        aditza: Aditza = Aditza.random()

        while True:
            modua = Modua.random()
            denbora = Denbora.random()
            
            if not (modua not in [Modua.BALDINTZA, Modua.AHALERA] and denbora == Denbora.ALEGIAZKOA):
                break
        
        nor, nori, nork = Pertsona.random()

        aditzak = {}
        for modua in [Modua.INDIKATIBOA, Modua.BALDINTZA, Modua.AHALERA, Modua.SUBJUNTIBOA]:
            moduaDict = {}
            for denbora in [Denbora.ORAIN, Denbora.LEHEN, Denbora.ALEGIAZKOA]:
                if denbora == Denbora.ALEGIAZKOA and modua in [Modua.INDIKATIBOA, Modua.SUBJUNTIBOA]:
                    continue
                moduaDict[denbora.name.lower()] = mintegia.search(aditza.name, modua.name, denbora.name, nor.name, 
                                    nori.name, nork.name)
                
            aditzak[modua.name.lower()] = moduaDict
        
        return {"success": True, 
                "infinitiboa": aditza.name,
                "nor": nor.name,
                "nori": nori.name,
                "nork": nork.name,
                "aditzak": aditzak} # resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

app.setup()