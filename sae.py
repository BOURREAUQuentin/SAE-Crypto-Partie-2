""" Module pour chiffrer un texte quelconque, quelle que soit sa taille avec double SDES """

import time
from SDES import decrypt, encrypt
import constantes as CONST

def sdes_encrypt_text(cle, message_clair):
    """Chiffre un texte de taille quelconque avec SDES"""
    message_chiffre = ""
    for lettre in message_clair:
        lettre_chiffree = encrypt(cle, ord(lettre))
        message_chiffre += chr(lettre_chiffree)
    return message_chiffre

def sdes_decrypt_text(cle, message_chiffre):
    """Déchiffre un texte de taille quelconque avec SDES"""
    message_dechiffre = ""
    for lettre in message_chiffre:
        lettre_dechiffree = decrypt(cle, ord(lettre))
        message_dechiffre += chr(lettre_dechiffree)
    return message_dechiffre

def double_sdes_encrypt_text(premiere_cle, seconde_cle, message_clair):
    """Double chiffrement d'un texte de taille quelconque avec SDES"""
    message_chiffre_intermediaire = sdes_encrypt_text(premiere_cle, message_clair)
    message_chiffre_final = sdes_encrypt_text(seconde_cle, message_chiffre_intermediaire)
    return message_chiffre_final

def double_sdes_decrypt_text(premiere_cle, seconde_cle, message_chiffre):
    """Double déchiffrement d'un texte de taille quelconque avec SDES"""
    message_dechiffre_intermediaire = sdes_decrypt_text(seconde_cle, message_chiffre)
    message_dechiffre_final = sdes_decrypt_text(premiere_cle, message_dechiffre_intermediaire)
    return message_dechiffre_final

def cassage_brutal(message_clair, message_chiffre):
    """Cassage brutal du chiffrement double SDES"""
    for premiere_cle in range(0, CONST.NOMBRE_CLES_POSSIBLES): # 2**10 possibilités -> clé de 10 bits
        for seconde_cle in range(0, CONST.NOMBRE_CLES_POSSIBLES): # même chose que premiere_cle
            decrypted_text_result = double_sdes_decrypt_text(premiere_cle, seconde_cle, message_chiffre)
            if decrypted_text_result == message_clair:
                return seconde_cle, premiere_cle   # Les clés correctes ont été trouvées
    return None, None  # si aucune clé correcte n'est trouvée

def cassage_astucieux(message_clair, message_chiffre):
    """Cassage astucieux avec meet-in-the-middle sur le chiffrement double SDES"""
    # Précalculer les résultats intermédiaires pour le chiffrement avec la première clé
    dict_resultats_intermediaires = {}
    for premiere_cle in range(0, CONST.NOMBRE_CLES_POSSIBLES):
        texte_chiffre_intermediaire = sdes_encrypt_text(premiere_cle, message_clair)
        dict_resultats_intermediaires[texte_chiffre_intermediaire] = premiere_cle
    # Tester les déchiffrements avec la deuxième clé et chercher une correspondance
    for seconde_cle in range(0, CONST.NOMBRE_CLES_POSSIBLES):
        texte_dechiffre_intermediaire = sdes_decrypt_text(seconde_cle, message_chiffre)
        if texte_dechiffre_intermediaire in dict_resultats_intermediaires:
            premiere_cle = dict_resultats_intermediaires[texte_dechiffre_intermediaire]
            return seconde_cle, premiere_cle
    return None, None # si aucune clé correcte n'est trouvée

if __name__ == "__main__":
    texte_chiffre_1 = sdes_encrypt_text(CONST.PREMIERE_CLE_TEST, CONST.TEXTE_TEST)
    print("Texte chiffré 1er passage : ", texte_chiffre_1)
    texte_chiffre_2 = sdes_encrypt_text(CONST.DEUXIEME_CLE_TEST, texte_chiffre_1)
    print("Texte chiffré 2e passage : ", texte_chiffre_2)
    texte_dechiffre_1 = sdes_decrypt_text(CONST.DEUXIEME_CLE_TEST, texte_chiffre_2)
    print("Texte déchiffré 1er passage : ", texte_dechiffre_1)
    texte_dechiffre_2 = sdes_decrypt_text(CONST.PREMIERE_CLE_TEST, texte_dechiffre_1)
    print("Texte déchiffré 2e passage : ", texte_dechiffre_2)

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
    print(f"Temps d'exécution cassage brutal : {execution_time} secondes")

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
    print(f"Temps d'exécution cassage astucieux : {execution_time} secondes")
