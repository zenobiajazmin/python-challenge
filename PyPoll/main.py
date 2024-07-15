import csv
import os
import statistics

#created empty lists
votes = []
candidates = []
candidate_votes = {}
percent_candidate_votes = {}
#find the data
data = os.path.join(r"C:\\Users\\zenob\\CodeRepos\\2024DataViz\\python-challenge\\PyPoll\\Resources","election_data.csv")

#open the csv file
with open(data) as csvfile:

    #read csv file 
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    header = next(csvreader)

    #calculate through the rows
    for row in csvreader:
        #add each row of votes to the list
        votes.append(row[0])
        
        #add each row of candidates to the list
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

#calculate the percentage of votes for each candidate
for candidate in candidate_votes:
    percent_candidate_votes[candidate] = round((candidate_votes[candidate]/len(votes))*100, 3)

#find the winner
winner = max(candidate_votes, key=candidate_votes.get)

#print resuts
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(votes)))
print("-------------------------")
print(candidates[0]+ ": " + str(percent_candidate_votes[candidates[0]]) + "% " + "(" + str(candidate_votes[candidates[0]]) + ")")
print(candidates[1]+ ": " + str(percent_candidate_votes[candidates[1]]) + "% " + "(" + str(candidate_votes[candidates[1]]) + ")")
print(candidates[2]+ ": " + str(percent_candidate_votes[candidates[2]]) + "% " + "(" + str(candidate_votes[candidates[2]]) + ")")
print("------------------------")
print("Winner: " + winner)
print("------------------------")


#write the results to a text file
output = os.path.join(r"C:\\Users\\zenob\\CodeRepos\\2024DataViz\\python-challenge\\PyPoll\\analysis", "output.txt")

#used the same format as the print statments about with the \n to create a new line 
with open(output, 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(len(votes)) + "\n")
    text.write("-------------------------\n")
    text.write(candidates[0]+ ": " + str(percent_candidate_votes[candidates[0]]) + "% " + "(" + str(candidate_votes[candidates[0]]) + ")\n")
    text.write(candidates[1]+ ": " + str(percent_candidate_votes[candidates[1]]) + "% " + "(" + str(candidate_votes[candidates[1]]) + ")\n")
    text.write(candidates[2]+ ": " + str(percent_candidate_votes[candidates[2]]) + "% " + "(" + str(candidate_votes[candidates[2]]) + ")\n")
    text.write("-------------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("-------------------------\n")