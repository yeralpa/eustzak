import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


class TestConjugationNorNori:
    def test_ni_zuei(self):
        # regression: axes were swapped, ni+zuei returned zuek+niri form
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=NI&nori=zuei")
        assert res.status_code == 200
        assert res.json()["aditza"] == "natzaizue"

    def test_ni_hari(self):
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=NI&nori=hari")
        assert res.status_code == 200
        assert res.json()["aditza"] == "natzaio"

    def test_hura_niri(self):
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=HURA&nori=niri")
        assert res.status_code == 200
        assert res.json()["aditza"] == "zait"

    def test_ni_hari_is_not_hura_niri(self):
        res_a = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=NI&nori=hari")
        res_b = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=HURA&nori=niri")
        assert res_a.json()["aditza"] != res_b.json()["aditza"]


class TestConjugation:
    def test_known_form(self):
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=NI")
        assert res.status_code == 200
        assert res.json()["aditza"] == "naiz"

    def test_known_form_hura(self):
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=HURA")
        assert res.status_code == 200
        assert res.json()["aditza"] == "da"

    def test_known_form_past(self):
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=LEHEN&nor=NI")
        assert res.status_code == 200
        assert res.json()["aditza"] == "nintzen"

    def test_invalid_combination_returns_422(self):
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=NI&nori=NI")
        assert res.status_code == 422

    def test_invalid_modua_denbora_combo_returns_404(self):
        # INDIKATIBOA has no ALEGIAZKOA
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ALEGIAZKOA&nor=NI")
        assert res.status_code == 404

    def test_unknown_aditza_returns_422(self):
        res = client.get("/conjugation?aditza=EDUN&modua=INDIKATIBOA&denbora=ORAIN&nor=NI")
        assert res.status_code == 422

    def test_unknown_person_returns_422(self):
        res = client.get("/conjugation?aditza=IZAN&modua=INDIKATIBOA&denbora=ORAIN&nor=BERA")
        assert res.status_code == 422


class TestConjugationRandom:
    def test_returns_expected_keys(self):
        res = client.get("/conjugation/random")
        assert res.status_code == 200
        data = res.json()
        assert data["success"] is True
        for key in ("infinitiboa", "modua", "denbora", "nor", "nori", "nork", "aditza"):
            assert key in data

    def test_aditza_is_string(self):
        res = client.get("/conjugation/random")
        assert isinstance(res.json()["aditza"], str)
        assert len(res.json()["aditza"]) > 0


class TestConjugationsRandom:
    def test_default_returns_five(self):
        res = client.get("/conjugations/random")
        assert res.status_code == 200
        assert len(res.json()["items"]) == 5

    def test_custom_count(self):
        res = client.get("/conjugations/random?n=3")
        assert res.status_code == 200
        assert len(res.json()["items"]) == 3

    def test_count_capped_at_20(self):
        res = client.get("/conjugations/random?n=99")
        assert res.status_code == 200
        assert len(res.json()["items"]) == 20

    def test_minimum_count_is_1(self):
        res = client.get("/conjugations/random?n=0")
        assert res.status_code == 200
        assert len(res.json()["items"]) == 1

    def test_each_item_has_expected_keys(self):
        res = client.get("/conjugations/random?n=1")
        item = res.json()["items"][0]
        for key in ("infinitiboa", "modua", "denbora", "nor", "nori", "nork", "aditza"):
            assert key in item


class TestTable:
    def test_returns_full_structure(self):
        res = client.get("/table?aditza=IZAN&nor=NI")
        assert res.status_code == 200
        data = res.json()
        assert data["success"] is True
        assert data["infinitiboa"] == "IZAN"
        assert "aditzak" in data

    def test_table_has_all_modes(self):
        res = client.get("/table?aditza=IZAN&nor=NI")
        aditzak = res.json()["aditzak"]
        for modua in ("indikatiboa", "baldintza", "ahalera", "subjuntiboa"):
            assert modua in aditzak

    def test_indikatiboa_has_no_alegiazkoa(self):
        res = client.get("/table?aditza=IZAN&nor=NI")
        indikatiboa = res.json()["aditzak"]["indikatiboa"]
        assert "alegiazkoa" not in indikatiboa

    def test_baldintza_has_alegiazkoa(self):
        res = client.get("/table?aditza=IZAN&nor=NI")
        baldintza = res.json()["aditzak"]["baldintza"]
        assert "alegiazkoa" in baldintza

    def test_nor_only_correct_values(self):
        res = client.get("/table?aditza=IZAN&nor=NI")
        aditzak = res.json()["aditzak"]
        assert aditzak["indikatiboa"]["orain"] == "naiz"
        assert aditzak["indikatiboa"]["lehen"] == "nintzen"

    def test_invalid_combination_returns_422(self):
        res = client.get("/table?aditza=IZAN&nor=NI&nori=NI")
        assert res.status_code == 422

    def test_unknown_aditza_returns_422(self):
        res = client.get("/table?aditza=EDUN&nor=NI")
        assert res.status_code == 422


class TestTableRandom:
    def test_returns_expected_keys(self):
        res = client.get("/table/random")
        assert res.status_code == 200
        data = res.json()
        assert data["success"] is True
        for key in ("infinitiboa", "nor", "nori", "nork", "aditzak"):
            assert key in data

    def test_aditzak_is_nested_dict(self):
        res = client.get("/table/random")
        aditzak = res.json()["aditzak"]
        assert isinstance(aditzak, dict)
        for modua in aditzak.values():
            assert isinstance(modua, dict)
