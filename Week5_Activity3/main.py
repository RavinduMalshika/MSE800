from academic_staff import AcademicStaff
from general_staff import GeneralStaff

def main():
    lecturer = AcademicStaff(
        "John Doe",
        "1 Street, City",
        32,
        "A001",
        "TX001",
        ["pub1", "pub2"]
    );

    print(lecturer.describe())
    print(f"Number of Publications: {lecturer.getNumOfPublications()}")

    admin1 = GeneralStaff(
        "Sam",
        "2 Street, City",
        25,
        "G001",
        "TX002",
        32
    )
    print(admin1.describe())
    print(f"Pay rate: {admin1.getPayRate()}")

if __name__ == "__main__":
    main()
