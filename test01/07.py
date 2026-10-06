try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    else:
        raise ValueError("Invalid operator")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError as e:
    print("Error:", e)
else:
    print("Result:", result)
finally:
    print("Program completed.")