# Import necessary libraries
import os
import csv
import math

# Clear the console/terminal window
os.system('clear')

# Declare/Instantiate/Initialize necessary global scope variables
csv_path = "Resources/budget_data.csv"
greatest_Increase_profits = float('-inf')
greatest_Decrease_profits = float('inf')

# Exception handling for when the file is not found.
if not os.path.exists(csv_path):
    print("File does not exist.")
    exit()

# Finds the file and performs operations with it.
with open(csv_path, "r") as csv_read:
    reader = csv.reader(csv_read, delimiter = ",")
    next(reader) # skips the first row of the <reader> CSV file

    list_reader = list(reader) # Stores the <reader> file without a header as a list datatype.

    total_num_months = len(list_reader) # Calculates the number of months in the csv file, <budget_data.csv>.

# Converting the string values in the [value] column to integers and storing in the new <data> list.
data = [[month, int(value)] for month, value in list_reader] # Datatype = <class 'list'>

# Calculating the profits and losses for ecah month
profit_losses = [data[row][1] for row in range(len(data))]

# Calculating the net total amount of "Profit/Losses" over the entire budget_data.csv data
total_profit_losses = sum(profit_losses)

# Calculating the change in profits and losses for between months
change_in_profit_losses = [data[row+1][1] - data[row][1] for row in range(len(data)-1)]

# Calculating the average of those changes
average_profit_losses = sum(change_in_profit_losses) / len(change_in_profit_losses)
rounded_average_profit_losses = math.floor(average_profit_losses*100)/100

# loop through the list of lists
for month_data in data:
    # compare the value of the current month_data item the value of the <greated_Increase_profits> variable.
    if month_data[1] > greatest_Increase_profits:
        greatest_Increase_profits = month_data[1]

    if month_data[1] < greatest_Decrease_profits:
        greatest_Decrease_profits = month_data[1]

# Final Printed output:
print("Financial Analysis",
"\n----------------------------",
"\nTotal months:", str(total_num_months),
"\nTotal: $", total_profit_losses,
"\nAverage Change:", rounded_average_profit_losses,
"\nGreatest Increase in Profits:", greatest_Increase_profits, # currently returns the second to last value of the list <data>
"\nGreatest Decrease in Profits:", greatest_Decrease_profits) # currently returns the last value of the list <data>

# Printing the results to a text file stored in the "Analysis" subdirectory
with open("analysis/Financial Analysis.txt", "w") as file:
    # Write a list of strings to the file
    lines = ["Financial Analysis",
            "\n----------------------------",
            "\nTotal months: ", str(total_num_months),
            "\nTotal: $", str(total_profit_losses),
            "\nAverage Change: ", str(rounded_average_profit_losses),
            "\nGreatest Increase in Profits: ", str(greatest_Increase_profits),
            "\nGreatest Decrease in Profits: ", str(greatest_Decrease_profits)]
    file.writelines(lines)