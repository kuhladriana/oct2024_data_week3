# Imports
import csv
import os

filepath = "Resources/election_data.csv"
file_to_output = "analysis/election_analysis.txt"

# Define Variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(filepath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # Vote count total
        total_votes += 1

        # Candidate name per row
        candidate_name = row[2]

        # If candidate is different from existing candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Initialize candidate vote count
            candidate_votes[candidate_name] = 0

        # Increment candidate vote count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results)
    txt_file.write(election_results)

    # Loop through vote counts
    for candidate in candidate_votes:
        # Vote counts and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Winning Candidate
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's vote and percentage count
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)

    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)