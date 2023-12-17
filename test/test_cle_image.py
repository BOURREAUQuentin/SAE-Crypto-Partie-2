""" Module de tests de recherche de clé dans les images """
# pylint: disable=E0401, C0413
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from cassages import CONST
from cle_image import trouver_cle_image


def test_trouver_cle_image():
    """
    Test de la recherche de clé dans l'image
    """
    assert trouver_cle_image(
        CONST.CleImage.CHEMIN_CLE_IMAGE.value
    ) == "1110011101101101001100010011111110010010101110011001000001001100"


if __name__ == "__main__":
    test_trouver_cle_image()
