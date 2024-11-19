import numpy as np
import os

#the file name is book1.csv
file1="book1.csv"

if os.path.isfile(file1):
    #extracting the 1-D array from the csv file
    arr_read_1 = np.loadtxt(file1,dtype=str)

    #reading the csv file and converting the string to integer
    arr1=arr_read_1[1:,1].astype(np.uint32)


    # print statement for question1
    #printing the  max and min of the book-1.csv file 
    # using the numpy max and min function
    print(f"The minimum of the {file1} 1-D array is {np.min(arr1)}")
    print(f"The maximum of the {file1} 1-D array is {np.max(arr1)}")

else:
    print(f"The file {file1} is not present or could not be read.")