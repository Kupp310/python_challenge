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
    for i in range(1, len(budget_data)):
    change = budget_data[i] - budget_data[i-1]
    profit_loss_changes.append(change)
    print(profit_loss_changes)

#total number of months
total_months = len(budget_data)
#total amount of profit/losses over the entire period
total_profit_loss = sum(budget_data.values())
print(total_profit_loss)



average_profit_loss_change = []
greatest_increase = {"date"}