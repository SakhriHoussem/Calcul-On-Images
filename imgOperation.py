
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
    print(rows,'*',cols)
    vect = [0 for x in range(256)]
    for x in range(cols):
        for y in range(rows):
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
    for x in range(cols):
        for y in range(rows):
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
    print(cols,' ',rows)
    print(range(rows))
    vect = [0 for x in range(256)]
    for x in range(cols):
        for y in range(rows):
            val = img.getpixel((x, y))
            rgb = val[1]
            vect[rgb] += 1
    return vect


def printMat (matrix):
    """
    affiche le contenu de la matrice
    :param matrix: list()
    """
    for x in range(len(matrix)):
       print(matrix[x])

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
    print(cols,'*',rows)
    mat = list()
    mat = initMatrix(mat,rows,cols) # init matrix a 0
    for x in range(rows):
        for y in range(cols):
            val = img.getpixel((y,x))
            mat[y][x] = int(val[2]*0.299+val[1]*0.587+val[0]*0.114)
            if t != 0:
                mat[x][y] = int(mat[x][y]*t/256)
    return mat
