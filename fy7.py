def c3(p, r=4, d=1):
     i = p * r * d / 100
     t = i * .2
     return i , t

print(c3(1000))
i, t = c3(1000)
print(i)
print(t)
