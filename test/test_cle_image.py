""" Module de tests de recherche de clé dans les images """
# pylint: disable=E0401, C0413
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from cle_image import trouver_cle_image

def test_trouver_cle_image():
    print(trouver_cle_image("./rossignol2.bmp"))

if __name__ == "__main__":
    test_trouver_cle_image()
