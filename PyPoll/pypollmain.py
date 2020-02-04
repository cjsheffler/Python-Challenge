#import the modules needed

import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # for row in csvreader:
        # print(row)

#The three columns are voterid, county, and candidate

    total_votes = sum(1 for row in csvreader)

    print(total_votes)