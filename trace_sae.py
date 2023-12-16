""" Module pour filtrer les messages échangés à partir d'une trace réseau """

from scapy.all import rdpcap, Raw
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import constantes as CONST

def dechiffrer_aes_cbc(cle, vecteur_initialisation, texte_chiffre):
    """
    Déchiffre un texte chiffré en AES à partir d'une clé et d'un vecteur
    d'initialisation de 16 bits

    Args:
        cle (bin): la clé utilisé pour le texte chiffré (AES-256)
        vecteur_initialisation (bytes): le vecteur d'initialisation utilisé
                                        pour le mode de chiffrement CBC (Cipher
                                        Block Chaining) avec l'algorithme AES
        texte_chiffre (bytes): le texte chiffré sans compter le vecteur d'initialisation

    Returns:
        (bytes): le texte déchiffré avec le chiffrement CBC avec l'algorithme AES
    """
    cle_bytes = cle.to_bytes(32, 'big')
    cipher = Cipher(algorithms.AES(cle_bytes),
                    modes.CBC(vecteur_initialisation),
                    backend=default_backend())
    decryptor = cipher.decryptor()
    texte_dechiffre = decryptor.update(texte_chiffre) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    texte_dechiffre_unpadded = unpadder.update(
        texte_dechiffre) + unpadder.finalize()
    return texte_dechiffre_unpadded


def extraire_messages(liste_paquets, cle_256_bits):
    """
    Extrait les paquets reçus sur la trace réseau en messages clairs

    Args:
        liste_paquets (list): la liste des paquets sur la trace réseau
        cle_256_bits (bin): la clé utilisée pour le chiffrement des messages

    Returns:
        (list): la liste des messages clairs sur la trace réseau
    """
    liste_messages = []
    for paquet in liste_paquets:
        if "UDP" in paquet and paquet[
                "UDP"].dport == CONST.TraceReseau.PORT.value:
            donnees_paquet = paquet[Raw].load
            vecteur_initialisation = donnees_paquet[:CONST.TraceReseau.
                                                    TAILLE_VECTEUR_INITIALISATION
                                                    .value]
            texte_chiffre = donnees_paquet[
                CONST.TraceReseau.TAILLE_VECTEUR_INITIALISATION.value:]
            message_dechiffre = dechiffrer_aes_cbc(cle_256_bits,
                                                   vecteur_initialisation,
                                                   texte_chiffre)
            liste_messages.append(message_dechiffre.decode("utf8"))
    return liste_messages


def afficher_messages(liste_messages):
    """
    Affiche chaque message de la trace réseau

    Args:
        liste_messages (list): la liste des messages
    """
    for (i, message) in enumerate(liste_messages):
        print("Message", i + 1, ":", message)


if __name__ == "__main__":
    trace = rdpcap('trace_sae.cap')  # chargement de la trace réseau
    CLE_256_BITS = 0b1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100
    messages = extraire_messages(trace, CLE_256_BITS)
    afficher_messages(messages)
