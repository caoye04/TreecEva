from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def unused_metric_analysis(x):
    return sum(i * 2 for i in x if i % 3 == 0)

# Misleading intermediate computation
temp_buffer = [i ** 2 for i in range(15) if i % 2 == 1]
shadow_sum = sum(temp_buffer) // 4  # Looks important, never used

# Simulated sensor readings with noise
data = [
    {'temp': 23.5, 'pressure': 1013, 'humidity': 45},
    {'temp': 25.1, 'pressure': 1009, 'humidity': 52},
    {'temp': 22.8, 'pressure': 1015, 'humidity': 43},
    {'temp': 26.3, 'pressure': 1007, 'humidity': 57}
]

# Weight configuration (some weights are decoys)
weights = {
    'temp': 0.4,
    'pressure': 0.1,
    'humidity': 0.3,
    'altitude': 0.2,  # Unused in computation
    'luminance': 0.0   # Red herring
}

# Auxiliary transformation table (partially used)
normalization_factor = defaultdict(lambda: 1.0)
normalization_factor['temp'] = 0.5
normalization_factor['humidity'] = 0.8
# pressure normalization intentionally omitted to mislead

# Decoy statistical summary
decoys = []
for entry in data:
    avg_val = (entry['temp'] + entry['pressure'] + entry['humidity']) / 3
    decoys.append(avg_val)
overall_avg = sum(decoys) / len(decoys)  # Not used later

# Core processing pipeline
processed_entries = []
for idx, reading in enumerate(data):
    adjusted = 0.0
    for key, val in reading.items():
        if key in weights and weights[key] > 0:  # Skip zero-weight keys
            norm = normalization_factor[key]
            contribution = val * weights[key] * norm
            adjusted += contribution
    # Transform using lambda in non-trivial context
    transform_fn = lambda x, i: x * (1 + i * 0.05)
    transformed_adjusted = transform_fn(adjusted, idx)
    processed_entries.append(transformed_adjusted)

# Secondary aggregation using zip and enumerate together
aggregated = 0
for i, (entry, buf_val) in enumerate(zip(processed_entries, temp_buffer)):
    if i % 2 == 0:
        aggregated += entry * 0.9
    else:
        aggregated += buf_val * 0.01  # Minor distraction using irrelevant buffer

# Conditional override simulation (never triggers due to logic)
critical_threshold = 120
if any(x > critical_threshold for x in processed_entries):
    aggregated *= 0.5  # Dead branch

# Final fusion with tuple unpacking and min/max logic
extremes = (min(processed_entries), max(processed_entries))
mid_point = sum(extremes) / 2
final_score = aggregated + mid_point * 0.2

# Output result as required
print(f"Result: {final_score}")