import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b
def menu():
    print("Select operation:")
    print("1. Suma")
    print("2. Resta")
    print("4. Division")


    choice = int(input("Enter choice: "))
    return choice
def perform_operation(choice):
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", add(a, b))

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", subtract(a, b))
    
    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", divide(a, b))
def main():
    while True:
        choice = menu()
        perform_operation(choice)

if __name__ == "__main__":
    main() 
