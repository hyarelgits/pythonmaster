l = []
for i in range(100):
    l.append(i+1)
print(l)

print("============")
l_4 = []

MAX = 5
j = 0;
for i in l:
    if i %2 !=0:
       continue



    if  i % 4 == 0:
          l_4.append(i)
          j += 1
          if j < MAX:
              break
print(l_4)
print()
