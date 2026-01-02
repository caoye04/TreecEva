import itertools

# Simulated sensor data processing pipeline with red herrings
raw_readings = [0.7, -1.2, 0.95, -0.3, 1.4, -0.8, 2.1, -1.6]
dummy_offsets = [0.1 * i for i in range(8)]

# Irrelevant transformation 1: phase shifting (unused later)
shifted_phases = [(x + 0.5) % 1.0 for x in raw_readings]

# Real processing path starts here
filtered_data = [x for x in raw_readings if abs(x) > 0.5]
scaled_data = list(map(lambda x: x * 1.8 + 32 if x > 0 else x * 2.1 - 10, filtered_data))

# Decoy statistical analysis (never used)
mean_value = sum(scaled_data) / len(scaled_data)
variance_proxy = sum((x - mean_value) ** 2 for x in scaled_data)
threshold_mask = [abs(x) > 1.5 for x in scaled_data]

# Complex but irrelevant bit manipulation on indices
index_flags = []
for i in range(len(scaled_data)):
    flag = (i << 2) ^ 0b101
    if flag & 0b100:
        index_flags.append(flag | 0b11)
    else:
        index_flags.append(flag)

# Destructuring and multiple assignments (some are decoys)
a, b, c, d = scaled_data[0], scaled_data[1], scaled_data[2], scaled_data[3]
reassigned_x, y_temp = c, a  # Partially unused
_ = b * d  # Dead computation

# Real logic: frequency pattern extraction using itertools
grouped_signs = [k for k, g in itertools.groupby(scaled_data, key=lambda x: x >= 0)]
pattern_score = len(grouped_signs) * 100

# Conditional data routing with misleading branches
if len(grouped_signs) > 2:
    temp_result = pattern_score - 25
    secondary_check = any(scaled_data[i] < 0 for i in range(0, len(scaled_data), 2))
    if secondary_check:
        temp_result += 15
else:
    temp_result = pattern_score + 50  # Dead branch (not taken)

# Another red herring: unused dictionary aggregation
stats_summary = {
    'count': len(scaled_data),
    'positive_ratio': len([x for x in scaled_data if x > 0]) / len(scaled_data),
    'extremes': [x for x in scaled_data if abs(x) > 35],
    'checksum': sum(abs(int(x)) for x in scaled_data)
}

# Core algorithm: hidden in the middle
adjusted_values = [round(x / 1.5) for x in scaled_data]
unique_adjusted = list(set(adjusted_values))

def analyze_signal(data):
    base = sum(data) * 2
    if len(data) % 2 == 0:
        base -= 17
    else:
        base += 7
    # Apply correction based on sign transitions
    transitions = 0
    for i in range(1, len(data)):
        if (data[i-1] >= 0) != (data[i] >= 0):
            transitions += 1
    return base + (transitions * 11)

# Critical assignment
processed_data = adjusted_values
final_diagnostic = analyze_signal(processed_data)

# Output required format
print(f"Result: {final_diagnostic}")