class OrdinaryCalc:

    num1 = float
    num2 = float

    def set_num1(self, num1):
        self.num1 = num1


    def get_num1(self):
        return self.num1


    def get_num2(self):
        return self.num2


    def set_num2(self, num2):
         self.num2 = num2


    def Add(self):
        return self.num1 + self.num2


    def Div(self):
        return self.num1 / self.num2


    def Mul(self):
        return self.num1 * self.num2


    def Sub(self):
        return self.num1 - self.num2
