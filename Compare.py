from PIL import Image
import imgOperation as op

img = Image.open("img/test.jpg")
img2 = Image.open("img/test.jpg")

Green=op.getGreenVector(img)
Rouge=op.getRedVector(img)
Bleu=op.getBlueVector(img)
print("************green",Green)
print("************Rouge",Rouge)
print("************Blue",Bleu)


Green2=op.getGreenVector(img2)
Rouge2=op.getRedVector(img2)
Bleu2=op.getBlueVector(img2)
print("************green2",Green2)
print("************Rouge2",Rouge2)
print("************Blue2",Bleu2)

GreenReduced = op.reduce(Green)
RougeReduced = op.reduce(Rouge)
BleuReduced = op.reduce(Bleu)

GreenReduced2 = op.reduce(Green2)
RougeReduced2 = op.reduce(Rouge2)
BleuReduced2 = op.reduce(Bleu2)


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

print("distance entre les 2 images ",op.distance(histo1,histo2))


