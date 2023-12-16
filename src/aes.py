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
    donnees_bytes = cle.to_bytes(32, 'big')
    vecteur_initialisation = b'\x00' * 16
    cipher = Cipher(algorithms.AES(donnees_bytes), modes.CFB(vecteur_initialisation),
                    backend=default_backend())
    encryptor = cipher.encryptor()
    message_clair_bytes = message_clair.encode('utf-8')
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    message_clair_padded = padder.update(message_clair_bytes) + padder.finalize()
    message_chiffre = encryptor.update(message_clair_padded) + encryptor.finalize()
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
    donnees_bytes = cle.to_bytes(32, 'big')
    message_chiffre = b64decode(message_chiffre)
    vecteur_initialisation = b'\x00' * 16
    cipher = Cipher(algorithms.AES(donnees_bytes), modes.CFB(vecteur_initialisation),
                    backend=default_backend())
    decryptor = cipher.decryptor()
    message_dechiffre_padded = decryptor.update(message_chiffre) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    message_dechiffre = unpadder.update(message_dechiffre_padded) + unpadder.finalize()
    return message_dechiffre.decode('utf-8')
