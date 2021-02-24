# Test report for javascript / file:///tmp/top-repos-quality-repos-rzj_lvb6/create-react-app HEAD 32106d216e4c31fda30ec475f9f03186d116c893

### Classification report

PPCR: 0.818

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.929| 0.932| 0.842| 0.931| 0.883| 2069| 2290| 0.903 |
| `␣` | 0.832| 0.901| 0.607| 0.865| 0.702| 616| 914| 0.674 |
| `'` | 0.998| 1.000| 0.954| 0.999| 0.975| 418| 438| 0.954 |
| `⏎` | 0.952| 0.758| 0.412| 0.844| 0.575| 157| 289| 0.543 |
| `⏎␣⁺␣⁺` | 0.701| 0.777| 0.754| 0.737| 0.727| 130| 134| 0.970 |
| `⏎␣⁻␣⁻` | 1.000| 0.744| 0.685| 0.853| 0.813| 117| 127| 0.921 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 12| 111| 0.108 |
| `micro avg` | 0.912| 0.912| 0.746| 0.912| 0.821| 3519| 4303| 0.818 |
| `weighted avg` | 0.912| 0.912| 0.746| 0.910| 0.804| 3519| 4303| 0.818 |
| `macro avg` | 0.773| 0.730| 0.608| 0.747| 0.668| 3519| 4303| 0.818 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| 
|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |
|221 |1929 |102 |0 |0 |38 |0 |0 |
|298 |55 |555 |0 |1 |5 |0 |0 |
|20 |0 |0 |418 |0 |0 |0 |0 |
|132 |38 |0 |0 |119 |0 |0 |0 |
|4 |21 |7 |1 |0 |101 |0 |0 |
|10 |24 |3 |0 |3 |0 |87 |0 |
|99 |10 |0 |0 |2 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\u0027": {"f1-score": 0.998805256869773, "precision": 0.9976133651551312, "recall": 1.0, "support": 418}, "macro avg": {"f1-score": 0.7469485113629808, "precision": 0.7731185131342614, "recall": 0.7302547272883789, "support": 3519}, "micro avg": {"f1-score": 0.9119067917021881, "precision": 0.9119067917021881, "recall": 0.9119067917021881, "support": 3519}, "weighted avg": {"f1-score": 0.9104444333384334, "precision": 0.911844476638912, "recall": 0.9119067917021881, "support": 3519}, "\u2205": {"f1-score": 0.930535455861071, "precision": 0.9287433798748195, "recall": 0.9323344610923151, "support": 2069}, "\u23ce": {"f1-score": 0.8439716312056738, "precision": 0.952, "recall": 0.7579617834394905, "support": 157}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 12}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.7372262773722628, "precision": 0.7013888888888888, "recall": 0.7769230769230769, "support": 130}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8529411764705882, "precision": 1.0, "recall": 0.7435897435897436, "support": 117}, "\u2423": {"f1-score": 0.8651597817614965, "precision": 0.8320839580209896, "recall": 0.900974025974026, "support": 616}},
  "cl_report_full": {"\u0027": {"f1-score": 0.9754959159859976, "precision": 0.9976133651551312, "recall": 0.954337899543379, "support": 438}, "macro avg": {"f1-score": 0.6679441798085205, "precision": 0.7731185131342614, "recall": 0.6077789148507465, "support": 4303}, "micro avg": {"f1-score": 0.8205062643825108, "precision": 0.9119067917021881, "recall": 0.7457587729491053, "support": 4303}, "weighted avg": {"f1-score": 0.8038183740860633, "precision": 0.8878493708095702, "recall": 0.7457587729491053, "support": 4303}, "\u2205": {"f1-score": 0.883444011907488, "precision": 0.9287433798748195, "recall": 0.8423580786026201, "support": 2290}, "\u23ce": {"f1-score": 0.5748792270531401, "precision": 0.952, "recall": 0.4117647058823529, "support": 289}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 111}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.726618705035971, "precision": 0.7013888888888888, "recall": 0.753731343283582, "support": 134}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8130841121495327, "precision": 1.0, "recall": 0.6850393700787402, "support": 127}, "\u2423": {"f1-score": 0.7020872865275143, "precision": 0.8320839580209896, "recall": 0.6072210065645515, "support": 914}},
  "ppcr": 0.8178015338136184
}
```
</details>