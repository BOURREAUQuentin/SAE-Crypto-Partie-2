""" Module de tests de temps d'exécution de chiffrement/déchiffrement SDES et AES """
# pylint: disable=E0401, C0413
import sys
import os
import time

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from cassages import cassage_brutal, cassage_astucieux, chiffrement_sdes, dechiffrement_sdes, CONST
from double_sdes import double_chiffrement_sdes
from aes import chiffrement_aes, dechiffrement_aes

def test_moyenne_temps_dechiffrement_sdes():
    """
    Test la moyenne de temps d'exécution de déchiffrement de SDES
    """
    texte_chiffre = chiffrement_sdes(CONST.TempsExecution.CLE_TEST.value,
                                     CONST.TempsExecution.TEXTE_TEST.value)
    somme_temps = 0
    for _ in range(CONST.TempsExecution.NOMBRE_DE_TESTS_AES_DSES.value):
        start_time = time.time()
        dechiffrement_sdes(CONST.TempsExecution.CLE_TEST.value, texte_chiffre)
        end_time = time.time()
        execution_time = end_time - start_time
        somme_temps += execution_time
    print("La moyenne du temps d'exécution du déchiffrement SDES est de :",
          somme_temps/CONST.TempsExecution.NOMBRE_DE_TESTS_AES_DSES.value,"secondes\n")

def test_moyenne_temps_chiffrement_sdes():
    """
    Test la moyenne de temps d'exécution de chiffrement de SDES
    """
    somme_temps = 0
    for _ in range(CONST.TempsExecution.NOMBRE_DE_TESTS_AES_DSES.value):
        start_time = time.time()
        chiffrement_sdes(CONST.TempsExecution.CLE_TEST.value,
                                     CONST.TempsExecution.TEXTE_TEST.value)
        end_time = time.time()
        execution_time = end_time - start_time
        somme_temps += execution_time
    print("La moyenne du temps d'exécution du chiffrement SDES est de :",
          somme_temps/CONST.TempsExecution.NOMBRE_DE_TESTS_AES_DSES.value,"secondes\n")

def test_moyenne_temps_dechiffrement_aes():
    """
    Test la moyenne de temps d'exécution de déchiffrement de AES
    """
    texte_chiffre = chiffrement_aes(CONST.TempsExecution.CLE_TEST.value,
                                     CONST.TempsExecution.TEXTE_TEST.value)
    somme_temps = 0
    for _ in range(CONST.TempsExecution.NOMBRE_DE_TESTS_AES_DSES.value):
        start_time = time.time()
        dechiffrement_aes(CONST.TempsExecution.CLE_TEST.value, texte_chiffre)
        end_time = time.time()
        execution_time = end_time - start_time
        somme_temps += execution_time
    print("La moyenne du temps d'exécution du déchiffrement AES est de :",
          somme_temps/CONST.TempsExecution.NOMBRE_DE_TESTS_AES_DSES.value,"secondes\n")

def test_moyenne_temps_chiffrement_aes():
    """
    Test la moyenne de temps d'exécution de chiffrement de AES
    """
    somme_temps = 0
    for _ in range(CONST.TempsExecution.NOMBRE_DE_TESTS_AES_DSES.value):
        start_time = time.time()
        chiffrement_aes(CONST.TempsExecution.CLE_TEST.value,
                                     CONST.TempsExecution.TEXTE_TEST.value)
        end_time = time.time()
        execution_time = end_time - start_time
        somme_temps += execution_time
    print("La moyenne du temps d'exécution du chiffrement AES est de :",
          somme_temps/CONST.TempsExecution.NOMBRE_DE_TESTS_AES_DSES.value,"secondes\n")

def test_moyenne_temps_cassage_brutal():
    """
    Test la moyenne de temps d'exécution du cassage brutal de double SDES
    """
    print("Voici le texte utilisé lors du cassage brutal:", CONST.TEXTE_TEST,"\n")
    texte_chiffre = double_chiffrement_sdes(CONST.PREMIERE_CLE_TEST,
                                            CONST.DEUXIEME_CLE_TEST, CONST.TEXTE_TEST)
    somme_temps = 0
    for _ in range(CONST.TempsExecution.NOMBRE_DE_TESTS_CASSAGE.value):
        start_time = time.time()
        _, _ = cassage_brutal(CONST.TEXTE_TEST, texte_chiffre,False)
        end_time = time.time()
        execution_time = end_time - start_time
        somme_temps += execution_time
    print("La moyenne du temps d'exécution du cassage brutal de double SDES est de :",
          somme_temps/CONST.TempsExecution.NOMBRE_DE_TESTS_CASSAGE.value,"secondes\n")

def test_moyenne_temps_cassage_astucieux():
    """
    Test la moyenne de temps d'exécution du cassage astucieux de double SDES
    """
    print("Voici le texte utilisé lors du cassage astucieux:", CONST.TEXTE_TEST,"\n")
    texte_chiffre = double_chiffrement_sdes(CONST.PREMIERE_CLE_TEST,
                                            CONST.DEUXIEME_CLE_TEST, CONST.TEXTE_TEST)
    somme_temps = 0
    for _ in range(CONST.TempsExecution.NOMBRE_DE_TESTS_CASSAGE.value):
        start_time = time.time()
        _, _ = cassage_astucieux(CONST.TEXTE_TEST, texte_chiffre,False)
        end_time = time.time()
        execution_time = end_time - start_time
        somme_temps += execution_time
    print("La moyenne du temps d'exécution du cassage astucieux de double SDES est de :",
          somme_temps/CONST.TempsExecution.NOMBRE_DE_TESTS_CASSAGE.value,"secondes\n")

if __name__ == "__main__":
    # test_moyenne_temps_dechiffrement_sdes()
    # test_moyenne_temps_chiffrement_sdes()
    # test_moyenne_temps_dechiffrement_aes()
    # test_moyenne_temps_chiffrement_aes()
    test_moyenne_temps_cassage_brutal()
    test_moyenne_temps_cassage_astucieux()
