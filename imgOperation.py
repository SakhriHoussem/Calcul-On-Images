
def coccurrenceZero(matrix):
    """
     calcul cocurance de matrix
    :param matrix:
    :param cols: column de matrix
    :param rows: ligne de matrix
    :return:
    """
    result = list
    rows = len(matrix)
    cols = len(matrix[0])
    rowMax = findMax(matrix)
    print("max : ",rowMax)
    result = initMatrix(result,rowMax+1,rowMax+1)
    for y in range(rows):
       for x in range(cols-1):
           vx = matrix[y][x]
           vy = matrix[y][x+1]
           result[vy][vx] += 1
           if matrix[y][x] == matrix[y][x+1]:
               result[vy][vx] += 1
    return result



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


def getRedVector(img):
    '''
    get rgb
    :param img:
    :param color:list(int)
    :param rows:
    :param cols:
    :return:
    '''
    cols,rows = img.size
    vect = [0 for x in range(256)]
    for y in range(rows):
        for x in range(cols):
            val=img.getpixel((x,y))
            rgb = val[2]
            vect[rgb] += 1
    return vect
def getBlueVector(img):
    '''
    get rgb
    :param img:
    :param color:list(int)
    :param rows:
    :param cols:
    :return:
    '''
    cols,rows = img.size
    vect = [0 for x in range(256)]
    for y in range(rows):
        for x in range(cols):
            val=img.getpixel((x, y))
            rgb = val[0]
            vect[rgb] += 1
    return vect
def getGreenVector(img):
    '''
    get rgb
    :param img:
    :param color:list(int)
    :param rows:
    :param cols:
    :return: list()
    '''

    cols, rows = img.size
    vect = [0 for x in range(256)]
    for y in range(rows):
        for x in range(cols):
            val = img.getpixel((x, y))
            rgb = val[1]
            vect[rgb] += 1
    return vect


def printMat (matrix):
    """
    affiche le contenu de la matrice
    :param matrix: list()
    """
    for row in range(len(matrix)):
       print(matrix[row])
def findMax(matrix):
    return max(max(x) for x in matrix)

def distance(histo1,histo2):
    '''
    calculer distance entre 2 histograme d image
    :param histo1: list()
    :param histo2: list()
    :return: int()
    '''
    denominateur=0
    som = 0
    for i in range(len(histo1)):
        som+= histo1[i]-histo2[i]
        denominateur+= histo1[i]
    return som/denominateur

def initMatrix(matrix,cols,rows):
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    return matrix


def ndg(img,t = False):
    """
    calculer niveau de gris avce T
    :param matrix: list()
    :param rows: int()
    :param cols: int()
    :param t: bool()
    :return: list()
    """
    cols, rows = img.size
    mat = list()
    mat = initMatrix(mat,cols,rows) # init matrix a 0
    for y in range(rows):
        for x in range(cols):
            val = img.getpixel((x,y))
            mat[y][x] = int(val[0]*0.299+val[1]*0.587+val[1]*0.114)
            if t != 0:
                mat[y][x] = int(mat[y][x]*t/256)
    return mat
