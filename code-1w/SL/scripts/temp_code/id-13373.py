from collections import defaultdict
import math

def preprocess_records(raw_entries):
    processed = []
    temp_sum = 0
    for entry in raw_entries:
        if 'valid' in entry and entry['valid']:
            normalized = entry['value'] / (entry['factor'] or 1)
            temp_sum += normalized
            if normalized > 0.5:
                processed.append(math.log(normalized + 1))
    return processed

def analyze_trends(data_stream):
    trends = defaultdict(int)
    for i, val in enumerate(data_stream):
        trends['positive' if val > 0 else 'negative'] += 1
        if i % 2 == 0:
            trends['even_index'] += 1
    # Irrelevant aggregation
    total_updates = sum(trends.values())
    avg_update = total_updates / len(trends) if trends else 0
    return trends

def calculate_efficiency(dataset, limit):
    count = 0
    magnitude_total = 0.0
    for x in dataset:
        if x < 0:
            continue
        magnitude_total += x ** 0.5
        count += 1
    average_root = magnitude_total / count if count else 0
    penalty = 0.1 * len([y for y in dataset if y > limit])
    efficiency = (average_root * count) - penalty
    return round(efficiency, 4)

# Main execution
raw_input_data = [
    {'value': 16, 'factor': 4, 'valid': True},
    {'value': 25, 'factor': 5, 'valid': True},
    {'value': 9, 'factor': 3, 'valid': True},
    {'value': 0, 'factor': 1, 'valid': True},
    {'value': 36, 'factor': 6, 'valid': False},
    {'value': 49, 'factor': 7, 'valid': True}
]

processed_data = preprocess_records(raw_input_data)
trend_analysis = analyze_trends(processed_data)
baseline = sum(processed_data) / len(processed_data) if processed_data else 0
threshold = baseline * 1.1

# Key computation point
intermediate_metric = [x for x in processed_data if x > threshold]
dummy_counter = 0
for item in intermediate_metric:
    dummy_counter += int(item)

efficiency_score = calculate_efficiency(processed_data, threshold)

# Red herring variable
consistency_check = all(math.isfinite(x) for x in processed_data)

Result: efficiency_score