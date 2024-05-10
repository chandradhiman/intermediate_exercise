def add(a,b):
    print(f"Adding {a} + {b}")
    return a+b

def sub(a,b):
    print(f"Sub {a} +{b}")
    return a-b

def multiply(a,b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"Divide {a} / {b}")
    return a / b

print("Let's do somthing math with just function!")

age = add(10,20)
height = sub (30,10)
weight = multiply(10,6)
iq = divide(100,2)

print(f"Age :{age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")

what = add(age, sub(height,multiply(weight,divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")


