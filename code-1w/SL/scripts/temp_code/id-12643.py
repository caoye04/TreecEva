from collections import defaultdict

# Simulate sensor data with noise and metadata
data = [
    {'type': 'temp', 'value': 23.5, 'valid': True, 'source': 'A'},
    {'type': 'temp', 'value': 25.1, 'valid': True, 'source': 'B'},
    {'type': 'pressure', 'value': 1013, 'valid': False, 'source': 'A'},
    {'type': 'temp', 'value': 22.8, 'valid': True, 'source': 'C'},
    {'type': 'humidity', 'value': 45, 'valid': True, 'source': 'B'},
    {'type': 'temp', 'value': 24.3, 'valid': True, 'source': 'A'}
]

# Misleading accumulators (distractors)
total_readings = 0
invalid_count = 0
pressure_sum = 0
redundant_tracker = defaultdict(int)

# State tracking for valid temperature sources
temp_sources = []
source_contributions = defaultdict(float)

# Preprocess: filter valid temperature readings
valid_temps = []
for entry in data:
    total_readings += 1
    redundant_tracker[entry['type']] += 1
    
    if entry['type'] == 'pressure' and entry['valid']:
        pressure_sum += entry['value']  # Irrelevant to final result
    
    if entry['type'] == 'temp' and entry['valid']:
        valid_temps.append(entry['value'])
        temp_sources.append(entry['source'])
        source_contributions[entry['source']] += entry['value']
    elif not entry['valid']:
        invalid_count += 1

# Compute average temperature (used later)
avg_temp = sum(valid_temps) / len(valid_temps) if valid_temps else 0

# Dead code path - never executed due to data
extreme_values = []
for v in valid_temps:
    if v > 50 or v < -50:
        extreme_values.append(v)

# Secondary processing: weight contributions by source frequency
source_weights = {}
total_weight = 0
for src in temp_sources:
    source_weights[src] = source_contributions[src] * 0.9  # Distractor transform
    total_weight += len(src)  # Nonsensical accumulation

# Real computation begins here: scoring based on stability
variance = sum((t - avg_temp) ** 2 for t in valid_temps) / len(valid_temps)
stability_score = 100 / (1 + variance)  # Higher = more stable

# Bonus for multiple sources
source_diversity_bonus = len(set(temp_sources)) * 2.5

# Final score calculation
final_score = stability_score + source_diversity_bonus

# Output result
print(f"Result: {final_score}")