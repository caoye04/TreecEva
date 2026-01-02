from collections import defaultdict
import itertools

# Simulate sensor data aggregation and performance scoring
def collect_diagnostics(raw_readings):
    diagnostics = defaultdict(int)
    temp_fragments = []

    for reading in raw_readings:
        parts = reading.split('_')
        key = parts[0]
        value = int(parts[1])

        if key == 'err':
            diagnostics['errors'] += value
        elif key == 'cnt':
            diagnostics['count'] += value
        elif key == 'lat':
            temp_fragments.append(value)

    avg_latency = sum(temp_fragments) / len(temp_fragments) if temp_fragments else 0
    diagnostics['avg_latency'] = int(avg_latency)
    return diagnostics

def normalize_metrics(data):
    normalized = {}
    max_val = max(data.values())
    for k, v in data.items():
        normalized[k] = round(v / max_val, 3) if max_val > 0 else 0.0
    
    # Distractor: irrelevant transformation
    flipped = {k: 1 - v for k, v in normalized.items()}
    ignored_total = sum(flipped.values())
    return normalized

def calculate_weighted_index(items, multipliers):
    index = 0
    for item, weight in zip(items, multipliers):
        index += item * weight
    return index

def evaluate_performance(metrics, weights):
    ordered_keys = ['errors', 'count', 'avg_latency']
    values = [metrics.get(k, 0) for k in ordered_keys]
    base_score = calculate_weighted_index(values, weights)
    
    # Apply penalty for high latency
    if metrics['avg_latency'] > 50:
        base_score *= 1.2
    
    # Distractor: unused branch with complex logic
    if metrics['count'] > 1000 and metrics['errors'] == 0:
        bonus = 0
        for i in range(5):
            bonus += i ** 3
        base_score += bonus  # This path won't be taken

    return int(base_score)

# Main execution
raw_data = ['err_12', 'cnt_850', 'lat_64', 'err_8', 'lat_58', 'cnt_150', 'lat_73']
weights = [2, -0.1, 0.5]  # Higher error -> worse; higher count -> slightly better; higher latency -> worse

raw_metrics = collect_diagnostics(raw_data)
normalized_metrics = normalize_metrics(raw_metrics)

# Irrelevant grouping operation using itertools
grouped = itertools.groupby(sorted(normalized_metrics.keys()), key=lambda x: x[0])
key_initials = [k for k, _ in grouped]

dummy_sum = 0
for char in key_initials:
    dummy_sum += ord(char)

final_score = evaluate_performance(raw_metrics, weights)
print(f"Result: {final_score}")