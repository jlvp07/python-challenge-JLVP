# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
output_path = os.path.join('.', 'Analysis', 'output.txt')

# Creating Variables 
TotalMonths = 0
TotalProfits =0
MaxProfits = 0
MaxDate = ''
MinProfits = 0
MinDate = ''
averageChange = 0
lastProfits = False
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        curMonth = row[0]
        curProfits = int(row[1])
        if not lastProfits:
            lastProfits = curProfits
        #print(f'{curMonth} : {curProfits}')
        #Count this month
        TotalMonths += 1
        TotalProfits += int(row[1])
        averageChange = ((averageChange*(TotalMonths-1))+(curProfits - lastProfits))/TotalMonths

        # Check for Min and Max 
        
        if curProfits > MaxProfits:
            MaxProfits = curProfits
            MaxDate = curMonth

        if curProfits < MinProfits:
            MinProfits = curProfits
            MinDate = curMonth

    
        lastProfits = curProfits
    print('Done.')

with open(output_path, 'w') as outfile:

    print('Financial Analysis')
    print('*************************')
    print(f'Total Months: {TotalMonths}')
    print(f'Total: ${TotalProfits}')
    print(f'Average Change: ${averageChange:0.2f}')
    print(f'Greatest Increase in Profits: {MaxDate} (${MaxProfits})')
    print(f'Greatest Decrease in Profits: {MinDate} (${MinProfits})')
  
    outfile.write('Financial Analysis')
    outfile.write('\n*************************')
    outfile.write(f'\nTotal Months: {TotalMonths}')
    outfile.write(f'\nTotal: ${TotalProfits}')
    outfile.write(f'\nAverage Change: ${averageChange:0.2f}')
    outfile.write(f'\nGreatest Increase in Profits: {MaxDate} (${MaxProfits})')
    outfile.write(f'\nGreatest Decrease in Profits: {MinDate} (${MinProfits})')