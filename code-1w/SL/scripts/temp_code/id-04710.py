def analyze_temperature(readings):
    avg_temp = sum(readings) / len(readings)
    temp_deviation = [abs(t - avg_temp) for t in readings]
    filtered_readings = [t for t in readings if abs(t - avg_temp) <= 2 * sum(temp_deviation) / len(temp_deviation)]
    return sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0


def calculate_moisture_score(level_list):
    score_map = {i: val * 0.75 for i, val in enumerate(level_list)}
    adjusted_scores = [score_map[i] for i in range(len(level_list))]
    cumulative = 0
    for s in adjusted_scores:
        cumulative += s
    return cumulative / len(adjusted_scores) if adjusted_scores else 0


def process_growth_cycles(cycles):
    growth_index = []
    for cycle in cycles:
        base = cycle.get('initial', 0)
        peak = max(cycle.get('measurements', [0]))
        duration = cycle.get('days', 1)
        index = (peak - base) / duration if duration > 0 else 0
        growth_index.append(index)
    
    sorted_indices = sorted(growth_index)
    midpoint = len(sorted_indices) // 2
    median_index = sorted_indices[midpoint] if len(sorted_indices) % 2 == 1 else (sorted_indices[midpoint-1] + sorted_indices[midpoint]) / 2
    
    outlier_threshold = median_index * 1.5
    cleaned = [idx for idx in growth_index if idx <= outlier_threshold]
    return sum(cleaned) / len(cleaned) if cleaned else 0


def harvest_results(data):
    # Extract and preprocess temperature data
    temps = [entry['temp'] for entry in data if 'temp' in entry]
    moisture_levels = [entry['moisture'] for entry in data if 'moisture' in entry]
    cycles = [entry['cycle'] for entry in data if 'cycle' in entry]
    
    # Core metrics
    temp_metric = analyze_temperature(temps)
    moisture_metric = calculate_moisture_score(moisture_levels)
    growth_metric = process_growth_cycles(cycles)
    
    # Irrelevant distractions below
    dummy_weights = [0.1, 0.2, 0.3]
    shadow_calc = sum([w * w for w in dummy_weights])  # unused
    metadata_summary = {'entries': len(data), 'valid': True}
    metadata_summary['version'] = '1.2'
    version_check = metadata_summary.get('version') == '1.2'
    
    # Red herring computation
    phantom_score = 0
    for i in range(3):
        phantom_score += temp_metric * 0.01  # negligible impact
    
    # Actual yield formula
    raw_yield = temp_metric * 0.4 + moisture_metric * 0.3 + growth_metric * 0.3
    
    # Extra slicing distraction
    sliced_temps = temps[1:-1]
    if len(sliced_temps) > 2:
        temp_slice_avg = sum(sliced_temps) / len(sliced_temps)
        raw_yield += (temp_slice_avg * 0.05)  # minor but real adjustment
    
    final_yield = int(raw_yield * 100) / 100.0  # round to two decimals
    return final_yield

# Simulated experiment data
experiment_data = [
    {'temp': 22.1, 'moisture': 60, 'cycle': {'initial': 10, 'measurements': [10, 18, 25], 'days': 7}},
    {'temp': 23.5, 'moisture': 68, 'cycle': {'initial': 12, 'measurements': [12, 20, 29, 31], 'days': 8}},
    {'temp': 19.8, 'moisture': 55, 'cycle': {'initial': 11, 'measurements': [11, 17, 23], 'days': 6}},
    {'temp': 24.0, 'moisture': 70, 'cycle': {'initial': 13, 'measurements': [13, 22, 30, 33, 34], 'days': 9}},
    {'temp': 20.5, 'moisture': 58, 'cycle': {'initial': 10, 'measurements': [10, 16, 21], 'days': 5}},
    {'temp': 35.0, 'moisture': 40, 'cycle': {'initial': 9,  'measurements': [9, 10, 11], 'days': 10}},  # outlier
]

final_yield = harvest_results(experiment_data)
print(f"Target result: {final_yield}")