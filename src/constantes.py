""" Module pour les constantes de la SAÉ Crypto - Partie 2 """
# pylint: disable=C0301
from enum import Enum

PREMIERE_CLE_TEST = 0b1110101110
DEUXIEME_CLE_TEST = 0b1110101100
TEXTE_TEST = "test"
NOMBRE_CLES_POSSIBLES = 1024


class CleImage(Enum):
    """
    Énumération définissant des constantes liées à la recherche de clé dans l'image.

    - 'NOMBRE_BITS_CLE_IMAGE': Nombre de bits pour la clé à trouver dans l'image.
    - 'CHEMIN_CLE_IMAGE': Chemin de l'image contenant la clé à trouver.

    Ces constantes sont utilisées pour le code et le test de la recherche de clé
    dans l'image.
    """
    NOMBRE_BITS_CLE_IMAGE = 64
    CHEMIN_CLE_IMAGE = "./rossignol2.bmp"


class TempsExecution(Enum):
    """
    Enumération définissant des constantes liées aux tests de temps d'exécution.

    - 'TEXTE_TEST': Texte pour tester les temps d'exécution à partir du fichier
    donné dans le sujet.
    - 'CLE_TEST': Clé pour tester les temps d'exécution de 256 bits (demandé dans
    le sujet).
    - 'NOMBRE_DE_TESTS': Nombre de tests effectués par fonction.

    Ces constantes sont utilisées pour le test de temps d'exécution de chiffrement
    et déchiffrement pour AES et SDES.
    """
    with open('arsene_lupin_extrait.txt', 'r', encoding="utf8") as FICHIER:
        TEXTE_TEST = FICHIER.read()
    CLE_TEST = 0b1101101101101101101101101101101101101101101101101101101101101101110110110110110110110110110110110110110110110110110110110110110111011011011011011011011011011011011011011011011011011011011011011101101101101101101101101101101101101101101101101101101101101101
    NOMBRE_DE_TESTS = 1000


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
