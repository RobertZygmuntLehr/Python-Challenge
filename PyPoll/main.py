# Import necessary libraries
import os
import csv
import math

# Clear the console/terminal window
os.system('clear')


# Assign values to variables
csv_path = "Resources/election_data.csv"
vote_counter_Charles = 0 # Used to calculate the percentage of votes Charles won
vote_counter_Diana = 0 # Used to calculate the percentage of votes Diana won
vote_counter_Raymon = 0 # Used to calculate the percentage of votes Anthony won
winner = None

# Exception handling for when the file is not found.
if not os.path.exists(csv_path):
    print("File does not exist.")
    exit()

# Finds the file and performs operations with it.
with open(csv_path, "r") as csv_read:
    reader = csv.reader(csv_read, delimiter = ",") # reader is a csv file type.
    next(reader) # skips the first row of the <reader> CSV file
    election_votes_list = list(reader) # Stores the <reader> file without a header as a list datatype.

# Figure out how to check if each voter ID is unique.

    # START DEBUGGING
    test = election_votes_list[167678][2]
    print(test)
    # END DEBUGGING

    # Returns the total number of votes cast.
    total_number_of_votes_cast = len(election_votes_list)

    # Returns a complete list of candidates who received votes.
    list_of_candidates = list(set([poll_data_list[2] for poll_data_list in election_votes_list]))

    # The percentage of votes each candidate won
    for vote in election_votes_list:
        # print(vote[2])
        if vote[2] == "Charles Casper Stockham":
            vote_counter_Charles = vote_counter_Charles + 1
        elif vote[2] == "Diana DeGette":
            vote_counter_Diana = vote_counter_Diana + 1
        elif vote[2] == "Raymon Anthony Doane":
            vote_counter_Raymon = vote_counter_Raymon + 1
        else:
            print("You didn't vote for any of the candidates!")

    # The winner of the election base on popular vote is:
    if vote_counter_Charles > vote_counter_Diana and vote_counter_Charles > vote_counter_Raymon:
        winner = "Charles Casper Stockham"
    elif vote_counter_Diana > vote_counter_Charles and vote_counter_Diana > vote_counter_Raymon:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"

print("\nElection Results",
      "\n--------------------------",
      "\nTotal Votes: ", total_number_of_votes_cast,
      "\n--------------------------",
      "\nCharles Casper Stockham: ", str(math.floor(vote_counter_Charles/total_number_of_votes_cast*100000)/1000) + "% (" + str(vote_counter_Charles) + ")",
      "\nDiana DeGette: ", str(math.floor(vote_counter_Diana/total_number_of_votes_cast*100000)/1000) + "% (" + str(vote_counter_Diana) + ")"
      "\nRaymon Anthony Doane: ", str(math.floor(vote_counter_Raymon/total_number_of_votes_cast*100000)/1000) + "% (" + str(vote_counter_Raymon) + ")"
      "\n--------------------------",
      "\nWinner:", winner,
      "\n--------------------------")

# Printing the results to a text file stored in the "Analysis" subdirectory
with open("analysis/Election_Results.txt", "w") as file:
    # Write a list of strings to the file
    lines = ["\nElection Results",
            "\n--------------------------",
            "\nTotal Votes: ", str(total_number_of_votes_cast),
            "\n--------------------------",
            "\nCharles Casper Stockham: ", str(math.floor(vote_counter_Charles/total_number_of_votes_cast*100000)/1000) + "% (" + str(vote_counter_Charles) + ")",
            "\nDiana DeGette: ", str(math.floor(vote_counter_Diana/total_number_of_votes_cast*100000)/1000) + "% (" + str(vote_counter_Diana) + ")"
            "\nRaymon Anthony Doane: ", str(math.floor(vote_counter_Raymon/total_number_of_votes_cast*100000)/1000) + "% (" + str(vote_counter_Raymon) + ")"
            "\n--------------------------",
            "\nWinner:", winner,
            "\n--------------------------"]
    
    file.writelines(lines)