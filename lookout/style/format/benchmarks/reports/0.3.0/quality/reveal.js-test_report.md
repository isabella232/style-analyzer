# Test report for javascript / file:///tmp/top-repos-quality-repos-dhds81z3/reveal.js HEAD 0b3e7839ebf4ed8b6c180aca0abafa28c67aee6d

### Classification report

PPCR: 0.816

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.992| 0.977| 0.918| 0.984| 0.954| 4704| 5006| 0.940 |
| `␣` | 0.945| 0.938| 0.767| 0.942| 0.847| 2898| 3542| 0.818 |
| `'` | 0.993| 0.934| 0.528| 0.963| 0.689| 606| 1072| 0.565 |
| `⏎⇥⁻` | 0.732| 0.968| 0.968| 0.833| 0.833| 186| 186| 1.000 |
| `⏎` | 0.675| 0.804| 0.326| 0.734| 0.440| 168| 414| 0.406 |
| `⏎⇥⁺` | 0.569| 0.837| 0.421| 0.678| 0.484| 98| 195| 0.503 |
| `⏎⏎` | 0.631| 0.802| 0.265| 0.706| 0.373| 96| 291| 0.330 |
| `⏎⏎⇥⁻` | 0.636| 0.200| 0.163| 0.304| 0.259| 35| 43| 0.814 |
| `⏎⏎⇥⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 16| 36| 0.444 |
| `"` | 0.167| 0.333| 0.143| 0.222| 0.154| 6| 14| 0.429 |
| `micro avg` | 0.949| 0.949| 0.774| 0.949| 0.853| 8813| 10799| 0.816 |
| `weighted avg` | 0.953| 0.949| 0.774| 0.949| 0.840| 8813| 10799| 0.816 |
| `macro avg` | 0.634| 0.679| 0.450| 0.637| 0.503| 8813| 10799| 0.816 |

### Confusion matrix

|refusal|  ∅| ␣| ⏎| '| ⏎⏎| "| ⏎⇥⁻| ⏎⇥⁺| ⏎⏎⇥⁺| ⏎⏎⇥⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|302 |4596 |94 |0 |0 |11 |0 |1 |2 |0 |0 |
|644 |33 |2718 |49 |0 |17 |0 |38 |43 |0 |0 |
|246 |0 |21 |135 |0 |12 |0 |0 |0 |0 |0 |
|466 |1 |23 |0 |566 |0 |10 |5 |1 |0 |0 |
|195 |0 |3 |16 |0 |77 |0 |0 |0 |0 |0 |
|8 |0 |0 |0 |4 |0 |2 |0 |0 |0 |0 |
|0 |1 |1 |0 |0 |0 |0 |180 |0 |0 |4 |
|97 |1 |15 |0 |0 |0 |0 |0 |82 |0 |0 |
|20 |0 |0 |0 |0 |0 |0 |0 |16 |0 |0 |
|8 |1 |0 |0 |0 |5 |0 |22 |0 |0 |7 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.2222222222222222, "precision": 0.16666666666666666, "recall": 0.3333333333333333, "support": 6}, "\u0027": {"f1-score": 0.9625850340136053, "precision": 0.9929824561403509, "recall": 0.933993399339934, "support": 606}, "macro avg": {"f1-score": 0.6366387228353018, "precision": 0.6340717179963151, "recall": 0.6792387139023746, "support": 8813}, "micro avg": {"f1-score": 0.9489390672869624, "precision": 0.9489390672869624, "recall": 0.9489390672869624, "support": 8813}, "weighted avg": {"f1-score": 0.9494587573255722, "precision": 0.9528072571144169, "recall": 0.9489390672869624, "support": 8813}, "\u2205": {"f1-score": 0.9844703866338225, "precision": 0.9920138139434491, "recall": 0.9770408163265306, "support": 4704}, "\u23ce": {"f1-score": 0.7336956521739131, "precision": 0.675, "recall": 0.8035714285714286, "support": 168}, "\u23ce\u21e5\u207a": {"f1-score": 0.6776859504132232, "precision": 0.5694444444444444, "recall": 0.8367346938775511, "support": 98}, "\u23ce\u21e5\u207b": {"f1-score": 0.8333333333333334, "precision": 0.7317073170731707, "recall": 0.967741935483871, "support": 186}, "\u23ce\u23ce": {"f1-score": 0.7064220183486238, "precision": 0.6311475409836066, "recall": 0.8020833333333334, "support": 96}, "\u23ce\u23ce\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 16}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.30434782608695654, "precision": 0.6363636363636364, "recall": 0.2, "support": 35}, "\u2423": {"f1-score": 0.9416248051273168, "precision": 0.945391304347826, "recall": 0.937888198757764, "support": 2898}},
  "cl_report_full": {"\"": {"f1-score": 0.15384615384615383, "precision": 0.16666666666666666, "recall": 0.14285714285714285, "support": 14}, "\u0027": {"f1-score": 0.6894031668696713, "precision": 0.9929824561403509, "recall": 0.5279850746268657, "support": 1072}, "macro avg": {"f1-score": 0.503298921361764, "precision": 0.6340717179963151, "recall": 0.44980407924458454, "support": 10799}, "micro avg": {"f1-score": 0.8528451968182744, "precision": 0.9489390672869624, "recall": 0.7744235577368275, "support": 10799}, "weighted avg": {"f1-score": 0.8395783334220888, "precision": 0.9370334732242648, "recall": 0.7744235577368275, "support": 10799}, "\u2205": {"f1-score": 0.9536258948023655, "precision": 0.9920138139434491, "recall": 0.9180982820615262, "support": 5006}, "\u23ce": {"f1-score": 0.4397394136807818, "precision": 0.675, "recall": 0.32608695652173914, "support": 414}, "\u23ce\u21e5\u207a": {"f1-score": 0.48377581120943947, "precision": 0.5694444444444444, "recall": 0.4205128205128205, "support": 195}, "\u23ce\u21e5\u207b": {"f1-score": 0.8333333333333334, "precision": 0.7317073170731707, "recall": 0.967741935483871, "support": 186}, "\u23ce\u23ce": {"f1-score": 0.3728813559322034, "precision": 0.6311475409836066, "recall": 0.2646048109965636, "support": 291}, "\u23ce\u23ce\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 36}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.2592592592592593, "precision": 0.6363636363636364, "recall": 0.16279069767441862, "support": 43}, "\u2423": {"f1-score": 0.847124824684432, "precision": 0.945391304347826, "recall": 0.7673630717108978, "support": 3542}},
  "ppcr": 0.816094082785443
}
```
</details>