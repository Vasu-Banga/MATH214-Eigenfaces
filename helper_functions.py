import os
from os import listdir
faceDir = "./Files/smallerFaces/"

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
    for image in os.listdir(faceDir):
        print(image)
        file = open(faceDir + image, 'rb')
        # print(file.read())
        array = read_pgm(file)
        if array != False:
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
    products = []
    sums = []
    covars = []
    for row in range(len(meanCentered[0])):
        newRow = []
        for col in range(len(meanCentered[0])):
            if col == row:
                #Calculate variance
                var = 0
                for i in range(len(meanCentered)):
                    var += pow(meanCentered[i][col],2)
                var = var / (len(meanCentered) - 1)
                newRow.append(var)
            else:
                #Calculate covariance
                if ((row * col) in products) and ((row + col) in sums):
                    newRow.append(covars[products.index(row * col)])
                else:
                    covar = 0
                    for i in range(len(meanCentered)):
                        covar += meanCentered[i][col] * meanCentered[i][row]
                    covar = covar / (len(meanCentered) - 1)
                    newRow.append(covar)
                    products.append(row * col)
                    sums.append(row + col)
                    covars.append(covar)
        returnVal.append(newRow)
        print("\r",end="")
        print(row, end="")
    print("\n")
    return returnVal