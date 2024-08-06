print("""
      *****************Calculator***************""")

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

operation = input("Enter the operation: ")

if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    if number_2 == 0:
        print("Division by 0 is not valid.")
    else:
        result = number_1 / number_2
else:
    print("Invalid Entry")
print("Result: ", result)
