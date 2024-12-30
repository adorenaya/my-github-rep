# Ask for two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = number1 + number2 
print(f"The result is: {result}")

# Ask the user what operation they want to perform 
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on the users choice 
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
    else: 
        result = "Error: Cannot divide by zero."
else: 
    result = "Invalif operation."

#print the result 
print(f"The result is: {result}")