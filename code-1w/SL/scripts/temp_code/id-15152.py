from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant readings
temperature_readings = [23.4, 24.1, 22.9, 25.0, 23.4, 26.7, 23.4, 24.1, 38.2, -999]
humidity_readings = [45, 47, 45, 50, 52, 45, 60, 47, 1000]
pressure_readings = [1013, 1015, 1013, 1020, 1013, 1018, 9999]

# Flagged invalid entries (outliers or placeholders)
def validate_readings(data, valid_range):
    return [x for x in data if valid_range[0] <= x <= valid_range[1]]

temp_valid = validate_readings(temperature_readings, (15, 35))
humid_valid = validate_readings(humidity_readings, (0, 80))
press_valid = validate_readings(pressure_readings, (900, 1100))

duplicates_tracker = defaultdict(int)
for val in temp_valid:
    duplicates_tracker[val] += 1

top_freq = Counter(duplicates_tracker).most_common(1)
primary_mode_temp = top_freq[0][0] if top_freq else 0

# Irrelevant transformation: character analysis of number strings (red herring)
str_data = ''.join(map(str, temperature_readings))
char_case_count = {'upper': 0, 'lower': 0}
for char in str_data:
    if char.isalpha():
        if char.isupper():
            char_case_count['upper'] += 1
        else:
            char_case_count['lower'] += 1

# Fake correlation matrix (dead code path)
correlation_matrix = {}
for t in temp_valid:
    for h in humid_valid:
        key = round(t * h % 7, 2)
        correlation_matrix[key] = correlation_matrix.get(key, 0) + 1

# Decoy statistical function that's never used
def compute_entropy(vals):
    total = sum(vals)
    probs = [v / total for v in vals]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

# Bit manipulation distraction
even_temps_packed = 0
for i, t in enumerate([int(x) for x in temp_valid]):
    if t % 2 == 0:
        even_temps_packed |= (1 << i)

# Data alignment via index mapping (partially relevant)
min_length = min(len(temp_valid), len(humid_valid), len(press_valid))
aligned_data = [
    {'temp': temp_valid[i], 'humid': humid_valid[i], 'press': press_valid[i]}
    for i in range(min_length)
]

# Weight assignment with decoy weights
device_weights = {'sensor_A': 0.4, 'sensor_B': 0.3, 'sensor_C': 0.2, 'backup': 0.1}
weights = [0.5, 0.3, 0.2]  # final model uses positional weights

# Secondary validation filter based on stability
def is_stable(val_list, threshold=2.0):
    return max(val_list) - min(val_list) <= threshold

stability_flags = {
    'temp': is_stable(temp_valid, 3.0),
    'humid': is_stable(humid_valid, 10.0),
    'press': is_stable(press_valid, 15.0)
}

# Only proceed if at least two sensors are stable
valid_sensors_count = sum(stability_flags.values())
validated_data = aligned_data if valid_sensors_count >= 2 else []

# Core processing function
def process_results(data_batch, w):
    if not data_batch:
        return -999
    
    # Aggregate weighted average per entry
    totals = []
    for entry in data_batch:
        # Emphasis on temperature deviation from mode
        temp_dev = abs(entry['temp'] - primary_mode_temp)
        score = (
            w[0] * (entry['temp'] - temp_dev) +
            w[1] * entry['humid'] / 10.0 +
            w[2] * (entry['press'] / 100.0)
        )
        totals.append(score)
    
    # Final result is median of aggregated scores
    sorted_totals = sorted(totals)
    mid = len(sorted_totals) // 2
    return (sorted_totals[mid] + sorted_totals[-mid-1]) / 2

# Misleading intermediate calculation (unused)
avg_temperature = sum(temp_valid) / len(temp_valid) if temp_valid else 0

# Critical execution point
final_score = process_results(validated_data, weights)
print(f"Result: {final_score}")