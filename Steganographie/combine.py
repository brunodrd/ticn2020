from PIL import Image
#
def combine(pix1,pix2):
    """
    Récupère les 4 bits de poids forts de la représentation binaire
    de deux nombres A7...A0, B7...B0 et les combine sous la forme:
    A7A6A5A4 B7B6B5B4
    Entrées: pix1, pix2 deux entiers traduisant la composante r, v ou b
    d'un pixel;
    Retour: chaine de caractères résultant de la concaténation des 4 bits
    de poids forts de chaque nombre.    
    """
    
    #bpix1 = "{:0>8}".format(bin(pix1)[2:])
    bpix1 = "{:08b}".format(pix1)
    #bpix2 ="{:0>8}".format(bin(pix2)[2:])
    bpix2 ="{:08b}".format(pix2)
    return int(bpix1[:4]+bpix2[:4],base=2)
    #return bpix1[:4]+bpix2[:4]

def separe(pix):
    bpix = "{:08b}".format(pix)
    return (int(bpix[:4]+'0000',base=2),int(bpix[4:]+'0000',base=2))
