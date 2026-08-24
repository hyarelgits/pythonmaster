def a(p,d = 2):

    r = 2

    def b():
        global r
        r = 4
        print(p, r, d)
        print(p * r * d / 100)
        print("New r ", r)
    b()
