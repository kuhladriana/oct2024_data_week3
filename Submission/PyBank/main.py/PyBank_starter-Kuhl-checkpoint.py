# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

filepath = "Resources/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"

total_months= 0 
total_net = 0

last_month_profit = 0
curr_month_profit = 0
total_change = 0

max_change = ["",0]
min_change =["", 87]
max_month = ""
min_month = ""

with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
       # print(row)
       total_months += 1
       total_net += int(row[1])
      
    #check if first row - skip first row
    if total_months == 1:
        last_month_profit = int(row[1])
    else:
        # get the change
        curr_month_profit = int(row[1])
        change = last_month_profit - curr_month_profit
        total_change += change

        # reset
        last_month_profit = curr_month_profit

        # New Max Change?
        if change > max_change:
           max_change = change
           max_month = row[0]

        # New Min Change?
        if change < min_change:
           min_change = change
           min_month = row[0]

#generate the output summary    
output =f""""
Financial Analysis
-------------------
Total Months: {total_months}\n
Total: ${total_net}\n
Average Change: {total_change/ (total_months - 1)}\n
Greatest Increase in Profit: {max_month}{max_change}\n
Greatest Decrease in Profit: {min_month}{min_change}\n
"""

#Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)





