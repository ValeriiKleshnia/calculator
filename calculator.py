def calculator():
 operation = input("Select operation (+, -, *, /):")
 num1 = float(input("Enter the first number:"))
 num2 = float(input("Enter second number: "))
 if operation == '+':
  result = num1 + num2
 elif operation == '-':
  result = num1 - num2
 elif operation == '*':
  result = num1 * num2
 elif operation == '/':
  result = num1 / num2
 else:
  print("Incorrect operation.")
  return
 print("Result:", result)
calculator()
