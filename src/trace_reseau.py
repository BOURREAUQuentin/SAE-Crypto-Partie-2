""" Module pour filtrer les messages échangés à partir d'une trace réseau """

from scapy.all import Raw
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
    cle_bytes = cle.to_bytes(32, 'big')  # converti la clé en bytes
    # crée un objet Cipher avec l'algorithme AES, le mode CBC et la clé
    cipher = Cipher(algorithms.AES(cle_bytes),
                    modes.CBC(vecteur_initialisation),
                    backend=default_backend())  # crée un objet Cipher
    decryptor = cipher.decryptor()  # initialise le décrypteur
    # déchiffre le texte et finalise le processus de déchiffrement
    texte_dechiffre = decryptor.update(texte_chiffre) + decryptor.finalize()
    # crée un objet unpadder pour enlever le bourrage PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    # applique le débourrage au texte déchiffré
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
    liste_messages = []  # liste des messages extraits
    for paquet in liste_paquets:
        # vérifie si le paquet est de type UDP et a le port attendu (9999)
        if "UDP" in paquet and paquet[
                "UDP"].dport == CONST.TraceReseau.PORT.value:
            donnees_paquet = paquet[Raw].load  # Extrait les données du paquet
            # extrait le vecteur d'initialisation du début des données du paquet
            vecteur_initialisation = donnees_paquet[:CONST.TraceReseau.
                                                    TAILLE_VECTEUR_INITIALISATION
                                                    .value]
            # extrait le texte chiffré à partir des données du paquet
            texte_chiffre = donnees_paquet[
                CONST.TraceReseau.TAILLE_VECTEUR_INITIALISATION.value:]
            # déchiffre le texte chiffré
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
