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
#Finding the maximum and minimums of the monthly profit changes
maximum_profit= max(Monthly_Profit_Change)
minimum_profit= min(Monthly_Profit_Change)

#CORELATE MAX AND MIN W MONTHS
#Add 1 because it is referring to the next month
maximum_month = Monthly_Profit_Change.index(maximum_profit)+1
minimum_month= Monthly_Profit_Change.index(minimum_profit)+1
 
#create varaibles for the equations to simplify print statements
print_total= len(Month_Total)
print_sum= sum(Profit_Total)
print_difference= sum(Monthly_Profit_Change)/len(Monthly_Profit_Change)

#Print the text
print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Print total amount of months using the length function
print(f"Total Months: {print_total}")
#Print total Profit using sum function
print(f"Total: ${print_sum}")
#finding the average monthly profit difference
print(f"Average Change: ${print_difference}")
print(f'Greatest Increase in Profits: {Month_Total[maximum_month]} ${(maximum_profit)}')
print(f'Greatest Decrease in Profits: {Month_Total[minimum_month]} ${(minimum_profit)}')



#export your results
results_file= os.path.join('analysis','budget_data_results.txt.')
#do NOT forget :
with open (results_file, "w") as text:
#Write results into text file
    text.write("Financial Analysis")
    text.write('\n')
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    text.write('\n')
    text.write(f"Total Months: {len(Month_Total)}")
    text.write('\n')
    text.write(f"Total: $ {sum(Profit_Total)}")
    text.write('\n')
    text.write(f"Average Change: ${sum(Monthly_Profit_Change)/len(Monthly_Profit_Change)}")
    text.write('\n')
    text.write(f'Greatest Increase in Profits: {Month_Total[maximum_month]} ${(maximum_profit)}')
    text.write('\n')
    text.write(f' Greatest Decrease in Profits: {Month_Total[minimum_month]} ${(minimum_profit)}')
    lines=text.write
    print(lines)
