# imports
import os
import csv
# find current working directory and set file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))
pybank_csv = os.path.join("Resources","budget_data.csv")

# make lists for the data
dates = []
results = []
changes = []

# make a boolean variable for the first row
is_first_row = True

# read the csv 
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    # store the header
    header = next(csvreader)
    # loop through the data and pull the data into lists
    for row in csvreader:
        # pull data into lists
        dates.append(row[0])
        results.append(int(row[1]))
        # calculate changes from month to month
        profit_loss = int(row[1])
        if not is_first_row:
            change = profit_loss - previous
            changes.append(change)
        else:
            changes.append(0)
        # prepare for next row
        is_first_row = False
        previous = profit_loss

# function to find the average changes
def average(changes):
    length = len(changes)-1
    total = sum(changes)
    return total/ length

# return resuilts of analysis in terminal
print("Financial Analysis")
print("-----------------------------------")
# The total number of months included in the dataset
print(f'Total Months: {len(dates)}')
# The net total amount of "Profit/Losses" over the entire period
print(f'Total: ${sum(results)}')
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print(f'Average Change: ${round((average(changes)))}')
#here we should zip the dates to the changes and then search that tuple
zipped_data = zip(dates,changes)
# The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits:')
for row in zipped_data:
    if row[1] == max(changes):
        print(row)
# The greatest decrease in profits (date and amount) over the entire period
zipped_data = zip(dates,changes)
print(f'Greatest Decrease in Profits:')
for row in zipped_data:
    if row[1] == min(changes):
        print(row)

#write the results into a txt

with open('output', 'w') as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write('\n')
    txtfile.write("-----------------------------------")
    txtfile.write('\n')
    txtfile.write(f'Total Months: {len(dates)}')
    txtfile.write('\n')
    txtfile.write(f'Total: ${sum(results)}')
    txtfile.write('\n')
    txtfile.write(f'Average Change: ${round((average(changes)))}')
    txtfile.write('\n')
    zipped_data = zip(dates,changes)
    txtfile.write(f'Greatest Increase in Profits:')
    for row in zipped_data:
        if row[1] == max(changes):
            txtfile.write(str((row)))
    txtfile.write('\n')
    zipped_data = zip(dates,changes)
    txtfile.write(f'Greatest Decrease in Profits:')
    for row in zipped_data:
        if row[1] == min(changes):
            txtfile.write(str((row)))