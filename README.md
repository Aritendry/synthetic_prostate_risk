# synthetic_prostate_risk
# Projet IA Santé : Prédiction du risque de santé à partir du mode de vie

## Introduction

Dans ce projet, j’ai voulu tester si on pouvais utiliser l’intelligence artificielle pour prédire si une personne est à risque ou pas niveau santé. On utilise des données assez simples qu’on peut trouver facilement chez les gens, comme est-ce qu’ils fument, dorment bien, mangent gras, etc. L’objectif c’est de montrer que même des infos de base peuvent servir à aider dans la prévention de certaines maladies.

## Problématique

Est-ce qu’on peut prédire le **niveau de risque santé** d’une personne (Low, Medium ou High) juste avec ses habitudes de vie et quelques infos médicales de base ?  
Est-ce que l’IA peut aider à prévenir plutôt que guérir en se basant sur ces données-là ?

## Description des données

Voici les colonnes qu’on a dans le dataset :

- `id` : identifiant unique (sert à rien pour l’IA mais utile pour suivre les lignes)
- `age` : l’âge de la personne
- `bmi` : l’indice de masse corporelle (poids / taille²)
- `smoker` : si la personne fume ou pas
- `alcohol_consumption` : si elle boit de l’alcool ou pas (certains sont vides)
- `diet_type` : ce qu’elle mange en général (Fatty, Mixed, etc)
- `physical_activity_level` : si elle est active physiquement (Low, Moderate, High)
- `family_history` : si y’a des antécédents médicaux dans la famille
- `mental_stress_level` : niveau de stress mental (Low, Moderate, High)
- `sleep_hours` : combien d’heures elle dort en moyenne
- `regular_health_checkup` : est-ce qu’elle fait des bilans de santé régulièrement
- `prostate_exam_done` : si elle a fait un examen de la prostate ou pas
- `risk_level` : **la variable qu’on veut prédire** (Low, Medium, High)

## Solution apportée

J’ai utilisé un modèle de machine learning simple : un **arbre de décision**. C’est un algorithme qui apprend à poser des questions sur les données (comme “est-ce que la personne fume ?”) pour arriver à une prédiction.

Après avoir analysé et nettoyé les données (suppression des valeurs manquantes, transformation des catégories en chiffres, etc), j’ai entraîné ce modèle pour qu’il apprenne à prédire le `risk_level`.

### Ce que le modèle peut faire

- Prédire si une personne est à **faible, moyen ou haut risque** santé
- Montrer **quelles habitudes influencent le plus le risque** (ex : sommeil, stress, tabac, activité physique)
- Aider à sensibiliser les gens sur **l’importance d’un bon mode de vie**

### Limites

- Le dataset est un peu déséquilibré (peu de gens avec un “High” risque), donc le modèle a plus de mal à prédire cette catégorie
- Certaines colonnes ont des valeurs manquantes (comme `alcohol_consumption`)
- C’est un modèle simple, y’a moyen de faire mieux avec des techniques plus avancées (Random Forest, XGBoost, etc)

## Conclusion

Ce projet montre qu’on peut commencer à faire des prédictions utiles avec des modèles simples et des données pas trop complexes. C’est une bonne première approche pour comprendre comment l’IA peut être utile dans le domaine de la santé et de la prévention.

