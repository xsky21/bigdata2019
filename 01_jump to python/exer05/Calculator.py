class Calculator():
    sum_result = 0
    def __init__(self, numberlist):
        self.numberlist = numberlist
    def sum(self):
        for a in self.numberlist:
            self.sum_result +=a
        print(self.sum_result)
    def avg(self):
        self.sum_result=0
        for a in self.numberlist:
            self.sum_result +=a
        print(self.sum_result/len(self.numberlist))

if __name__=="__main__":
    cal1=Calculator([1,2,3,4,5])
    cal1.sum()
    cal1.avg()
    cal2=Calculator([6,7,8,9,10])
    cal2.sum()
    cal2.avg()