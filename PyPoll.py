#Add our Dependencies
import csv
dir(csv)
import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open results and read file
with open(file_to_load) as election_data:

#To Do: Read and Analyze data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

 # Print the Header Row
    headers = next(file_reader)
    print(headers)