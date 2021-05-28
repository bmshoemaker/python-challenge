import os
import csv

#Create file path to CSV and txt files
election_file = os.path.join(os.getcwd(),'Desktop', 'data_analytics', 'python_homework', 'python-challenge', 'PyPoll','Resources', 'election_data.csv')

# The total number of votes cast
with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_votes = len(list(csvreader)) + 1
       
# A complete list of candidates 
candidate_list = set()
with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        candidate_list.add(row[2])
print(candidate_list)
# who received votes along with percentage of votes and total number of votes
candidate_results = {}

# The winner of the election based on popular vote.

# Print Final Analysis
final_analysis = (
    'Election Results\n'
    '-------------------------\n'
    f'Total Votes: {total_votes}\n'
    '-------------------------\n'
)
print(final_analysis)
# Export a text file with the results 