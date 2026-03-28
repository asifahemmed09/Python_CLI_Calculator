import utils.transport
import utils.session
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2  

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

print("Welcome to the simple calculator!")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter the number corresponding to the operation you want to perform: ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == '1':
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == '2':
    result = subtract(num1, num2)
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == '3':
    result = multiply(num1, num2)
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == '4':
    result = divide(num1, num2)
    print(f"The result of {num1} / {num2} is: {result}")
else:
    print("Invalid operation selected. Please choose a valid option.")