from data.AditzaBase import AditzaBase
from data.taulak.eduki.nor_nork import nor_nork_taula
from data.enums import Aditza

class Eduki(AditzaBase):
    key = Aditza.EDUKI

    def __init__(self) -> None:
        super().__init__()
        self.__nnkTaula = nor_nork_taula


    def nor(self) -> dict | None:
        return None

    def norNori(self) -> dict | None:
        return None

    def norNork(self) -> dict:
        return self.__nnkTaula

    def norNoriNork(self) -> dict | None:
        return None