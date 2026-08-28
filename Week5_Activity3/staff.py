from person import Person

class Staff(Person):
    def __init__(self, name, address, age, staff_id, tax_num):
        super().__init__(name, address, age)
        self.staff_id = staff_id
        self.tax_num= tax_num
