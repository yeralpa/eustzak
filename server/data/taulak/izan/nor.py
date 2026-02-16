from data.taulak.builder import buildNor as __buildDF
from data.enums import Denbora, Modua

nor_taula = {
    Modua.INDIKATIBOA: {
        Denbora.ORAIN: __buildDF("naiz", "da", "gara", "zara", "zarete", "dira"),
        Denbora.LEHEN: __buildDF("nintzen", "zen", "ginen", "zinen", "zineten", "ziren")
    },
    Modua.AHALERA: {
        Denbora.ORAIN: __buildDF("naiteke", "daiteke", "gaitezke", "zaitezke", "zaitezkete", "daitezke"),
        Denbora.LEHEN: __buildDF("nintekeen", "zitekeen", "gintezkeen", "zintezkeen", "zintezketen", "zitezkeen"),
        Denbora.ALEGIAZKOA: __buildDF("ninteke", "liteke", "gintezke", "zintezke", "zintezkete", "litezke")
    },
    Modua.BALDINTZA: {
        Denbora.ORAIN: __buildDF("banintz", "balitz", "bagina", "bazina", "bazinate", "balira"),
        Denbora.LEHEN: __buildDF("nintzatekeen", "zatekeen", "ginatekeen", "zinatekeen", "zinateketen", "ziratekeen"),
        Denbora.ALEGIAZKOA: __buildDF("nintzateke", "litzateke", "ginateke", "zinateke", "zinatekete", "lirateke")
    },
    Modua.SUBJUNTIBOA: {
        Denbora.ORAIN: __buildDF("nadin", "dadin", "gaitezen", "zaitezen", "zaitezten", "daitezen"),
        Denbora.LEHEN: __buildDF("nendin", "zedin", "gintezen", "zintezen", "zintezten", "zitezen")
    }
}