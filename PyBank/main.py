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
    for mp in range(len(Profit_Total)-1):
#create equation to find the difference in monthly profits (i.e current month profit  - last months profit)
        Monthly_Profit_Change.append(Profit_Total[mp+1]-Profit_Total[mp])
maximum_profit= max(Monthly_Profit_Change)
minimum_profit= min(Monthly_Profit_Change)

#CORELATE MAX AND MIN W MONTHS 
        
#define variable for finding the average of the monthly profit change

#Print the text
print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Print total amount of months using the length function
print(f"Total Months: {len(Month_Total)}")
#Print total Profit using sum function
print(f"Total: $ {sum(Profit_Total)}")
#finding the average monthly profit difference
print(f"Average Change: ${sum(Monthly_Profit_Change)/len(Monthly_Profit_Change)}")
print(maximum_profit)
print(minimum_profit)

#export your results
results_file= os.path.join('analysis','budget_data_results.txt.')
#do NOT forget :
with open (results_file, "w") as text:
#Write results into text file
    text.write("Financial Analysis")
    text.write('/n')
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    text.write('/n')
    text.write(f"Total Months: {len(Month_Total)}")
    text.write('/n')
    text.write(f"Total: $ {sum(Profit_Total)}")
    text.write('/n')
    lines=text.write
    print(lines)
