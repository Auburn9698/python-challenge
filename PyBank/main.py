# PyBank Challenge

# Import modules:
import os
import csv

# Paths for CSV files:
csvpath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("Resources", "analysis.txt")

# Create the variables:
total_months = 0
total_amount = 0
greatest_profit = 0
greatest_profit_month = 0
greatest_loss = 0
greatest_loss_month = 0
initial_amount = 0
monthly_changes = []

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvreader)
    
    # Loop through file:
    for row in csvreader:
        #Calculations for totals:
        total_months = total_months + 1
        total_amount = total_amount + int(row[1])

        # Check to see if this is the greatest profit so far:
        if int(row[1]) > greatest_profit:
            greatest_profit = int(row[1])
            greatest_profit_month = row[0]

        # Check to see if this is the greatest loss so far:        
        if int(row[1]) < greatest_loss:
            greatest_loss = int(row[1])
            greatest_loss_month = row[1]

        # Calculate the average monthly change amount:
        monthly_amount = int(row[1])
        monthly_change = monthly_amount - initial_amount
        initial_amount = monthly_amount
        monthly_changes.append(monthly_change)
        average_change = sum(monthly_changes)/ len(monthly_changes)

# Print the output:
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: {total_amount}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_profit_month} {greatest_profit}")
print(f"Greatest Decrese in Losses: {greatest_loss_month} {greatest_loss}")

# Create a list for the output:
#output = (f"Financial Analysis:",
#          f"---------------------------",
#          f"Total Months: {total_months}",
#          f"Net Total: {total_amount}",
#          f"Average Change: {average_change}",
#          f"Greatest Increase in Profits: {greatest_profit_month} {greatest_profit}",
#          f"Greatest Decrese in Losses: {greatest_loss_month} {greatest_loss}"
#
#print(output)
#
# Write to the analysis.text text file as pathout:



# Create a list for the output:
#output = (f"Financial Analysis:",
#          f"---------------------------",
#          f"Total Months: {total_months}",
#          f"Net Total: {total_amount}",
#          f"Average Change: {average_change}",
#          f"Greatest Increase in Profits: {greatest_profit_month} {greatest_profit}",
#          f"Greatest Decrese in Losses: {greatest_loss_month} {greatest_loss}")#

#print(output)

# Write to the analysis.text text file as pathout:
#with open(pathout, "w") as text_file:
#    text_file.write(output)

