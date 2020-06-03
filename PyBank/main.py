#Import and read csv file, import pandas and statistics
import os
import csv
budget_csv = "/Users/caitlindonovan/Desktop/ColumbiaBootcamp/Homework/python-challenge/PyBank/Resources/budget_data.csv"
export_file = "/Users/caitlindonovan/Desktop/ColumbiaBootcamp/Homework/python-challenge/PyBank/PyBank.txt"
import pandas as pd 
import statistics


#Define the function for the analysis
def budget_analysis(budget_csv):
    #Read the CSV
    budget_csv_df = pd.read_csv(budget_csv, encoding="UTF8")

    # Count the total number of months in the dataset
    Total_Months = len(budget_csv_df)
    
    # Calculate net total amount of "Profit/Losses" over the entire period
    Net_Total = sum(budget_csv_df['Profit/Losses'])

    # Calculate average of the changes in "Profit/Losses" over the entire period
    MoM_Diff = budget_csv_df["Profit/Losses"].diff()
    Diffs = []
    for item in MoM_Diff:
        diff = float(item)
        Diffs.append(diff)

    #Store values in new column
    budget_csv_df.insert(2, "MoM Change", Diffs)

    #Find the average of the profits/losses
    Net_Avg = MoM_Diff.mean()
    Net_Avg = round(Net_Avg, 2)

    #Find greatest increase
    maxValue = budget_csv_df['MoM Change'].max()
    maxValueLoc = budget_csv_df['MoM Change'].idxmax(axis=0, skipna=True)
    maxValueMonth = budget_csv_df.loc[maxValueLoc][0]

    #Find greatest decrease
    minValue = budget_csv_df['MoM Change'].min()
    minValueLoc = budget_csv_df['MoM Change'].idxmin(axis=0, skipna=True)
    minValueMonth = budget_csv_df.loc[minValueLoc][0]

    # Produce Summary
    output = (
        f"Financial Analysis\n"
        f"-----------------------\n"
        f"Total Months:  {Total_Months}\n"
        f"Total: {Net_Total}\n"
        f"Average Change: ${Net_Avg}\n"
        f"Greatest Increase in Profits: {maxValueMonth} (${maxValue})\n"
        f"Greatest Decrease in Profits: {minValueMonth} (${minValue})\n")
    
    # Print the Summary in Terminal
    print(output)

    # Export Summary to text file
    text_file = open(export_file, "w")
    text_file.write(output)
    text_file.close()
   
#Execute the function
budget_analysis(budget_csv)





