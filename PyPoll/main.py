#import dependancies to read data
import csv
import os
#create empty list to store total votes
Votes_Total=[]
#Make candidates variables so they become iterable
Candidate_K_Votes=0
Candidate_C_Votes=0
Candidate_L_Votes=0
Candidate_O_Votes=0
#open the csv file
csvpath=os.path.join('..','PyPoll','Resources','election_data.csv')
#read csv file
with open (csvpath,'r') as election_data:
    csvreader= csv.reader(election_data, delimiter=',')
#remove header before manipulating the data
    header=next(csvreader)
#REMEMBER Column[0]= Voter ID, Column[1]=County, & Column[2]=Candidate
#Finding total amount of votes
    for column in csvreader:
        Votes_Total.append(column[0])
#If statement to decifer votes per candidate
#remember the double ==
        if column[2]== "Khan":
            Candidate_K_Votes +=1
        elif column[2]== "Correy":
            Candidate_C_Votes +=1
        elif column[2]== "Li":
            Candidate_L_Votes +=1
        elif column[2]== "O'Tooley":
            Candidate_O_Votes +=1
#Finding the percentages
quotient_k= Candidate_K_Votes/len(Votes_Total)
percent_k= quotient_k *100

quotient_c= Candidate_C_Votes/len(Votes_Total)
percent_c= quotient_c *100

quotient_l= Candidate_L_Votes/len(Votes_Total)
percent_l= quotient_l *100

quotient_o= Candidate_O_Votes/len(Votes_Total)
percent_o= quotient_o *100
#Create 2 lists (candidates/votes) and zip them together to find the winner
candidates= ["Kahn","Correy", "Li", "O'Tooley"]
#List of vote counts ^
Vote_Count= [Candidate_K_Votes,Candidate_C_Votes, Candidate_L_Votes, Candidate_O_Votes ]
dictionary= dict(zip(candidates, Vote_Count))
Winner_key= max(dictionary, key=dictionary.get)

#creating variables for equations
VT= len(Votes_Total)



print("Election Results")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Votes: {VT}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Votes for Candidate Khan: {percent_k:.2f}% ({(Candidate_K_Votes)} Votes)")
print(f"Total Votes for Candidate Correy: {percent_c:.2f}% ({(Candidate_C_Votes)} Votes)")
print(f"Total Votes for Candidate Li: {percent_l:.2f}%  ({(Candidate_L_Votes)} Votes)")
print(f"Total Votes for Candidate O'Tooley: {percent_o:.2f}%    ({(Candidate_O_Votes)} Votes)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("And the winner of the election is..........")
print(Winner_key)

#exporting as a text file
results_file=os.path.join('analysis','election_data_results.txt')
with open (results_file, "w") as text:
    text.write("Election Results\n")
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    text.write('\n')
    text.write(f"Total Votes for Candidate Khan: {percent_k:.3f}% ({(Candidate_K_Votes)} Votes)")
    text.write('\n')
    text.write(f"Total Votes for Candidate Correy: {percent_c:.3f}% ({(Candidate_C_Votes)} Votes)")
    text.write('\n')
    text.write(f"Total Votes for Candidate Li: {percent_l:.3f}%  ({(Candidate_L_Votes)} Votes)")
    text.write('\n')
    text.write(f"Total Votes for Candidate O'Tooley: {percent_o:.3f}%    ({(Candidate_O_Votes)} Votes)")
    text.write('\n')
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    text.write('\n')
    text.write("And the winner of the election is..........")
    text.write('\n')
    text.write(Winner_key)
    lines=text.write
    print(lines)
