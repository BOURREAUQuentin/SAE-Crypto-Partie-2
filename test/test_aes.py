""" Module de tests de aes (déchiffrement et chiffrement) """
# pylint: disable=E0401, C0413
import sys
import os
import time

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from cassages import CONST
from aes import chiffrement_aes, dechiffrement_aes

def test_chiffrement_aes():
    """
    Test le temps d'exécution du chiffrement AES
    """
    start_time = time.time()
    texte_chiffre = chiffrement_aes(CONST.TempsExecution.CLE_TEST.value
                                    ,CONST.TempsExecution.TEXTE_TEST.value)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Temps d'exécution du chiffrement AES :",execution_time, "secondes")
    print("Texte chiffré en AES:\n",texte_chiffre,"\n\n")

def test_dechiffrement_aes():
    """
    Test le temps d'exécution du déchiffrement AES
    """
    texte_chiffre = chiffrement_aes(CONST.TempsExecution.CLE_TEST.value
                                    ,CONST.TempsExecution.TEXTE_TEST.value)
    start_time = time.time()
    texte_dechiffre = dechiffrement_aes(CONST.TempsExecution.CLE_TEST.value, texte_chiffre)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Temps d'exécution du déchiffrement AES :",execution_time, "secondes")
    print("Texte déchiffré en AES:\n",texte_dechiffre,"\n\n")

if __name__ == "__main__":
    print("Texte original :\n", CONST.TempsExecution.TEXTE_TEST.value,"\n\n")
    test_chiffrement_aes()
    test_dechiffrement_aes()
