#Static Methods

class Calculator:

    @staticmethod
    def Add(num1, num2):
        return num1 + num2

    @staticmethod
    def Sub(num1, num2):
        return num1 - num2

    @staticmethod
    def Div(num1, num2):
        return num1 / num2

    @staticmethod
    def Mult(num1, num2):
        return num1 * num2


print(Calculator.Add(3, 4))
print(Calculator.Sub(13, 4))
print(Calculator.Mult(3, 4))
print(Calculator.Div(28, 4))