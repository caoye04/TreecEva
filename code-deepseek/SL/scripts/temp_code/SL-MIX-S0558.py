temperature_data = {'New York': 75, 'Los Angeles': 82, 'Chicago': 68, 'Miami': 88, 'Seattle': 65}
city_weights = {'New York': 1.1, 'Los Angeles': 0.9, 'Chicago': 1.2, 'Miami': 0.8, 'Seattle': 1.0}

# Calculate average temperature (distractor)
avg_temp = sum(temperature_data.values()) / len(temperature_data)

# Find maximum temperature (distractor)
max_temp_city = max(temperature_data, key=temperature_data.get)

# Main logic: adjust city based on conditions
base_city = 'Chicago'
season_factor = 1.1

if temperature_data[base_city] > 70:
    adjusted_city = 'Miami'
else:
    if season_factor > 1.0:
        adjusted_city = 'Los Angeles'
    else:
        adjusted_city = 'New York'

# Intermediate calculation that doesn't affect final result (interference)
weighted_temp = temperature_data[base_city] * city_weights[base_city]

# Final assignment
final_temperature = temperature_data[adjusted_city]

print(f"Target result: {final_temperature}")