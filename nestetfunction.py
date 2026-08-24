def a(p,d = 2):

    r = 2
    def b():
        print(p, r, d)
        print(p * r * d / 100)
    b()

a(1000)
