import numpy as np 
import cv2 as cv

image_file="a.png"

#reading the image file
X1=cv.imread(image_file)

if X1 is None:
    print("The file is not present or could not be read.")

else:
    X=X1.astype(np.float64)


    #Question 6 solving
    X=cv.cvtColor(X1,cv.COLOR_BGR2GRAY)
    #converting the image to the greyscale image
    cv.imshow('greyscale image',X)
    
    # Waits for a keystroke
    cv.waitKey(0)  
    # Destroys all the windows created
    cv.destroyAllWindows() 