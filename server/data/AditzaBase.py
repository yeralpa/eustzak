from abc import abstractmethod, ABC

class AditzaBase(ABC):
    @abstractmethod
    def nor(self) -> dict: pass

    @abstractmethod
    def norNori(self) -> dict: pass

    @abstractmethod
    def norNork(self) -> dict: pass

    @abstractmethod
    def norNoriNork(self) -> dict: pass