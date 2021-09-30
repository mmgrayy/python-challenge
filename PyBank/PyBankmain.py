#importing os and csv in order to read the files
import os
import csv
#create empty lists to store data
Month_Total=[]
Profit_Total=[]
Monthly_Profit_Change=[]

#translate path taken in terminal to python
csvpath= os.path.join('..','PyBank','Resources','budget_data.csv')
#Read the csv file
with open(csvpath, 'r') as budget_data:
    
    csvreader= csv.reader(budget_data, delimiter=',')
#skipping the header so you may only iterate through the data
    header= next(csvreader)
#looping through rows to assign Month list and Profit list
#append directly into empty lists we have previously created
    for column in csvreader:
        Month_Total.append(column[0])
        Profit_Total.append(int(column[1]))
#iterate through the lenghth of the Profit Total index, but -1 to include the upper bound
    for monthlyprofit in range(len(Profit_Total)-1):
#create equation to find the difference in monthly profits (i.e current month profit  - last months profit)
        Monthly_Profit_Change.append(Profit_Total[monthlyprofit+1]-Profit_Total[monthlyprofit])
        
#define variable for finding the average of the monthly profit change

#Print the text
print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Print total amount of months using the length function
print(f"Total Months: {len(Month_Total)}")
#Print total Profit using sum function
print(f"Total: $ {sum(Profit_Total)}")


#export your results
results_file= os.join.path('..', 'PyBank','budget_data_results.txt.')
with open (results_file, "w") as text
#Write results into text file
    text.write("Financial Analysis")
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    text.write(f"Total Months: {len(Month_Total)}")
    text.write(f"Total: $ {sum(Profit_Total)}")


