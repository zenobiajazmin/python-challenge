import csv
import os
import statistics



data = os.path.join(r"C:\\Users\\zenob\\CodeRepos\\2024DataViz\\python-challenge\\PyBank\\Resources", "budget_data.csv")

with open(data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")