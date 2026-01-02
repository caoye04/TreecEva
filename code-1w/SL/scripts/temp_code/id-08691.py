def analyze_temperatures(readings):
    temp_stats = {}
    above_freezing = [t for t in readings if t > 0]
    below_freezing = [t for t in readings if t <= 0]
    temp_stats['avg_above'] = sum(above_freezing) / len(above_freezing) if above_freezing else 0
    temp_stats['avg_below'] = sum(below_freezing) / len(below_freezing) if below_freezing else 0
    temp_stats['total_fluctuation'] = max(readings) - min(readings)
    return temp_stats

readings_data = [3, -5, 2, 8, -1, 0, 6, -3, 7, 1]
stats_summary = analyze_temperatures(readings_data)

# Misleading computation: unrelated to final result
days_count = len(readings_data)
daily_changes = [abs(readings_data[i] - readings_data[i-1]) for i in range(1, len(readings_data))]
avg_daily_change = sum(daily_changes) / len(daily_changes)

# Process data using dictionary operations and lambda
valid_readings = list(filter(lambda x: x != 0, readings_data))
reading_bins = {'cold': 0, 'moderate': 0, 'warm': 0}
for temp in valid_readings:
    if temp < 0:
        reading_bins['cold'] += 1
    elif 0 < temp <= 5:
        reading_bins['moderate'] += 1
    else:
        reading_bins['warm'] += 1

# Simulate sensor reliability adjustment (distractor)
sensor_weights = {'s1': 0.9, 's2': 1.1, 's3': 1.0}
weighted_sum = sum(valid_readings) * sensor_weights['s3']
adjusted_avg = weighted_sum / len(valid_readings)

# Core logic chain begins
baseline = stats_summary['avg_above']
penalty_factor = len(stats_summary['avg_below'].as_integer_ratio()) if stats_summary['avg_below'] != 0 else 1

processed_data = []
for idx, (temp, bin_key) in enumerate(zip(valid_readings, cycle(reading_bins.keys()))):
    normalized = temp / baseline
    if bin_key == 'cold':
        score = normalized * 1.5
    elif bin_key == 'moderate':
        score = normalized * 2.0
    else:
        score = normalized * 1.2
    
    # Apply artificial time decay (irrelevant but looks important)
    time_weight = 0.95 ** idx
    final_entry = {
        'index': idx,
        'raw': temp,
        'score': score * time_weight,
        'category': bin_key
    }
    processed_data.append(final_entry)

# Accumulate scores with distraction
aggregate_scores = {k: sum(e['score'] for e in processed_data if e['category'] == k) for k in reading_bins.keys()}

# Distractor: unused complex structure
detailed_report = [
    f"{entry['category'].title()} at {entry['raw']}C: {entry['score']:.3f}" 
    for entry in processed_data if entry['raw'] > 2
]

compute_final_score = lambda data: sum(item['score'] for item in data) * (1 + stats_summary['total_fluctuation'] / 100)

final_score = compute_final_score(processed_data)

# Output must follow required format
print(f"Result: {final_score}")