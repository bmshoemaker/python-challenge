import os
import csv

#Create file path to CSV and txt files
election_file = os.path.join(os.getcwd(),'Desktop', 'data_analytics', 'python_homework', 'python-challenge', 'PyPoll','Resources', 'election_data.csv')
output_file = os.path.join(os.getcwd(),'Desktop', 'data_analytics', 'python_homework', 'python-challenge', 'PyPoll','analysis', 'election_analysis.txt')

votes=[]
candidate_list = []
otooley_votes = 0
li_votes = 0
correy_votes = 0
khan_votes = 0

# The total number of votes cast

with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
       votes.append(row[0])
       total_votes=len(votes)
       
# A complete list of candidates 
candidate_list = set()
with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        candidate_list.add(row[2])

# Number of votes for each candidate
with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
        elif row[2] == "Li":
            li_votes = li_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Khan":
            khan_votes = khan_votes + 1
        next

 #Percentage of votes   
khan_percent = (khan_votes/total_votes)
khan_percent = "{:.3%}".format(khan_percent)

correy_percent = (correy_votes/total_votes)
correy_percent = "{:.3%}".format(correy_percent)

li_percent = (li_votes/total_votes)
li_percent = "{:.3%}".format(li_percent)

otooley_percent = (otooley_votes/total_votes)
otooley_percent = "{:.3%}".format(otooley_percent)

# The winner of the election based on popular vote.
most_votes = max(khan_votes, correy_votes, li_votes, otooley_votes)
if khan_votes == most_votes: 
    winner = "Khan"
elif correy_votes == most_votes:
    winner = "Correy"
elif li_votes == most_votes:
    winner = "Li"
elif otooley_votes == most_votes:
    winner = "O'Tooley"

# Print Final Analysis
final_analysis = (
    'Election Results\n'
    '-------------------------\n'
    f'Total Votes: ({total_votes})\n'
    '-------------------------\n'
    f'Khan: {khan_percent} ({khan_votes})\n'
    f'Correy: {correy_percent} ({correy_votes})\n'
    f'Li: {li_percent} ({li_votes})\n'
    f"O'Tooley: {otooley_percent} ({otooley_votes}) \n"
    '-------------------------\n'
    f'Winner: {winner}\n'
    '-------------------------\n'
)
print(final_analysis)

# Export a text file with the results 
with open(output_file, "a") as txt_file:
    txt_file.write(final_analysis)