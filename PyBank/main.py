#import Modules
import os
import csv
import pandas as pd

#assign path to source material
budget = os.path.join('Resources', 'budget_data.csv')

#create dataframe
BudgetDataPd = pd.read_csv(budget)

#create an additional column that shifts all values down one position
BudgetDataPd["Profit/Losses + 1"] = BudgetDataPd["Profit/Losses"].shift(1)
#create a new column that uses the 2 values to give you the month to month difference
BudgetDataPd["Difference"] = BudgetDataPd["Profit/Losses"] - BudgetDataPd["Profit/Losses + 1"]

#counts the number of values in the Date column
TotalMonths = BudgetDataPd["Date"].count()
#total the entire Profit/Losses column, then formats it to a whole number with commas
TotalValue = format(BudgetDataPd["Profit/Losses"].sum(), ",.0f")
#averages the month to month change and then formats the number to show 2 decimal places with commas
AverageChange = format(BudgetDataPd["Difference"].mean(), ",.2f")
#give the highest value in the month to month change 
MaxChange = BudgetDataPd["Difference"].max()
#give the lowest value in the month to month change
MinChange = BudgetDataPd["Difference"].min()
#formats the min and max to a whole number
MaxChangeF = format(BudgetDataPd["Difference"].max(), ",.0f")
MinChangeF = format(BudgetDataPd["Difference"].min(), ",.0f")
#index the data by "Difference"
FindMonthIndex = BudgetDataPd.set_index("Difference")
#find the value of the 'Date' column at indexed values that correspond to the Min and Max values.
MaxChangeMonth = FindMonthIndex.at[MaxChange, 'Date']
MinChangeMonth = FindMonthIndex.at[MinChange, 'Date']

#print all of the information to console
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${TotalValue}")
print(f"Average Change: ${AverageChange}")
print(f"Greatest Increase in Profits: {MaxChangeMonth} (${MaxChangeF})")
print(f"Greatest Decrease in Profits: {MinChangeMonth} (${MinChangeF})")

#print all of the information to a cvs file in the same folder, titled "PyBankOutput.csv"
Output = os.path.join("PyBankOutput.csv")
with open(Output, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow([f"Total Months: {TotalMonths}"])
    csvwriter.writerow([f"Total: ${TotalValue}"])
    csvwriter.writerow([f"Average Change: ${AverageChange}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {MaxChangeMonth} (${MaxChangeF})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {MinChangeMonth} (${MinChangeF})"])

#Things I had difficulty with: 
#Finding the difference, month to month. used stack overflow to find and learn about the shift function.
#  after figuring this out, finding min, max, and average were easy.
#Formatting the outputs, i was trying to format the values in just the print function, 
#  then decided to create a variable with the already formatted information, figured out exactly how to format on stack overflow.
#Finding the specific date that corresponds to the min and max month changes, GoogleFu'd the at function. 
#  Unsure if I overthought how I utilized it, or if I could have used it without changing the index first.