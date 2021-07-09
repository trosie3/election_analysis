# The data we need to retrieve
#add dependencies
import csv
import os
# assign variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote 
total_votes = 0

# find the candidate names
candidate_options = []

#votes per candidate
candidate_votes = {}

# open election results and read
with open(file_to_load) as election_data:

    # to do: perform analysis
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # read header row.
    headers = next(file_reader)
 
    # Print each row in the CSV file.
    for row in file_reader:
        # add to total vote count
        total_votes += 1

        # Print candidate name
        candidate_name = row[2]
        # to get unique names only
        if candidate_name not in candidate_options:
            # add cand name to list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # add to vote
        candidate_votes[candidate_name] += 1

        #go thru t find vote percentage
    for candidate_name in candidate_votes:
            #get votes per candidate
        votes = candidate_votes[candidate_name]
            # percentage of total vote
        vote_percentage = (votes/total_votes)*100
            #print candidates percentage   
        print(f"{candidate_name}: received {float(vote_percentage):.1f}% of the vote")



# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# 1.Total number of votes cast
# maybe for later? ---  txt_file.write(f"Total number of votes str(total_votes)\n")
# 2.A complete list of candidates who received votes
# maybe for later? ---  txt_file.write(f"The candidates are {candidate_options}\n")
# 3.Total number of votes each candidate received
# maybe for later? ---  txt_file.write(f"The total votes per are: {candidate_name}:{candidate_votes}\n")
# 4.Percentage of votes each candidate won
# maybe for later? ---  txt_file.write(f"{candidate_name}: recieved {float(vote_percentage):.1f} of the total vote\n")
# 5.The winner of the election based on popular vote
# The data we need to retrieve
#add dependencies
