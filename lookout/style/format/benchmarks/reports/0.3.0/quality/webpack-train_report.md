# Train report for javascript / file:///tmp/top-repos-quality-repos-frbmq7ku/webpack HEAD babe736cfa1ef7e8014ed32ba4a4ec38049dce14

### Classification report

PPCR: 0.855

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.952| 0.996| 0.964| 0.973| 0.958| 188228| 194538| 0.968 |
| `␣` | 0.968| 0.942| 0.794| 0.955| 0.873| 73417| 87068| 0.843 |
| `"` | 0.983| 1.000| 0.865| 0.992| 0.920| 28599| 33078| 0.865 |
| `⏎⇥⁺` | 0.959| 0.848| 0.737| 0.900| 0.833| 13399| 15424| 0.869 |
| `⏎⇥⁻` | 0.945| 0.867| 0.605| 0.904| 0.738| 10144| 14543| 0.698 |
| `⏎` | 0.954| 0.600| 0.229| 0.737| 0.369| 9841| 25772| 0.382 |
| `'` | 0.000| 0.000| 0.000| 0.000| 0.000| 480| 1774| 0.271 |
| `⏎⇥⁻⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 271| 437| 0.620 |
| `⏎⏎` | 0.972| 0.531| 0.022| 0.687| 0.043| 258| 6252| 0.041 |
| `⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 201| 604| 0.333 |
| `⏎⏎⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 21| 102| 0.206 |
| `⏎␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 20| 454| 0.044 |
| `weighted avg` | 0.956| 0.958| 0.819| 0.955| 0.858| 324879| 380046| 0.855 |
| `macro avg` | 0.561| 0.482| 0.351| 0.512| 0.394| 324879| 380046| 0.855 |
| `micro avg` | 0.958| 0.958| 0.819| 0.958| 0.883| 324879| 380046| 0.855 |

### Confusion matrix

|refusal|  ∅| ␣| "| ⏎| ⏎⇥⁺| ⏎⇥⁻| ⏎⏎| '| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⇥⁻⇥⁻| ⏎⏎⇥⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|6310 |187439 |632 |0 |1 |47 |109 |0 |0 |0 |0 |0 |0 |
|13651 |3659 |69131 |0 |181 |268 |178 |0 |0 |0 |0 |0 |0 |
|4479 |0 |0 |28599 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|15931 |3013 |897 |0 |5905 |3 |22 |1 |0 |0 |0 |0 |0 |
|2025 |1540 |492 |0 |2 |11365 |0 |0 |0 |0 |0 |0 |0 |
|4399 |1123 |153 |0 |71 |0 |8797 |0 |0 |0 |0 |0 |0 |
|5994 |51 |43 |0 |27 |0 |0 |137 |0 |0 |0 |0 |0 |
|1294 |0 |0 |480 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|403 |10 |26 |0 |0 |165 |0 |0 |0 |0 |0 |0 |0 |
|434 |11 |9 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|166 |63 |1 |0 |5 |0 |202 |0 |0 |0 |0 |0 |0 |
|81 |0 |13 |0 |0 |0 |5 |3 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| test/browsertest/mocha.js | 875 |
| lib/Parser.js | 655 |
| lib/Stats.js | 341 |
| lib/Compilation.js | 285 |
| lib/optimize/ConcatenatedModule.js | 261 |
| lib/optimize/SplitChunksPlugin.js | 180 |
| lib/dependencies/HarmonyExportImportedSpecifierDependency.js | 172 |
| test/Parser.unittest.js | 141 |
| lib/HotModuleReplacement.runtime.js | 139 |
| lib/WebpackOptionsValidationError.js | 125 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.9916779361281598, "precision": 0.9834932425461673, "recall": 1.0, "support": 28599}, "\u0027": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 480}, "macro avg": {"f1-score": 0.5123061954102869, "precision": 0.561064184495082, "recall": 0.4819906329581793, "support": 324879}, "micro avg": {"f1-score": 0.9584275991984709, "precision": 0.9584275991984709, "recall": 0.9584275991984709, "support": 324879}, "weighted avg": {"f1-score": 0.9552246601987714, "precision": 0.9556160541377852, "recall": 0.9584275991984709, "support": 324879}, "\u2205": {"f1-score": 0.9733627254717153, "precision": 0.9519067183318183, "recall": 0.9958082750706589, "support": 188228}, "\u23ce": {"f1-score": 0.7366057506393064, "precision": 0.9536498708010336, "recall": 0.600040646275785, "support": 9841}, "\u23ce\u21e5\u207a": {"f1-score": 0.9003049867310967, "precision": 0.9592336259284268, "recall": 0.8481976266885588, "support": 13399}, "\u23ce\u21e5\u207b": {"f1-score": 0.9042503983142314, "precision": 0.9445935788682487, "recall": 0.8672121451104101, "support": 10144}, "\u23ce\u21e5\u207b\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 271}, "\u23ce\u23ce": {"f1-score": 0.68671679197995, "precision": 0.9716312056737588, "recall": 0.5310077519379846, "support": 258}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 21}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 201}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 20}, "\u2423": {"f1-score": 0.9547557556589833, "precision": 0.9682619717915318, "recall": 0.941621150414754, "support": 73417}},
  "cl_report_full": {"\"": {"f1-score": 0.9202181572469713, "precision": 0.9834932425461673, "recall": 0.8645927807001632, "support": 33078}, "\u0027": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 1774}, "macro avg": {"f1-score": 0.394475016303953, "precision": 0.561064184495082, "recall": 0.35123849503820187, "support": 380046}, "micro avg": {"f1-score": 0.8834216406000639, "precision": 0.9584275991984709, "recall": 0.8193034527399314, "support": 380046}, "weighted avg": {"f1-score": 0.8580044098768878, "precision": 0.9504196824586498, "recall": 0.8193034527399314, "support": 380046}, "\u2205": {"f1-score": 0.9576724307505231, "precision": 0.9519067183318183, "recall": 0.9635084148084179, "support": 194538}, "\u23ce": {"f1-score": 0.36947816293329994, "precision": 0.9536498708010336, "recall": 0.22912463138289615, "support": 25772}, "\u23ce\u21e5\u207a": {"f1-score": 0.8334555588149017, "precision": 0.9592336259284268, "recall": 0.7368386929460581, "support": 15424}, "\u23ce\u21e5\u207b": {"f1-score": 0.7375083836351441, "precision": 0.9445935788682487, "recall": 0.6048958261706663, "support": 14543}, "\u23ce\u21e5\u207b\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 437}, "\u23ce\u23ce": {"f1-score": 0.042859377444079465, "precision": 0.9716312056737588, "recall": 0.021912987843889956, "support": 6252}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 102}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 604}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 454}, "\u2423": {"f1-score": 0.8725081248225159, "precision": 0.9682619717915318, "recall": 0.7939886066063306, "support": 87068}},
  "ppcr": 0.8548412560584772
}
```
</details>
