
from PIL import Image
from math import log


def initMatrix(matrix,cols,rows):
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    return matrix

def ndg(matrix,rows,cols,t = False):
    '''
        calculer niveau de gris avce T
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :param t: bool()
    :return: list()
    '''

    mat = list()
    mat = initMatrix(mat,cols,rows) # init matrix a 0
    for x in range(cols):
        for y in range(rows):
            val = matrix[x, y]
            mat[x][y] = int(val[2]*0.299+val[1]*0.587+val[0]*0.114)
            if t != 0:
                mat[x][y] = int(mat[x][y]*t/256)
    return mat

def inergie(matrix,rows,cols):
    '''
    calculer l inergie dune matrice
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :return: float()
    '''
    result = float()
    for x in range(cols):
        for y in range(rows):
            result += (matrix[x][y])**2
    return result

def inertie(matrix, rows, cols):
    '''
    calculer l inertie dune matrice
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :return: float()
    '''
    result = float()
    for x in range(cols):
        for y in range(rows):
            result += matrix[x][y]*(x-y)**2
    return result

def entropie(matrix,rows,cols):
    '''
    calculer l entropie dune matrice
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :return: float()
    '''
    result = float()
    for x in range(cols):
        for y in range(rows):
            result += matrix[x][y]*log(matrix[x][y])
    return -result

def momentDiffInverse(matrix,rows,cols):
    '''
    calculer l moment Differentiel Inverse d'une matrice
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :return: float()
    '''
    result = float()
    for x in range(cols):
        for y in range(rows):
            result += 1/(1+(x-y)**2)*matrix[x][y]
    return result

img = Image.open("C://Users/shous/Desktop/houssem.jpg")
pix = img.load()
cols, rows = img.size
m= ndg(pix, cols, rows,8)
v = img.getpixel((1, 1))




for x in range(rows):
   print(m[x])



