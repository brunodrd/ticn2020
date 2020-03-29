from PIL import Image
import os


def resiz(file, basewidth=600):
    img = Image.open(file)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize),Image.ANTIALIAS)
    img.save(file.split('.')[0]+'_resize.jpg')

def samesize(file1,file2):
    resiz(file1)
    resiz(file2)
    file1 = file1.split('.')[0]+'_resize.jpg'
    file2 = file2.split('.')[0]+'_resize.jpg'
    im1 = Image.open(file1)
    im2 = Image.open(file2)
    minheight = min(im1.size[1],im2.size[1])
    #print(minheight)
    def handlefile(im1object,im2object,m,filename1,filename2):
        """
            Affecte la même taille aux 2 images;
            Sauve sous un autre autre nom (suffixe _new ajouté);
            Efface les fichiers temporaires inutiles
        """
        try:
            im1object = im1object.resize((im1object.size[0],m))
            im1object.save(filename1.split('.')[0]+'_new.jpg')
            im1object.close()
            im2object.close()
            os.remove(filename1)
            os.rename(filename2,filename2.split('.')[0]+'_new.jpg')
        except Exception as e:
            print("Erreur lors du traitement du fichier image")
            print(e)
        
    if im1.size[1] >im2.size[1]:
        handlefile(im1,im2,minheight,file1,file2)
    else:
        handlefile(im2,im1,minheight,file2,file1)
        
