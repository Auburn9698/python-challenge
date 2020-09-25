# PyBank Challenge

# Import modules:
import os
import csv

# Paths for CSV files:
csvpath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("analysis", "analysis.txt")

# Create the variables:
total_months = 0
total_amount = 0
previous_amount = 0
month = []
monthly_changes = []

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)

    # Loop through file, calculate basic totals:
    for row in csvreader:
        total_months = total_months + 1
        total_amount = total_amount + int(row[1])
        # Add to the months list, used later for month indexing
        month.append(row[0])
        # For Calculating the average monthly change amount:
        monthly_change = int(row[1]) - previous_amount
        monthly_changes.append(monthly_change)
        previous_amount = int(row[1])


    #Remove the first value from monthly_changes, since there was no previous month to subtract:
    monthly_changes.pop(0)
    #Remove the first value from the months, same reason as above:
    month.pop(0)

    # Calculate average change:
    average_change = sum(monthly_changes) / (total_months -1)

    # Find the largest increase and decrease:
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    increase_month = month[monthly_changes.index(greatest_increase)]
    decrease_month = month[monthly_changes.index(greatest_decrease)]

# Storing output in a tuple to print and write to text file:        
output = (
    " \n"
    "Financial Analysis: \n"
    "----------------------------------------------- \n"
    f"Total Months:    {total_months} \n"
    f"Net Total:      ${total_amount} \n"
    f"Average Change: ${average_change:.2f} \n"
    f"Greatest Increase in Profits: {increase_month} ($ {greatest_increase}) \n"
    f"Greatest Decrese in Losses:   {decrease_month} (${greatest_decrease}) \n")

# Print the output:
print(output)

# Write the output to text file analysis.txt:  
with open(pathout, "w") as text_file:
    text_file.write(output)

