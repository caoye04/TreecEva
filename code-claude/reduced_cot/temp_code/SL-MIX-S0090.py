import itertools

def calculate_potential_energy(particles):
    # Calculate potential energy (not used in final calculation)
    energy = 0
    for p1, p2 in itertools.combinations(particles, 2):
        distance = sum(abs(a - b) for a, b in zip(p1, p2))
        energy += distance
    return energy

def process_signal(signal_data, threshold=50):
    # Process signal data (not relevant to main calculation)
    processed = []
    for signal in signal_data:
        if signal > threshold:
            processed.append(signal * 0.8)
        else:
            processed.append(signal * 1.2)
    return processed

# Sensor readings from different monitoring stations
sensor_readings = [
    [42, 18, 35, 19, 42],
    [29, 16, 22, 31, 54],
    [38, 47, 23, 15, 63],
    [21, 44, 39, 72, 11]
]

# Calculate mean values for each station (distraction)
mean_values = [sum(station) / len(station) for station in sensor_readings]

# Extract values exceeding threshold (key operation)
threshold = 40
all_readings = [reading for station in sensor_readings for reading in station]
valid_readings = list(filter(lambda x: x > threshold, all_readings))

# Apply correction factor based on environmental conditions
correction_factors = [1.05, 0.98, 1.12, 0.91, 1.03]
modified_readings = []

for i, reading in enumerate(all_readings):
    factor_idx = i % len(correction_factors)
    modified_readings.append(reading * correction_factors[factor_idx])

# Calculate some statistics (distraction)
max_reading = max(all_readings)
min_reading = min(all_readings)
range_value = max_reading - min_reading

# Extract specific slices for analysis (key operation)
slice1 = all_readings[5:15]
slice2 = all_readings[10:20]

# Calculate overlapping values (distraction)
overlap = set(slice1) & set(slice2)
overlap_energy = sum(overlap) if overlap else 0

# Apply bitwise operations to generate flags (distraction)
flags = []
for i in range(0, len(all_readings), 2):
    if i+1 < len(all_readings):
        flags.append(all_readings[i] | all_readings[i+1])

# Calculate energy levels
energy_levels = [reading ** 2 // 100 for reading in valid_readings]

# Filter values based on complex condition (key operation)
filtered_values = []
for level in energy_levels:
    if level % 3 == 0 or level % 5 == 0:
        filtered_values.append(level)
    elif level > 20:
        filtered_values.append(level - 10)

# Calculate target energy (the answer)
target_energy = sum(filtered_values)

# Some additional post-processing (distraction)
adjusted_energy = target_energy * 0.85
normalized_energy = (target_energy - min(energy_levels)) / (max(energy_levels) - min(energy_levels)) if energy_levels else 0

print(f"Result: {target_energy}")