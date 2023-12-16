""" Module de tests de temps d'exécution de chiffrement/déchiffrement SDES et AES """
# pylint: disable=E0401, C0413
import sys
import os
import time

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from cassages import chiffrement_sdes, dechiffrement_sdes, CONST

def test_temps_chiffrement_sdes():
    """
    Test la moyenne de temps d'exécution de chiffrement de SDES
    """
    texte_chiffre = chiffrement_sdes(CONST.TempsExecution.CLE_TEST.value, CONST.TempsExecution.TEXTE_TEST.value)
    somme_temps = 0
    for i in range(1000):
        start_time = time.time()
        texte_dechiffre = dechiffrement_sdes(CONST.TempsExecution.CLE_TEST.value, texte_chiffre)
        end_time = time.time()
        execution_time = end_time - start_time
        somme_temps += execution_time
    print(somme_temps/1000)

if __name__ == "__main__":
    test_temps_chiffrement_sdes()
