# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os


filepath = "Resources/election_data.csv"


# Define Variables
total_votes = 0
vote_tally = {}
winner =""
max_votes = 0

# Open the CSV file and process it
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after  the header
    for row in csvreader:
        # print(row)
        total_votes += 1

        #Candidate Total
        candidate= row[2]
        if candidate in vote_tally.keys():
            vote_tally[candidate] += 1
        else:
            vote_tally[candidate] = 1
    

 


output =f""""
Election Results
--------------------------
Total Votes: {total_votes}
Candidate: {vote_tally}

--------------------------
"""
# print the output
print(output)



