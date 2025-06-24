# Classification-d-images
Ce workshop a pour objectif d'entraîner et comparer trois architectures différentes de réseaux de neurones convolutifs (CNN) pour la classification des images manuscrites de la base de données MNIST. MNIST contient 70 000 images en niveaux de gris de chiffres manuscrits (0 à 9).

Vous apprendrez à :

- Préparer et normaliser les données MNIST,
- Construire trois modèles CNN différents avec des architectures variées,
- Entraîner chaque modèle,
- Évaluer la performance des modèles (précision, perte),
- Visualiser les résultats d'entraînement.

## Prérequis

- Python 3.7 ou plus
- Librairies Python :
  -- TensorFlow (ou Keras)
  -- NumPy
  -- Matplotlib (optionnel pour visualisation)
- Accès internet pour télécharger la base MNIST (automatique via Keras)

## Contenu

Le workshop inclut :

- Préparation des données MNIST
- Définition des 3 architectures CNN :

| Modèle  | Convolutions | Pooling | Dropout | Dense cachée(s)     | Paramètres | Usage pédagogique  |
|---------|--------------|---------|---------|---------------------|------------|--------------------|
| Small   | 2            | Non     | Non     | Non                 | Faible     | Introduction       |
| Medium  | 1            | 1       | Oui     | 1 (128)             | Moyen      | Approfondissement  |
| Large   | 2            | 2       | Oui     | 2 (128 + 50)        | Plus élevé | Expérimentation    |


- Entraînement et sauvegarde des modèles
- Évaluation et comparaison des performances
- Visualisation des courbes d'apprentissage (loss, accuracy)

## Instructions

1. Cloner ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/mnist-cnn-workshop.git
   cd mnist-cnn-workshop

2. Installer les dépendances :

`
pip install tensorflow numpy matplotlib
Exécuter le script principal :
`

Ce notebook va :

- Charger et préparer les données MNIST,

- Construire et entraîner les 3 modèles CNN,

- Afficher les courbes de performance,

- Sauvegarder les poids des modèles entraînés.

- (Optionnel) Modifier les hyperparamètres dans le script pour expérimenter avec :

* Le nombre d’époques

* La taille des batchs

* Les architectures des CNN

* L'algorithme d'optimisation pour ajuster les poids du réseau pendant l'entraînement

Résultats attendus
Trois modèles entraînés avec des précisions supérieures à 98% sur l'ensemble test.

Courbes d'entraînement montrant la perte et la précision au fil des époques.

Comparaison des performances des trois architectures.

Ressources
MNIST Dataset

TensorFlow Keras Documentation

Auteur :
Ghita BENCHEIKH
ghita.bencheikh@gmail.com
