def add(a, b):
    return a + b

def subtract(a,b,opt=0):
    if opt > 1 or opt < 0 :
        raise ValueError("Invalid argument...")
    return a - b if opt == 0 else b - a

def multiply(a, b):
    return a * b

def divide(a, b ,opt=0):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    if opt > 1 or opt < 0 :
        raise ValueError("Invalid argument...")
    return a / b if opt == 0 else b / a
