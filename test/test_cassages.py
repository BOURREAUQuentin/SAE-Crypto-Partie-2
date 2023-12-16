""" Module de tests des cassages (brutal et astucieux) """
# pylint: disable=E0401
import sys
import os
from sae import (double_sdes_encrypt_text, cassage_brutal, cassage_astucieux,
                 sdes_decrypt_text, CONST, time)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

def test_cassage_brutal():
    start_time = time.time()
    texte_chiffre = double_sdes_encrypt_text(CONST.PREMIERE_CLE_TEST,
                                             CONST.DEUXIEME_CLE_TEST, CONST.TEXTE_TEST)
    premiere_cle_trouvee, deuxieme_cle_trouvee = cassage_brutal(CONST.TEXTE_TEST, texte_chiffre)
    if premiere_cle_trouvee is not None and deuxieme_cle_trouvee is not None:
        print("Clé 1:", bin(premiere_cle_trouvee))
        print("Clé 2:", bin(deuxieme_cle_trouvee))
        texte_dechiffre_1 = sdes_decrypt_text(int(bin(premiere_cle_trouvee), 2), texte_chiffre)
        texte_dechiffre_2 = sdes_decrypt_text(int(bin(deuxieme_cle_trouvee), 2), texte_dechiffre_1)
        print("Message original : ", texte_dechiffre_2)
    else:
        print("Aucune clé trouvée")
    end_time = time.time()
    execution_time = end_time - start_time
    print("Temps d'exécution cassage brutal :", execution_time, "secondes\n")

def test_cassage_astucieux():
    start_time = time.time()
    texte_chiffre = double_sdes_encrypt_text(CONST.PREMIERE_CLE_TEST,
                                             CONST.DEUXIEME_CLE_TEST, CONST.TEXTE_TEST)
    premiere_cle_trouvee, deuxieme_cle_trouvee = cassage_astucieux(CONST.TEXTE_TEST, texte_chiffre)
    if premiere_cle_trouvee is not None and deuxieme_cle_trouvee is not None:
        print("Clé 1:", bin(premiere_cle_trouvee))
        print("Clé 2:", bin(deuxieme_cle_trouvee))
        texte_dechiffre_1 = sdes_decrypt_text(int(bin(premiere_cle_trouvee), 2), texte_chiffre)
        texte_dechiffre_2 = sdes_decrypt_text(int(bin(deuxieme_cle_trouvee), 2), texte_dechiffre_1)
        print("Message original : ", texte_dechiffre_2)
    else:
        print("Aucune clé trouvée")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Temps d'exécution cassage astucieux : {execution_time} secondes\n")

if __name__ == "__main__":
    test_cassage_brutal()
    test_cassage_astucieux()
