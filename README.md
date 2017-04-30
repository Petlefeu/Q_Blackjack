# Q_Blackjack

## Introduction

This repo is highly inspired by [Simon's technical blog ](http://simontechblog.blogspot.fr/2010/08/pybrain-reinforcement-learning-tutorial.html).

In Q-Learning :
  - alpha = 0 implies that it never learn
  - alpha = 1 implies that it replace it vales each times (too easy)
  - gamma = 0 implies that the agent will try to optimize its learning for the long-term
  - gamma = 1 implies that the agent will optimize for short-term (greedy learning)


## Description

Le programme choisit un chiffre (ou deux cartes) au hasard entre 2 et 21 (état 2 à 21).
Il a deux choix : Garder ses cartes (choix 0) ou en Prendre une nouvelle (choix 1).
Le croupier possède aussi ses deux cartes de départ, mais n'en tire jamais de nouvelles.

Enfin, si le joueur gagne il gagne 10€. Sinon, il perd 10€.

**Exemple :**

  - Le programme a une somme de cartes égale 15 (état **15**)
  - Le programme choisi le tirer une carte (choix **1**)
  - Le programme tire la carte 3 (nouvel état **18**)
  - Le croupier est battu (peu importe son score)
  - Le programme gagne **+10**€

La Q valeur de l'état 15 avec le choix 1 va augmenter.

> Attention, l'état 18 ne va pas du tout être actualisé ! 

## Go further with doInteraction()

```
Experiment Env (EE)
Experiment Task (ET)
Q Learner (QL)
Q Agent (QA)
```

**Observations :**

```
QL --getObservation--> ET --getSensors--> EE
QL --integrateObservation--> QA
```

**Action :**

```
QL --getAction--> QA
QL --performAction--> ET --performAction--> EE
```

**Reward :**

```
QL --getReward()--> ET (--reset--> EE)
QL --giveReward --> QA
```

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
| 1 | -9.17339932262 | -9.8514148314 | 0.678015508784 |
| 2 | -9.94650150981 | 0.110589365311 | -10.0570908751 |
| 3 | -9.73469662394 | 0.134612190547 | -9.86930881449 |
| 4 | -7.90662803907 | 0.196708234402 | -8.10333627348 |
| 5 | -10.138935689 | 0.213279060497 | -10.3522147495 |
| 6 | -7.96193890553 | 0.195053653347 | -8.15699255888 |
| 7 | -7.96955598687 | 0.437135775385 | -8.40669176225 |
| 8 | -10.3132567122 | 0.508873729792 | -10.8221304419 |
| 9 | 0.0979196899506 | 0.120497639025 | -0.0225779490748 |
| 10 | -8.10229355485 | 1.47423475073 | -9.57652830557 |
| 11 | -9.77771889427 | 1.07948871868 | -10.8572076129 |
| 12 | -9.92484120048 | 0.8735575689 | -10.7983987694 |
| 13 | -9.93860962004 | 0.654298496211 | -10.5929081162 |
| 14 | -2.67233493361 | -1.14750081125 | -1.52483412236 |
| 15 | -9.86935483854 | 0.296087103777 | -10.1654419423 |
| 16 | 8.42727478794 | -1.83306270881 | 10.2603374967 |
| 17 | 9.71013593438 | 0.0 | 9.71013593438 |
| 18 | 9.7102684236 | 0.0 | 9.7102684236 |
| 19 | 10.1513897361 | 0.0 | 10.1513897361 |
| 20 | 10.519308811 | 0.0 | 10.519308811 |
| 21 | 10.3112485672 | 0.0 | 10.3112485672 |
