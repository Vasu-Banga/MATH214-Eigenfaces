#All images need to be the same dimension, so this will contain all the functions necessary to convert the photos
from helper_functions import *
import numpy as np
from numpy.linalg import eig


#Check if data has been parsed before

print("Loading images: ")
imageArray = load_images()
print("Done loading images")
print("Loading mean: ")
meanCentered = calculateMean(imageArray)
print("Mean centered")
# test = [[0, -4/3 -10/3],[3,-1/3,14/3],[-3,5/3,-4/3]]
print("Loading covariant matrix: ")
covarMatrix = calculateCovariance(meanCentered)
print("Covariance calculated")
print("Loading eigenvalues and eigenvectors: ")
convertedMatrix = np.array(covarMatrix)
print("Matrix successfully converted")
w,v = eig(convertedMatrix)
print("Found eigenvalues and eigenvectors")
print("Sorting faces")
parseFaces(w,v)
print("Faces sorted")


