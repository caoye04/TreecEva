from itertools import combinations, cycle

# Simulated sensor array data for environmental diagnostics
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1]
humidity_readings = [45, 47, 50, 44, 52, 48, 55]
pressure_readings = [1013, 1015, 1012, 1016, 1010, 1014, 1018]

# Irrelevant transformations (distractors)
decoy_transform = [round((t * 1.8) + 32, 2) for t in temperature_readings]  # Fahrenheit
scaled_humidity = [h * 2.1 for h in humidity_readings]
pressure_zscore = [(p - 1014) / 3.2 for p in pressure_readings]

# Real processing path begins
baseline_temp = sum(temperature_readings) / len(temperature_readings)
fluctuation = max(temperature_readings) - min(temperature_readings)

# Character counting in fake device ID (red herring)
device_id = 'SENS-TRX9000'
id_char_count = len([c for c in device_id if c.isalpha()])

# Bit manipulation decoy (unused later)
encoded_flag = 0
for h in humidity_readings[:3]:
    encoded_flag ^= int(h) << 2

# Generate all possible 3-element combos of temps (irrelevant but looks important)
temp_combinations = list(combinations(temperature_readings, 3))
avg_combs = [sum(combo)/3 for combo in temp_combinations]
high_temp_groups = [a for a in avg_combs if a > 24.5]

# Misleading diagnostic score
false_diagnostic = len(high_temp_groups) * id_char_count

# Real logic: detect sustained high-pressure trend
windowed_pressure = [sum(pressure_readings[i:i+3]) for i in range(len(pressure_readings)-2)]
increasing_windows = 0
for i in range(len(windowed_pressure)-1):
    if windowed_pressure[i+1] > windowed_pressure[i]:
        increasing_windows += 1

# Correction factor based on trend reliability
if increasing_windows >= 3:
    correction_factor = 17.8
else:
    correction_factor = -9.4

# Accumulate weighted contributions
weight_sum = 0.0
for i, p in enumerate(pressure_readings):
    weight_sum += (p - 1000) * (i + 1) * 0.1

aggregate_score = round(baseline_temp * 2.1 + fluctuation * 3.7 + weight_sum, 1)

# Key assignment: target answer depends on this
final_diagnostic = aggregate_score + correction_factor

# Dead code path (never executed, but looks relevant)
def compute_entropy(arr):
    from math import log
    total = sum(arr)
    probs = [x/total for x in arr if x > 0]
    return -sum(p * log(p) for p in probs)

# Unused itertools cycle
cycler = cycle([1, 0])
mask_sequence = [next(cycler) for _ in range(10)]

# Print final result as required
print(f"Result: {final_diagnostic}")