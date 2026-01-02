from collections import defaultdict

# Simulate sensor data with some noise and redundancy
data = [
    {'temp': 25.1, 'pressure': 101.3, 'humidity': 45.2},
    {'temp': 26.4, 'pressure': 100.8, 'humidity': 47.9},
    {'temp': 24.9, 'pressure': 102.1, 'humidity': 43.5},
    {'temp': 25.1, 'pressure': 101.3, 'humidity': 45.2},
    {'temp': 27.3, 'pressure': 99.7, 'humidity': 50.1}
]

# Weight factors for weighted metric calculation
weights = {'temp': 0.5, 'pressure': 0.3, 'humidity': 0.2}

# Redundant transformation: create a duplicate map (distractor)
duplicate_map = defaultdict(int)
for i, entry in enumerate(data):
    key = f"{entry['temp']}-{entry['pressure']}"
    duplicate_map[key] += 1

# Apply normalization to each metric (some preprocessing)
normalized = []
base_temp, base_pressure, base_humidity = 25.0, 100.0, 45.0
for reading in data:
    norm_temp = (reading['temp'] - base_temp) / base_temp
    norm_pressure = (reading['pressure'] - base_pressure) / base_pressure
    norm_humidity = (reading['humidity'] - base_humidity) / base_humidity
    normalized.append({'temp': norm_temp, 'pressure': norm_pressure, 'humidity': norm_humidity})

# Compute moving average over normalized values (not used later - distractor)
moving_avg = []
window_size = 2
for i in range(len(normalized) - window_size + 1):
    avg_temp = sum(normalized[j]['temp'] for j in range(i, i + window_size)) / window_size
    avg_pressure = sum(normalized[j]['pressure'] for j in range(i, i + window_size)) / window_size
    avg_humidity = sum(normalized[j]['humidity'] for j in range(i, i + window_size)) / window_size
    moving_avg.append({'temp': avg_temp, 'pressure': avg_pressure, 'humidity': avg_humidity})

# Define processing function using lambda and slicing
aggregator = lambda x, w: sum(x[k] * w[k] for k in x)

# Extract last three entries (slicing - relevant)
recent_data = normalized[-3:]

# Process metrics: main logic path
def process_metrics(metrics_list, weight_dict):
    total = 0.0
    # Use Counter to count temp patterns (partly irrelevant)
    from collections import Counter
    temp_bins = [round(m['temp'], 1) for m in metrics_list]
    freq = Counter(temp_bins)
    
    # Real computation: weighted sum of last entry
    last_entry = metrics_list[-1]
    raw_value = aggregator(last_entry, weight_dict)
    
    # Adjust based on frequency (minor effect)
    adjustment = freq[round(last_entry['temp'], 1)] * 0.05
    
    # Secondary correction: if pressure deviation > 0.015, reduce score
    if abs(last_entry['pressure']) > 0.015:
        raw_value *= 0.9
    
    final = raw_value + adjustment
    return round(final, 4)

# Unused helper: calculates variance (dead code path)
def calculate_variance(values):
    mean_val = sum(values) / len(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)

# Execute main computation
final_score = process_metrics(data, weights)  # Mistake: passing raw data instead of normalized?

# Correction: actually use normalized recent data
final_score = process_metrics(recent_data, weights)

print(f"Result: {final_score}")