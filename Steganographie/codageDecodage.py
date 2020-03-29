from PIL import Image
from combine import combine, separe
import sys


def codage(file1,file2):
    try:
        im1 = Image.open(file1)
        im2 = Image.open(file2)
    except Exception as e:
        print("Problème lors de l'ouverture d'un fichier")
        print(f"Le système signale l'erreur {e}")
        sys.exit()
    w,h = im1.size
    im0 = Image.new('RGB',(w,h))
    try:
        for j in range(h):
            for i in range(w):
                r1,v1,b1 = im1.getpixel((i,j))
                r2,v2,b2 = im2.getpixel((i,j))
                r0,v0,b0 = combine(r1,r2),combine(v1,v2),combine(b1,b2)
                im0.putpixel((i,j),(r0,v0,b0))
        im0.save('resultat.tif')
    except Exception as e:
        print("Pb codage")
        print(e)
    finally:
        im1.close()
        im2.close()
        im0.close()
def decodage(file):
    im = Image.open(file)
    w,h = im.size
    im1 = Image.new('RGB',(w,h))
    im2 = Image.new('RGB',(w,h))
    for j in range(h):
        for i in range(w):
            r,v,b = im.getpixel((i,j))
            r1,r2 = separe(r)
            v1,v2 = separe(v)
            b1,b2 = separe(b)
            im1.putpixel((i,j),(r1,v1,b1))
            im2.putpixel((i,j),(r2,v2,b2))
    im1.save('res1.tif')
    im2.save('res2.tif')
    im.close()
    im1.close()
    im2.close()
