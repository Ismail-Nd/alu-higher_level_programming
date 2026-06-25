def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: cannot divide by zero"
        return num1 / num2
    else:
        return "Error: invalid operator"

    
# Ask the user for input
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Call the function and show the result
result = calculate(num1, operator, num2)
print("Result:", result)

with open("results.txt", "a") as file:
    file.write(f"{num1} {operator} {num2} = {result}\n")

print("Result saved to results.txt")