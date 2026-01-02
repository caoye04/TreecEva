from itertools import combinations

# Sensor readings from three different stations
temperature_readings = [20, 25, 30]
humidity_readings = [40, 50, 60]
pressure_readings = [1010, 1020]

# Generate all possible triplets (temp, humidity, pressure)
all_combinations = list(combinations(temperature_readings + humidity_readings + pressure_readings, 3))

# Filter combinations where product of elements is divisible by 1000
calculated_products = [a * b * c for a, b, c in all_combinations]
filtered_products = [prod for prod in calculated_products if prod % 1000 == 0]

# Final computation
result = sum(filtered_products)
print(f"Result: {result}")