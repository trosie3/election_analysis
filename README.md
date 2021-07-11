# Election Analysis

## Project Overview
Colorado Board of Elections give following data points to collect, and tasks to complete an election audit on a recent local congressional election.

  1. Total number of votes cast
  2. Total number of votes, and percentage of votes per County
  3. Largest County Voter Turnout
  4. A complete list of candidates who received votes
  5. Total number of votes each candidate received and percentage of votes each candidate won
  6. The winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python version 3.8.2 and Visual Studio Code version 1.57.1

## Election Audit Results
The analysis of the election shows:
- There were 369,711 total votes.
- Results by County results were:
  - Jefferson County voter turnout accounted for 10.5% of the total vote, with 38,855 ballots cast.
  - Denver County voter turnout accounted for 82.8% of the total vote, with 306,055 ballots cast.
  - Arapahoe County voter turnout accounted for 6.7% of the total vote, with 24,801 ballots cast.
- Largest voter turnout was in Denver County.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606.
- The winner of the election based on the popular vote:
  - Diana DeGette who with 272,892 votes received 73.8% of the vote.

## Election Audit Summary
The audit shows that the script as is can quickly sort through large data to determine the election winner, where the largest voter turnout was, total votes and percentage of votes. 

This script could be easily modified to look at another local area election like the one already completed by updating the .csv file to pull from, so long as the format of the csv is: Ballot ID, Candidate, County. See snip of where that modification would need to be made below for the 'file_to_load' variable.

![image](https://github.com/trosie3/election_analysis/blob/main/Resources/CSV_code_to_change.png)

Another thing to note is with a few small tweaks the script could be make more versatile and allow one to look at city or state elections. Again, the new .csv uploaded would still need to be in same layout of Ballot ID, Candidate and Location but by changing a few variable names within the code to pull a more generic location title the code can be used for almost any election. County should be changed to Location throughout or removed entirely to broaden the use of the code. For example: Largest County Turnout could be modified to say Largest Voter Turnout so the code and results aren't confined only to county elections. See snips of a couple spots simple modifications can be made to make the code more inclusive but changing 'county' to 'location'.

![Image](https://github.com/trosie3/election_analysis/blob/main/Resources/variable_names_to_change1.png) ![image](https://github.com/trosie3/election_analysis/blob/main/Resources/variable_names_to_change2.png) ![image](https://github.com/trosie3/election_analysis/blob/main/Resources/variable_names_to_change3.png)
