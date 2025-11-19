import math

def compute_cake_price(base_price, cakes_sold):
    demand_factor = math.log(cakes_sold + 1)
    final_price = base_price * math.exp(demand_factor)
    return final_price

base_price = 10
cakes_sold = 7
final_price = compute_cake_price(base_price, cakes_sold)
print(f'Result: {final_price}')