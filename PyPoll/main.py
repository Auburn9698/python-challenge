# PyPoll Challenge

# Import modules:
import os
import csv

# Paths for CSV files:
csvpath = os.path.join("Resources", "election_data.csv")
pathout = os.path.join("Resources", "analysis.txt")

# Create variables:
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
Total_votes = 0

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First 
    csv_header = next(csvreader)
    
    # Loop through file:
    for row in csvreader:

	# Calculate total 
        Total_votes = Total_votes + 1 

        # Add up votes per candidate:
        if (row[2] == "Khan"):
            Khan_votes = Khan_votes + 1
        elif (row[2]) == "Correy"):
            Correy_votes = Correy_votes + 1
        elif (row[2]) == "Li"):
            Li_votes = Li_votes + 1
        else:
            OTooley_votes = OTooley_votes + 1
    
    # Compare Totals:
    Totals = (Khan_votes, Correy_votes, Li_votes, OTooley_votes)
    Winner = max(Totals)
    
    #Setting name of winner:
    If Winner == Khan_votes:
        Winning_Name = "Khan"
    Elif Winner == Correy_votes:
        Winning_Name = "Correy"
    Elif Winner == Li_votes:
        Winning_Name = "Li"
    Else:
        Winning_Name = "O'Tooley"
            # Calculate percentages for each candidate:
    Khan_percent = Khan_votes / Total_votes
    Correy_percent = Correy_votes / Total_votes
    Li_percent = Li_votes / Total_votes
    OTooley_percent = OTooley_votes / Total_votes

#Printing Election Results:
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {Total_votes}")
print("----------------------------------------")
print(f"Khan: {Khan_percent:.3%} ({Khan_votes}))
print(f"Correy: {Correy_percent: .3%} ({Correy_votes})
print(f"Li: {Li_percent: .3%} ({Li_votes})
print(f"OTooley: {OTooley_percent: ..3%} ({OTooley_votes})
print("----------------------------------------")
print(f"Winner: {Winning_name})

print("----------------------------------------")