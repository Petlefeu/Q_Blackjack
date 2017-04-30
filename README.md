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
Q_ALPHA = 0.5
Q_GAMMA = 0.1

| First State       | Choice 0 (Stand)           | Choice 1 (Hit)  | Relative value of Hitting over Standing  |
|:-------:|:-------|:-----|:-----|
| 1 | 0.0 | 0.0 | 0.0 |
| 2 | -0.92847140554 | -0.227437485533 | 0.701033920007 |
| 3 | -1.00785129805 | -1.0223956995 | -0.0145444014494 |
| 4 | -1.02962634499 | -0.82558077209 | 0.204045572902 |
| 5 | -0.714518466818 | -0.589659066233 | 0.124859400585 |
| 6 | -1.02832916332 | 0.398075607143 | 1.42640477046 |
| 7 | -1.04187967648 | 0.44956804751 | 1.49144772399 |
| 8 | -0.298744153089 | -0.779848155796 | -0.481104002707 |
| 9 | -1.05364142485 | -0.728955460264 | 0.324685964591 |
| 10 | -0.937184570146 | 0.140991248788 | 1.07817581893 |
| 11 | -0.516479348546 | -1.01836804566 | -0.501888697114 |
| 12 | 0.607780326117 | -1.10077415068 | -1.70855447679 |
| 13 | 0.690343310009 | -0.96550538668 | -1.65584869669 |
| 14 | 0.869846930724 | 0.0 | -0.869846930724 |
| 15 | 0.232715121814 | -0.985945422129 | -1.21866054394 |
| 16 | 0.998888724369 | -1.03034505799 | -2.02923378236 |
| 17 | 0.742000647041 | -1.01817318097 | -1.76017382801 |
| 18 | 1.00151419091 | -1.05573220161 | -2.05724639252 |
| 19 | 0.0693151058871 | -0.976728519719 | -1.04604362561 |
| 20 | 0.883437644585 | -1.01582668791 | -1.8992643325 |
| 21 | 1.06931719372 | -0.937184570146 | -2.00650176387 |


