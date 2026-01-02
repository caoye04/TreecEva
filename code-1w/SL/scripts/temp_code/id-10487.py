temperatures_celsius = [23, 19, 17, 25, 30, 18, 21, 27, 29, 20]

# Irrelevant distraction: unused variable
offset_correction = 2.5

temp_with_index = list(enumerate(temperatures_celsius))

city_zones = ['North', 'South', 'East', 'West']
zone_mapping = {i: city_zones[i % len(city_zones)] for i in range(len(temperatures_celsius))}

# Convert to Fahrenheit as distraction
temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]

# Main logic: find temps above 22C and compute average in Celsius
high_temp_indices = [i for i, temp in temp_with_index if temp > 22]
filtered_temps = [temperatures_celsius[i] for i in high_temp_indices]
filtered_avg = sum(filtered_temps) / len(filtered_temps)

Result: filtered_avg