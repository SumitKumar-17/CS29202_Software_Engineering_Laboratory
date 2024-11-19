import numpy as np 
import cv2 as cv
import copy
import time

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
    time_1_strt=time.time()
    print("Matrix multiplication by the Numpy Library is going on....")
    Z=np.matmul(X,Y)
    # print(Z)
    print("Matrix multiplication by the Numpy Library is done")
    time_1_end=time.time()


    #Question 8 for checking the time taken by
    # the numpy library and the python program
    time_2_strt = time.time()
    # x_less=np.divide(X,100)
    # y_less=np.divide(Y,100)
    x_less=X
    y_less=Y
    Z = []
    # Check if the matrices can be multiplied
    if len(X[0]) != len(Y):
        raise ValueError("The matrix multiplication is not possible")
    else:
        Z = np.zeros((len(x_less), len(x_less)), dtype=np.int64)

    # gh=1
    # Perform matrix multiplication
    print("Matrix multiplication by the Python Program is going on....")
    for i in range(len(x_less)):
        # print(gh)
        # gh+=1
        # continue
        for j in range(len(y_less[0])):
            for k in range(len(y_less)):
                Z[i][j] += x_less[i][k] * y_less[k][j]
    
    # X=np.multiply(x_less,100)
    # Y=np.multiply(y_less,100)
    # print(Z)

    

    print("Matrix multiplication by the Python Program is done")
    time_2_end = time.time()

    #Printing the time taken by the numpy 
    # library and the python program
    print(f"The time taken by the Numpy Library is{time_1_end-time_1_strt}")
    print(f"The time taken by the Python Program is{time_2_end-time_2_strt}")
