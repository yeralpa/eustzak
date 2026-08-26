import importlib
from pathlib import Path

from data.AditzaBase import AditzaBase
from data.enums import Aditza, Modua, Denbora, Pertsona
from data.exceptions import ParseException, NotImplementedException, InvalidCombinationException, NotFoundException

class AditzMintegia:
    def __init__(self) -> None:
        self.data: dict[Aditza, AditzaBase] = {}
        taulak_dir = Path(__file__).parent / "taulak"
        for folder in sorted(taulak_dir.iterdir()):
            if not folder.is_dir() or folder.name.startswith("_"):
                continue
            try:
                mod = importlib.import_module(f"data.taulak.{folder.name}.{folder.name.capitalize()}")
            except ImportError:
                continue
            for obj in vars(mod).values():
                if isinstance(obj, type) and issubclass(obj, AditzaBase) and obj is not AditzaBase and hasattr(obj, "key"):
                    self.data[obj.key] = obj()

    def search(self, aditza: str, modua: str, denbora: str, nor: str, nori: str, nork: str) -> str:
        pAditza = Aditza.fromString(aditza)
        if pAditza == Aditza.ERR:
            raise ParseException("aditza", aditza, "Aditza ez da existitzen! Ondo idatzi al duzu?")
        elif pAditza not in self.data:
            raise NotImplementedException("aditza", aditza)

        aditzaClass = self.data[pAditza]

        pModua = Modua.fromString(modua)
        if pModua == Modua.ERR:
            raise ParseException("modua", modua, "Modua ez da existitzen! Ondo idatzi al duzu?")
        
        pDenbora = Denbora.fromString(denbora)
        if pDenbora == Denbora.ERR:
            raise ParseException("denbora", denbora, "Denbora ez da existitzen! Ondo idatzi al duzu?")
        
        pertsonak = (nor, nori, nork)
        pPertsonak = Pertsona.fromTuple(pertsonak)
        if Pertsona.ERR in pPertsonak:
            raise ParseException("pertsona", pertsonak[pPertsonak.index(Pertsona.ERR)], "Pertsona ez da existitzen! Ondo idatzi al duzu?")
        elif not Pertsona.checkValid(pPertsonak):
            raise InvalidCombinationException(nor, nori, nork)
        
        isNori = pPertsonak[1] != Pertsona.NONE
        isNork = pPertsonak[2] != Pertsona.NONE

    
        if isNori and isNork:
            taulaType = aditzaClass.norNoriNork()
        elif isNori:
            taulaType = aditzaClass.norNori()
        elif isNork:
            taulaType = aditzaClass.norNork()
        else:
            taulaType = aditzaClass.nor()

        if taulaType is None:
            raise NotFoundException("mota", "Mota hau ez dago ezarrita aditza honentzat")

        try:
            denboraClass = taulaType[pModua][pDenbora]
        except KeyError:
            raise NotFoundException("modua - denbora", f"Ez da konbinazioa topatu: {pModua} - {pDenbora}")

        try:
            if isNori and isNork:
                out = denboraClass[pPertsonak[0]][pPertsonak[2]][pPertsonak[1]]
            elif isNori:
                out = denboraClass[pPertsonak[0]][pPertsonak[1]]
            elif isNork:
                out = denboraClass[pPertsonak[0]][pPertsonak[2]]
            else:
                out = denboraClass[pPertsonak[0]]
        except KeyError:
            out = None

        if out is None:
            raise NotFoundException("aditza", f"Ez da aditza lortu! Datuak berrikusi eta, ondoren, egilearekin harremaneman jarri.")

        return out