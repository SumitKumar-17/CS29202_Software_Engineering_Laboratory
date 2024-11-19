import numpy as np 
import cv2 as cv

# Question 5 solving
image_file="a.png"

#reading the image file
X1=cv.imread(image_file)
if X1 is None:
    print("The file is not present or could not be read.")

else:
    #converting the image to the color image
    cv.imshow('color image',X1)  
    X=X1.astype(np.float64)

    # Waits for a keystroke
    cv.waitKey(0)
    # Destroys all the windows created
    cv.destroyAllWindows()