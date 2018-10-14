import os
import csv
import pandas as pd

votes = os.path.join('Resources', 'election_data.csv')
VotePd = pd.read_csv(votes)

Votes = {}
UniqueCandidates = []
CandidateVotes = []
VotePercentage =[]

TotalVotes = 0
with open(votes, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)

    for row in csvreader:
        TotalVotes += 1
        if row[2] in Votes.keys():
            Votes[row[2]] += 1
        else:
            Votes[row[2]] = 1

for key, value in Votes.items():
    UniqueCandidates.append(key)
    CandidateVotes.append(value)


print("Election Results")
print("----------------")
print(f"Total Votes: {TotalVotes}")
print("----------------")
for vote in CandidateVotes:
    VotePercentage.append((float(vote)/float(TotalVotes))*100)
    VoterResults = f"{UniqueCandidates}: {VotePercentage:.2f}% ({CandidateVotes})\n"
    print(VoterResults)
print("----------------")

Output = os.path.join("PyPollOutput.csv")
with open(Output, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------"])
    csvwriter.writerow([f"Total Votes: {TotalVotes}"])
    csvwriter.writerow(["----------------"])
    for vote in CandidateVotes:
        VotePercentage.append((float(vote)/float(TotalVotes))*100)
        VoterResults = f"{UniqueCandidates}: {VotePercentage:.2f}% ({CandidateVotes})\n"
    csvwriter.writerow(VoterResults)
    csvwriter.writerow([f"----------------"])
    