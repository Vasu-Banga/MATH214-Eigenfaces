import os
from os import listdir
import time
import numpy as np
faceDir = "./Files/debugFaces/"
uniqueFaces = 0
eigenfaces = []
names = []
totalNames = []

def read_pgm(file):
    line = file.readline()
    try:
        line = str(line, 'utf-8')
    except:
        return False
    assert line == 'P5\n'
    (width, height) = [int(i) for i in file.readline().split()]
    depth = int(file.readline())
    assert depth <= 255

    raster = []
    for i in range(height * width):
        raster.append(ord(file.read(1)))
    return raster

def load_images():
    databaseArray = []
    global uniqueFaces
    global totalNames
    for image in os.listdir(faceDir):
        file = open(faceDir + image, 'rb')
        if (image[len(image) - 8 : len(image) - 4]) == "0001":
            uniqueFaces += 1
        # print(file.read())
        array = read_pgm(file)
        if array != False:
            totalNames.append(image[:len(image) - 9])
            if len(array) != 4096:
                print("ERROR")
            else:
                databaseArray.append(array)
        else:
            print("Failed on ", image)
    return databaseArray


def calculateMean(imgArr):
    for i in range(len(imgArr[0])):
        #go through each column, add up and take the mean value of that pixel
        sum = 0
        for img in imgArr:
            sum += img[i]
        mean = sum / len(imgArr)
        for img in imgArr:
            img[i] = img[i] - mean
        if i % int(len(imgArr[0])/15) == 0:
            print(".", end=" ",flush=True)
    print("\n")
    return imgArr

def calculateCovariance(meanCentered):
    returnVal = []
    for row in range(len(meanCentered[0])):
        newRow = []
        start = time.time()
        for col in range(len(meanCentered[0])):
            if col == row:
                #Calculate variance
                var = 0
                for i in range(len(meanCentered)):
                    var += pow(meanCentered[i][col],2)
                var = var / (len(meanCentered))
                newRow.append(var)
            else:
                #Calculate covariance
                    covar = 0
                    for i in range(len(meanCentered)):
                        covar += meanCentered[i][col] * meanCentered[i][row]
                    covar = covar / (len(meanCentered))
                    newRow.append(covar)
        end = time.time()
        returnVal.append(newRow)
        print("\r",end="")
        print(str(row) + ", Time elapsed: " + str(end - start), end="")
    print("\n")
    return returnVal

def parseFaces(w,v):
    global eigenfaces
    global names
    global totalNames
    indexes = []
    for i in range(len(w)):
        indexes.append(i)
    w = np.array(w)
    v = np.array(v)
    indicies = np.array(indexes)
    sortKey = np.argsort(w,axis=0)
    values = w[sortKey]
    vectors = v[sortKey]
    indicies = indicies[sortKey]
    indicies = indicies.tolist()
    np.flip(vectors,0)
    np.flip(values,0)
    indicies.reverse()
    values = values[:uniqueFaces]
    vectors = vectors[:uniqueFaces]
    indicies = indicies[:uniqueFaces]
    for i in range(uniqueFaces):
        try:
            names.append(totalNames[int(indicies[i])])
            eigenfaces.append(vectors[i])
        except:
            print("Failed on type " + str(type(indicies[i])) + " for value " + str(indicies[i]))

def displayNames():
    global names
    for name in names:
        print("Faces found: " + name)

