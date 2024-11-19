import numpy as np
import os.path

# Initialize the array for the print statement of question 4
arr = []

# List of file names
file_names = ["book1.csv", "book2.csv", "book3.csv"]

# Iterate through each file
for file_name in file_names:
    if os.path.isfile(file_name):
        # Extracting the 1-D array from the csv file
        arr_read = np.loadtxt(file_name, dtype=str, skiprows=1)
        # Reading the csv file and converting the string to integer
        arr_data = arr_read[:, 1].astype(np.float32)
        # Calculate the mean and append to the array
        arr.append(np.mean(arr_data))
    else:
        print(f"File '{file_name}' is not present.")

# Print the mean of the 3 csv files in a list format
# if all files are present
if len(arr) == len(file_names):
    print("The mean of the 3 csv files is =", arr)
