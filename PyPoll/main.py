# imports
import os
import csv
# find current working directory and set file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))
pypoll_csv = os.path.join("Resources","election_data.csv")

#make lists to store the data
voter_id = []
county = []
candidate = []

#read the csv 
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #store the header
    header = next(csvreader)
    #loop through the data and pull the data into lists
    for row in csvreader:
    #pull data into lists
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#The total number of votes cast
total_votes = len(voter_id)

#A complete list of candidates who received votes
candidates = list(set(candidate))

#count each candidates votes
doane = 0
degette = 0
stockham = 0

#read the csv again
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #store the header
    header = next(csvreader)
    #loop through the data and pull the data into lists
    for row in csvreader:
        if row[2] == candidates[0]:
            doane = doane+1 
        elif row[2] == candidates[1]:
            degette = degette+1
        elif row[2] == candidates [2]:
            stockham = stockham+1

vote_totals = [doane,degette,stockham]

#The percentage of votes each candidate won

doane_share = doane / total_votes
degette_share = degette/ total_votes
stockham_share = stockham / total_votes

# results to print out
print("Election Results")
print("---------------------------------")
print(f'Total Votes : {total_votes}')
print("---------------------------------")
print(f'{candidates[2]} {stockham_share} {stockham}')
print(f'{candidates[1]} {degette_share} {degette}')
print(f'{candidates[0]} {doane_share} {doane}')

#The winner of the election based on popular vote

winner = zip(candidates,vote_totals)
for row in winner:
    if row[1] == max(vote_totals):
        print(f'Winner: {row[0]}')

#write the results into a txt

with open('output', 'w') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("-----------------------------------")
    txtfile.write(f'Total Votes : {total_votes}')
    txtfile.write("---------------------------------")
    txtfile.write(f'{candidates[2]} {stockham_share} {stockham}')
    txtfile.write(f'{candidates[1]} {degette_share} {degette}')
    txtfile.write(f'{candidates[0]} {doane_share} {doane}')
    winner = zip(candidates,vote_totals)
    for row in winner:
        if row[1] == max(vote_totals):
            txtfile.write(f'Winner: {row[0]}')