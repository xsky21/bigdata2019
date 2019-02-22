class HousePark:
    lastname= "박"
    def setname(self, a):
        self.firstname = a
        self.fullname = self.lastname + self.firstname
    def travel(self, b):
        print(self.fullname+", 부산여행을 가다.")

pey = HousePark()
pey.setname("응용")
print(pey.fullname)
pey.travel("부산")