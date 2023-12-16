""" Module de tests de double sdes (déchiffrement et chiffrement) """
# pylint: disable=E0401, C0413
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from cassages import chiffrement_sdes, dechiffrement_sdes, CONST

def test_double_sdes():
    """
    Test le double sdes en chiffrant 2 fois avec une deux clés différentes et
    en déchiffrant par la suite pour retrouver le même texte
    """
    print("Texte original :\n", CONST.TEXTE_TEST)
    texte_chiffre_1 = chiffrement_sdes(CONST.PREMIERE_CLE_TEST, CONST.TEXTE_TEST)
    print("Texte chiffré 1er passage : \n", texte_chiffre_1)
    texte_chiffre_2 = chiffrement_sdes(CONST.DEUXIEME_CLE_TEST, texte_chiffre_1)
    print("Texte chiffré 2e passage : \n", texte_chiffre_2)
    texte_dechiffre_1 = dechiffrement_sdes(CONST.DEUXIEME_CLE_TEST, texte_chiffre_2)
    print("Texte déchiffré 1er passage : \n", texte_dechiffre_1)
    texte_dechiffre_2 = dechiffrement_sdes(CONST.PREMIERE_CLE_TEST, texte_dechiffre_1)
    print("Texte une fois double sdes fini : \n", texte_dechiffre_2,"\n")

if __name__ == "__main__":
    test_double_sdes()
