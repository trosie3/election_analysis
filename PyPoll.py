# The data we need to retrieve
import csv
import os
# assign variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# open election results and read
with open(file_to_load) as election_data:

    # to do: perform analysis
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


# 1.Total number of votes cast
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote
