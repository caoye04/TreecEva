def analyze_temperatures(raw_readings):
    adjusted = [x - 273.15 for x in raw_readings if x >= 0]
    positive_count = len([x for x in adjusted if x > 0])
    avg_temp = sum(adjusted) / len(adjusted) if adjusted else 0
    temp_ranges = {'cold': 0, 'moderate': 0, 'hot': 0}
    for t in adjusted:
        if t < 15:
            temp_ranges['cold'] += 1
        elif t < 30:
            temp_ranges['moderate'] += 1
        else:
            temp_ranges['hot'] += 1
    return avg_temp, temp_ranges, positive_count


def extract_signals(sensor_data):
    signals = []
    for i, val in enumerate(sensor_data):
        if i % 2 == 0 and val > 0:
            signals.append(val * 2)
    normalized = [s / max(signals) if max(signals) != 0 else 0 for s in signals]
    return normalized


def calculate_final_score(data_chunk):
    base_scores = []
    for item in data_chunk:
        if isinstance(item, dict):
            score = item.get('score', 0) * item.get('weight', 1)
            base_scores.append(score)
    total = sum(base_scores)
    penalty = 0.1 * len([x for x in base_scores if x < 0])
    return total - penalty

# Simulated sensor and temperature data
raw_temperature_data = [280, 295, 310, -1, 275, 305, 260]
sensor_input = [1, -2, 3, 4, -5]

# Step 1: Process temperature readings
mean_temp, category_counts, active_sensors = analyze_temperatures(raw_temperature_data)

categorized_list = list(category_counts.items())
indexed_categories = list(enumerate(categorized_list))

# Misleading computation - not used later (distractor)
dummy_aggregate = sum([v for k, v in category_counts.items()]) * mean_temp

# Step 2: Extract and normalize signals
filtered_signals = extract_signals(sensor_input)
signal_power = sum([s**2 for s in filtered_signals])

# Prepare structured data for scoring
processed_data = [
    {'score': mean_temp, 'weight': 0.8},
    {'score': signal_power, 'weight': 1.2},
    {'score': active_sensors, 'weight': 0.5},
    {'score': len(indexed_categories), 'weight': 0.3}
]

# Introduce irrelevant set operation (distractor)
unique_weights = set([item['weight'] for item in processed_data])
weight_pairs = set(zip([1, 2, 3], [4, 5, 6]))  # unused

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")