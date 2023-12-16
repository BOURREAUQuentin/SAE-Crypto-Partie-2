from scapy.all import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def dechiffrer_ASE_CBC(cle, iv, texte_chiffre):
    cle_bytes = cle.to_bytes(32, 'big')
    cipher = Cipher(algorithms.AES(cle_bytes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    texte_dechiffre = decryptor.update(texte_chiffre) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    texte_dechiffre_unpadded = unpadder.update(texte_dechiffre) + unpadder.finalize()
    return texte_dechiffre_unpadded

def extraire_messages(liste_paquets, cle_64_bits):
    liste_messages = []
    for paquet in liste_paquets:
        if "UDP" in paquet and paquet["UDP"].dport == 9999:
            donnees_paquet = paquet[Raw].load
            iv = donnees_paquet[:16]
            texte_chiffre = donnees_paquet[16:]
            message_dechiffre = dechiffrer_ASE_CBC(cle_64_bits, iv, texte_chiffre)
            liste_messages.append(message_dechiffre.decode("utf8"))
    return liste_messages

def afficher_messages(liste_messages):
    for (i, message) in enumerate(liste_messages):
        print("Message",(i+1), ":", message)

if __name__ == "__main__":
    trace = rdpcap('trace_sae.cap') # chargement de la trace réseau
    cle_256_bits = 0b1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100
    messages = extraire_messages(trace, cle_256_bits)
    afficher_messages(messages)
