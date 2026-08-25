import sys
import os
import csv
print(os.getcwd())
os.chdir("/home/devops/Desktop")
print(os.getcwd())

data = [
    [1,'Kevin','ART'],
    [2,'sammy','BRT'],
    [3,'molly','CRT']
]

with open('csv2_w.csv', 'w', newline="") as f:
    writer = csv.writer(f)

    for row in data:
        	writer.writerow(row)	
