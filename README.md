# Q_Blackjack

## Introduction

This repo is highly inspired by [Simon's technical blog ](http://simontechblog.blogspot.fr/2010/08/pybrain-reinforcement-learning-tutorial.html).

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
git clone git://github.com/pybrain/pybrain.git
cd pybrain/
sudo python setup.py install
```

## Result

| First State       | Choice 0 (Stand)           | Choice 1 (Hit)  | Relative value of Hitting over Standing  |
| ------------- |:-------------:| -----:|-----:|
| 2 |-0.8908373 | -0.28060541 | 0.610231896944|
| 3 |-1.03798549 | -0.68411891 | 0.353866575388|
| 4 |-1.03740923 | 0.37917396 | 1.41658318796|
| 5 |-0.98793687 | 0.29635112 | 1.28428799515|
| 6 |-0.96482714 | -0.84787925 | 0.116947887203|
| 7 |-0.90024445 | -1.02866711 | -0.128422663401|
| 8 |-0.99081519 | 0.09084443 | 1.08165962306|
| 9 |-0.74793091 | -0.72986532 | 0.0180655868055|
| 10 | 0.03701233 | -0.95452835 | -0.991540680694|
| 11 | 0.04092572 | -0.92891645 | -0.969842164526|
| 12 | 0.28547482 | -0.85094472 | -1.13641953585|
| 13 | 1.09271139 | -1.02805868 | -2.12077007924|
| 14 | 0.56011036 | -0.27897845 | -0.839088806997|
| 15 |-0.1609111 | -0.93084986 | -0.769938754938|
| 16 | 1.0181259 | -1.02725993 | -2.04538583208|
| 17 | 0.77924908 | -0.28242243 | -1.06167150815|
| 18 | 1.00840545 | 0. | -1.00840545194|
| 19 | 1.06053154 | 0. | -1.06053154042|
| 20 | 0.98768149 | -1.08399064 | -2.07167213734|
| 21 | 1.08204851 | -0.89611367 | -1.97816217921|

