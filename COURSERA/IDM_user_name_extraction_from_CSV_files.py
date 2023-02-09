
#########################
# This is a python script to consolidate all
# users into email format for a folder of csv
# files
#########################


import os
import csv
import pandas as pd

folder_path = 'C:\\Temp\\AD'

os.chdir(folder_path)

# Use os.listdir to get a list of all files in the folder
for file_name in os.listdir(folder_path):

    
    # Check if the file is a CSV file
    if file_name.endswith(".csv"):

        ################################
        # Load the CSV file into a pandas DataFrame
        #file_path = os.path.join(folder_path, file_name)
        #df = pd.read_csv(file_path)
        ###############################

        with open(file_name, "r") as file:
            #define object
            reader = csv.reader(file)
            # iterate through each line and return a list
            for row in reader:
                # extract the name portion
                name=row[1]
                # replace spaces with a dot
                email=name.replace(" ", ".")

                # now append to a file
                with open("IDM_output.txt", "a") as output_file:
                    #print("{}@iag.com.au".format(email))
                    full_email="{}@iag.com.au".format(email)
                    #print(full_email)
                    new_line=output_file.write(full_email + "\n")
      



"""
import pandas as pd

df = pd.read_csv("c:\\Temp\\AD\\ACCUM_PROD.csv")

# Print the second column
print(df.iloc[:, 1])

"""