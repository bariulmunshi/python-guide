def calculator():
    try:
        # Taking input for the first number
        num1 = float(input("Enter the first number: "))
        
        # Taking input for the second number
        num2 = float(input("Enter the second number: "))
        
        # Performing calculations
        print("Sum:", num1 + num2)
        print("Difference:", num1 - num2)
        print("Product:", num1 * num2)
        
        # Checking if the second number is not zero for division
        if num2 != 0:
            print("Quotient:", num1 / num2)
        else:
            print("Cannot divide by zero.")
    except ValueError:
        print("Please enter valid numeric values.")

# Example Usage:
calculator()
