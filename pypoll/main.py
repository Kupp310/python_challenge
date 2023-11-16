import os
import csv

pypoll_csv = os.path.join("Resources","election_data.csv")

with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    columns_as_lists = [list(c) for c in zip(csv_reader)]

# Calculate total votes
total_votes = len(pypoll_csv)
 
# Get a list of unique candidates
candidates = pypoll_csv["Candidate"].unique()
 
# Create a dictionary to store candidate votes
candidate_votes = {}
 
# Loop through the data to count votes for each candidate
for candidate in candidates:
    candidate_votes[candidate] = pypoll_csv[pypoll_csv["Candidate"] == candidate]["Candidate"].count()
 
# Find the winner based on the popular vote
winner = max(candidate_votes, key=candidate_votes.get)
 
# Print the results
print("Election Results")
print("-" * 28)
print(f"Total Votes: {total_votes}")
print("-" * 28)
 
for candidate in candidates:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})")
 
print("-" * 28)
print(f"Winner: {winner}")
print("-" * 28)