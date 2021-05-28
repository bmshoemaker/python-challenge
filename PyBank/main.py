import os
import csv

# Create file path to CSV file
budget_file = os.path.join(os.getcwd(),'Desktop', 'data_analytics', 'python_homework', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')
output_file = os.path.join(os.getcwd(),'Desktop', 'data_analytics', 'python_homework', 'python-challenge', 'PyBank', 'analysis', 'budget_analysis.txt' )

    
# The total number of months included in the dataset   
months=[]
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
       months.append(row[0])
       total_months=len(months)

# The net total amount of Profit/Losses over the entire period
total = []
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)   
    for row in csvreader:
        total.append(int(float(row[1])))
        total_profits = sum(total)
        
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
monthly_change = []
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)   
    for i in range(len(total)-1):
        monthly_change.append(total[i+1]-total[i])
        average_change = (sum(monthly_change)/len(monthly_change))
        format_average = "{:.2f}".format(average_change)

# The greatest increase in profits (date and amount) over the entire period
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)   
    max_increase = max(monthly_change)
    max_month_index = monthly_change.index(max(monthly_change)) + 1
    max_month = months[max_month_index]

# The greatest decrease in losses (date and amount) over the entire period
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)   
    max_decrease = min(monthly_change)
    min_month_index = monthly_change.index(min(monthly_change)) + 1
    min_month = months[min_month_index]
    
# Print Final Analysis
final_analysis = (
    'Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${total_profits}\n'
    f'Average Change: ${format_average}\n'
    f'Greatest Increase in Profits: {max_month}  (${max_increase})\n'
    f'Greatest Decrease in Profits: ${min_month} (${max_decrease})\n')
    
print(final_analysis)

# Export a text file with the results
with open(output_file, "a") as txt_file:
    txt_file.write(final_analysis)