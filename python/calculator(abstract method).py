

from abc import abstractmethod

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    __num1 = None
    __num2 = None
    __ans = None

    @property
    def num1(self):
        return self.__num1

    @property
    def num2(self):
        return self.__num2

    @property
    def ans(self):
        return self.__ans

    @num1.setter
    def num1(self, val):
        self.__num1 = val

    @num2.setter
    def num2(self, val):
        self.__num2 = val

    @ans.setter
    def ans(self, val):
        self.__ans = val

    @abstractmethod
    def calculate(self):
        pass

    def display(self):
        print(self.__ans)


class CalcSum(Calculator):

    def calculate(self):
        self.ans = self.num1 + self.num2
        
class CalcDiff(Calculator):
        
    def calculate(self):
        self.ans = self.num1 - self.num2

class CalcProd(Calculator):
        
    def calculate(self):
        self.ans = self.num1 * self.num2

class CalcQuo(Calculator):
        
    def calculate(self):
        self.ans = self.num1 / self.num2



c = CalcProd(12,2)
c.calculate()
c.display()