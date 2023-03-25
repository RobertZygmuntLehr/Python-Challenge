# Import necessary libraries
import os
import csv
import math

# Clear the console/terminal window
os.system('clear')

# Declare/Instantiate/Initialize necessary global scope variables
csv_path = "Resources/budget_data.csv"
greatest_Increase_profits = 0
greatest_Decrease_profits = 0
index = 0
month_of_greatest_Increase_profits = None
month_of_greatest_Decrease_profits = None

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
integer_list_reader = [[month, int(value)] for month, value in list_reader] # Datatype = <class 'list'>

# Calculating the profits and losses for ecah month
profit_losses = [integer_list_reader[row][1] for row in range(len(integer_list_reader))]

# Calculating the net total amount of "Profit/Losses" over the entire budget_data.csv data
total_profit_losses = sum(profit_losses)

# Calculating the change in profits and losses for between months
change_in_profit_losses = [integer_list_reader[row+1][1] - integer_list_reader[row][1] for row in range(len(integer_list_reader)-1)]

# Calculating the average of those changes
average_profit_losses = sum(change_in_profit_losses) / len(change_in_profit_losses)
rounded_average_profit_losses = math.floor(average_profit_losses*100)/100

# Calculates the greatest increaese and decrease
while index < len(integer_list_reader) - 1:
    diff = integer_list_reader[index + 1][1] - integer_list_reader[index][1]
    if diff > greatest_Increase_profits:
        greatest_Increase_profits = diff
        month_of_greatest_Increase_profits = integer_list_reader[index + 1][0]
        print(month_of_greatest_Increase_profits, greatest_Increase_profits)
    if diff < greatest_Decrease_profits:
        greatest_Decrease_profits = diff
        month_of_greatest_Decrease_profits = integer_list_reader[index + 1][0]
        print(month_of_greatest_Decrease_profits, greatest_Decrease_profits)
    index += 1

# Final Printed output:
print("Financial_Analysis",
"\n-----------------------------",
"\nTotal months:", str(total_num_months),
"\nTotal: $" + str(total_profit_losses),
"\nAverage Change: $" + str(rounded_average_profit_losses),
"\nGreatest Increase in Profits: " + month_of_greatest_Increase_profits + " ($" + str(greatest_Increase_profits) + ")", # currently returns the second to last value of the list <data>
"\nGreatest Decrease in Profits: " + month_of_greatest_Decrease_profits + " ($" + str(greatest_Decrease_profits) + ")") # currently returns the last value of the list <data>

# Printing the results to a text file stored in the "Analysis" subdirectory
with open("analysis/Financial_Analysis.txt", "w") as file:
    # Write a list of strings to the file
    lines = ["Financial Analysis",
            "\n-----------------------------",
            "\nTotal months:", str(total_num_months),
            "\nTotal: $" + str(total_profit_losses),
            "\nAverage Change: $" + str(rounded_average_profit_losses),
            "\nGreatest Increase in Profits: " + month_of_greatest_Increase_profits + " ($" + str(greatest_Increase_profits) + ")", # currently returns the second to last value of the list <data>
            "\nGreatest Decrease in Profits: " + month_of_greatest_Decrease_profits + " ($" + str(greatest_Decrease_profits) + ")"]
    file.writelines(lines)