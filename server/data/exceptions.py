class AditzException(Exception):
    """Base class for all domain exceptions."""

class ParseException(AditzException):
    def __init__(self, what: str, get: str, msg: str) -> None:
        super().__init__(f"Ezin izan da '{get}' {what} bihurtu!\nMezua: {msg}")

class NotImplementedException(AditzException):
    def __init__(self, what: str, get: str) -> None:
        super().__init__(f"'{get}' {what} ez dago oraindik ezarrita!")

class InvalidCombinationException(AditzException):
    def __init__(self, nor: str, nori: str, nork: str) -> None:
        super().__init__(f"Pertsonen konbinazio baliogabea — NOR: {nor}, NORI: {nori}, NORK: {nork}")

class NotFoundException(AditzException):
    def __init__(self, what: str, msg: str) -> None:
        super().__init__(f"Ez da {what} topatu!\nMezua: {msg}")
