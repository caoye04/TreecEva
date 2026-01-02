from collections import defaultdict, Counter

# Simulated sensor array data processing with diagnostic analysis
def preprocess_sensors(raw_readings):
    processed = []
    for entry in raw_readings:
        sensor_id = entry['id']
        readings = entry['values']
        avg = sum(readings) / len(readings)
        variance = sum((x - avg) ** 2 for x in readings) / len(readings)
        # Irrelevant transformation (distractor)
        normalized = [round((r - avg) / (variance + 1e-5), 3) for r in readings]
        processed.append({'sensor': sensor_id, 'mean': avg, 'var': variance})
    return processed

# Dead function - never called (red herring)
def legacy_calibrate(data):
    return [x * 0.98 for x in data if x > 0]

# Filtering logic with misleading intermediate metrics
def evaluate_stability(metrics):
    stable_count = 0
    instability_flags = []
    for m in metrics:
        if m['var'] < 5.0:
            stable_count += 1
        if m['mean'] > 100 and m['var'] > 10.0:
            instability_flags.append(m['sensor'])
    # Decoy calculation
    phantom_score = stable_count * len(instability_flags) if instability_flags else -1
    return stable_count

# Core analysis function with critical computation path
def generate_threshold_map(sensors):
    mapping = defaultdict(float)
    categories = defaultdict(list)
    
    for s in sensors:
        key = s['sensor'][0]  # First letter of sensor ID
        categories[key].append(s['mean'])
    
    for cat, vals in categories.items():
        if len(vals) > 1:
            # Real threshold logic
            mapping[cat] = sum(vals) / len(vals)
        else:
            mapping[cat] = vals[0] * 0.75  # Unused path (distractor)
    
    # Extra irrelevant operations
    temp_debug = {k: round(v, 2) for k, v in mapping.items()}
    unused_stats = dict(Counter([s['sensor'][0] for s in sensors]))
    
    return mapping

# Main analysis with nested logic and list comprehensions
def analyze_readings(clean_data, thresholds):
    diagnostics = []
    total_contrib = 0.0
    
    for item in clean_data:
        sensor = item['sensor']
        category = sensor[0]
        base_val = item['mean']
        noise_level = item['var']
        
        # Complex conditional with red herring branch
        if noise_level > 8.0:
            adjusted = base_val * 0.85
            flag = 'NOISE_HIGH'
        elif base_val > thresholds.get(category, 50.0):
            adjusted = base_val * 1.15
            flag = 'SIGNAL_BOOST'
        else:
            adjusted = base_val * 1.0
            flag = 'NORMAL'
        
        # Irrelevant classification tree (dead code path)
        if flag == 'NOISE_HIGH':
            classification = 'ERRATIC'
        elif base_val > 200:
            classification = 'CRITICAL'
        else:
            classification = 'STABLE'
        
        # Only this contributes to final result
        if flag != 'NOISE_HIGH':
            total_contrib += adjusted
        
        diagnostics.append({
            'node': sensor,
            'adjusted_value': adjusted,
            'status': flag
        })
    
    # Final aggregation with slicing distraction
    sorted_diagnostics = sorted(diagnostics, key=lambda x: x['adjusted_value'])
    top_half = sorted_diagnostics[len(sorted_diagnostics)//2:]
    contribution_slice = [d['adjusted_value'] for d in top_half]
    
    # REAL answer computation (non-obvious due to distractions)
    final_sum = sum(contribution_slice) * 0.9
    return int(round(final_sum))

# Simulated input data
raw_sensor_data = [
    {'id': 'A01', 'values': [85, 87, 86, 83, 88]},
    {'id': 'A02', 'values': [90, 92, 89, 94, 91]},
    {'id': 'B01', 'values': [130, 135, 133, 140, 132]},
    {'id': 'B02', 'values': [155, 158, 153, 160, 157]},
    {'id': 'C01', 'values': [205, 210, 208, 215, 212]},
    {'id': 'C02', 'values': [75, 73, 77, 70, 74]},
    {'id': 'D01', 'values': [115, 118, 112, 120, 117]}
]

# Processing pipeline with decoy variables
processed_metrics = preprocess_sensors(raw_sensor_data)
decoys = [x for x in processed_metrics if x['mean'] < 80]  # Unused list comprehension
stability_index = evaluate_stability(processed_metrics)
filtered_data = [m for m in processed_metrics if m['mean'] >= 80]  # Relevant filtering
threshold_map = generate_threshold_map(filtered_data)

# Critical execution point
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Print result
print(f"Result: {final_diagnostic}")