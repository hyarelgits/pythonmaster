marks = 51
if marks > 90:
    print("A grade")
elif marks > 70:
    print("B grade")
elif marks > 50:
    print("C grade")
else:
    print("D grade")


marks=35
grade = "A" if marks > 40 else "B"
print(grade)
print("add bonus marks")
marks = marks + 5  if marks > 80 else marks - 20
print(marks)




x=250
y=200
z=300


if x < y:
   print("x < y")
   if x < z:
      print("x < z")
   else:
      print("x > z")
else:
    print("x > y")
    if x < z:
       print("x < z")
    else:
        print("x > z")

