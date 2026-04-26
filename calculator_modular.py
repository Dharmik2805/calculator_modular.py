# modular_calculator.py
# Internship Task 5: Functions & Modular Programming

# 1. Functions for basic arithmetic operations

def add_numbers(x, y=0):
    """Return the addition of x and y. Default y=0."""
    return x + y

def subtract_numbers(x, y=0):
    """Return the subtraction of x and y. Default y=0."""
    return x - y

def multiply_numbers(x, y=1):
    """Return the multiplication of x and y. Default y=1."""
    return x * y

def divide_numbers(x, y=1):
    """Return division of x by y. Handles division by zero."""
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# 2. Function to select operation based on user input
def run_calculator():
    """Interactive calculator for user choice."""
    print("=== Welcome to Your Calculator ===")
    print("Options: 1-Add, 2-Subtract, 3-Multiply, 4-Divide")
    
    choice = input("Choose an operation (1/2/3/4): ")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Numbers only!")
        return

    if choice == '1':
        print(f"Result: {add_numbers(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract_numbers(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply_numbers(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide_numbers(num1, num2)}")
    else:
        print("Invalid choice! Please enter 1-4.")

# 3. Independent testing of functions
if __name__ == "__main__":
    print("Testing all functions individually:")
    print("Add 12 + 8:", add_numbers(12, 8))
    print("Subtract 20 - 7:", subtract_numbers(20, 7))
    print("Multiply 9 * 5:", multiply_numbers(9, 5))
    print("Divide 15 / 3:", divide_numbers(15, 3))
    print("Divide 10 / 0:", divide_numbers(10, 0))
    print("\nStarting interactive calculator...\n")
    
    run_calculator()