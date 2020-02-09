#import modules
import os
import csv

#import the csv data - taken from class example
csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #set default values for variables. Create lists to store data
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0
    total_count = 0

    #I ended up not using this data; however it could be printed into a 
    #CSV or set of CSVs for auditing
    khan_dict = []
    correy_dict = []
    li_dict = []
    otooley_dict = []
    total_dict = []

    #Create a for loop to count votes, add to lists
    for row in csvreader:
        total_count = total_count + 1
        if row[2] == "Khan":
            khan_count = khan_count + 1
            khan_dict.append(row[0])
        elif row[2] == "Correy":
            correy_count = correy_count + 1
            correy_dict.append(row[1])
        elif row[2] == "Li":
            li_count = li_count + 1
            li_dict.append(row[0])
        elif row[2] == "O'Tooley":
            otooley_count = otooley_count + 1
            otooley_dict.append(row[0])
    
    #calculate the percentage of votes per candidate
    khan_per = khan_count/total_count
    correy_per = correy_count/total_count
    li_per = li_count/total_count
    otooley_per = otooley_count/total_count

    #percentage formatting found here https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
    khan_per = "{:.4%}".format(khan_per)
    correy_per = "{:.4%}".format(correy_per)
    li_per = "{:.4%}".format(li_per)
    otooley_per = "{:.4%}".format(otooley_per)

    #determine the winner
    finalcount = [khan_count, correy_count, li_count, otooley_count]
    winner = ""
    maxvotes = max(finalcount)
    maxvoteloc = finalcount.index(maxvotes)

    #assign top vote getter to winner variable
    if maxvoteloc == 0:
        winner = "Khan"
    elif maxvoteloc == 1:
        winner = "Correy"
    elif maxvoteloc == 2:
        winner = "Li"
    elif maxvoteloc == 3:
        winner = "O'Tooley"

    #put lines for printing into variables for easier coding
    line1 = " "
    line2 = "Election Results"
    line3 = "--------------------------"
    line4 = f"Total Votes: {total_count}"
    line5 = "--------------------------"
    line6 = f"Khan: {khan_per} ({khan_count})"
    line7 = f"Correy: {correy_per} ({correy_count})"
    line8 = f"Li: {li_per} ({li_count})"
    line9 = f"O'Tooley: {otooley_per} ({otooley_count})"
    line10 = "--------------------------"
    line11 = f"Winner: {winner}"
    line12 = "--------------------------"

    #print lines into terminal
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(line8)
    print(line9)
    print(line10)
    print(line11)
    print(line12)
    print("Data analysis exported as votinganalysis.csv")

    #output to CSV - method taken from class
    output_path = os.path.join('votinganalysis.csv')
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([line2])
        csvwriter.writerow([line3])
        csvwriter.writerow([line4])
        csvwriter.writerow([line5])
        csvwriter.writerow([line6])
        csvwriter.writerow([line7])
        csvwriter.writerow([line8])
        csvwriter.writerow([line9])
        csvwriter.writerow([line10])
        csvwriter.writerow([line11])
        csvwriter.writerow([line12])
    