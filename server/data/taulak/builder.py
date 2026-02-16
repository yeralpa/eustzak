from pandas import Series, DataFrame as df
from data.enums import Pertsona


def buildNor(ni, hura, gu, zu, zuek, haiek):
    return Series([ni, hura, gu, zu, zuek, haiek], 
                  index = [Pertsona.NI, Pertsona.HURA, Pertsona.GU, Pertsona.ZU, Pertsona.ZUEK, Pertsona.HAIEK])

def buildNorNork(ni, hura, gu, zu, zuek, haiek):
    return df({ # Nor
            Pertsona.NI: ni, Pertsona.HURA: hura, Pertsona.GU: gu,
            Pertsona.ZU: zu, Pertsona.ZUEK: zuek, Pertsona.HAIEK: haiek
        }, index = [Pertsona.NI, Pertsona.HURA, Pertsona.GU, Pertsona.ZU, Pertsona.ZUEK, Pertsona.HAIEK]) # Nik

def buildNorNori(ni, hura, gu, zu, zuek, haiek):
    return df({ # Nor
            Pertsona.NI: ni, Pertsona.HURA: hura, Pertsona.GU: gu,
            Pertsona.ZU: zu, Pertsona.ZUEK: zuek, Pertsona.HAIEK: haiek
        }, index = [Pertsona.NI, Pertsona.HURA, Pertsona.GU, Pertsona.ZU, Pertsona.ZUEK, Pertsona.HAIEK]) # Niri

def buildNorNoriNork(niri, hari, guri, zuri, zuei, haiei):
    return df({ # Niri
            Pertsona.NI: niri, Pertsona.HURA: hari, Pertsona.GU: guri,
            Pertsona.ZU: zuri, Pertsona.ZUEK: zuei, Pertsona.HAIEK: haiei
        }, index = [Pertsona.NI, Pertsona.HURA, Pertsona.GU, Pertsona.ZU, Pertsona.ZUEK, Pertsona.HAIEK]) # Nork