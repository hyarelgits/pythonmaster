import sys
import os
import csv
print(os.getcwd())
os.chdir("/home/devops/Desktop")
print(os.getcwd())

with open("file1.csv") as f:
    lines = csv.reader(f)
   
    for line in lines:
        print(line)
with open("file1.csv") as f:
    lines = csv.reader(f, delimiter=";")
    print("*" * 20)
