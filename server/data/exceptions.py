
class ParseException(Exception):
    def __init__(self, what: str, get: str, msg: str) -> None:
        super().__init__(f"Ezin izan da {get} {what} bihurtu! \n Mezua: {msg}")

class NotImplementedException(Exception):
    def __init__(self, what: str, get: str) -> None:
        super().__init__(f"Ezin izan da {get} erabili {what} ez baitago oraindik ezarrita!")

class InvalidCombinationException(Exception):
    def __init__(self, nor: str, nori: str, nork: str) -> None:
        super().__init__(f"Ezin izan da pertsonen konbinazio hau erabili. NOR: {nor}. NORI: {nori}. NORK: {nork}.")

class NotFoundException(Exception):
    def __init__(self, what: str, msg: str) -> None:
        super().__init__(f"Ez da {what} topatu! \n Mezua: {msg}")