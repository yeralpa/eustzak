from data.taulak.builder import buildNorNork as __buildDF
from data.enums import Denbora, Modua


nor_nork_taula = {
    Modua.INDIKATIBOA: {
        Denbora.ORAIN: __buildDF(
            [None, "nau", None, "nauzu", "nauzue", "naute"],
            ["dut", "du", "dugu", "duzu", "duzue", "dute"],
            [None, "gaitu", None, "gaituzu", "gaituzue", "gaituzte"],
            ["zaitut", "zaitu", "zaitugu", None, None, "zaituzte"],
            ["zaituztet", "zaituzte", "zaituztegu", None, None, "zaituztete"],
            ["ditut", "ditu", "ditugu", "dituzu", "dituzue", "dituzte"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "ninduen", None, "ninduzun", "ninduzuen", "ninduten"],
            ["nuen", "zuen", "genuen", "zenuen", "zenuten", "zuten"],
            [None, "gintuen", None, "gintuzun", "gintuzuen", "gintuzten"],
            ["zintudan", "zintuen", "zintugun", None, None, "zintuzten"],
            ["zintuztedan", "zintuzten", "zintuztegun", None, None, "zintuzteten"],
            ["nituen", "zituen", "genituen", "zenituen", "zenituzten", "zituzten"]
        )
    },
    Modua.AHALERA: {
        Denbora.ORAIN: __buildDF(
            [None, "nazake", None, "nazakezu", "nazakezue", "nazakete"],
            ["dezaket", "dezake", "dezakegu", "dezakezu", "dezakezue", "dezakete"],
            [None, "gaitzake", None, "gaitzakezu", "gaitzakezue", "gaitzakete"],
            ["zaitzaket", "zaitzake", "zaitzakegu", None, None, "zaitzakete"],
            ["zaitzaketet", "zaitzakete", "zaitzaketegu", None, None, "zaitzaketete"],
            ["ditzaket", "ditzake", "ditzakegu", "ditzakezu", "ditzakezue", "ditzakete"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nintzakeen", None, "nintzakezun", "nintzakezuen", "nintzaketen"],
            ["nezakeen", "zezakeen", "genezakeen", "zenezakeen", "zenezaketen", "zezaketen"],
            [None, "gintzakeen", None, "gintzakezun", "gintzakezuen", "gintzaketen"],
            ["zintzakedan", "zintzakeen", "zintzakegun", None, None, "zintzaketen"],
            ["zintzaketedan", "zintzaketen", "zintzaketegun", None, None, "zintzaketeten"],
            ["nitzakeen", "zitzakeen", "genitzakeen", "zenitzakeen", "zenitzaketen", "zitzaketen"]
        ),
        Denbora.ALEGIAZKOA: __buildDF(
            [None, "nintzake", None, "nintzakezu", "nintzakezue", "nintzakete"],
            ["nezake", "lezake", "genezake", "zenezake", "zenezakete", "lezakete"],
            [None, "gintzake", None, "gintzakezu", "gintzakezue", "gintzakete"],
            ["zintzaket", "zintzake", "zintzakegu", None, None, "zintzakete"],
            ["zintzaketet", "zintzakete", "zintzaketegu", None, None, "zintzaketete"],
            ["nitzake", "litzake", "genitzake", "zenitzake", "zenitzakete", "litzakete"]
        )
    },
    Modua.BALDINTZA: {
        Denbora.ORAIN: __buildDF(
            [None, "banindu", None, "baninduzu", "baninduzue", "banindute"],
            ["banu", "balu", "bagenu", "bazenu", "bazenute", "balute"],
            [None, "bagintu", None, "bagintuzu", "bagintuzue", "bagintuzte"],
            ["bazintut", "bazintu", "bazintugu", None, None, "bazintuzte"],
            ["bazintuztet", "bazintuzte", "bazintuztegu", None, None, "bazintuztete"],
            ["banitu", "balitu", "bagenitu", "bazenitu", "bazenituzte", "balituzte"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nindukeen", None, "nindukezun", "nindukezuen", "ninduketen"],
            ["nukeen", "zukeen", "genukeen", "zenukeen", "zenuketen", "zuketen"],
            [None, "gintuzkeen", None, "gintuzkezun", "gintuzkezuen", "gintuzketen"],
            ["zintuzkedan", "zintuzkeen", "zintuzkegun", None, None, "zintuzketen"],
            ["zintuzketedan", "zintuzketen", "zintuzketegun", None, None, "zintuzketeten"],
            ["nituzkeen", "zituzkeen", "genituzkeen", "zenituzkeen", "zenituzketen", "zituzketen"]
        ),
        Denbora.ALEGIAZKOA: __buildDF(
            [None, "ninduke", None, "nindukezu", "nindukezue", "nindukete"],
            ["nuke", "luke", "genuke", "zenuke", "zenukete", "lukete"],
            [None, "gintuzke", None, "gintuzkezu", "gintuzkezue", "gintuzkete"],
            ["zintuzket", "zintuzke", "zintuzkegu", None, None, "zintuzkete"],
            ["zintuzketet", "zintuzkete", "zintuzketegu", None, None, "zintuzketete"],
            ["nituzke", "lituzke", "genituzke", "zenituzke", "zenituzkete", "lituzkete"]
        )
    },
    Modua.SUBJUNTIBOA: {
        Denbora.ORAIN: __buildDF(
            [None, "nazan", None, "nazazun", "nazazuen", "nazaten"],
            ["dezadan", "dezan", "dezagun", "dezazun", "dezazuen", "dezaten"],
            [None, "gaitzan", None, "gaitzazun", "gaitzazuen", "gaitzaten"],
            ["zaitzadan", "zaitzan", "zaitzagun", None, None, "zaitzaten"],
            ["zaitzatedan", "zaitzaten", "zaitzategun", None, None, "zaitzateten"],
            ["ditzadan", "ditzan", "ditzagun", "ditzazun", "ditzazuen", "ditzaten"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nintzan", None, "nintzazun", "nintzazuen", "nintzaten"],
            ["nezan", "zezan", "genezan", "zenezan", "zenezaten", "zezaten"],
            [None, "gintzan", None, "gintzazun", "gintzazuen", "gintzaten"],
            ["zintzadan", "zintzan", "zintzagun", None, None, "zintzaten"],
            ["zintzatedan", "zintzaten", "zintzategun", None, None, "zintzateten"],
            ["nitzan", "zitzan", "genitzan", "zenitzan", "zenitzaten", "zitzaten"]
        )
    }
}