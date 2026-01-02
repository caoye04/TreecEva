def normalize(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return [(x - mean) / (variance ** 0.5) if variance != 0 else 0 for x in data]

raw_inputs = [88, 92, 75, 64, 91, 85, 77]
decoy_data = [x ** 2 for x in raw_inputs if x < 80]
filtered = [x for x in raw_inputs if x >= 75]

# Misleading transformation chain
temp_result = 0
for i in range(len(filtered)):
    temp_result += filtered[i] * (i + 1)
scaling_factor = sum(i > 80 for i in filtered)
adjusted_scaling = scaling_factor if scaling_factor != 0 else 1
normalized_vals = normalize(filtered)
scaled_values = [val * adjusted_scaling * 10 for val in normalized_vals]

# Dummy structure processing
dummy_matrix = [[i*j for j in range(3)] for i in range(len(scaled_values))]
checksum = sum(sum(row) for row in dummy_matrix) % 100

# Threshold logic with red herring conditions
thresholds = {}
for idx, val in enumerate(scaled_values):
    if val > 5:
        thresholds[idx] = 'high'
    elif val > -5:
        thresholds[idx] = 'medium'
    else:
        thresholds[idx] = 'low'

# Irrelevant string manipulation distraction
data_tag = "SRC_" + "_".join(str(int(x)) for x in scaled_values[::2])[:10]
status_flags = {i: 'active' if i % 2 == 0 else 'pending' for i in range(len(scaled_values))}

# Core computation buried in logic
high_count = sum(1 for v in thresholds.values() if v == 'high')
penalty = 0
for i, val in enumerate(scaled_values):
    if i in thresholds and thresholds[i] == 'low' and i % 2 == 1:
        penalty += val

intermediate_score = sum(scaled_values) + high_count * 10
final_score = int(intermediate_score - abs(penalty))

# Redundant validation check (does not alter result)
validation_sum = sum(1 for x in status_flags.values() if x == 'active')
if validation_sum > 3:
    pass  # Placeholder, no effect

Result: final_score