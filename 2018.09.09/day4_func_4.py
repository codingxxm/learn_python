def add (a,b):
    print(f"ADDING {a} + {b}")
    return a+b

def subtract(a,b):
    print(f"SUBTRACT {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a/b

print("Let's do some math with just functions!")

age = add(20,4)
height = subtract(187,7)
weight = multiply(15,10)
iq = divide(1000,2)

print(f"Age {age} , height {height} , weight {weight} , iq {iq} ")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That becomes : ",what ,"Can you do it by hand?")
