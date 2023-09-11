class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 / self.num1
obj = Calculator(10, 94)
add_result = obj.add()
subtract_result = obj.subtract()
multiply_result = obj.multiply()
divide_result = obj.divide()
print("Addition:", add_result)
print("Subtraction:", subtract_result)
print("Multiplication:", multiply_result)
print("Division:", divide_result)
