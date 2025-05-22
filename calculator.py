#Create a basic calculator
def add(x, y):
    """Add two numbers."""
    return x + y
def subtract(x, y):
    """Subtract two numbers."""
    return x - y
def multiply(x, y):
    """Multiply two numbers."""
    return x * y
def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def calculator():   
    """A simple calculator."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                except ValueError as e:
                    print(e)
        else:
            print("Invalid choice. Please select a valid operation.")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
if __name__ == "__main__":
    calculator()    
# This code is a simple calculator that allows the user to perform basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers.
# It includes error handling for invalid inputs and division by zero.
# The calculator function prompts the user to select an operation and enter two numbers, then performs the selected operation and displays the result.
# The user can choose to perform another calculation or exit the program.