from staff import Staff

class AcademicStaff(Staff):
    def __init__(self, name, address, age, staff_id, tax_num, publications):
        super().__init__(name, address, age, staff_id, tax_num)
        self.publications = publications

    def describe(self):
            return "Academic Staff: {} {}".format(self.name, self.age)

    def getNumOfPublications(self):
        return len(self.publications)
