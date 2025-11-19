import math

ingredients_count = 16
base_price = 10 * math.log2(ingredients_count)
discount_factor = 0.85

if base_price > 20 and ingredients_count > 8:
    final_price = base_price * discount_factor
else:
    final_price = base_price

print(f'Result: {final_price}')