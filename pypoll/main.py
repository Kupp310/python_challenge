import os
import csv

election_data = {}

election_csv = os.path.join("Resources","election_data.csv")

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
# Get a list of unique candidates
    unique_candidates = [row[2] for row in csv_reader]
# Calculate total votes
total_votes = len(unique_candidates)

# List of candidates who received votes
candidates_received_votes = list(set(unique_candidates))

#Dictionary of Total votes won by each candidate
votes_won_by_candidate = {candidate: unique_candidates.count(candidate) for candidate in candidates_received_votes}

#Calculate percentage of votes won by each candidate in a dictionary
vote_percentage = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_won_by_candidate.items()}

#Get the winner based on the popular vote
election_winner = max(votes_won_by_candidate, key=votes_won_by_candidate.get)

#write results to new file
#new file path
output_path = os.path.join("analysis", "election_winner.txt")

#write the results in the new file
with open(output_path, "w") as txtfile:
    csvwriter = csv.writer(txtfile)
    txtfile.write("Election Results\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("---------------------------\n")
    for candidate in candidates_received_votes:
        txtfile.write(f"{candidate}: {vote_percentage[candidate]:.3f}% ({votes_won_by_candidate[candidate]})\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Winner: {election_winner}")