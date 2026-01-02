from collections import defaultdict

# Simulate sensor data with some noise and redundancy
data = [
    {'temp': 25.1, 'humidity': 60, 'pressure': 1013},
    {'temp': 24.9, 'humidity': 62, 'pressure': 1012},
    {'temp': 25.2, 'humidity': 58, 'pressure': 1014},
    {'temp': 35.0, 'humidity': 70, 'pressure': 1000},  # outlier
    {'temp': 25.0, 'humidity': 61, 'pressure': 1013}
]

# Weight configuration for scoring
weights = defaultdict(float, temp=0.5, humidity=0.3, pressure=0.2)

# Auxiliary function to detect outliers (not actually used in final score)
def is_outlier(entry):
    return entry['temp'] > 30 or entry['humidity'] < 40

# Misleading accumulator for normalized values (distractor)
normalized_data = []
for entry in data:
    norm_entry = {
        'temp_norm': entry['temp'] / max(d['temp'] for d in data),
        'humidity_norm': entry['humidity'] / 100,
        'pressure_norm': entry['pressure'] / max(d['pressure'] for d in data)
    }
    normalized_data.append(norm_entry)

# Secondary weight map for an unused calculation path
alt_weights = {'temp': 0.4, 'humidity': 0.4, 'pressure': 0.2}

# Filter out only valid entries based on hidden criteria (subtle logic)
valid_entries = [e for e in data if not (e['temp'] > 30)]

# Aggregation using lambda for dynamic contribution calculation
contribution_fn = lambda x, w: sum(x[k] * w[k] for k in w)

# Accumulate weighted scores
weighted_sum = 0.0
entry_count = 0

for entry in valid_entries:
    score_component = contribution_fn(entry, weights)
    weighted_sum += score_component
    entry_count += 1

# Dead code block: computes average normalization but unused
if len(normalized_data) > 0:
    avg_norm_temp = sum(nd['temp_norm'] for nd in normalized_data) / len(normalized_data)
    adjustment_factor = avg_norm_temp * 0.1  # irrelevant to final result

# Final aggregation
average_weighted_score = weighted_sum / entry_count if entry_count else 0

# Apply fixed calibration offset (minor adjustment)
calibrated_score = average_weighted_score + 0.5

# Additional red herring: complex dictionary comprehension with no effect
diagnostic_report = {
    f"metric_{i}": {"raw": d, "calibrated": calibrated_score * 1.01} 
    for i, d in enumerate([1, 2, 3])
}

# Core result computation
final_score = int(calibrated_score * 10)  # scale and discretize

print(f"Result: {final_score}")