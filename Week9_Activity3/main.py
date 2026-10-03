def calculate_total(price, quantity):
    total = price * quantity
    discount = 10
    final_price = total - discount
    return final_price

price = 25
quantity = 3

breakpoint()

result = calculate_total(price, quantity)
print(result)
