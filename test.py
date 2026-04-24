class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def summa(self):
        print(self.num1 + self.num2)


o1 = Calculator(10, 40)

o1.summa()


calcul = Calculator(100, 300)

calcul.summa()