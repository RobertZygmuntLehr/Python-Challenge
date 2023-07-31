# Financial Records Analysis

## Overview

This project aims to perform financial records analysis and election poll data processing using Python scripts. The two scripts here, [PyBank](https://github.com/robert-z-lehr/Financial-Records-Analysis/tree/main/PyBank/main.py) and [PyPoll](https://github.com/robert-z-lehr/Financial-Records-Analysis/blob/main/PyPoll/main.py), are designed to analyze and extract essential information from large datasets with Python.

## Tools and Skills Used

- Python
- Pandas
- Reading and writing CSV files
- Data analysis and manipulation
- Conditional statements and loops

## Project Description

### PyBank

This script analyzes the financial records of a company by analyzing the data from `budget_data.csv`, available in [`/PyBank/Resources/budget_data.csv`](https://github.com/robert-z-lehr/Financial-Records-Analysis/blob/main/PyBank/Resources/budget_data.csv), displaying results on Terminal and written to a text file, available in [`/PyBank/Analysis/Financial_Analysis.txt`](https://github.com/robert-z-lehr/Financial-Records-Analysis/blob/main/PyBank/Analysis/Financial_Analysis.txt).

### PyPoll

The script helps a small, rural town modernize its vote-counting process by analyzing the data from `election_data.csv`, available in [`/PyPoll/Resources/election_data.csv`](https://raw.githubusercontent.com/robert-z-lehr/Financial-Records-Analysis/main/PyPoll/Resources/election_data.csv), displaying the results on Terminal and written to a text file, available in [`/PyPoll/Analysis/Election_Results.txt`](https://github.com/robert-z-lehr/Financial-Records-Analysis/blob/main/PyPoll/Analysis/Election_Results.txt).

## Output Results

**PyBank Results:**

Financial Analysis
----------------------------
- Total Months: 86
- Total: $22564198
- Average Change: $-8311.11
- Greatest Increase in Profits: Aug-16 ($1862002)
- Greatest Decrease in Profits: Feb-14 ($-1825558)

**PyPoll Results:**

Election Results
-------------------------
- Total Votes: 369711
-------------------------
- Charles Casper Stockham: 23.049% (85213)
- Diana DeGette: 73.812% (272892)
- Raymon Anthony Doane: 3.139% (11606)
-------------------------
- Winner: Diana DeGette
-------------------------
