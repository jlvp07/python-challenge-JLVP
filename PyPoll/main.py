# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
output_path = os.path.join('.', 'Analysis', 'output.txt')

# Creating Variables 
AllCandidate = {"delete":0}
TotalVotes = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        Candidate = row[2]
        TotalVotes += 1
        if not Candidate in AllCandidate:
            AllCandidate[Candidate] = 0
        AllCandidate[Candidate] += 1
    del AllCandidate["delete"]
with open(output_path, 'w') as outfile:

    outText = 'Election Results'
    outText += '\n********************'
    outText += f'\nTotal Votes: {TotalVotes}'
    outText += '\n********************'
    
    winner = ''
    mostVotes = 0
    for c in AllCandidate:
        if AllCandidate[c] > mostVotes:
            mostVotes = AllCandidate[c]
            winner = c
        outText += f'\n {c}: {(AllCandidate[c]/TotalVotes*100):0.3f}% ({AllCandidate[c]})'
    
    outText += '\n********************'
    outText += f'\nWinner: {winner}'
    outText += '\n********************'

    
    print(outText)
    outfile.write(outText)