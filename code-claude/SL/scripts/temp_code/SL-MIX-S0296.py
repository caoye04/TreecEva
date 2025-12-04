import itertools

# Smart thermostat data processing
# Analyzing temperature readings to determine optimal settings

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Temperature readings from different rooms (in Celsius)
temperature_readings = {
    'living_room': [21.5, 22.0, 20.8, 21.2, 22.5],
    'bedroom': [19.8, 20.2, 20.5, 19.5, 20.0],
    'kitchen': [22.8, 23.5, 22.0, 23.0, 22.5],
    'bathroom': [21.0, 21.5, 20.8, 21.2, 21.5]
}

# Comfort ratings for each temperature point
comfort_ratings = {
    19.5: 3, 19.8: 4, 20.0: 5, 20.2: 6, 20.5: 7,
    20.8: 8, 21.0: 9, 21.2: 8, 21.5: 7, 22.0: 6,
    22.5: 5, 22.8: 4, 23.0: 3, 23.5: 2
}

# Energy efficiency factors (lower is better)
energy_factors = {
    'living_room': 1.2,
    'bedroom': 0.9,
    'kitchen': 1.5,
    'bathroom': 1.1
}

# Calculate average temperatures for each room
avg_temperatures = {room: sum(temps)/len(temps) 
                  for room, temps in temperature_readings.items()}

# Find the room with the most consistent temperature
temp_variations = {room: max(temps) - min(temps) 
                  for room, temps in temperature_readings.items()}
most_consistent_room = min(temp_variations, key=temp_variations.get)

# Convert some temperatures to Fahrenheit for alternative analysis
fahrenheit_temps = {room: [celsius_to_fahrenheit(t) for t in temps]
                   for room, temps in temperature_readings.items()}

# Combine all temperature readings into a single list
all_readings = list(itertools.chain(*temperature_readings.values()))

# Calculate highest comfort temperatures
high_comfort_threshold = 7
high_comfort_temps = [temp for temp, rating in comfort_ratings.items() 
                     if rating >= high_comfort_threshold]

# Find optimal temperature settings based on comfort and energy
filtered_readings = []
for temp in all_readings:
    if temp in comfort_ratings:
        if comfort_ratings[temp] >= 6:
            filtered_readings.append(temp)

# Calculate energy impact (not used in final determination)
energy_impact = sum(factor * avg_temperatures[room] 
                   for room, factor in energy_factors.items())

# Determine the optimal temperature setting
optimal_temperature = min(filtered_readings)

# Alternative calculation that isn't used
alternative_optimal = sum(high_comfort_temps) / len(high_comfort_temps)

print(f"Result: {optimal_temperature}")