class Bill:
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period

class Flatmates:
    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay(self, bill,flatmate2):
        self.bill = bill
        weight = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        return bill.amount * weight