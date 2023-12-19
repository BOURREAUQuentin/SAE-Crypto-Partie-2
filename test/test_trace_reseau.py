""" Module de tests de la trace réseau (filtrage des messages) """
# pylint: disable=E0401, C0413, C0301
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from scapy.all import rdpcap
from trace_reseau import extraire_messages, afficher_messages

if __name__ == "__main__":
    trace = rdpcap('./trace_sae.cap')  # chargement de la trace réseau
    CLE_256_BITS = 0b1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100
    messages = extraire_messages(trace, CLE_256_BITS)
    afficher_messages(messages)
