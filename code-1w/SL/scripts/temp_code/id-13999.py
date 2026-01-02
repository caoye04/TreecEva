from collections import defaultdict, Counter

# Simulate sensor data from a chemical distillation process
def get_sensor_readings():
    return [
        {'temp': 80, 'pressure': 1.2, 'purity': 0.88},
        {'temp': 85, 'pressure': 1.4, 'purity': 0.91},
        {'temp': 90, 'pressure': 1.6, 'purity': 0.87},
        {'temp': 88, 'pressure': 1.5, 'purity': 0.93},
        {'temp': 87, 'pressure': 1.5, 'purity': 0.90}
    ]

# Filter valid readings above minimum purity threshold
def filter_valid_runs(readings, min_purity=0.85):
    return [r for r in readings if r['purity'] >= min_purity]

# Compute rolling average for a given key using lambda
compute_avg = lambda data, key: sum(item[key] for item in data) / len(data) if data else 0

# Misleading function - appears useful but not used in final path
def analyze_efficiency_trends(data):
    trends = []
    for i in range(1, len(data)):
        delta_temp = data[i]['temp'] - data[i-1]['temp']
        delta_pressure = data[i]['pressure'] - data[i-1]['pressure']
        efficiency_estimate = delta_temp * 0.3 + delta_pressure * 0.7
        trends.append(efficiency_estimate)
    return trends

# Heuristic scoring (distractor computation)
def compute_stability_score(valid_runs):
    if not valid_runs:
        return 0.0
    temp_range = max(r['temp'] for r in valid_runs) - min(r['temp'] for r in valid_runs)
    pressure_range = max(r['pressure'] for r in valid_runs) - min(r['pressure'] for r in valid_runs)
    return (10 - temp_range * 0.2) + (5 - pressure_range * 0.5)

# Core processing pipeline
def preprocess_runs(valid_runs):
    processed = []
    count_by_temp = defaultdict(int)
    purity_counter = Counter()

    for run in valid_runs:
        temp_key = f"{run['temp']}C"
        count_by_temp[temp_key] += 1
        purity_counter[round(run['purity'], 2)] += 1

        # Transform data into normalized performance vector
        norm_pressure = run['pressure'] / 1.6
        adjusted_purity = run['purity'] * 1.05  # minor correction
        score = (norm_pressure * 0.4) + (adjusted_purity * 0.6)
        
        processed.append({
            'score': score,
            'temp': run['temp'],
            'priority': 1 if run['temp'] >= 88 else 0
        })
    
    # Distractor: unused aggregation
    avg_counts = compute_avg([{'cnt': v} for v in count_by_temp.values()], 'cnt')
    mode_purity = purity_counter.most_common(1)

    return processed

# Determine optimal yield based on prioritized high-temp runs
def calculate_optimal_yield(processed_data):
    high_priority = [p for p in processed_data if p['priority'] == 1]
    if not high_priority:
        return compute_avg(processed_data, 'score') * 50
    
    base_yield = compute_avg(high_priority, 'score') * 60
    
    # Apply small bonus if multiple high-priority runs exist
    if len(high_priority) > 1:
        bonus = len(high_priority) * 1.5
        base_yield += bonus
    
    return base_yield

# Execution flow
raw_data = get_sensor_readings()
valid_runs = filter_valid_runs(raw_data)
processed_data = preprocess_runs(valid_runs)
final_yield = calculate_optimal_yield(processed_data)

# Print result as required
print(f"Result: {final_yield}")