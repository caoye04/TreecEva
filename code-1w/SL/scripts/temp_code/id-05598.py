def process_readings(data, limit):
    adjusted = [x - 1 for x in data if x > 25]
    squared = [y ** 2 for y in adjusted]
    return sum(squared) // len(squared) if squared else 0

# Sensor data simulation and filtering
temp_readings = [20, 30, 40, 15, 28, 35, 22, 50]
duplicate_check = {x for x in temp_readings}
offset = 5
calibration_factor = offset * 2  # unused but plausible

# Irrelevant transformation chain
shifted = [z + offset for z in temp_readings]
doubled = [w * 2 for w in shifted if w < 40]
aggregate = sum(doubled) % 17  # red herring computation

# Actual processing path
threshold = 27
filtered_data = [val for val in temp_readings if val >= threshold - 2]

# Noise generation (dead code)
signal_noise = []
for i in range(len(temp_readings)):
    if i % 3 == 0:
        signal_noise.append(temp_readings[i] ^ 4)  # bitwise distraction

# Key diagnostic computation
final_diagnostic = process_readings(filtered_data, threshold)

# Additional irrelevant tracking
status_flags = []
for val in filtered_data:
    status_flags.append(True if val % 2 == 0 else False)

# Print result as required
print(f"Target result: {final_diagnostic}")