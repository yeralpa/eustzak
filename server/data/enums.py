from enum import Enum
from typing import Union, cast
from .utils import randomEnum
from random import randint, choice

class Pertsona(Enum):
    ERR = -1
    NONE = 0
    NI = 1
    # HI = 2
    HURA = 3
    GU = 4
    ZU = 5
    ZUEK = 6
    HAIEK = 7

    @staticmethod
    def invalidPairs():
        return [
            (Pertsona.NI, Pertsona.NI), (Pertsona.NI, Pertsona.GU), 
            (Pertsona.GU, Pertsona.NI), (Pertsona.GU, Pertsona.GU), 
            (Pertsona.ZU, Pertsona.ZU), (Pertsona.ZU, Pertsona.ZUEK), 
            (Pertsona.ZUEK, Pertsona.ZU), (Pertsona.ZUEK, Pertsona.ZUEK)
        ]

    @staticmethod
    def fromString(p: Union[None, str]) -> Pertsona:
        if p is None: return Pertsona.NONE
        p = p.lower().strip()
        if p in ["none", "ezer", "huts", ""]: return Pertsona.NONE
        
        mapping = {
            "ni": Pertsona.NI, "nik": Pertsona.NI, "niri": Pertsona.NI,
            "hura": Pertsona.HURA, "hark": Pertsona.HURA, "hari": Pertsona.HURA,
            "gu": Pertsona.GU, "guk": Pertsona.GU, "guri": Pertsona.GU,
            "zu": Pertsona.ZU, "zuk": Pertsona.ZU, "zuri": Pertsona.ZU,
            "zuek": Pertsona.ZUEK, "zueki": Pertsona.ZUEK, "zuei": Pertsona.ZUEK,
            "haiek": Pertsona.HAIEK, "haiek": Pertsona.HAIEK, "haiei": Pertsona.HAIEK
        }
        return mapping.get(p, Pertsona.ERR)
    
    @staticmethod
    def fromTuple(it: tuple[str, str, str]) -> tuple[Pertsona, Pertsona, Pertsona]:
        return tuple(Pertsona.fromString(s) for s in it) # type: ignore
    
    @staticmethod
    def checkValid(t: tuple[Pertsona, Pertsona, Pertsona]) -> bool:
        nor, nori, nork = t
        if nor in [None, Pertsona.NONE, Pertsona.ERR]: 
            return False
        
        invalid = Pertsona.invalidPairs()

        if nori not in [None, Pertsona.NONE, Pertsona.ERR]: 
            if (t[0], t[1]) in invalid: return False
            
        if nork not in [None, Pertsona.NONE, Pertsona.ERR]: 
            if (t[0], t[2]) in invalid: return False

        # Check Nori vs Nork
        if (nori not in [None, Pertsona.NONE, Pertsona.ERR] and 
            nork not in [None, Pertsona.NONE, Pertsona.ERR]):
            if nor not in [Pertsona.HURA, Pertsona.HAIEK]: return False
            if (nori, nork) in invalid: return False

        return True

    @staticmethod
    def random() -> tuple[Pertsona, Pertsona, Pertsona]:
        while True:
            out: list[Pertsona] = [Pertsona.NONE, Pertsona.NONE, Pertsona.NONE]
            length = randint(1, 3)
            if length == 3: 
                out[0] = choice([Pertsona.HURA, Pertsona.HAIEK])
                out[2] = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            else: out[0] = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])

            if length == 2:
                out[randint(1, 2)] = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            elif length == 3:
                out[1] = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])

            if Pertsona.checkValid((out[0], out[1], out[2])):
                return out[0], out[1], out[2]


class Denbora(Enum):
    ERR = -1
    NONE = 0
    ORAIN = 1
    LEHEN = 2
    ALEGIAZKOA = 3

    @staticmethod
    def fromString(d: str) -> Denbora:
        d = d.lower()
        if d in ["orain", "orainaldia"]: return Denbora.ORAIN
        elif d in ["lehen", "lehenaldia", "iragana"]: return Denbora.LEHEN
        elif d in ["alegia", "alegiazkoa", "hipotetikoa"]: return Denbora.ALEGIAZKOA
        return Denbora.ERR#nbhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh                     hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    
    @staticmethod
    def random() -> Denbora:
        return randomEnum(Denbora, [Denbora.ERR, Denbora.NONE])

class Modua(Enum):
    ERR = -1
    NONE = 0
    INDIKATIBOA = 1
    BALDINTZA = 2
    AHALERA = 3
    SUBJUNTIBOA = 4

    @staticmethod
    def fromString(m: str) -> Modua:
        m = m.lower()
        if m in ["indikatiboa"]: return Modua.INDIKATIBOA
        elif m in ["baldintza", "baldintzazkoa"]: return Modua.BALDINTZA
        elif m in ["ahalera", "potentziala"]: return Modua.AHALERA
        elif m in ["subjuntiboa", "subjuntibera", "subjuntiboera"]: return Modua.SUBJUNTIBOA
        return Modua.ERR

    @staticmethod
    def random() -> Modua:
        return randomEnum(Modua, [Modua.ERR, Modua.NONE])

class Aditza(Enum):
    ERR = -1
    NONE = 0
    IZAN = 1
    
    @staticmethod
    def fromString(a: str) -> Aditza:
        a = a.lower()
        if a in ["izan"]: return Aditza.IZAN
        return Aditza.ERR
    
    @staticmethod
    def random() -> Aditza:
        return randomEnum(Aditza, [Aditza.ERR, Aditza.NONE])