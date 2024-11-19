import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

image_file="a.png"

#reading the image file
X1=cv.imread(image_file)

if X1 is None:
    print("The file is not present or could not be read.")

else:
    X=X1.astype(np.float64)

    #converting the image to the greyscale image
    X=cv.cvtColor(X1,cv.COLOR_BGR2GRAY)


    #Question 10 solving
    X[40:71,100:201]=0
    cv.imshow('greyscale image rectangular box',X)
    # Waits for a keystroke
    cv.waitKey(0)
    # Destroys all the windows created
    cv.destroyAllWindows()






