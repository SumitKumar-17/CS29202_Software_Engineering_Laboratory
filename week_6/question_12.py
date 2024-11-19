import numpy as np 
import cv2 as cv

image_file="a.png"

#reading the image file
X1=cv.imread(image_file)

if X1 is None:
    print("The file is not present or could not be read.")

else:
    X=X1.astype(np.float64)

    #converting the image to the greyscale image
    X=cv.cvtColor(X1,cv.COLOR_BGR2GRAY)

    #Question 12 solving
    #filter creation
    filter_1=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
    #showing the filtered image
    filtered_image=cv.filter2D(X1,-1,filter_1)
    cv.imshow('filtered image',filtered_image)
    # Waits for a keystroke
    cv.waitKey(0)
    # Destroys all the windows created
    cv.destroyAllWindows()




