from PIL import Image
from math import log
from imgOperation import ndg
from imgOperation import printMat
from imgOperation import initMatrix
from imgOperation import coccurrenceZero


def inergie(matrix,rows,cols):
    """
    calculer l inergie dune matrice
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :return: float()
    """
    result = float()
    for x in range(cols):
        for y in range(rows):
            result += (matrix[x][y])**2
    return result

def inertie(matrix, rows, cols):
    """
    calculer l inertie dune matrice
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :return: float()
    """
    result = float()
    for x in range(cols):
        for y in range(rows):
            result += matrix[x][y]*(x-y)**2
    return result

def entropie(matrix,rows,cols):
    """
    calculer l entropie dune matrice
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :return: float()
    """
    result = float()
    for x in range(cols):
        for y in range(rows):
            if log(matrix[y][x],10)> 0:
                result += log(matrix[y][x]) * matrix[y][x]
    return result

def momentDiffInverse(matrix,rows,cols):
    """
    calculer l moment Differentiel Inverse d'une matrice
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :return: float()
    """
    result = float()
    for x in range(cols):
        for y in range(rows):
            result += 1/(1+(x-y)**2)*matrix[x][y]
    return result

img = Image.open("C://Users/shous/Desktop/test.jpg")


m = ndg(img,8)
printMat(m)
print('\n')
m = coccurrenceZero(m)
##printMat(m)

"""
def coccurrence(matrix,cols,rows):

    rowMax = max(max(matrix))
    result = [[ 0 for x in range(rowMax+1)] for x in range(rowMax+1)]
    for x in range(cols):
       for y in range(rows-1):
           valx = matrix[x][y]
           valy = matrix[x+1][y]
           if matrix[x][y] == matrix[x][y+1]:
               result[valx][valy] += 1
           result[valx][valy] += 1
    printMat(result)
    return result

print('matrice coccurrence 0 degre')
m = coccurrenceZero(m,cols,rows)


print('inertie coccurrence 0 degre')
print(inertie(m,8,8))

print('energie coccurrence 0 degre')
print(inergie(m,8,8))

print('entropie coccurrence 0 degre')
print(entropie(m,8,8))

print('moument deffi inverse coccurrence 0 degre')
print(momentDiffInverse(m,8,8))
"""

