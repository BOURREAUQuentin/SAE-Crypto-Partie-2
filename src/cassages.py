""" Module pour les cassages de sdes (brutal et astucieux) """

from double_sdes import chiffrement_sdes, dechiffrement_sdes, double_dechiffrement_sdes
import constantes as CONST


def cassage_brutal(message_clair, message_chiffre):
    """
    Cassage brutal du chiffrement double SDES

    Args:
        message_clair (str): le message en clair
        message_chiffre (str): le message chiffré

    Returns:
        (tuple): le tuple contenant la 1ère clé et la 2ème clé possiblement utilisé pour le
                 chiffrement du message
    """
    for premiere_cle in range(
            0,
            CONST.NOMBRE_CLES_POSSIBLES):  # 2**10 possibilités clé de 10 bits
        for seconde_cle in range(
                0, CONST.NOMBRE_CLES_POSSIBLES):  # même chose que premiere_cle
            # déchiffre le message avec les clés en cours d'essai
            texte_dechiffre_resultat = double_dechiffrement_sdes(
                premiere_cle, seconde_cle, message_chiffre)
            # si le texte déchiffré correspond au message en clair
            if texte_dechiffre_resultat == message_clair:
                return seconde_cle, premiere_cle  # les clés correctes ont été trouvées
    return None, None  # si aucune clé correcte n'est trouvée


def cassage_astucieux(message_clair, message_chiffre):
    """
    Cassage astucieux avec meet-in-the-middle sur le chiffrement double SDES

    Args:
        message_clair (str): le message en clair
        message_chiffre (str): le message chiffré

    Returns:
        (tuple): le tuple contenant la 1ère clé et la 2ème clé possiblement utilisé pour le
                 chiffrement du message
    """
    # précalcule les résultats intermédiaires pour le chiffrement avec la première clé
    dict_resultats_intermediaires = {}
    for premiere_cle in range(0, CONST.NOMBRE_CLES_POSSIBLES):
        texte_chiffre_intermediaire = chiffrement_sdes(premiere_cle,
                                                       message_clair)
        dict_resultats_intermediaires[
            texte_chiffre_intermediaire] = premiere_cle
    # teste les déchiffrements avec la deuxième clé et chercher une correspondance
    for seconde_cle in range(0, CONST.NOMBRE_CLES_POSSIBLES):
        texte_dechiffre_intermediaire = dechiffrement_sdes(
            seconde_cle, message_chiffre)
        # si un texte déchiffré correspond à un résultat intermédiaire trouvé avant
        if texte_dechiffre_intermediaire in dict_resultats_intermediaires:
            premiere_cle = dict_resultats_intermediaires[
                texte_dechiffre_intermediaire]
            return seconde_cle, premiere_cle
    return None, None  # si aucune clé correcte n'est trouvée
