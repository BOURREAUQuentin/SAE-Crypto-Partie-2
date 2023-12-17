""" Module pour le chiffrement et déchiffrement AES """

from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def chiffrement_aes(cle, message_clair):
    """
    Chiffre un texte de taille quelconque avec AES

    Args:
        cle (int): la clé de chiffrement
        message_clair (str): le message en clair à chiffrer

    Returns:
        (str): le message chiffré avec la clé de chiffrement
    """
    donnees_bytes = cle.to_bytes(32, 'big')  # converti la clé en bytes
    # initialise un vecteur d'initialisation pour le mode CFB
    vecteur_initialisation = b'\x00' * 16
    # crée un objet Cipher avec l'algorithme AES, le mode CFB, et la clé
    cipher = Cipher(algorithms.AES(donnees_bytes),
                    modes.CFB(vecteur_initialisation),
                    backend=default_backend())
    # initialise l'encrypteur
    encryptor = cipher.encryptor()
    # converti le message en clair en bytes
    message_clair_bytes = message_clair.encode('utf-8')
    # applique le bourrage PKCS7
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    message_clair_padded = padder.update(
        message_clair_bytes) + padder.finalize()
    # chiffre le message et finalise le processus de chiffrement
    message_chiffre = encryptor.update(
        message_clair_padded) + encryptor.finalize()
    # retourne le message chiffré encodé en base64
    return b64encode(message_chiffre)


def dechiffrement_aes(cle, message_chiffre):
    """
    Déchiffre un texte de taille quelconque avec AES

    Args:
        cle (int): la clé de chiffrement
        message_clair (str): le message en clair à déchiffrer

    Returns:
        (str): le message chiffré avec la clé de chiffrement
    """
    donnees_bytes = cle.to_bytes(32, 'big')  # converti la clé en bytes
    # décode le message chiffré depuis base64
    message_chiffre = b64decode(message_chiffre)
    # initialise un vecteur d'initialisation pour le mode CFB
    vecteur_initialisation = b'\x00' * 16
    # crée un objet Cipher avec l'algorithme AES, le mode CFB, et la clé
    cipher = Cipher(algorithms.AES(donnees_bytes),
                    modes.CFB(vecteur_initialisation),
                    backend=default_backend())
    # initialise le decrypteur
    decryptor = cipher.decryptor()
    # déchiffre le message et finalise le processus de déchiffrement
    message_dechiffre_padded = decryptor.update(
        message_chiffre) + decryptor.finalize()
    # crée un objet unpadder pour enlever le bourrage PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    # appliquer le débourrage au message déchiffré
    message_dechiffre = unpadder.update(
        message_dechiffre_padded) + unpadder.finalize()
    return message_dechiffre.decode('utf-8')
