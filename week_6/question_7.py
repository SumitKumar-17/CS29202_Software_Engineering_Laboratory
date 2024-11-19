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
    X=X.astype(int)


    #Question 7 solving
    # make Y transpose of x
    X_copy=copy.deepcopy(X)
    Y=np.transpose(X_copy)

    #multiply X and Y using the numpy library for the question in part 7
    Z=np.matmul(X,Y)
    print("The matrix multiplication using the numpy library is:")
    print(Z)

