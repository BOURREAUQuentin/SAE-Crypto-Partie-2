""" Module pour chiffrer un texte quelconque, quelle que soit sa taille avec double SDES """

from SDES import decrypt, encrypt
import time

def sdes_encrypt_text(cle, message_clair):
    """Chiffre un texte de taille quelconque avec SDES"""
    texte_chiffre = ""
    for lettre in message_clair:
        lettre_chiffree = encrypt(cle, ord(lettre))
        texte_chiffre += chr(lettre_chiffree)
    return texte_chiffre

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

if __name__ == "__main__":
    premiere_cle = 0b1110001110
    seconde_cle = 0b1110100110
    text = "test"
    encrypted_text1 = sdes_encrypt_text(premiere_cle, text)
    print("Texte chiffré 1er passage : ", encrypted_text1)
    encrypted_text2 = sdes_encrypt_text(seconde_cle, encrypted_text1)
    print("Texte chiffré 2e passage : ", encrypted_text2)
    decrypted_text1 = sdes_decrypt_text(seconde_cle, encrypted_text2)
    print("Texte déchiffré 1er passage : ", decrypted_text1)
    decrypted_text2 = sdes_decrypt_text(premiere_cle, decrypted_text1)
    print("Texte déchiffré 2e passage : ", decrypted_text2)
