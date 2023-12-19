# SAÉ Crypto - Partie 2 - Liaisons épistolaires

## Notre équipe

### Développeur 1

- Nom : BOURREAU
- Prénom : QUENTIN
- Identifiant Github : [BOURREAUQuentin](https://github.com/BOURREAUQuentin)

### Développeur 2

- Nom : CHHUM--MOXEL
- Prénom : LOANN
- Identifiant Github : [loannchhum](https://github.com/loannchhum)

## Introduction

Cette SAÉ s'inscrit dans le cours de Cryptographie. Le sujet repose sur un scénario romantique impliquant Alice et Bob, qui maintiennent une relation secrète grâce à des messages chiffrés. Ils utilisent le protocole "PlutotBonneConfidentialité", comprenant un échange de clés RSA pour la session et un chiffrement symétrique basé sur l'algorithme SDES. Eve, une amie d'Alice, tente de déchiffrer les messages et à besoin de notre aide.

## Nos choix

### Le respect des bonnes pratiques

Pour respecter les bonnes pratiques de programmation et de gestion de projet vu à l’IUT, nous avons tout d'abord crée un référentiel GitHub commun. En effet, celui-ci a permis de faciliter la collaboration, la gestion du code source, la communication au sein de l'équipe, mais également de suivre notre avancée sur cette SAÉ.

Lien du GitHub : [Lien vers le GitHub](https://github.com/BOURREAUQuentin/SAE-Crypto-Partie-2)

Quant au code en lui-même, nous avons respecté les bonnes pratiques apprises à l'IUT notamment avec une structuration des fichiers compréhensibles (un dossier src et un dossier test), des fonctions avec des docstrings, des commentaires quand le code semblait plus compliqué à comprendre et bien évidemment un code lisible.

### Formatage du code avec yapf

YAPF (Yet Another Python Formatter) est un outil de formatage de code source Python pour maintenir un code cohérent et bien s'appuyant sur différentes règles de formatage prédéfinies.

Par conséquent, yapf a utilisé sur mon code une indentation de 4 espaces par niveau d'indentation. Ensuite, il a configuré une longueur maximale des lignes de code en effectuant automatiquement une mise en forme pour la rendre conforme. De plus, il ajoute également des espaces autour des opérateurs binaires, avant et après les parenthèses, etc. Enfin, yapf a aussi mis en forme le code pour aligner les déclarations des méthodes et des blocs (if, while, for).

### Pylint

Pylint est un outil statique d'analyse de code pour le langage de programmation Python. Son objectif principal est d'identifier les erreurs, les incohérences et les conventions non respectées dans le code source Python. Il est souvent utilisé comme un outil de linting, qui est le processus de vérification automatique du code source pour détecter les erreurs de programmation, les pratiques non conformes aux conventions et les problèmes potentiels.

Ainsi, nous l'avons utilisé au sein de cette SAÉ dans l'objectif de respecter toutes les normes et conventions de Python. Il nous a servi également car il aide à maintenir un codebase propre, cohérent et conforme aux bonnes pratiques de programmation et donc garder une qualité propre du code.

## Exécution de notre programme

Avant de lancer nos fichier, assurez-vous que la bibliothèque Python scapy, soit installée sur votre système.

Une fois téléchargée, pour lancer nos fichiers, il faut être obligatoirement dans le répertoire racine, soit SAE-CRYPTO-PARTIE-2. Une fois dedans, vous pouvez lancez le fichier désiré. Par exemple, vous pouvez lancer le fichier test_cassages en tapant la commande suivante :

```python
python3 test/test_cassages.py
```

#

BOURREAU Quentin / CHHUM--MOXEL Loann - BUT Informatique 2.3.B