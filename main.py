#All images need to be the same dimension, so this will contain all the functions necessary to convert the photos
from helper_functions import *

imageArray = load_images()
meanCentered = calculateMean(imageArray)