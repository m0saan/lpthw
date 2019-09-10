def add(a , b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a , b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a , b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def devide(a, b):
    print(f"Deviding {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(12 , 24)
height = subtract(30 , 5)
weight = multiply(100 , 3)
iq = devide(50 , 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit , type it anyway
print("Here is a puzzle")

# age + (height - (weight * (iq / 2))) 
what = add(age, subtract(height , multiply(weight , devide(iq , 2))))

print("That becomes : ", what , "Can you do it with it by hand?")