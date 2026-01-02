def analyze_performance(records):
    base_multiplier = 1.5
    bonus_factor = 0.0
    penalties = []

    for record in records:
        if record['score'] > 80:
            bonus_factor += 5.5
        elif record['score'] < 50:
            penalties.append(record['id'])

    # Irrelevant aggregation
    total_penalties = sum([len(str(p)) for p in penalties]) * 0.1
    adjusted_bonus = bonus_factor - total_penalties

    return adjusted_bonus


def calculate_ranking(data_list):
    scaling_constant = 2.3
    temp_results = []
    intermediate_sum = 0

    filter_fn = lambda x: x['active']

    filtered_data = list(filter(filter_fn, data_list))

    for item in filtered_data:
        raw_value = item['metrics']['base'] * scaling_constant
        if item['metrics'].get('bonus', 0) > 0:
            raw_value += item['metrics']['bonus'] * 1.2
        temp_results.append(raw_value)
        intermediate_sum += raw_value ** 0.5

    # Dummy tracking variables
    avg_sqrt = intermediate_sum / len(temp_results) if temp_results else 0
    fluctuation_index = abs(avg_sqrt - sum(temp_results) / len(temp_results))

    final_rank = sum(temp_results) * 0.9 + (fluctuation_index * 0.1)

    return int(final_rank)

# Main execution block
raw_entries = [
    {'id': 101, 'score': 85, 'active': True, 'metrics': {'base': 40, 'bonus': 10}},
    {'id': 102, 'score': 45, 'active': False, 'metrics': {'base': 30, 'bonus': 0}},
    {'id': 103, 'score': 90, 'active': True, 'metrics': {'base': 50, 'bonus': 15}},
    {'id': 104, 'score': 78, 'active': True, 'metrics': {'base': 45, 'bonus': 5}},
    {'id': 105, 'score': 60, 'active': True, 'metrics': {'base': 35, 'bonus': 0}}
]

# Preprocessing step with distraction
processed_stats = [r for r in raw_entries if r['score'] >= 60]
score_analysis = analyze_performance(raw_entries)

# Key computation path
processed_data = []
for entry in processed_stats:
    entry_copy = entry.copy()
    if entry_copy['active']:
        entry_copy['metrics']['base'] += int(score_analysis / 10)
    processed_data.append(entry_copy)

final_score = calculate_ranking(processed_data)
print(f"Result: {final_score}")