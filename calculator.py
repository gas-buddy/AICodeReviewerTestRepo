class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def calculate_average(self, numbers):
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)

    def find_max(self, numbers):
        max_val = numbers[0]
        for num in numbers:
            if num > max_val:
                max_val = num
        return max_val

def process_user_input():
    calc = Calculator()
    operation = input("Enter operation (add/subtract/multiply/divide): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "add":
        result = calc.add(num1, num2)
    elif operation == "subtract":
        result = calc.subtract(num1, num2)
    elif operation == "multiply":
        result = calc.multiply(num1, num2)
    elif operation == "divide":
        result = calc.divide(num1, num2)

    print("Result: " + str(result))
    return result

if __name__ == "__main__":
    process_user_input()
