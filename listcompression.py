l = [i for i in range(1,100)]
print(l)


l_even = [i for i in range(2,100,2)]
print(l_even)

l_even = [ i for i in range(1,101) if i % 2 == 0]
print(l_even)


l_even = [ i for i in range(2,101,2) if i % 3 == 0 and i % 4 == 0]
print(l_even)
