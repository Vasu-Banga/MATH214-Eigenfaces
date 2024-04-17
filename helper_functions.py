import os
from os import listdir
faceDir = "./Files/faces/"

def read_pgm(file):
    line = file.readline()
    line = str(line, 'utf-8')
    assert line == 'P5\n'
    (width, height) = [int(i) for i in file.readline().split()]
    depth = int(file.readline())
    assert depth <= 255

    raster = []
    for i in range(height * width):
        raster.append(ord(file.read(1)))
    # for y in range(height):
    #     row = []
    #     for y in range(width):
    #         row.append(ord(file.read(1)))
    #     raster.append(row)
    return raster

def load_images():
    databaseArray = []
    for image in os.listdir(faceDir):
        file = open(faceDir + image, 'rb')
        # print(file.read())
        array = read_pgm(file)
        if len(array) != 4096:
            print("ERROR")
        else:
            databaseArray.append(array)
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
    return imgArr