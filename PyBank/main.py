#import the modules needed

import os
import csv

#import the csv data
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#set default values for variables. Create lists to store data
    monthcount = 0
    differencetable = []
    monthlist = []
    monthdiff = 0
    lastmonthvalue = 0
    currmonth = 0
    totalvalue = 0
    avgchange = 0

#create a for loop to count the number of months, add the values together, calculate
#the average change, and put values into lists
    for row in csvreader:
        if monthcount == 0:
            totalvalue = 0
            currmonth = row[1]
            lastmonthvalue = row[1]
            monthlist.append(row[0])
            totalvalue = currmonth
            monthcount = monthcount + 1
        else:
            monthcount = monthcount + 1
            currmonth = row[1]
            monthlist.append(row[0])
            totalvalue = int(totalvalue) + int(currmonth)
            monthdiff = int(currmonth) - int(lastmonthvalue)
            differencetable.append(monthdiff)
            lastmonthvalue = row[1]
    
    #define a function to calculate the mean of the values in the created list
    def mean(numbers):
        return sum(numbers)/len(numbers)

    #calculate the average change, find the max increase value and max decrease value
    avgchange = round(mean(differencetable), 2)
    maxinc = max(differencetable)
    maxdec = min(differencetable)

    #Index the Max increase and Max Decrease location
    #https://www.programiz.com/python-programming/methods/list/index provided help

    maxincloc = differencetable.index(maxinc)
    maxdecloc = differencetable.index(maxdec)

    #use the indexed data from previous step to find corresponding month
    maxincmonthval = monthlist[maxincloc + 1]
    minincmonthval = monthlist[maxdecloc + 1]

    line1 = "Financial Analysis"
    line2 = "-------------------------------------"
    line3 = (f"Total Months:  {monthcount}")
    line4 = (f"Total: ${totalvalue}")
    line5 = (f"Average Change: ${avgchange}")
    line6 = (f"Greatest Increase in Profits:  {maxincmonthval} (${maxinc})")
    line7 = (f"Greatest Decrease in Profits: {minincmonthval} (${maxdec})")
    line8 = ("-------------------------------------")

    #print results
    print(" ")
    print(" ")
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(line8)
    print("Data analysis output as financialanalysis.csv")

    #output to CSV - method from Python Lesson 2.9
    output_path = os.path.join('financialanalysis.csv')
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([line1])
        csvwriter.writerow([line2])
        csvwriter.writerow([line3])
        csvwriter.writerow([line4])
        csvwriter.writerow([line5])
        csvwriter.writerow([line6])
        csvwriter.writerow([line7])
        csvwriter.writerow([line8])