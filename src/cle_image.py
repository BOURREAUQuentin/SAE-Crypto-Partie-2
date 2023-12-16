""" Module pour la recherche de clé dans les images """

from PIL import Image

def trouver_cle_image(image_contenant_cle):
    image_contenant_cle = Image.open(image_contenant_cle)
    cle_de_session_cachee = ""
    for x in range(64):
        pixel_contenant_cle = image_contenant_cle.getpixel((x, 0))
        cle_de_session_cachee += str(pixel_contenant_cle % 2)
    return cle_de_session_cachee
