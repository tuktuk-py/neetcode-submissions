import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self,num1:int, num2:int=None):
        if num2 is None:
            return round(math.pi * num1 ** 2, 2)
        else:
            return num1 * num2

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
