import os
import csv

#Dictionary to store data
budget_data = {}

#Path of CSV file
budget_csv = os.path.join('Resources','budget_data.csv')

#Open CSV file
with open(budget_csv, 'r') as budgetfile:
    #create reader
    budget_reader = csv.reader(budgetfile, delimiter=',')
    #skip header
    next(budget_reader)
    #start loop
    for row in budget_reader:
        budget_data[row[0]] = int(row[1])
#Calculate the changes in profit/loss over the whole period
profit_loss_changes = []
values = list(budget_data.values())
for i in range(1, len(budget_data)):
    change = values[i] - values[i-1]
    profit_loss_changes.append(change)
#Calculate the aveage change in profit/loss
average_profit_loss_change = sum(profit_loss_changes) / len(profit_loss_changes)

#total number of months
total_months = len(budget_data)
#total amount of profit/losses over the entire period
total_profit_loss = sum(budget_data.values())
#Biggest increase in profit/loss
greatest_increase = max(profit_loss_changes)
#smallest increase in profit/loss
greatest_decrease = min(profit_loss_changes)

#write to other file
output_path = os.path.join("analysis", "pybank_analysis.txt")

with open(output_path, "w") as txtfile:
    csvwriter = csv.writer(txtfile)
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_profit_loss_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: ${greatest_increase}\n")
    txtfile.write(f"Greatest Decrease in Profits: ${greatest_decrease}")
