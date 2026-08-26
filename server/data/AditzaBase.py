from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from data.enums import Aditza

class AditzaBase(ABC):
    key: ClassVar["Aditza"]
    @abstractmethod
    def nor(self) -> dict | None: pass

    @abstractmethod
    def norNori(self) -> dict | None: pass

    @abstractmethod
    def norNork(self) -> dict | None: pass

    @abstractmethod
    def norNoriNork(self) -> dict | None: pass
