class TravelPackage:
    def __init__(self, destination, hotel, transport, meal_plan, activities, insuarance):
        self.destination = destination
        self.hotel = hotel
        self.transport = transport
        self.meal_plan= meal_plan
        self.activities = activities
        self.insuarance = insuarance

    def display(self):
        print("Destination: ", self.destination)
        print("Hotel: ", self.hotel)
        print("Transport: ", self.transport)
        print("Meal Plan: ", self.meal_plan)
        print("Activities: ", self.activities)
        print("Insuarance: ", self.insuarance)

class TravelPackageBuilder:
    def __init__(self):
        self.destination = None
        self.hotel = None
        self.transport = None
        self.meal_plan= None
        self.activities = []
        self.insuarance = None

    def set_destination(self, destination):
        self.destination = destination
        return self

    def set_hotel(self, hotel):
        self.hotel = hotel
        return self

    def set_transport(self, transport):
        self.transport = transport
        return self

    def set_meal_plan(self, meal_plan):
        self.meal_plan = meal_plan
        return self

    def set_activities(self, activities):
        self.activities = activities
        return self

    def set_insuarance(self, insuarance):
        self.insuarance = insuarance
        return self

    def build(self):
        return TravelPackage(
            self.destination,
            self.hotel,
            self.transport,
            self.meal_plan,
            self.activities,
            self.insuarance
        )

package = (
    TravelPackageBuilder()
    .set_destination("Auckland")
    .set_hotel("5-star")
    .set_transport("Car")
    .set_meal_plan("Lunch")
    .set_activities(["City Tour", "Museum"])
    .set_insuarance("Yes")
    .build()
)

package.display()
