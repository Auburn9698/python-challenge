# PyPoll Challenge

# Import modules:
import os
import csv

# Paths for CSV files:
csvpath = os.path.join("Resources", "election_data.csv")
pathout = os.path.join("analysis", "analysis.txt")

# Create variables:
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
Other_votes = 0
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
        elif (row[2] == "Correy"):
            Correy_votes = Correy_votes + 1
        elif (row[2] == "Li"):
            Li_votes = Li_votes + 1
        elif (row[2] == "O'Tooley"):
            OTooley_votes = OTooley_votes + 1
        #Adding an error catch in case some cells don't match names exactly:
        else:
            Other_votes = Other_votes + 1
    
    # Compare Totals:
    Winner = max(Khan_votes, Correy_votes, Li_votes, OTooley_votes, Other_votes)
       
    #Setting name of winner:
    if Winner == Khan_votes:
        Winning_Name = "Khan"
    elif Winner == Correy_votes:
        Winning_Name = "Correy"
    elif Winner == Li_votes:
        Winning_Name = "Li"
    elif Winner == OTooley_votes:
        Winning_Name = "O'Tooley"
    else:
        Winning_name = "Other"

    # Calculate percentages for each candidate:
    Khan_percent = Khan_votes / Total_votes
    Correy_percent = Correy_votes / Total_votes
    Li_percent = Li_votes / Total_votes
    OTooley_percent = OTooley_votes / Total_votes
    Other_percent = Other_votes / Total_votes

# Printing Election Results:
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {Total_votes}")
print("----------------------------------------")
print(f"Khan: {Khan_percent:.2%} ({Khan_votes})")
print(f"Correy: {Correy_percent: .2%} ({Correy_votes})")
print(f"Li: {Li_percent:.2%} ({Li_votes})")
print(f"O'Tooley: {OTooley_percent:.2%} ({OTooley_votes})")
# Commenting out the line below since it isnt' needed; produces count of 0
# print(f"Other: {Other_percent:.2%} ({Other_votes})")  
print("----------------------------------------")
print(f"Winner: {Winning_Name}")
print("----------------------------------------")

with open(pathout, "w") as text_file:
    text_file.write("Election Results")
    text_file.write("----------------------------------------")
    text_file.write(f"Total Votes: {Total_votes}")
    text_file.write("----------------------------------------")
    text_file.write(f"Khan: {Khan_percent:.2%} ({Khan_votes})")
    text_file.write(f"Correy: {Correy_percent: .2%} ({Correy_votes})")
    text_file.write(f"Li: {Li_percent:.2%} ({Li_votes})")
    text_file.write(f"O'Tooley: {OTooley_percent:.2%} ({OTooley_votes})")
    text_file.write("----------------------------------------")
    text_file.write(f"Winner: {Winning_Name}")
    text_file.write("----------------------------------------")