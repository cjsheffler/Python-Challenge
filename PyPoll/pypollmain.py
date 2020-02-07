# list all candidates who received votes
# Count the number of votes
# percentage of votes for each candidate
# total votes for each candidate
# winner of the election
# export to csv and print to terminal
# voterid county candidate


#import the modules needed

import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    candidatelist = []
    kahncount = 0
    correycount = 0
    licount = 0
    otooleycount = 0
    totalvotes = 0

    for row in csvreader:
        totalvotes = totalvotes + 1  
        if row[2] == 'Kahn':
            kahncount = kahncount + 1,
        elif row[2] == 'Correy':
            correycount = correycount + 1,
        elif row[2] == 'Li':
            licount = licount + 1,
        elif row[2] == "O'Tooley":
            otooleycount = otooleycount + 1

print(candidatelist)
print(totalvotes)
print(kahncount)