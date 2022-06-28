def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else "undefined!"

print("****************")
print("MENU")
print("****************")

print("[A] - Addition")
print("[S] - Subtraction")
print("[M] - Multiplication")
print("[D] - Division")
print("[X] - Exit")

print("-----------------")

choice = input("Enter your choice: ")
print()

if choice == 'A':
    print("ADDITION")
elif choice == 'S':
    print("SUBTRACTION")
elif choice == 'M':
    print("MULTIPLICATION")
elif choice == 'D':
    print("DIVISION")
elif choice == 'E':
    print("Thank you!")
    print("Press any key to continue . . . ")
    quit()
else:
    print("INPUT NOT INCLUDED!")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 'A':
    print("The sum is", add(num1, num2))
elif choice == 'S':
    print("The difference is", subtract(num1, num2))
elif choice == 'M':
    print("The product is", multiply(num1, num2))
elif choice == 'D':
    print("The quotient is", divide(num1, num2))
else:
    print("ERROR!")