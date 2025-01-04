# Dependencies
import csv
import os

filepath = "Resources/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"

total_revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]
total_months = 0

with open(filepath) as csvfile:
    # CSV reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Tracking the totals
    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])

        # Track the revenue change
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])

        if total_months > 1:  
            revenue_change_list.append(revenue_change)
            month_of_change.append(row[0])

        # Greatest increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change

        # Greatest decrease
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

# Calculate the average revenue change
if len(revenue_change_list) > 0:
    revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
else:
    revenue_avg = 0

# Generate the output summary
output = (
    f"""
Financial Analysis
-------------------
Total Months: {total_months}
Total: ${total_revenue}
Average Change: ${revenue_avg:.2f}
Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})
"""
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)




