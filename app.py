# Simple Calculator Application

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"

print("Welcome to the Simple Calculator!")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter the number of the operation you'd like to perform: ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == "1":
    print("The result is:", add(num1, num2))
elif choice == "2":
    print("The result is:", subtract(num1, num2))
elif choice == "3":
    print("The result is:", multiply(num1, num2))
elif choice == "4":
    print("The result is:", divide(num1, num2))
else:
    print("Invalid choice!")
