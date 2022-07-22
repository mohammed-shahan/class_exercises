

#creating a class calculator
class calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        self.sum = self.num1+self.num2
        print("Sum of the two numbers is :",self.sum)

    def multiply(self):
        self.product = self.num1*self.num2
        print("Product of the two numbers is :",self.product)
    
    def divide(self):
        self.division = self.num1/self.num2
        print("Division of the two numbers is :",self.division)
    
calc = calculator(int(input("Enter the first number")), int(input("enter the second number")))
calc.add()
calc.multiply()
calc.divide()