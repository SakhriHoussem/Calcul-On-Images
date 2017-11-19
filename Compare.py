
from matplotlib import pyplot
import numpy

from PIL import Image

# reduce Vector
def reduce(color):
    '''
    reduce Color Vector by Malik
    :param color:
    :return: Vector
    '''
    Reduced  = [0 for x in range(8)]
    j = 0
    som = 0
    for i in range(256):
        som += color[i]
        if i%32 == 0:
            Reduced[j] = som
            j+=1
            som = 0
    return    Reduced

# create RGB Vector


def getRedVector(img,rows,cols):
    '''
    get rgb
    :param img:
    :param color:list(int)
    :param rows:
    :param cols:
    :return:
    '''
    vect = [0 for x in range(256)]
    for x in range(rows):
        for y in range(cols):
            val=img[x, y]
            rgb = val[2]
            vect[rgb] += 1
    return vect
def getBlueVector(img,rows,cols):
    '''
    get rgb
    :param img:
    :param color:list(int)
    :param rows:
    :param cols:
    :return:
    '''
    vect = [0 for x in range(256)]
    for x in range(rows):
        for y in range(cols):
            val=img[x, y]
            rgb = val[0]
            vect[rgb] += 1
    return vect
def getGreenVector(img,rows,cols):
    '''
    get rgb
    :param img:
    :param color:list(int)
    :param rows:
    :param cols:
    :return: list()
    '''
    vect = [0 for x in range(256)]
    for x in range(rows):
        for y in range(cols):
            val=img[x, y]
            rgb = val[1]
            vect[rgb] += 1
    return vect

def distance(histo1,histo2):
    '''
    calculer distance entre 2 histograme d image
    :param histo1: list()
    :param histo2: list()
    :return: int()
    '''
    i=0
    denominateur=0
    som = 0
    for i in range(len(histo1)):
        som+= histo1[i]-histo2[i]
        denominateur+= histo1[i]
    return som/denominateur




img = Image.open("C://Users/shous/Desktop/houssem.jpg")
pix = img.load()
cols,rows = img.size


img2 = Image.open("C://Users/shous/Desktop/viber image.jpg")
pix2 = img2.load()
cols2,rows2 = img2.size
x=cols
y=rows


Green =  [0 for x in range(256)]
Bleu=  [0 for x in range(256)]
Rouge=  [0 for x in range(256)]

Green2 =  [0 for x in range(256)]
Bleu2=  [0 for x in range(256)]
Rouge2=  [0 for x in range(256)]



GreenReduced = [0 for x in range(8)]
BleuReduced= [0 for x in range(8)]
RougeReduced= [0 for x in range(8)]

GreenReduced2 = [0 for x in range(8)]
BleuReduced2= [0 for x in range(8)]
RougeReduced2= [0 for x in range(8)]


Green=getGreenVector(pix,cols,rows)
Rouge=getRedVector(pix,cols,rows)
Bleu=getBlueVector(pix,cols,rows)
print("************green",Green)
print("************Rouge",Rouge)
print("************Blue",Bleu)


Green2=getGreenVector(pix2,cols2,rows2)
Rouge2=getRedVector(pix2,cols2,rows2)
Bleu2=getBlueVector(pix2,cols2,rows2)
print("************green2",Green2)
print("************Rouge2",Rouge2)
print("************Blue2",Bleu2)


GreenReduced = reduce(Green)
RougeReduced = reduce(Rouge)
BleuReduced = reduce(Bleu)


GreenReduced2 = reduce(Green2)
RougeReduced2 = reduce(Rouge2)
BleuReduced2 = reduce(Bleu2)


print("Green Reduced: ")
print(GreenReduced)

print("Rouge Reduced: ")
print(RougeReduced)

print("Bleu Reduced:  ")
print(BleuReduced)

print("Green Reduced2: ")
print(GreenReduced2)

print("Rouge Reduced2: ")
print(RougeReduced2)

print("Bleu Reduced2:  ")
print(BleuReduced2)

histo1 = RougeReduced + BleuReduced +GreenReduced
print('histo1 ',histo1)

histo2 = RougeReduced2 + BleuReduced2 +GreenReduced2
print('histo2 ',histo2)

print("distance entre les 2 images ",distance(histo1,histo2))


