def add(num1, num2):
  """Adds two numbers."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers."""
  return num1 / num2

def main():
  """Main function."""
  operator = input("Enter an operator (+, -, *, /): ")
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operator.")
    return

  print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
  main()
