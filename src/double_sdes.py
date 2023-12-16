""" Module pour chiffrer un texte quelconque, quelle que soit sa taille avec double SDES """

from sdes import decrypt, encrypt

def chiffrement_sdes(cle, message_clair):
    """
    Chiffre un texte de taille quelconque avec SDES

    Args:
        cle (int): la clé de chiffrement
        message_clair (str): le message en clair à chiffrer

    Returns:
        (str): le message chiffré avec la clé de chiffrement
    """
    message_chiffre = ""
    for lettre in message_clair:
        lettre_chiffree = encrypt(cle, ord(lettre))
        message_chiffre += chr(lettre_chiffree)
    return message_chiffre

def dechiffrement_sdes(cle, message_chiffre):
    """
    Déchiffre un texte de taille quelconque avec SDES

    Args:
        cle (int): la clé de chiffrement
        message_clair (str): le message en clair à déchiffrer

    Returns:
        (str): le message chiffré avec la clé de chiffrement
    """
    message_dechiffre = ""
    for lettre in message_chiffre:
        lettre_dechiffree = decrypt(cle, ord(lettre))
        message_dechiffre += chr(lettre_dechiffree)
    return message_dechiffre

def double_chiffrement_sdes(premiere_cle, seconde_cle, message_clair):
    """
    Double chiffrement d'un texte de taille quelconque avec SDES

    Args:
        premiere_cle (int): la première clé de chiffrement
        seconde_cle (int): la deuxième clé de chiffrement
        message_clair (str): le message en clair à chiffrer

    Returns:
        (str): le message chiffré avec les deux clés de chiffrement
    """
    message_chiffre_intermediaire = chiffrement_sdes(premiere_cle, message_clair)
    message_chiffre_final = chiffrement_sdes(seconde_cle, message_chiffre_intermediaire)
    return message_chiffre_final

def double_dechiffrement_sdes(premiere_cle, seconde_cle, message_chiffre):
    """
    Double déchiffrement d'un texte de taille quelconque avec SDES

    Args:
        premiere_cle (int): la première clé de chiffrement
        seconde_cle (int): la deuxième clé de chiffrement
        message_clair (str): le message en clair à chiffrer

    Returns:
        (str): le message chiffré avec les deux clés de chiffrement
    """
    message_dechiffre_intermediaire = dechiffrement_sdes(seconde_cle, message_chiffre)
    message_dechiffre_final = dechiffrement_sdes(premiere_cle, message_dechiffre_intermediaire)
    return message_dechiffre_final
