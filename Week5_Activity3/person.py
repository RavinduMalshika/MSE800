class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def describe(self):
        return "Person {} {}".format(self.name, self.age)

    