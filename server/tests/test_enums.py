import pytest
from data.enums import Pertsona, Modua, Denbora, Aditza


class TestPersonaFromString:
    def test_basic_lowercase(self):
        assert Pertsona.fromString("ni") == Pertsona.NI
        assert Pertsona.fromString("hura") == Pertsona.HURA
        assert Pertsona.fromString("gu") == Pertsona.GU
        assert Pertsona.fromString("zu") == Pertsona.ZU
        assert Pertsona.fromString("zuek") == Pertsona.ZUEK
        assert Pertsona.fromString("haiek") == Pertsona.HAIEK

    def test_uppercase_input(self):
        assert Pertsona.fromString("NI") == Pertsona.NI
        assert Pertsona.fromString("HURA") == Pertsona.HURA
        assert Pertsona.fromString("GU") == Pertsona.GU
        assert Pertsona.fromString("ZU") == Pertsona.ZU
        assert Pertsona.fromString("ZUEK") == Pertsona.ZUEK
        assert Pertsona.fromString("HAIEK") == Pertsona.HAIEK

    def test_aliases_ni(self):
        assert Pertsona.fromString("nik") == Pertsona.NI
        assert Pertsona.fromString("niri") == Pertsona.NI

    def test_aliases_hura(self):
        assert Pertsona.fromString("hark") == Pertsona.HURA
        assert Pertsona.fromString("hari") == Pertsona.HURA

    def test_aliases_gu(self):
        assert Pertsona.fromString("guk") == Pertsona.GU
        assert Pertsona.fromString("guri") == Pertsona.GU

    def test_aliases_zu(self):
        assert Pertsona.fromString("zuk") == Pertsona.ZU
        assert Pertsona.fromString("zuri") == Pertsona.ZU

    def test_aliases_zuek(self):
        assert Pertsona.fromString("zuei") == Pertsona.ZUEK

    def test_aliases_haiek(self):
        assert Pertsona.fromString("haiei") == Pertsona.HAIEK

    def test_none_variants(self):
        assert Pertsona.fromString("none") == Pertsona.NONE
        assert Pertsona.fromString("NONE") == Pertsona.NONE
        assert Pertsona.fromString("ezer") == Pertsona.NONE
        assert Pertsona.fromString("huts") == Pertsona.NONE
        assert Pertsona.fromString("") == Pertsona.NONE
        assert Pertsona.fromString(None) == Pertsona.NONE

    def test_unknown_returns_err(self):
        assert Pertsona.fromString("bera") == Pertsona.ERR
        assert Pertsona.fromString("eznazexistitzen") == Pertsona.ERR


class TestPersonaCheckValid:
    def test_nor_only_valid(self):
        assert Pertsona.checkValid((Pertsona.NI, Pertsona.NONE, Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.HURA, Pertsona.NONE, Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.GU, Pertsona.NONE, Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.ZU, Pertsona.NONE, Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.ZUEK, Pertsona.NONE, Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.HAIEK, Pertsona.NONE, Pertsona.NONE)) is True

    def test_nor_cannot_be_none(self):
        assert Pertsona.checkValid((Pertsona.NONE, Pertsona.NONE, Pertsona.NONE)) is False

    def test_nor_nori_invalid_pairs(self):
        assert Pertsona.checkValid((Pertsona.NI,   Pertsona.NI,   Pertsona.NONE)) is False
        assert Pertsona.checkValid((Pertsona.NI,   Pertsona.GU,   Pertsona.NONE)) is False
        assert Pertsona.checkValid((Pertsona.GU,   Pertsona.NI,   Pertsona.NONE)) is False
        assert Pertsona.checkValid((Pertsona.GU,   Pertsona.GU,   Pertsona.NONE)) is False
        assert Pertsona.checkValid((Pertsona.ZU,   Pertsona.ZU,   Pertsona.NONE)) is False
        assert Pertsona.checkValid((Pertsona.ZU,   Pertsona.ZUEK, Pertsona.NONE)) is False
        assert Pertsona.checkValid((Pertsona.ZUEK, Pertsona.ZU,   Pertsona.NONE)) is False
        assert Pertsona.checkValid((Pertsona.ZUEK, Pertsona.ZUEK, Pertsona.NONE)) is False

    def test_nor_nork_invalid_pairs(self):
        assert Pertsona.checkValid((Pertsona.NI,   Pertsona.NONE, Pertsona.NI))   is False
        assert Pertsona.checkValid((Pertsona.NI,   Pertsona.NONE, Pertsona.GU))   is False
        assert Pertsona.checkValid((Pertsona.GU,   Pertsona.NONE, Pertsona.NI))   is False
        assert Pertsona.checkValid((Pertsona.GU,   Pertsona.NONE, Pertsona.GU))   is False
        assert Pertsona.checkValid((Pertsona.ZU,   Pertsona.NONE, Pertsona.ZU))   is False
        assert Pertsona.checkValid((Pertsona.ZU,   Pertsona.NONE, Pertsona.ZUEK)) is False
        assert Pertsona.checkValid((Pertsona.ZUEK, Pertsona.NONE, Pertsona.ZU))   is False
        assert Pertsona.checkValid((Pertsona.ZUEK, Pertsona.NONE, Pertsona.ZUEK)) is False

    def test_nor_nori_valid_combinations(self):
        assert Pertsona.checkValid((Pertsona.HURA,  Pertsona.NI,   Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.NI,    Pertsona.HURA, Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.HAIEK, Pertsona.NI,   Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.HURA,  Pertsona.GU,   Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.HURA,  Pertsona.ZU,   Pertsona.NONE)) is True
        assert Pertsona.checkValid((Pertsona.HURA,  Pertsona.ZUEK, Pertsona.NONE)) is True

    def test_three_person_requires_hura_or_haiek_as_nor(self):
        assert Pertsona.checkValid((Pertsona.NI,    Pertsona.HURA, Pertsona.HURA)) is False
        assert Pertsona.checkValid((Pertsona.GU,    Pertsona.HURA, Pertsona.HURA)) is False
        assert Pertsona.checkValid((Pertsona.ZU,    Pertsona.HURA, Pertsona.HURA)) is False
        assert Pertsona.checkValid((Pertsona.ZUEK,  Pertsona.HURA, Pertsona.HURA)) is False
        assert Pertsona.checkValid((Pertsona.HURA,  Pertsona.NI,   Pertsona.HURA)) is True
        assert Pertsona.checkValid((Pertsona.HAIEK, Pertsona.HURA, Pertsona.NI))   is True


class TestPersonaForms:
    def test_nor_forms(self):
        assert Pertsona.NI.nor == "ni"
        assert Pertsona.HURA.nor == "hura"
        assert Pertsona.GU.nor == "gu"
        assert Pertsona.ZU.nor == "zu"
        assert Pertsona.ZUEK.nor == "zuek"
        assert Pertsona.HAIEK.nor == "haiek"
        assert Pertsona.NONE.nor == "NONE"

    def test_nori_forms(self):
        assert Pertsona.NI.nori == "niri"
        assert Pertsona.HURA.nori == "hari"
        assert Pertsona.GU.nori == "guri"
        assert Pertsona.ZU.nori == "zuri"
        assert Pertsona.ZUEK.nori == "zuei"
        assert Pertsona.HAIEK.nori == "haiei"
        assert Pertsona.NONE.nori == "NONE"

    def test_nork_forms(self):
        assert Pertsona.NI.nork == "nik"
        assert Pertsona.HURA.nork == "hark"
        assert Pertsona.GU.nork == "guk"
        assert Pertsona.ZU.nork == "zuk"
        assert Pertsona.ZUEK.nork == "zuek"
        assert Pertsona.HAIEK.nork == "haiek"
        assert Pertsona.NONE.nork == "NONE"


class TestModuaFromString:
    def test_indikatiboa(self):
        assert Modua.fromString("indikatiboa") == Modua.INDIKATIBOA
        assert Modua.fromString("INDIKATIBOA") == Modua.INDIKATIBOA

    def test_baldintza(self):
        assert Modua.fromString("baldintza") == Modua.BALDINTZA
        assert Modua.fromString("baldintzazkoa") == Modua.BALDINTZA

    def test_ahalera(self):
        assert Modua.fromString("ahalera") == Modua.AHALERA
        assert Modua.fromString("potentziala") == Modua.AHALERA

    def test_subjuntiboa(self):
        assert Modua.fromString("subjuntiboa") == Modua.SUBJUNTIBOA
        assert Modua.fromString("subjuntibera") == Modua.SUBJUNTIBOA
        assert Modua.fromString("subjuntiboera") == Modua.SUBJUNTIBOA

    def test_unknown_returns_err(self):
        assert Modua.fromString("unknown") == Modua.ERR


class TestDenboraFromString:
    def test_orain(self):
        assert Denbora.fromString("orain") == Denbora.ORAIN
        assert Denbora.fromString("orainaldia") == Denbora.ORAIN

    def test_lehen(self):
        assert Denbora.fromString("lehen") == Denbora.LEHEN
        assert Denbora.fromString("lehenaldia") == Denbora.LEHEN
        assert Denbora.fromString("iragana") == Denbora.LEHEN

    def test_alegiazkoa(self):
        assert Denbora.fromString("alegiazkoa") == Denbora.ALEGIAZKOA
        assert Denbora.fromString("alegia") == Denbora.ALEGIAZKOA
        assert Denbora.fromString("hipotetikoa") == Denbora.ALEGIAZKOA

    def test_unknown_returns_err(self):
        assert Denbora.fromString("unknown") == Denbora.ERR


class TestAditzaFromString:
    def test_izan(self):
        assert Aditza.fromString("izan") == Aditza.IZAN
        assert Aditza.fromString("IZAN") == Aditza.IZAN

    def test_unknown_returns_err(self):
        assert Aditza.fromString("edun") == Aditza.ERR
        assert Aditza.fromString("eznazexistitzen") == Aditza.ERR
