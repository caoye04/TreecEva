def process_entry(x):
    return x ** 2 - 3 * x + 2

# Simulate sensor data drift correction
drift_compensation = lambda z: z + 5 if z < 0 else z - 2

# Raw signal sequence from multiple sensors
raw_readings = [4, -1, 3, 0, 2]
adjusted_readings = []

for val in raw_readings:
    adjusted = drift_compensation(val)
    adjusted_readings.append(adjusted)

# Secondary processing: apply polynomial filter
filtered_values = []
for v in adjusted_readings:
    filtered = process_entry(v)
    filtered_values.append(filtered)

# Accumulate transient states (irrelevant to final result)
transient_sum = 0
for i in range(len(filtered_values)):
    if i % 2 == 0:
        transient_sum += filtered_values[i] * 2
    else:
        transient_sum -= filtered_values[i]

# Noise threshold simulation (dead code path - never triggered due to fixed data)
noise_floor = 0.5
if transient_sum < 0:
    adjusted_readings = [x + noise_floor for x in adjusted_readings]

# Core flow calculation
multiplier_map = {0: 1, 1: 3, 2: 2, 3: 4, 4: 1}
weight_sum = 0
index = 0
for item in filtered_values:
    weight_sum += item * multiplier_map[index]
    index += 1

# Auxiliary tracking variable (distractor)
counter_state = {'high': 0, 'low': 0}
for f in filtered_values:
    if f > 5:
        counter_state['high'] += 1
    else:
        counter_state['low'] += 1

# Final aggregation function
def calculate_net_flow(sequence):
    base = 100
    for elem in sequence:
        base += elem // 2
    return int(base)

# Key statement
final_flux = calculate_net_flow(filtered_values)
print(f"Target result: {final_flux}")