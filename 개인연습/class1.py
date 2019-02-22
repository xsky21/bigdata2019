class FourCal:
    def setdata(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a * self.b)
    def sub(self):
        print(self.a-self.b)
    def div(self):
        print(self.a/self.b)
a = FourCal()
a.setdata(4,2)
a.sum()
a.sub()
a.mul()
a.div()
