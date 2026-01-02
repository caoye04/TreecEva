def analyze_pattern(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts

positions = [1, 3, 4, 2, 5, 3, 6, 1, 4, 5]
duplicate_check = set()
repeats = []
for idx, val in enumerate(positions):
    if val in duplicate_check:
        repeats.append(val)
    else:
        duplicate_check.add(val)

count_summary = analyze_pattern(positions)
sorted_vals = sorted(count_summary.items(), key=lambda x: x[1], reverse=True)

def compute_rarity_score(count_dict, rarity_threshold=2):
    rare_elements = [k for k, v in count_dict.items() if v < rarity_threshold]
    score = sum([1 / (i + 1) for i, _ in enumerate(rare_elements)])
    temp_debug = [x * 2 for x in rare_elements]  # irrelevant computation
    return score

rarity_score = compute_rarity_score(count_summary)

baseline_shift = 0.5
adjustment_factor = len(repeats) * 0.1

# Simulate multi-source data fusion
data = [
    {'source': 'A', 'value': 12.5},
    {'source': 'B', 'value': 8.7},
    {'source': 'C', 'value': 14.2},
    {'source': 'D', 'value': 9.1}
]

data_with_index = list(enumerate(data))
values_only = [entry['value'] for _, entry in data_with_index]
mean_value = sum(values_only) / len(values_only)

thresholds = {
    'high': mean_value + baseline_shift,
    'low': mean_value - baseline_shift
}

# Misleading intermediate transformation
transformed_data = []
for i, v in zip(range(len(values_only)), values_only):
    if v > thresholds['high']:
        transformed_data.append(v * adjustment_factor)
    elif v < thresholds['low']:
        transformed_data.append(v * 0.5)
    else:
        transformed_data.append(v)

status_flags = {i: 'processed' for i in range(len(data))}
debug_logs = []  # unused accumulator

valid_entries = []
for idx, record in data_with_index:
    if record['value'] >= thresholds['low']:
        valid_entries.append(record['value'])

# Core logic wrapped in function
def calculate_final_score(entries, limits):
    high_bound = limits['high']
    total_contribution = 0.0
    bonus_pool = 0.0  # distractor accumulator
    for val in entries:
        if val > high_bound:
            total_contribution += val * 0.3
        else:
            total_contribution += val * 0.1
    adjustment = compute_rarity_score(count_summary) * 10
    return int(total_contribution + adjustment)

final_score = calculate_final_score(valid_entries, thresholds)
print(f"Result: {final_score}")