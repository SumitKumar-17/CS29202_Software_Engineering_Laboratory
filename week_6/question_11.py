import numpy as np 
import cv2 as cv
import copy

image_file="a.png"

#reading the image file
X1=cv.imread(image_file)

if X1 is None:
    print("The file is not present or could not be read.")

else:
    X=X1.astype(np.float64)

    #converting the image to the greyscale image
    X=cv.cvtColor(X1,cv.COLOR_BGR2GRAY)


    #Question 11 solving
    Z50=copy.deepcopy(X)
    Z70=copy.deepcopy(X)
    Z100=copy.deepcopy(X)
    Z150=copy.deepcopy(X)

    #Thresholding the image of Z50,Z70,Z100,Z150
    print("Thresholding the image of Z50,Z70,Z100,Z150....")
    Z50[Z50>50]=1
    Z50[Z50<=50]=0

    Z70[Z70>70]=1
    Z70[Z70<=70]=0

    Z100[Z100>100]=1
    Z100[Z100<=100]=0

    Z150[Z150>150]=1
    Z150[Z150<=150]=0

    print("Thresholding the image of Z50,Z70,Z100,Z150 is done")





