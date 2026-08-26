from data.taulak.builder import buildNorNork as __buildDF
from data.enums import Denbora, Modua


nor_nork_taula = {
    Modua.INDIKATIBOA: {
        Denbora.ORAIN: __buildDF(
            [None, "nauka", None, "naukazu", "naukazue", "naukate"],
            ["daukat", "dauka", "daukagu", "daukazu", "daukazue", "daukate"],
            [None, "gauzka", None, "gauzkazu", "gauzkazue", "gauzkate"],
            ["zauzkat", "zauzka", "zauzkagu", None, None, "zauzkate"],
            ["zauzkatet", "zauzkate", "zauzkategu", None, None, "zauzkatete"],
            ["dauzkat", "dauzka", "dauzkagu", "dauzkazu", "dauzkazue", "dauzkate"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nindukan", None, "nindukazun", "nindukazuen", "nindukaten"],
            ["neukan", "zeukan", "geneukan", "zeneukan", "zeneukaten", "zeukaten"],
            [None, "ginduzkan", None, "ginduzkazun", "ginduzkazuen", "ginduzkaten"],
            ["zeuzkadan", "zeuzkan", "zeuzkagun", None, None, "zeuzkaten"],
            ["zeuzkatedan", "zeuzkaten", "zeuzkategun", None, None, "zeuzkateten"],
            ["neuzkan", "zeuzkan", "geneuzkan", "zeneuzkan", "zeneuzkaten", "zeuzkaten"]
        )
    },
    Modua.AHALERA: {
        Denbora.ORAIN: __buildDF(
            [None, "naukake", None, "naukakezu", "naukakezue", "naukakete"],
            ["daukaket", "daukake", "daukakegu", "daukakezu", "daukakezue", "daukakete"],
            [None, "gauzkake", None, "gauzkakezu", "gauzkakezue", "gauzkakete"],
            ["zauzkaket", "zauzkake", "zauzkakegu", None, None, "zauzkakete"],
            ["zauzkaketet", "zauzkakete", "zauzkaketegu", None, None, "zauzkaketete"],
            ["dauzkaket", "dauzkake", "dauzkakegu", "dauzkakezu", "dauzkakezue", "dauzkakete"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nindukakeen", None, "nindukakezun", "nindukakezuen", "nindukaketen"],
            ["neukakeen", "zeukakeen", "geneukakeen", "zeneukakeen", "zeneukaketen", "zeukaketen"],
            [None, "ginduzkakeen", None, "ginduzkakezun", "ginduzkakezuen", "ginduzkaketen"],
            ["zinduzkakedan", "zindukakeen", "zinduzkakegun", None, None, "zinduzkaketen"],
            ["zinduzkaketedan", "zindukaketen", "zinduzkaketegun", None, None, "zinduzkaketeten"],
            ["neuzkakeen", "zeuzkakeen", "geneuzkakeen", "zeneuzkakeen", "zeneuzkaketen", "zeuzkaketen"]
        ),
        Denbora.ALEGIAZKOA: __buildDF(
            [None, "nindukake", None, "nindukakezu", "nindukakezue", "nindukakete"],
            ["neukake", "zeukake", "geneukake", "zeneukake", "zeneukakete", "zeukakete"],
            [None, "ginduzkake", None, "ginduzkakezu", "ginduzkakezue", "ginduzkakete"],
            ["zinduzkaket", "zinduzkake", "zinduzkakegu", None, None, "zinduzkakete"],
            ["zinduzkaketet", "zinduzkakete", "zinduzkaketegu", None, None, "zinduzkaketete"],
            ["neuzkake", "zeuzkake", "geneuzkake", "zeneuzkake", "zeneuzkakete", "zeuzkakete"]
        )
    },
    Modua.BALDINTZA: {
        Denbora.ORAIN: __buildDF(
            [None, "baninduka", None, "banindukazu", "banindukazue", "banindukate"],
            ["baneuka", "bazeuka", "bageneuka", "bazeneuka", "bazeneukate", "bazeukate"],
            [None, "baginduzka", None, "baginduzkazu", "baginduzkazue", "baginduzkate"],
            ["bazeuzkat", "bazeuzka", "bazeuzkagu", None, None, "bazeuzkate"],
            ["bazeuzkatet", "bazeuzkate", "bazeuzkategu", None, None, "bazeuzkatete"],
            ["baneuzka", "bazeuzka", "bageneuzka", "bazeneuzka", "bazeneuzkate", "bazeuzkate"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nindukakeen", None, "nindukakezun", "nindukakezuen", "nindukaketen"],
            ["neukakeen", "zeukakeen", "geneukakeen", "zeneukakeen", "zeneukaketen", "zeukaketen"],
            [None, "ginduzkakeen", None, "ginduzkakezun", "ginduzkakezuen", "ginduzkaketen"],
            ["zeuzkakedan", "zeuzkakeen", "zeuzkakegun", None, None, "zeuzkaketen"],
            ["zeuzkaketedan", "zeuzkaketen", "zeuzkaketegun", None, None, "zeuzkaketeten"],
            ["neuzkakeen", "zeuzkakeen", "geneuzkakeen", "zeneuzkakeen", "zeneuzkaketen", "zeuzkaketen"]
        ),
        Denbora.ALEGIAZKOA: __buildDF(
            [None, "nindukake", None, "nindukakezu", "nindukakezue", "nindukakete"],
            ["neukake", "zeukake", "geneukake", "zeneukake", "zeneukakete", "zeukakete"],
            [None, "ginduzkake", None, "ginduzkakezu", "ginduzkakezue", "ginduzkakete"],
            ["zeuzkaket", "zeuzkake", "zeuzkakegu", None, None, "zeuzkakete"],
            ["zeuzkaketet", "zeuzkakete", "zeuzkaketegu", None, None, "zeuzkaketete"],
            ["neuzkake", "zeuzkake", "geneuzkake", "zeneuzkake", "zeneuzkakete", "zeuzkakete"]
        )
    },
    Modua.SUBJUNTIBOA: {
        Denbora.ORAIN: __buildDF(
            [None, "naukan", None, "naukazun", "naukazuen", "naukaten"],
            ["daukadan", "daukan", "daukagun", "daukazun", "daukazuen", "daukaten"],
            [None, "gauzkan", None, "gauzkazun", "gauzkazuen", "gauzkaten"],
            ["zauzkadan", "zauzkan", "zauzkagun", None, None, "zauzkaten"],
            ["zauzkatedan", "zauzkaten", "zauzkagun", None, None, "zauzkateten"],
            ["dauzkadan", "dauzkan", "dauzkagun", "dauzkazun", "dauzkazuen", "dauzkaten"]
        ),
        Denbora.LEHEN: __buildDF(
            [None, "nindukan", None, "nindukazun", "nindukazuen", "nindukaten"],
            ["neukan", "zeukan", "geneukan", "zeneukan", "zeneukaten", "zeukaten"],
            [None, "ginduzkan", None, "ginduzkazun", "ginduzkazuen", "ginduzkaten"],
            ["zinduzkadan", "zinduzkan", "zinduzkagun", None, None, "zinduzkaten"],
            ["zinduzkatedan", "zinduzkaten", "zinduzkategun", None, None, "zinduzkateten"],
            ["neuzkan", "zeuzkan", "geneuzkan", "zeneuzkan", "zeneuzkaten", "zeuzkaten"]
        ),
    }
}