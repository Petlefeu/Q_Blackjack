# Q_Blackjack

## Introduction

This repo is highly inspired by [Simon's technical blog ](http://simontechblog.blogspot.fr/2010/08/pybrain-reinforcement-learning-tutorial.html).

In Q-Learning :
  - alpha = 0 implies that it never learn
  - alpha = 1 implies that it replace it vales each times (too easy)
  - gamma = 0 implies that the agent will try to optimize its learning for the long-term
  - gamma = 1 implies that the agent will optimize for short-term (greedy learning)


## Description

### Français

Le programme choisit un chiffre (ou deux cartes) au hasard entre 2 et 21 (état 2 à 21).
Il a deux choix : Garder ses cartes (choix 0) ou en Prendre une nouvelle (choix 1).
Le croupier possède aussi ses deux cartes de départ, mais n'en tire jamais de nouvelles.

Enfin, si le joueur gagne il gagne 1€. Sinon, il perd 1€.

**Exemple :**

  - Le programme a une somme de cartes égale 15 (état **15**)
  - Le programme choisi le tirer une carte (choix **1**)
  - Le programme tire la carte 3 (nouvel état **18**)
  - Le croupier est battu (peu importe son score)
  - Le programme gagne **+1**€

La Q valeur de l'état 15 avec le choix 1 va augmenter.

> Attention, l'état 18 ne va pas du tout être actualisé ! 


### English

## Add PyBrain repository

```bash
sudo pip install --upgrade pybrain

# Apply fix https://github.com/pybrain/pybrain/issues/211
# Files are present in pybrain_fix/
```

## Result

NB_ITERATION = 300

> Alpha is low because we can loose with a good hand often, and win with a bad hand often too

Q_ALPHA = 0.2

> Gamma is low because we have to spend a lot of money (and time) in this try. But, we shouldn't put gamma too low.

Q_GAMMA = 0.2

|First State|Choice 0 (Stand)|Choice 1 (Hit)|Relative value of Standing over Hitting|
|:-------:|:-------|:-----|:-----|
| 0 | -9.8777920789 | -9.70872117691 | -0.169070901993 |
| 1 | -8.54199128836 | 0.0800608812971 | -8.62205216965 |
| 2 | -9.89873875734 | 0.114689521934 | -10.0134282793 |
| 3 | -3.96415747415 | 0.0915179037877 | -4.05567537793 |
| 4 | -1.08817707999 | 0.127911011893 | -1.21608809188 |
| 5 | -9.90939660566 | 0.258571897352 | -10.167968503 |
| 6 | -9.97296717733 | 0.361296346121 | -10.3342635234 |
| 7 | -9.71900797448 | 0.503309751064 | -10.2223177255 |
| 8 | -7.93349724006 | 0.580662093386 | -8.51415933345 |
| 9 | -1.20912903045 | 0.699306426796 | -1.90843545725 |
| 10 | -0.282385670895 | 0.920979036012 | -1.20336470691 |
| 11 | -9.89609325347 | 0.791208967545 | -10.687302221 |
| 12 | -0.627300674558 | 1.4104261359 | -2.03772681046 |
| 13 | -2.32902254457 | 0.0383726772416 | -2.36739522181 |
| 14 | -2.18371955416 | 0.630381850596 | -2.81410140475 |
| 15 | 7.23222398601 | 0.0 | 7.23222398601 |
| 16 | 9.24667780794 | -1.03340690851 | 10.2800847164 |
| 17 | 8.72165737102 | 0.0 | 8.72165737102 |
| 18 | 10.4104040812 | 0.0 | 10.4104040812 |
| 19 | 8.38700083806 | 0.0 | 8.38700083806 |
| 20 | 10.7125437904 | 0.0 | 10.7125437904 |


