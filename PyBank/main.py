import csv
import os
import statistics


#find the data
data = os.path.join(r"C:\\Users\\zenob\\CodeRepos\\2024DataViz\\python-challenge\\PyBank\\Resources", "budget_data.csv")


#create empty lists
months = []
profit_loss = []
change = []
previous_profit = 0

#open the csv file
with open(data) as csvfile:
    
    #read the csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    header = next (csvreader)

    #calculate throught the rows
    for row in csvreader:
        #add each row of months to the list 
        months.append(row[0])
        #add each row of the profit/loss column to the list
        profit_loss.append(int(row[1]))

        #creating a new list for the changed values
        current_profit = int(row[1])
        if previous_profit != 0:   
            change.append(current_profit - previous_profit)
        previous_profit = current_profit    
        #previous_profit = int(row[1])
        
    total_change = sum(change)
    average_change = format(total_change/len(change), '.2f')
    #add the list together
    total_profit_loss=sum(profit_loss)    
    
    #getting the greatest and lowest change and the months that they occured
    greatest_change = max(change)
    greatest_change_month = months[change.index(greatest_change)+1]
    lowest_change = min(change)
    lowest_change_month = months[change.index(lowest_change)+1]

  
    #print the results
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(months)))
    print("Total: $" + str(total_profit_loss))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + greatest_change_month +" ($"+ str(greatest_change)+")")
    print("Greatest Decrease in Profits: " + lowest_change_month + " ($" + str(lowest_change)+")")

#write the results to a text file
output = os.path.join(r"C:\\Users\\zenob\\CodeRepos\\2024DataViz\\python-challenge\\PyBank\\analysis", "output.txt")

#used the same format as the print statments above with the \n to create a new line
with open(output, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write("Total Months: " + str(len(months)) + "\n")
    text.write("Total: $" + str(total_profit_loss) + "\n")
    text.write("Average Change: $" + str(average_change) + "\n")
    text.write("Greatest Increase in Profits: " + greatest_change_month +" ($"+ str(greatest_change)+")\n")
    text.write("Greatest Decrease in Profits: " + lowest_change_month + " ($" + str(lowest_change)+")\n")