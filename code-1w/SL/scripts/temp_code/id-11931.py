temperatures_celsius = [25, 30, 35, 40, 45]

temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]

above_threshold = [temp for temp in temperatures_fahrenheit if temp > 86]

indexed_temps = list(enumerate(above_threshold))

filtered_values = [temp for i, temp in indexed_temps if i % 2 == 0]

filtered_sum = sum(filtered_values)
print(f"Result: {filtered_sum}")