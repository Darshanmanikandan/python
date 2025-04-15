from calculator import simple_calc, scientific_calc, prg_calc

def main():
    print("Welcome to Modular Calculator 🧮")
    print("Choose Operation Type:")
    print("1. Simple Calculator")
    print("2. Scientific Calculator")
    print("3. Programmer Calculator (Bitwise Ops)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")

        if op == "+":
            print("Result:", simple_calc.add(a, b))
        elif op == "-":
            print("press 0 to find (num_1 - num_2) \npress 1 to find (num_2 - num_1)")
            opt=int(input())
            print("Result:", simple_calc.subtract(a, b , opt))
        elif op == "*":
            print("Result:", simple_calc.multiply(a, b))
        elif op == "/":
            print("press 0 to find (num_1 / num_2) \npress 1 to find (num_2 / num_1)")
            print("Result:", simple_calc.divide(a, b))
        else:
            print("Invalid operation!")

    elif choice == "2":
        print("Scientific Operations: power, sqrt, sin, cos")
        op = input("Choose operation: ")

        if op == "power":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", scientific_calc.power(a, b))
        elif op == "sqrt":
            a = float(input("Enter number: "))
            print("Result:", scientific_calc.sqrt(a))
        elif op == "sin":
            a = float(input("Enter angle in degrees: "))
            print("Result:", scientific_calc.sin(a))
        elif op == "cos":
            a = float(input("Enter angle in degrees: "))
            print("Result:", scientific_calc.cos(a))
        else:
            print("Invalid scientific operation!")

    elif choice == "3":
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        print("Bitwise Ops: &, |, ^, <<, >>")
        op = input("Choose operation: ")

        if op == "&":
            print("Result:", prg_calc.bitwise_and(a, b))
        elif op == "|":
            print("Result:", prg_calc.bitwise_or(a, b))
        elif op == "^":
            print("Result:", prg_calc.bitwise_xor(a, b))
        elif op == "<<":
            print("Result:", prg_calc.left_shift(a, b))
        elif op == ">>":
            print("Result:", prg_calc.right_shift(a, b))
        else:
            print("Invalid bitwise operation!")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
