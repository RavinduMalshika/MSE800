def calculate_price(price, quantity, discount = 0):
    result = price * quantity * ((100 - discount) / 100)
    return round(result, 2)

