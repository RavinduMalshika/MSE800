class UniversityConfig:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance =  super().__new__(cls)
            cls.name = "Yoobee"
            cls.year = 2026
            cls.semester = "1st Semester"

        return cls._instance

    def display_config(self):
        print("University: ", self.name)
        print("Academic Year: ", self.year)
        print("Semester: ", self.semester)

    def set_config(self, name, year, semester):
        self.name = name
        self.year = year
        self.semester = semester

config1 = UniversityConfig()
config1.display_config()

print()

config2 = UniversityConfig()
config2.set_config("Yoobee College", 2026, "1")

config1.display_config()

print()
print(config1 == config2)
