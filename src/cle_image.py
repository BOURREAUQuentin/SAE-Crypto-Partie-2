""" Module pour la recherche de clé dans les images """

from PIL import Image
import constantes as CONST

def trouver_cle_image(image_contenant_cle):
    """
    Trouve la clé cachée dans l'image

    Args:
        image_contenant_cle (str): le chemin de l'image où
        chercher la clé

    Returns:
        (str): la clé trouvée dans l'image
    """
    image_contenant_cle = Image.open(image_contenant_cle)
    cle_de_session_cachee = ""
    for pixel in range(CONST.CleImage.NOMBRE_BITS_CLE_IMAGE.value):
        pixel_contenant_cle = image_contenant_cle.getpixel((pixel, 0))
        cle_de_session_cachee += str(pixel_contenant_cle % 2)
    return cle_de_session_cachee
