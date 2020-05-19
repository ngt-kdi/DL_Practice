import random

def LinearSearch(A, b):
    print(A)
    for i in A:
        if i == b:
            return True
    return False

A = [i * random.randint(1,10) for i in range(5)]
result = LinearSearch(A, 5)
print(result)