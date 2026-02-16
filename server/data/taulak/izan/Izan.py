from data.AditzaBase import AditzaBase
from data.taulak.izan.nor import nor_taula
from data.taulak.izan.nor_nori import nor_nori_taula
from data.taulak.izan.nor_nork import nor_nork_taula
from data.taulak.izan.nor_nori_nork import nor_nori_nork_taula

class Izan(AditzaBase):
    def __init__(self) -> None:
        super().__init__()
        self.__nTaula = nor_taula
        self.__nniTaula = nor_nori_taula
        self.__nnkTaula = nor_nork_taula
        self.__nninkTaula = nor_nori_nork_taula
    def nor(self) -> dict:
        return self.__nTaula

    def norNori(self) -> dict:
        return self.__nniTaula

    def norNork(self) -> dict:
        return self.__nnkTaula

    def norNoriNork(self) -> dict:
        return self.__nninkTaula