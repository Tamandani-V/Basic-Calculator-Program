# How to Build a Simple Calculator in Python
# This is a simple calculator program that can perform basic arithmetic operations
# such as addition, subtraction, multiplication, and division.

def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide two numbers."""   
    if y == 0:
        return "None"
    return x / y

def calculator():
    """Function to perform basic arithmetic operations."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user for operation choice
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                # Take input numbers from the user, converting them to float
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Based on user choice, call the corresponding function and print the result
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result is None:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"{num1} / {num2} = {result}")

            # Ask the user if they want to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        else:
            print("Invalid choice! Please select from 1, 2, 3, or 4.")

# Run the calculator program
calculator()

# End of Calculator.py
# This code defines a simple calculator that can perform addition, subtraction,
# multiplication, and division. It handles user input and provides feedback
# for invalid inputs or operations. 




