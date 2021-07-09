# The data we need to retrieve
import csv
import os
# assign variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# open election results and read
with open(file_to_load) as election_data:

    # to do: perform analysis
    print(election_data)

# 1.Total number of votes cast
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote
