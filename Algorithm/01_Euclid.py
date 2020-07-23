def Euclid(a, b):
    r = a % b
    if r != 0:
        Euclid(b, r)
    else:
        print(b)

Euclid(1633, 355)
Euclid(5873,30)

print("Hello")