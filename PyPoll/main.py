# Dependencies
import os
import csv

# Pathing for data file in the Resources folder
election_data_csv = os.path.join("c:/", "Users", "downr", "python-challenge", "PyPoll",
                                 "Resources", "election_data.csv")

with open(election_data_csv, 'r') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    header = next(election_data)

    voting_count = 0
    pop_vote = 0
    candidate_dict = {}

    for row in election_data:
        voting_count += 1
        candidate_dict[row[2]] = candidate_dict.get(row[2], 0) + 1

print(f"Election Results")
print(f"----------------------------")
print(f"Total vote: {voting_count}")
print(f"----------------------------")
for candidate, vote in candidate_dict.items():
    print(f"{candidate}: {vote / voting_count * 100:.3f}%")
    if vote > pop_vote:
        vote = pop_vote
        winner = candidate
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

# Path to export text file
file_to_output = os.path.join("c:/", "Users", "downr", "python-challenge", "PyPoll",
                                  "analysis", "New_election_data.csv")

Print_terminal = (
    f"Election Results \n"
    f"----------------------------\n"
    f"Total vote: {voting_count}\n"
    f"----------------------------\n"   
    f"{candidate}: {vote / voting_count * 100:.3f}% \n"
    f"----------------------------\n" 
    f"Winner: {winner}\n"
    f"----------------------------\n"
)
# Print to terminal
print(Print_terminal)

# Export to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(Print_terminal)
