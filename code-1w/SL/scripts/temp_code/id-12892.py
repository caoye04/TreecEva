def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x for x in data if x > threshold]

# Simulated sensor readings (distraction)
sensor_data = [0.6, 0.8, 0.4, 0.9, 0.7]
active_sensors = analyze_efficiency(sensor_data)

# Core problem: employee performance evaluation using weighted metrics
base_metrics = {'accuracy': 87, 'latency': 12, 'volume': 145, 'consistency': 91}

# Distractor: unrelated transformation
str_metrics = {k.upper(): str(v) for k, v in base_metrics.items()}
temp_result = ''.join([s[-1] for s in str_metrics.values() if len(s) > 1])

# Actual metric processing chain
raw_values = list(base_metrics.values())
weight_map = lambda idx: round(1 / (1 + idx * 0.1), 2)  # Higher weight for earlier metrics
weights = [weight_map(i) for i in range(len(raw_values))]

# Irrelevant sorting variation
desc_raw = sorted(raw_values, reverse=True)
asc_weights = sorted(weights)

# Key computation with distractors
aggregate = 0
for i, (val, w) in enumerate(zip(raw_values, weights)):
    if i % 2 == 0:
        aggregate += val * w * 1.1  # Boost even-indexed metrics
    else:
        aggregate -= val * w * 0.1  # Small penalty on odd

# Secondary adjustment based on auxiliary condition
threshold_condition = sum(1 for x in raw_values if x > 90)
adjustment_factor = 1.05 if threshold_condition >= 2 else 0.97

# Dummy string operation for interference
diagnostic_tag = ''.join(map(str, [len(str(int(aggregate))), int(aggregate) % 10]))
diagnostic_tag = diagnostic_tag.replace('5', 'X')  # Dead-end manipulation

# Core logic continuation
temp_cache = {}
for idx, char in enumerate(diagnostic_tag):
    temp_cache[f'key_{idx}'] = ord(char) ^ 128  # Bitwise red herring

# Real adjustment
aggregate *= adjustment_factor

# Additional irrelevant data structure
status_flags = {i: (v > 80) for i, v in enumerate(raw_values)}
flag_summary = list(enumerate(status_flags.values()))

# Final score calculation
final_score = int(round(aggregate))

# Decoy function call that does nothing meaningful
def update_status(flags):
    for k in flags:
        flags[k] = not flags[k]

update_status(status_flags)  # No effect on final_score

# Output the required result
print(f"Result: {final_score}")