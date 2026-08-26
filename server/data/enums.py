from enum import Enum
from typing import Union, TypeVar, Type, List
from random import randint, choice

T = TypeVar('T', bound=Enum)
def randomEnum(clazz: Type[T], exclude: List[T] | None = None) -> T:
    choices = [m for m in clazz if m not in (exclude or [])]
    if not choices:
        raise ValueError("No valid enum members left after exclusion.")
    return choice(choices)

class Pertsona(Enum):
    ERR   = (-1, None,        None,           None)
    NONE  = (0,  None,        None,           None)
    NI    = (1,  "ni",        "niri",         "nik")
    HURA  = (3,  "hura",      "hari",         "hark")
    GU    = (4,  "gu",        "guri",         "guk")
    ZU    = (5,  "zu",        "zuri",         "zuk")
    ZUEK  = (6,  "zuek",      "zuei",         "zuek")
    HAIEK = (7,  "haiek",     "haiei",        "haiek")

    nor_form: str | None
    nori_form: str | None
    nork_form: str | None

    def __new__(cls, value, nor_form, nori_form, nork_form):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.nor_form = nor_form
        obj.nori_form = nori_form
        obj.nork_form = nork_form
        return obj

    @property
    def nor(self) -> str:
        return self.nor_form if self.nor_form else "NONE"

    @property
    def nori(self) -> str:
        return self.nori_form if self.nori_form else "NONE"

    @property
    def nork(self) -> str:
        return self.nork_form if self.nork_form else "NONE"

    @staticmethod
    def invalidPairs():
        return [
            (Pertsona.NI, Pertsona.NI), (Pertsona.NI, Pertsona.GU),
            (Pertsona.GU, Pertsona.NI), (Pertsona.GU, Pertsona.GU),
            (Pertsona.ZU, Pertsona.ZU), (Pertsona.ZU, Pertsona.ZUEK),
            (Pertsona.ZUEK, Pertsona.ZU), (Pertsona.ZUEK, Pertsona.ZUEK)
        ]

    @staticmethod
    def fromString(p: Union[None, str]) -> 'Pertsona':
        if p is None: return Pertsona.NONE
        p = p.lower().strip()
        if p in ["none", "ezer", "huts", ""]: return Pertsona.NONE
        for persona in Pertsona:
            if p == persona.nor_form or p == persona.nori_form or p == persona.nork_form:
                return persona
        return Pertsona.ERR
    
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
                out[1] = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
                out[2] = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            else: out[0] = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])

            if length == 2:
                out[randint(1, 2)] = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])

            if Pertsona.checkValid((out[0], out[1], out[2])):
                return out[0], out[1], out[2]


class Denbora(Enum):
    ERR        = (-1, None)
    NONE       = (0,  None)
    ORAIN      = (1,  "Orainaldia")
    LEHEN      = (2,  "Lehenaldia")
    ALEGIAZKOA = (3,  "Alegiazkoa")

    label: str | None

    def __new__(cls, value, label):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj

    @staticmethod
    def fromString(d: str) -> 'Denbora':
        d = d.lower()
        if d in ["orain", "orainaldia"]: return Denbora.ORAIN
        elif d in ["lehen", "lehenaldia", "iragana"]: return Denbora.LEHEN
        elif d in ["alegia", "alegiazkoa", "hipotetikoa"]: return Denbora.ALEGIAZKOA
        return Denbora.ERR

    @staticmethod
    def random() -> 'Denbora':
        return randomEnum(Denbora, [Denbora.ERR, Denbora.NONE])


class Modua(Enum):
    ERR         = (-1, None,           [])
    NONE        = (0,  None,           [])
    INDIKATIBOA = (1,  "Indikatiboa",  ["ORAIN", "LEHEN"])
    BALDINTZA   = (2,  "Baldintza",    ["ORAIN", "LEHEN", "ALEGIAZKOA"])
    AHALERA     = (3,  "Ahalera",      ["ORAIN", "LEHEN", "ALEGIAZKOA"])
    SUBJUNTIBOA = (4,  "Subjuntiboa",  ["ORAIN", "LEHEN"])
    AGINTERA    = (5,  "Agintera",     ["ORAIN"])

    label: str | None
    denbora_keys: list

    def __new__(cls, value, label, denbora_keys):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        obj.denbora_keys = denbora_keys
        return obj

    @property
    def denborak(self) -> list[Denbora]:
        return [Denbora[key] for key in self.denbora_keys]

    @staticmethod
    def fromString(m: str) -> 'Modua':
        m = m.lower()
        if m in ["indikatiboa"]: return Modua.INDIKATIBOA
        elif m in ["baldintza", "baldintzazkoa"]: return Modua.BALDINTZA
        elif m in ["ahalera", "potentziala"]: return Modua.AHALERA
        elif m in ["subjuntiboa", "subjuntibera", "subjuntiboera"]: return Modua.SUBJUNTIBOA
        elif m in ["agintera", "agintea", "agindua"]: return Modua.AGINTERA
        return Modua.ERR

    @staticmethod
    def random() -> 'Modua':
        return randomEnum(Modua, [Modua.ERR, Modua.NONE])


class Aditza(Enum):
    ERR  = (-1, None,   [])
    NONE = (0,  None,   [])
    IZAN  = (1,  "Izan",  ["nor", "nor-nori", "nor-nork", "nor-nori-nork"])
    EDUKI = (2,  "Eduki", ["nor-nork"])

    label: str | None
    motak: list

    def __new__(cls, value, label, motak):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        obj.motak = motak
        return obj

    @staticmethod
    def fromString(a: str) -> 'Aditza':
        a = a.lower()
        if a in ["izan"]: return Aditza.IZAN
        if a in ["eduki"]: return Aditza.EDUKI
        return Aditza.ERR

    @staticmethod
    def random() -> 'Aditza':
        return randomEnum(Aditza, [Aditza.ERR, Aditza.NONE])