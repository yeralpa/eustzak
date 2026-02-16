from data.taulak.builder import buildNorNoriNork as __buildDF
from data.enums import Denbora, Modua, Pertsona

nor_nori_nork_taula = {
    Modua.INDIKATIBOA: {
        Denbora.ORAIN: {
            Pertsona.HURA: __buildDF(
                [None, "dit", None, "didazu", "didazue", "didate"],
                ["diot", "dio", "diogu", "diozu", "diozue", "diote"],
                [None, "digu", None, "diguzu", "diguzue", "digute"],
                ["dizut", "dizu", "dizugu", None, None, "dizute"],
                ["dizuet", "dizue", "dizuegu", None, None, "dizuete"],
                ["diet", "die", "diegu", "diezu", "diezue", "diete"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "dizkit", None, "dizkidazu", "dizkidazue", "dizkidate"],
                ["dizkiot", "dizkio", "dizkiogu", "dizkiozu", "dizkiozue", "dizkiote"],
                [None, "dizkigu", None, "dizkiguzu", "dizkiguzue", "dizkigute"],
                ["dizkizut", "dizkizu", "dizkizugu", None, None, "dizkizute"],
                ["dizkizuet", "dizkizue", "dizkizuegu", None, None, "dizkizuete"],
                ["dizkiet", "dizkie", "dizkiegu", "dizkiezu", "dizkiezue", "dizkiete"]
            )
        },
        Denbora.LEHEN: {
            Pertsona.HURA: __buildDF(
                [None, "zidan", None, "zenidan", "zenidaten", "zidaten"],
                ["nion", "zion", "genion", "zenion", "zenioten", "zioten"],
                [None, "zigun", None, "zenigun", "zeniguten", "ziguten"],
                ["nizun", "zizun", "genizun", None, None, "zizuten"],
                ["nizuen", "zizuen", "genizuen", None, None, "zizueten"],
                ["nien", "zien", "genien", "zenien", "zenieten", "zieten"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "zizkidan", None, "zenizkidan", "zenizkidaten", "zizkidaten"],
                ["nizkion", "zizkion", "genizkion", "zenizkion", "zenizkioten", "zizkioten"],
                [None, "zizkigun", None, "zenizkigun", "zenizkiguten", "zizkiguten"],
                ["nizkizun", "zizkizun", "genizkizun", None, None, "zizkizuten"],
                ["nizkizuen", "zizkizuen", "genizkizuen", None, None, "zizkizueten"],
                ["nizkien", "zizkien", "genizkien", "zenizkien", "zenizkieten", "zizkieten"]
            )
        }
    },
    Modua.AHALERA: {
        Denbora.ORAIN: {
            Pertsona.HURA: __buildDF(
                [None, "diezadake", None, "diezadakezu", "diezadakezue", "diezadakete"],
                ["diezaioket", "diezaioke", "diezaiokegu", "diezaiokezu", "diezaiokezue", "diezaiokete"],
                [None, "diezaguke", None, "diezagukezu", "diezagukezue", "diezagukete"],
                ["diezazuket", "diezazuke", "diezazukegu", None, None, "diezazukete"],
                ["diezazueket", "diezazueke", "diezazuekegu", None, None, "diezazuekete"],
                ["diezaieket", "diezaieke", "diezaiekegu", "diezaiekezu", "diezaiekezue", "diezaiekete"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "diezazkidake", None, "diezazkidakezu", "diezazkidakezue", "diezazkidakete"],
                ["diezazkioket", "diezazkioke", "diezazkiokegu", "diezazkiokezu", "diezazkiokezue", "diezazkiokete"],
                [None, "diezazkiguke", None, "diezazkigukezu", "diezazkigukezue", "diezazkigukete"],
                ["diezazkizuket", "diezazkizuke", "diezazkizukegu", None, None, "diezazkizukete"],
                ["diezazkizueket", "diezazkizueke", "diezazkizuekegu", None, None, "diezazkizuekete"],
                ["diezazkieket", "diezazkieke", "diezazkiekegu", "diezazkiekezu", "diezazkiekezue", "diezazkiekete"]
            )
        },
        Denbora.LEHEN: {
            Pertsona.HURA: __buildDF(
                [None, "ziezadakeen", None, "zeniezadakeen", "zeniezadaketen", "ziezadaketen"],
                ["niezaiokeen", "ziezaiokeen", "geniezaiokeen", "zeniezaiokeen", "zeniezaioketen", "ziezaioketen"],
                [None, "ziezagukeen", None, "zeniezagukeen", "zeniezaguketen", "ziezaguketen"],
                ["niezazukeen", "ziezazukeen", "geniezazukeen", None, None, "ziezazuketen"],
                ["niezazuekeen", "ziezazuekeen", "geniezazuekeen", None, None, "ziezazueketen"],
                ["niezaiekeen", "ziezaiekeen", "geniezaiekeen", "zeniezaiekeen", "zeniezaieketen", "ziezaieketen"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "ziezazkidakeen", None, "zeniezazkidakeen", "zeniezazkidaketen", "ziezazkidaketen"],
                ["niezazkiokeen", "ziezazkiokeen", "geniezazkiokeen", "zeniezazkiokeen", "zeniezazkioketen", "ziezazkioketen"],
                [None, "ziezazkigukeen", None, "zeniezazkigukeen", "zeniezazkiguketen", "ziezazkiguketen"],
                ["niezazkizukeen", "ziezazkizukeen", "geniezazkizukeen", None, None, "ziezazkizuketen"],
                ["niezazkizuekeen", "ziezazkizuekeen", "geniezazkizuekeen", None, None, "ziezazkizueketen"],
                ["niezazkiekeen", "ziezazkiekeen", "geniezazkiekeen", "zeniezazkiekeen", "zeniezazkieketen", "ziezazkieketen"]
            )
        },
        Denbora.ALEGIAZKOA: {
            Pertsona.HURA: __buildDF(
                [None, "liezadake", None, "zeniezadake", "zeniezadakete", "liezadakete"],
                ["niezaioke", "liezaioke", "geniezaioke", "zeniezaioke", "zeniezaiokete", "liezaiokete"],
                [None, "liezaguke", None, "zeniezaguke", "zeniezagukete", "liezagukete"],
                ["niezazuke", "liezazuke", "geniezazuke", None, None, "liezazukete"],
                ["niezazueke", "liezazueke", "geniezazueke", None, None, "liezazuekete"],
                ["niezaieke", "liezaieke", "geniezaieke", "zeniezaieke", "zeniezaiekete", "liezaiekete"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "liezazkidake", None, "zeniezazkidake", "zeniezazkidakete", "liezazkidakete"],
                ["niezazkioke", "liezazkioke", "geniezazkioke", "zeniezazkioke", "zeniezazkiokete", "liezazkiokete"],
                [None, "liezazkiguke", None, "zeniezazkiguke", "zeniezazkigukete", "liezazkigukete"],
                ["niezazkizuke", "liezazkizuke", "geniezazkizuke", None, None, "liezazkizukete"],
                ["niezazkizueke", "liezazkizueke", "geniezazkizueke", None, None, "liezazkizuekete"],
                ["niezazkieke", "liezazkieke", "geniezazkieke", "zeniezazkieke", "zeniezazkiekete", "liezazkiekete"]
            )
        }
    },
    Modua.BALDINTZA: {
        Denbora.ORAIN: {
            Pertsona.HURA: __buildDF(
                [None, "balit", None, "bazenit", "bazenidate", "balidate"],
                ["banio", "balio", "bagenio", "Bazenio", "bazeniote", "baliote"],
                [None, "baligu", None, "bazenigu", "bazenigute", "baligute"],
                ["banizu", "balizu", "bagenizu", None, None, "balizute"],
                ["banizue", "balizue", "bagenizue", None, None, "balizuete"],
                ["banie", "balie", "bagenie", "bazenie", "bazeniete", "baliete"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "balizkit", None, "bazenizkit", "bazenizkidate", "balizkidate"],
                ["banizkio", "balizkio", "bagenizkio", "bazenizkio", "bazenizkiote", "balizkiote"],
                [None, "balizkigu", None, "bazenizkigu", "bazenizkigute", "balizkigute"],
                ["banizkizu", "balizkizu", "bagenizkizu", None, None, "balizkizute"],
                ["banizkizue", "balizkizue", "bagenizkizue", None, None, "balizkizuete"],
                ["banizkie", "balizkie", "bagenizkie", "bazenizkie", "bazenizkiete", "balizkiete"]
            )
        },
        Denbora.LEHEN: {
            Pertsona.HURA: __buildDF(
                [None, "zidakeen", None, "zenidakeen", "zenidaketen", "zidaketen"],
                ["niokeen", "ziokeen", "geniokeen", "zeniokeen", "zenioketen", "zioketen"],
                [None, "zigukeen", None, "zenigukeen", "zeniguketen", "ziguketen"],
                ["nizukeen", "zizukeen", "genizukeen", None, None, "zizuketen"],
                ["nizuekeen", "zizuekeen", "genizuekeen", None, None, "zizueketen"],
                ["niekeen", "ziekeen", "geniekeen", "zeniekeen", "zenieketen", "zieketen"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "zizkidakeen", None, "zenizkidakeen", "zenizkidaketen", "zizkidaketen"],
                ["nizkiokeen", "zizkiokeen", "genizkiokeen", "zenizkiokeen", "zenizkioketen", "zizkioketen"],
                [None, "zizkigukeen", None, "zenizkigukeen", "zenizkiguketen", "zizkiguketen"],
                ["nizkizukeen", "zizkizukeen", "genizkizukeen", None, None, "zizkizuketen"],
                ["nizkizuekeen", "zizkizuekeen", "genizkizuekeen", None, None, "zizkizueketen"],
                ["nizkiekeen", "zizkiekeen", "genizkiekeen", "zenizkiekeen", "zenizkieketen", "zizkieketen"]
            )
        },
        Denbora.ALEGIAZKOA: {
            Pertsona.HURA: __buildDF(
                [None, "lidake", None, "zenidake", "zenidakete", "lidakete"],
                ["nioke", "lioke", "genioke", "zenioke", "zeniokete", "liokete"],
                [None, "liguke", None, "zeniguke", "zenigukete", "ligukete"],
                ["nizuke", "lizuke", "genizuke", None, None, "lizukete"],
                ["nizueke", "lizueke", "genizueke", None, None, "lizuekete"],
                ["nieke", "lieke", "genieke", "zenieke", "zeniekete", "liekete"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "lizkidake", None, "zenizkidake", "zenizkidakete", "lizkidakete"],
                ["nizkioke", "lizkioke", "genizkioke", "zenizkioke", "zenizkiokete", "lizkiokete"],
                [None, "lizkiguke", None, "zenizkiguke", "zenizkigukete", "lizkigukete"],
                ["nizkizuke", "lizkizuke", "genizkizuke", None, None, "lizkizukete"],
                ["nizkizueke", "lizkizueke", "genizkizueke", None, None, "lizkizuekete"],
                ["nizkieke", "lizkieke", "genizkieke", "zenizkieke", "zenizkiekete", "lizkiekete"]
            )
        }
    },
    Modua.SUBJUNTIBOA: {
        Denbora.ORAIN: {
            Pertsona.HURA: __buildDF(
                [None, "diezadan", None, "diezadazun", "diezadazuen", "diezadaten"],
                ["diezaiodan", "diezaion", "diezaiogun", "diezaiozun", "diezaiozuen", "diezaioten"],
                [None, "diezagun", None, "diezaguzun", "diezaguzuen", "diezaguten"],
                ["diezazudan", "diezazun", "diezazugun", None, None, "diezazuten"],
                ["diezazuedan", "diezazuen", "diezazuegun", None, None, "diezazueten"],
                ["diezaiedan", "diezaien", "diezaiegun", "diezaiezun", "diezaiezuen", "diezaieten"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "diezazkidan", None, "diezazkidazun", "diezazkidazuen", "diezazkidaten"],
                ["diezazkiodan", "diezazkion", "diezazkiogun", "diezazkiozun", "diezazkiozuen", "diezazkioten"],
                [None, "diezazkigun", None, "diezazkiguzun", "diezazkiguzuen", "diezazkiguten"],
                ["diezazkizudan", "diezazkizun", "diezazkizugun", None, None, "diezazkizuten"],
                ["diezazkizuedan", "diezazkizuen", "diezazkizuegun", None, None, "diezazkizueten"],
                ["diezazkiedan", "diezazkien", "diezazkiegun", "diezazkiezun", "diezazkiezuen", "diezazkieten"]
            )
        },
        Denbora.LEHEN: {
            Pertsona.HURA: __buildDF(
                [None, "ziezadan", None, "zeniezadan", "zeniezadaten", "ziezadaten"],
                ["niezaion", "ziezaion", "geniezaion", "zeniezaion", "zeniezaioten", "ziezaioten"],
                [None, "ziezagun", None, "zeniezagun", "zeniezaguten", "ziezaguten"],
                ["niezazun", "ziezazun", "geniezazun", None, None, "ziezazuten"],
                ["niezazuen", "ziezazuen", "geniezazuen", None, None, "ziezazueten"],
                ["niezaien", "ziezaien", "geniezaien", "zeniezaien", "zeniezaieten", "ziezaieten"]
            ),
            Pertsona.HAIEK: __buildDF(
                [None, "ziezazkidan", None, "zeniezazkidan", "zeniezazkidaten", "ziezazkidaten"],
                ["niezazkion", "ziezazkion", "geniezazkion", "zeniezazkion", "zeniezazkioten", "ziezazkioten"],
                [None, "ziezazkigun", None, "zeniezazkigun", "zeniezazkiguten", "ziezazkiguten"],
                ["niezazkizun", "ziezazkizun", "geniezazkizun", None, None, "ziezazkizuten"],
                ["niezazkizuen", "ziezazkizuen", "geniezazkizuen", None, None, "ziezazkizueten"],
                ["niezazkien", "ziezazkien", "geniezazkien", "zeniezazkien", "zeniezazkieten", "ziezazkieten"]
            )
        }
    }
}
