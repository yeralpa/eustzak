from .enums import Pertsona

def mota_from_pertsonak(pNori: Pertsona, pNork: Pertsona) -> str:
    isNori = pNori != Pertsona.NONE
    isNork = pNork != Pertsona.NONE
    if isNori and isNork: return "nor-nori-nork"
    if isNori:            return "nor-nori"
    if isNork:            return "nor-nork"
    return "nor"

def random_pertsonak_from_mota(mota: str) -> tuple[Pertsona, Pertsona, Pertsona]:
    from .enums import randomEnum
    while True:
        if mota == "nor":
            nor = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            nori, nork = Pertsona.NONE, Pertsona.NONE
        elif mota == "nor-nori":
            nor  = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            nori = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            nork = Pertsona.NONE
        elif mota == "nor-nork":
            nor  = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            nork = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            nori = Pertsona.NONE
        else:  # nor-nori-nork
            nor  = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            nori = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
            nork = randomEnum(Pertsona, [Pertsona.ERR, Pertsona.NONE])
        if Pertsona.checkValid((nor, nori, nork)):
            return nor, nori, nork
