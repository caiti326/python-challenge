#Import and read csv file, import pandas and statistics
import os
import csv
vote_csv = "/Users/caitlindonovan/Desktop/ColumbiaBootcamp/Homework/python-challenge/PyPoll/Resources/election_data.csv"
export_file = "/Users/caitlindonovan/Desktop/ColumbiaBootcamp/Homework/python-challenge/PyPoll/PyPoll.txt"
import pandas as pd 

# Set Vote Counter
total_votes = 0

# Define Candidates and their Votes 
candidates = []
candidate_votes = {}

# Identify the Winning Candidate
winner = ""
winner_count = 0

# Read the csv and convert it into a list of dictionaries
with open(vote_csv) as election_info:
    reader = csv.DictReader(election_info)

    # For each row...
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Find the candidate names in each row
        candidate_name = row["Candidate"]

        # Loop through to find all unique candidate names
        if candidate_name not in candidates:

            # Add new name to list of candidates
            candidates.append(candidate_name)

            # Track given candidate's voter count
            candidate_votes[candidate_name] = 0

        # Add a vote to given candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print results and export summary to text file
with open(export_file, "w") as txt_file:

    # Print the final vote count in terminal
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results) 

    # Save info to text file
    txt_file.write(election_results)

    # Loop through the data to find the winner
    for candidate in candidate_votes:

        # Determine vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winner_count):
            winner_count = votes
            winner = candidate

        # Print each candidate's voter count and percentage in terminal
        end_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(end_results)

        # Save all info to text file
        txt_file.write(end_results)

    # Print the winning candidate in terminal
    winner_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winner_summary)

    # Save all info to text file
    txt_file.write(winner_summary)