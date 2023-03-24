# Import necessary libraries
import os
import csv
import math

# Clear the console/terminal window
os.system('clear')

# Declare/Instantiate/Initialize necessary global scope variables
csv_path = "Resources/election_data.csv"
greatest_Increase_profits = 0
greatest_Decrease_profits = 0

# Exception handling for when the file is not found.
if not os.path.exists(csv_path):
    print("File does not exist.")
    exit()

# Finds the file and performs operations with it.
with open(csv_path, "r") as csv_read:
    reader = csv.reader(csv_read, delimiter = ",")
    # next(reader) # skips the first row of the <reader> CSV file
    # print(next(reader))

    list_reader = list(reader) # Stores the <reader> file without a header as a list datatype.

    election_data_size = len(list_reader)
    print(election_data_size)
    
    # print(list_reader)
'''
# Converting the string values in the [value] column to integers and storing in the new <data> list.
data = [[month, int(value)] for month, value in list_reader]

# Debugging
print(data,"\n") # Datatype = <class 'list'>

# Calculating the profits and losses for ecah month
profit_losses = [data[row][1] for row in range(len(data))]

# Calculating the net total amount of "Profit/Losses" over the entire budget_data.csv data
total_profit_losses = sum(profit_losses)

# Calculating the change in profits and losses for between months
change_in_profit_losses = [data[row+1][1] - data[row][1] for row in range(len(data)-1)]

# Calculating the average of those changes
average_profit_losses = sum(change_in_profit_losses) / len(change_in_profit_losses)
rounded_average_profit_losses = math.floor(average_profit_losses*100)/100

# Calculating the Greatest Increase and Greatest Decrease in Profits over the entire period.
for row in range(len(data)):
    print(data[row][1])
    if data[row][1] > data[row - 1][1]:
        greatest_Increase_profits = data[row][1]
    if data[row][1] < data[row - 1][1]:
        greatest_Decrease_profits = data[row][1]

# Final Printed output:
print("Financial Analysis",
"\n----------------------------",
"\nTotal months:", str(total_num_months),
"\nTotal: $", total_profit_losses,
"\nAverage Change:", rounded_average_profit_losses,
"\nGreatest Increase in Profits:", greatest_Increase_profits, # currently returns the second to last value of the list <data>
"\nGreatest Decrease in Proftis:", greatest_Decrease_profits) # currently returns the last value of the list <data>
'''