import sys
import os
print(os.getcwd())
os.chdir("/home/devops/Desktop")
print(os.getcwd())

f =  open("f1.py")
print(f)
f = open("f1.py",encoding = 'UTF-8')
print(f.read())
f.close()

