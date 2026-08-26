from data.enums import Pertsona

_P = [p for p in Pertsona if p not in (Pertsona.NONE, Pertsona.ERR)]

def buildNor(ni, hura, gu, zu, zuek, haiek):
    return dict(zip(_P, [ni, hura, gu, zu, zuek, haiek]))

def buildNorNori(ni, hura, gu, zu, zuek, haiek):
    # columns = NOR, rows = NORI  →  {NOR: {NORI: value}}
    return {nor: dict(zip(_P, nori_vals)) for nor, nori_vals in zip(_P, [ni, hura, gu, zu, zuek, haiek])}

def buildNorNork(ni, hura, gu, zu, zuek, haiek):
    # columns = NOR, rows = NORK  →  {NOR: {NORK: value}}
    return {nor: dict(zip(_P, nork_vals)) for nor, nork_vals in zip(_P, [ni, hura, gu, zu, zuek, haiek])}

def buildNorNoriNork(niri, hari, guri, zuri, zuei, haiei):
    # args are per-NORI lists of NORK values  →  {NORK: {NORI: value}}
    cols = [niri, hari, guri, zuri, zuei, haiei]
    return {
        nork: {nori: cols[j][i] for j, nori in enumerate(_P)}
        for i, nork in enumerate(_P)
    }