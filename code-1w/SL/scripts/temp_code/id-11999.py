from collections import defaultdict, Counter

# Simulated sensor data from environmental monitoring stations
data = [
    {'temp': 23.5, 'humidity': 60, 'co2': 410, 'pm25': 12},
    {'temp': 24.1, 'humidity': 65, 'co2': 425, 'pm25': 15},
    {'temp': 22.9, 'humidity': 58, 'co2': 405, 'pm25': 10},
    {'temp': 25.3, 'humidity': 70, 'co2': 460, 'pm25': 18},
    {'temp': 21.8, 'humidity': 55, 'co2': 395, 'pm25': 8}
]

# Irrelevant baseline thresholds (distractor)
thresholds = defaultdict(lambda: 0)
thresholds['temp'] = 25
thresholds['humidity'] = 60
thresholds['co2'] = 450
thresholds['pm25'] = 15

# Weight configuration for health impact scoring
weights = {
    'temp_w': 0.2,
    'humidity_w': 0.15,
    'co2_w': 0.3,
    'pm25_w': 0.35
}

# Decoy function - never called but looks relevant
def calculate_risk_index(values):
    risk = 0
    for v in values:
        if v > 100:
            risk += (v - 100) * 0.1
    return risk

# Auxiliary transformation map (partially used)
transform_map = {
    'temp': lambda x: (x - 20) * 1.5,
    'humidity': lambda x: x / 10,
    'co2': lambda x: max(0, (x - 400) / 100),
    'pm25': lambda x: x ** 0.5
}

# Unused intermediate tracking (red herring)
stats_log = []
for i, record in enumerate(data):
    log_entry = {"index": i, "flags": []}
    if record['temp'] > thresholds['temp']:
        log_entry["flags"].append("high_temp")
    if record['pm25'] > thresholds['pm25']:
        log_entry["flags"].append("high_pm25")
    stats_log.append(log_entry)  # Dead storage assignment

# Misleading aggregation (not used in final result)
avg_data = defaultdict(float)
for key in data[0].keys():
    avg_data[key] = sum(d[key] for d in data) / len(data)

# Real processing begins here
normalized = []
for entry in data:
    norm_entry = {}
    for k, v in entry.items():
        if k in transform_map:
            norm_entry[k] = transform_map[k](v)
    normalized.append(norm_entry)

# Scoring with weighted sum per entry
entry_scores = []
for n_entry in normalized:
    score = 0
    score += n_entry['temp'] * weights['temp_w']
    score += n_entry['humidity'] * weights['humidity_w']
    score += n_entry['co2'] * weights['co2_w']
    score += n_entry['pm25'] * weights['pm25_w']
    entry_scores.append(round(score, 6))

# Aggregation using median (resistant to outliers)
def get_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_arr[mid-1] + sorted_arr[mid]) / 2
    else:
        return sorted_arr[mid]

median_score = get_median(entry_scores)

# Final adjustment based on consensus deviation
consensus = sum(1 for s in entry_scores if abs(s - median_score) < 0.5)
adjustment_factor = consensus / len(entry_scores)

# Critical statement
final_score = int(median_score * 100 * adjustment_factor)

# Print result for inspection
print(f"Result: {final_score}")