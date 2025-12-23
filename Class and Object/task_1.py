class Calculator:
    brand = 'Casio MS990'

    def add(self, num1, num2): # selt --> bortoman object ke bojhay
        return num1 + num2

    def deduct(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        return num1 / num2

# Calculator class er object ba instance
my_calculator = Calculator()

# method gulake call korchi..
result_for_add = my_calculator.add(200, 100)
result_for_deduct = my_calculator.deduct(200, 100)
result_for_multiply = my_calculator.multiply(200, 100)
result_for_divide = my_calculator.divide(200, 100)

print('summation of num1 and num2 =', result_for_add)
print('deduct of num1 and num2 =', result_for_deduct)
print('multiply of num1 and num2 =', result_for_multiply)
print('division of num1 and num2 =', result_for_divide)