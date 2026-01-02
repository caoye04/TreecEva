def calculate_efficiency(data):
    base = sum(x ** 0.5 for x in data if x > 0)
    penalty = 0
    for i, val in enumerate(data):
        if i % 2 == 0 and val < 50:
            penalty += 10
    return int(base - penalty)

# Simulate sensor readings from industrial equipment
raw_readings = [36, 74, 16, 81, 49, 25, 9, 64]

# Irrelevant transformation - string-based encoding of numbers (distractor)
enoded_strings = [str(n) + '_enc' for n in raw_readings]
decode_map = {s: int(s.split('_')[0]) for s in enoded_strings}

# Preprocessing with filtering and scaling
filtered_readings = [x for x in raw_readings if x >= 15]
scaled_readings = list(map(lambda x: x * 1.1, filtered_readings))

# Additional irrelevant computation: reverse mapping check (dead path)
reversed_values = []
for key in decode_map:
    if decode_map[key] in [16, 81]:
        reversed_values.append(decode_map[key] // 2)

# Core processing pipeline
buffer = []
for val in scaled_readings:
    if val.is_integer():
        buffer.append(int(val))
processed_data = [x for x in buffer if x % 2 == 0]  # Only even values proceed

# Secondary distraction: unused temperature normalization
normalization_factor = 0.95
theoretical_max = max(raw_readings) * normalization_factor
adjusted_scores = [round(v / theoretical_max * 100, 2) for v in processed_data]

# Key computational step
efficiency_score = calculate_efficiency(processed_data)

# Output result as required
print(f"Result: {efficiency_score}")