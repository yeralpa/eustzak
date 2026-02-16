from data.taulak.builder import buildNorNori as __buildDF
from data.enums import Denbora, Modua

nor_nori_taula = {
    Modua.INDIKATIBOA: {
        Denbora.ORAIN: __buildDF(
            [None, "natzaio", None, "natzaizu", "natzaizue", "natzaie"],
            ["zait", "zaio", "zaigu", "zaizu", "zaizue", "zaie"],
            [None, "gatzaizkio", None, "gatzaizkizu", "gatzaizkizue", "gatzaizkie"],
            ["zatzaizkit", "zatzaizkio", "zatzaizkigu", None, None, "zatzaizkie"],
            ["zatzaizkidate", "zatzaizkiote", "zatzaizkigute", None, None, "zatzaizkiete"],
            ["zaizkit", "zaizkio", "zaizkigu", "zaizkizu", "zaizkizue", "zaizkie"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nintzaion", None, "nintzaizun", "nintzaizuen", "nintzaien"],
            ["zitzaidan", "zitzaion", "zitzaigun", "zitzaizun", "zitzaizuen", "zitzaien"],
            [None, "gintzaizkion", None, "gintzaizkizun", "gintzaizkizuen", "gintzaizkien"],
            ["zintzaizkidan", "zintzaizkion", "zintzaizkigun", None, None, "zintzaizkien"],
            ["zintzaizkidaten", "zintzaizkioten", "zintzaizkiguten", None, None, "zintzaizkieten"],
            ["zitzaizkidan", "zitzaizkion", "zitzaizkigun", "zitzaizkizun", "zitzaizkizuen", "zitzaizkien"]
        )
    },
    Modua.AHALERA: {
        Denbora.ORAIN: __buildDF(
            [None, "nakioke", None, "nakizuke", "nakizueke", "nakieke"],
            ["dakidake", "dakioke", "dakiguke", "dakizuke", "dakizueke", "dakieke"],
            [None, "gakizkioke", None, "gakizkizuke", "gakizkizueke", "gakizkieke"],
            ["zakizkidake", "zakizkioke", "zakizkiguke", None, None, "zakizkieke"],
            ["zakizkidakete", "zakizkiokete", "zakizkigukete", None, None, "zakizkiekete"],
            ["dakizkidake", "dakizkioke", "dakizkiguke", "dakizkizuke", "dakizkizueke", "dakizkieke"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nenkiokeen", None, "nenkizukeen", "nenkizuekeen", "nenkiekeen"],
            ["zekidakeen", "zekiokeen", "zekigukeen", "zekizukeen", "zekizuekeen", "zekiekeen"],
            [None, "genkizkiokeen", None, "genkizkizukeen", "genkizkizuekeen", "genkizkiekeen"],
            ["zenkizkidakeen", "zenkizkiokeen", "zenkizkigukeen", None, None, "zenkizkiekeen"],
            ["zenkizkidaketen", "zenkizkioketen", "zenkizkiguketen", None, None, "zenkizkieketen"],
            ["zekizkidakeen", "zekizkiokeen", "zekizkigukeen", "zekizkizukeen", "zekizkizuekeen", "zekizkiekeen"]
        ),
        Denbora.ALEGIAZKOA: __buildDF(
            [None, "nenkioke", None, "nenkizuke", "nenkizueke", "nenkieke"],
            ["lekidake", "lekioke", "lekiguke", "lekizuke", "lekizueke", "lekieke"],
            [None, "genkizkioke", None, "genkizkizuke", "genkizkizueke", "genkizkieke"],
            ["zenkizkidake", "zenkizkioke", "zenkizkiguke", None, None, "zenkizkieke"],
            ["zenkizkidakete", "zenkizkiokete", "zenkizkigukete", None, None, "zenkizkiekete"],
            ["lekizkidake", "lekizkioke", "lekizkiguke", "lekizkizuke", "lekizkizueke", "lekizkieke"]
        ),
    },
    Modua.BALDINTZA: {
        Denbora.ORAIN: __buildDF(
            [None, "banintzaio", None, "banintzaizu", "banintzaizue", "banintzaie"],
            ["balitzait", "balitzaio", "balitzaigu", "balitzaizu", "balitzaizue", "balitzaie"],
            [None, "bagintzaizkio", None, "bagintzaizkizu", "bagintzaizkizue", "bagintzaizkie"],
            ["bazintzaizkit", "bazintzaizkio", "bazintzaizkigu", None, None, "bazintzaizkie"],
            ["bazintzaizkidate", "bazintzaizkiote", "bazintzaizkigute", None, None, "bazintzaizkiete"],
            ["balitzaizkit", "balitzaizkio", "balitzaizkigu", "balitzaizkizu", "balitzaizkizue", "balitzaizkie"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nintzaiokeen", None, "nintzaizukeen", "nintzaizuekeen", "nintzaiekeen"],
            ["zitzaidakeen", "zitzaiokeen", "zitzaigukeen", "zitzaizukeen", "zitzaizuekeen", "zitzaiekeen"],
            [None, "gintzaizkiokeen", None, "gintzaizkizukeen", "gintzaizkizuekeen", "gintzaizkiekeen"],
            ["zintzaizkidakeen", "zintzaizkiokeen", "zintzaizkigukeen", None, None, "zintzaizkiekeen"],
            ["zintzaizkidaketen", "zintzaizkioketen", "zintzaizkiguketen", None, None, "zintzaizkieketen"],
            ["zitzaizkidakeen", "zitzaizkiokeen", "zitzaizkigukeen", "zitzaizkizukeen", "zitzaizkizuekeen", "zitzaizkiekeen"]
        ),
        Denbora.ALEGIAZKOA: __buildDF(
            [None, "nintzaioke", None, "nintzaizuke", "nintzaizueke", "nintzaieke"],
            ["litzaidake", "litzaioke", "litzaiguke", "litzaizuke", "litzaizueke", "litzaieke"],
            [None, "gintzaizkioke", None, "gintzaizkizuke", "gintzaizkizueke", "gintzaizkieke"],
            ["zintzaizkidake", "zintzaizkioke", "zintzaizkiguke", None, None, "zintzaizkieke"],
            ["zintzaizkidakete", "zintzaizkiokete", "zintzaizkigukete", None, None, "zintzaizkiekete"],
            ["litzaizkidake", "litzaizkioke", "litzaizkiguke", "litzaizkizuke", "litzaizkizueke", "litzaizkieke"]
        ),
    },
    Modua.SUBJUNTIBOA: {
        Denbora.ORAIN: __buildDF(
            [None, "nakion", None, "nakizun", "nakizuen", "nakien"],
            ["dakidan", "dakion", "dakigun", "dakizun", "dakizuen", "dakien"],
            [None, "gakizkion", None, "gakizkizun", "gakizkizuen", "gakizkien"],
            ["zakizkidan", "zakizkion", "zakizkigun", None, None, "zakizkien"],
            ["zakizkidaten", "zakizkioten", "zakizkiguten", None, None, "zakizkieten"],
            ["dakizkidan", "dakizkion", "dakizkigun", "dakizkizun", "dakizkizuen", "dakizkien"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nenkion", None, "nenkizun", "nenkizuen", "nenkien"],
            ["zekidan", "zekion", "zekigun", "zekizun", "zekizuen", "zekien"],
            [None, "genkizkion", None, "genkizkizun", "genkizkizuen", "genkizkien"],
            ["zenkizkidan", "zenkizkion", "zenkizkigun", None, None, "zenkizkien"],
            ["zenkizkidaten", "zenkizkioten", "zenkizkiguten", None, None, "zenkizkieten"],
            ["zekizkidan", "zekizkion", "zekizkigun", "zekizkizun", "zekizkizuen", "zekizkien"]
        )
    }
}