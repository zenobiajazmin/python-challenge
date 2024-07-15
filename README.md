# python-challenge

I have create two python source code files to correspond to module 3 pybank and pypoll. 

Before I started I had met with a tutor to understand the assignment better as I am still learning how to interpert the ask.

Once I understood the assignment I went forward to complete the assignment. The code will display the results in the terminal as well as create the output in a text file in each of the analysis folders in PyBank and PyPoll.

Went to Xpert Learnng Assistant for one part of the code where it was asking how to calculate the amount of votes per candidate and it used the code below, I modified it to understand it with my code. 

Xpert Learning sample:
Here's a general outline of how you can achieve this in Python:

import csv

# Initialize a dictionary to store the votes for each candidate
candidate_votes = {}

# Read the election data file
with open('election_data.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Iterate through each row in the data
    for row in reader:
        candidate = row['Candidate']
        
        # Check if the candidate is already in the dictionary
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
