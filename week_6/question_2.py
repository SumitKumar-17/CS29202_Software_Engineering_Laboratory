import numpy as np
import os

#the file name is book1.csv
file1="book1.csv"

if os.path.isfile(file1):
    #extracting the 1-D array from the csv file
    arr_read_1 = np.loadtxt(file1,dtype=str)

    #reading the csv file and converting the string to integer
    arr1=arr_read_1[1:,1].astype(np.uint32)

    # print statement for question2 
    print("The sorted array is =",end=" ")
    #using the numpy sort function to sort the array
    print(np.sort(arr1))
    
else:
    print(f"The file {file1} is not present or could not be read.")