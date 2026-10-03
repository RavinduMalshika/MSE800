class RentalError(Exception):
    pass

class InvalidDateRangeError(RentalError):
    print("Invalid Date Range")

class CarNotFoundError(RentalError):
    print("Invalid Car ID")

class CarUnavailableError(RentalError):
    print("Car is unavailable")

def create_booking(cars, car_id, start, end):
    pass
