ingredient_prices = [2.40, 3.10, 1.99, 2.75, 2.10, 4.00]
affordable_prices = [price for price in ingredient_prices if price < 2.50]
total_cost = sum(affordable_prices)
has_volume_discount = total_cost > 10.0
final_cake_cost = total_cost * 0.9 if has_volume_discount else total_cost
print(f"Result: {final_cake_cost}")