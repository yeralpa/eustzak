from data.taulak.izan.Izan import Izan
from data.enums import *
from data.exceptions import *
import pandas as pd

class AditzMintegia:
    def __init__(self) -> None:
        self.data = {
            Aditza.IZAN: Izan()
        }

    def search(self, aditza: str, modua: str, denbora: str, nor: str, nori: str, nork: str) -> str:
        pAditza = Aditza.fromString(aditza)
        if pAditza == Aditza.ERR:
            raise ParseException("aditza", aditza, "Aditza ez da existitzen! Ondo idatzi al duzu?")
        elif pAditza not in self.data.keys():
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

        # 2. Navegar por Modua y Denbora
        try:
            denboraClass = taulaType[pModua][pDenbora]
        except KeyError:
            raise NotFoundException("modua - denbora", f"Ez da konbinazioa topatu: {pModua} - {pDenbora}")

        print(nor, nori, nork)

        try:
            if isNori and isNork:
                out = denboraClass[pPertsonak[0]].at[pPertsonak[1], pPertsonak[2]]
            elif isNori:
                out = denboraClass.at[pPertsonak[0], pPertsonak[1]]
            elif isNork:
                out = denboraClass.at[pPertsonak[0], pPertsonak[2]]
            else:
                out = denboraClass[pPertsonak[0]]
        except (KeyError, AttributeError, IndexError):
            out = None

        if out is None or pd.isna(out):
            raise NotFoundException("aditza", f"Ez da aditza lortu! Datuak berrikusi eta, ondoren, egilearekin harremanean jarri.")

        return out