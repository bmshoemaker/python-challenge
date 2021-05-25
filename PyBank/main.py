import os
import csv

# Create file path to CSV file
budget_file = os.path.join(os.getcwd(),'Desktop', 'data_analytics', 'python_homework', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')
output_file = os.path.join(os.getcwd(),'Desktop', 'data_analytics', 'python_homework', 'python-challenge', 'PyBank', 'analysis', 'budget_analysis.txt' )

    
# The total number of months included in the dataset   
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
       total_months = len(list(csvreader)) + 1

# The net total amount of Profit/Losses over the entire period
total = 0
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)   
    for row in csvreader:
        total += int(float(row[1]))
        
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
average_change = total/total_months
format_average = "{:.2f}".format(average_change)

# The greatest increase in profits (date and amount) over the entire period
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)   
    max_increase = max(csvreader, key=lambda row: int(float(row[1])))

# The greatest decrease in losses (date and amount) over the entire period
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)   
    max_decrease = min(csvreader, key=lambda row: int(float(row[1])))
# Print Final Analysis
final_analysis = (
    'Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${total}\n'
    f'Average Change: ${format_average}\n'
    f'Greatest Increase in Profits: ${max_increase}\n'
    f'Greatest Decrease in Profits: ${max_decrease}\n')
    
print(final_analysis)

# Export a text file with the results
with open(output_file, "a") as txt_file:
    txt_file.write(final_analysis)