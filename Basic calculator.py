def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"

print("Simple Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter choice (1/2/3/4): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(x, y))
elif choice == '2':
    print("Result:", subtract(x, y))
elif choice == '3':
    print("Result:", multiply(x, y))
elif choice == '4':
    print("Result:", divide(x, y))
else:
    print("Invalid input")
