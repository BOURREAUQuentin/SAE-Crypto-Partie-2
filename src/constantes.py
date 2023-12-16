""" Module pour les constantes de la SAÉ Crypto - Partie 2 """
from enum import Enum

PREMIERE_CLE_TEST = 0b1110101110
DEUXIEME_CLE_TEST = 0b1110101100
with open('./arsene_lupin_extrait.txt', 'r',encoding="utf8") as fichier:
    TEXTE_TEST = "test"
NOMBRE_CLES_POSSIBLES = 1024

class TraceReseau(Enum):
    """
    Enumération définissant des constantes liées à la trace réseau.

    - 'PORT': Port utilisé pour la communication sur la trace réseau
    (valeur par défaut : 9999).
    - 'TAILLE_VECTEUR_INITIALISATION': Taille du vecteur d'initialisation
    en octets utilisé pour le mode de chiffrement CBC (Cipher Block Chaining)
    avec l'algorithme AES (valeur donnée dans le sujet : 16).

    Ces constantes sont utilisées pour la manipulation des paquets réseau dans
    le contexte de déchiffrement des messages entre Bob et Alice.
    """
    PORT = 9999
    TAILLE_VECTEUR_INITIALISATION = 16
