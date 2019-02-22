class City:
    crime = 100
    def __init__(self, poverty):
        self.crime +=poverty
        print(self.crime)
    def aggresive_peace(self, police_budget):
        self.crime -= police_budget/2
        print(self.crime)
    def gradual_peace(self,welfare_budget):
        self.crime -= welfare_budget
        print(self.crime)

