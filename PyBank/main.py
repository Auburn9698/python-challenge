# PyBank Challenge

# Import modules:
import os
import csv

# Paths for CSV files:
csvpath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("analysis", "analysis.txt")

# Create the variables:
total_months = 1
total_amount = 0
greatest_profit = 0
greatest_profit_month = 0
greatest_loss = 0
greatest_loss_month = 0
month = []
monthly_changes = []

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    row = next(csvreader)  #For skipping first month that messed with avg change.
    previous_amount = int(row[1])

    # Loop through file, calculate basic totals:
    for row in csvreader:
        total_months = total_months + 1
        total_amount = total_amount + int(row[1])
        # Add to the months list, used later for month indexing
        month.append(row[0])

        # Check to see if this is the greatest profit so far:
        if int(row[1]) > greatest_profit:
            greatest_profit = int(row[1])
            greatest_profit_month = row[0]

        # Note: Not sure I needed largest-profit or largest-loss.
        # It looked like the homework was asking for that at first,
        # but I think it was actually looking for the greatest changes
        # +/- from month to month.  Wasn't real clear at first.

        # Check to see if this is the greatest loss so far:      
        if int(row[1]) < greatest_loss:
            greatest_loss = int(row[1])
            greatest_loss_month = row[0]

        # For Calculating the average monthly change amount:
        monthly_change = int(row[1]) - previous_amount
        monthly_changes.append(monthly_change)
        previous_amount = int(row[1])
       

    # Calculate average change:
    average_change = sum(monthly_changes) / total_months

    # Find the largest increase and decrease:
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    increase_month = month[monthly_changes.index(greatest_increase)]
    decrease_month = month[monthly_changes.index(greatest_decrease)]

# Storing output in a tuple to print and write to text file(shorter code)        
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

