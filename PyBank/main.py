#imports

import os
import csv

#set file path

pybank_csv = os.path.join("/Users/oaklandsveryown/Documents/GitHub/python-challenge/PyBank/","Resources","budget_data.csv")

#make lists for the data

dates = []
results = []
changes = []

#make a variable for tracking change

previous = 0

#make counting variables

#months = 0
#profit_loss = 0

#read the csv 

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #store the header
    header = next(csvreader)

    #loop through the data and pull the data into lists

    for row in csvreader:
        dates.append(row[0])
        results.append(row[1])
        #months += row[0]
        #profit_loss += row[1]
        profit_loss = int(row[1])
        change = profit_loss - previous
        profit_loss = previous
        changes.append(change)
#look at the list of results and measure the change from month to month

#for i in results[1:]:
#        change = int(previous) - int(row)
#        previous = row
#        changes.append(change)


#function to find the total amount of profit/loss

def sum(results):
    total = 0.0
    for result in results:
        total += int(result)
    return total

#function to find the average changes

def average(changes):
    length = len(changes)
    total = 0.0
    for change in changes:
        total += int(change)
    return total/ length

print("Financial Analysis")
print("-----------------------------------")

# The total number of months included in the dataset

print(f'Total Months: {len(dates)}')

# The net total amount of "Profit/Losses" over the entire period

print(f'Total :{sum(results)}')

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

print(f'Average Change : {average(changes)}')


#for this we should subtract row+1 from row as we loop through the sheet, appending the results to a new dict. 
# then we can average the values in that dict 

# The greatest increase in profits (date and amount) over the entire period

print(f'Greatest Increase in Profits:')

#here we can try to reuse the method from the last challenge of having if row is > row+ 1, saving in
#a variable and checking if that variable is >
#to return the date and amount, we need to search for it in that dict

# The greatest decrease in profits (date and amount) over the entire period

print(f'Greatest Decrease in Profits:')