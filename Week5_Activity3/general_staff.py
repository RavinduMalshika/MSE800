from staff import Staff

class GeneralStaff(Staff):
    def __init__(self, name, address, age, staff_id, tax_num, rate_of_pay):
        super().__init__(name, address, age, staff_id, tax_num)
        self.id =id
        self.rate_of_pay = rate_of_pay

    def describe(self):
        return "General Staff: {} {}".format(self.name, self.age)

    def getPayRate(self):
        return self.rate_of_pay
