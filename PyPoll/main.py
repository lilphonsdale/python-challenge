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
print(f'Total Votes : {total_votes}' )

#A complete list of candidates who received votes
candidates = list(set(candidate))
print(candidates)

#The percentage of votes each candidate won


#The total number of votes each candidate won

#The winner of the election based on popular vote