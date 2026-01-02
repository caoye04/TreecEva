import math

# Simulated sensor fusion system for environmental monitoring

# Irrelevant calibration constants (distractors)
CALIBRATION_OFFSET_A = 0.023
REFERENCE_VOLTAGE = 3.3
TEMPORAL_DAMPING = 0.87
MAX_BUFFER_SIZE = 1024

# Real data inputs
raw_readings = [
    {'sensor': 'temp', 'value': 23.5, 'status': 'OK'},
    {'sensor': 'humid', 'value': 45.2, 'status': 'OK'},
    {'sensor': 'co2', 'value': 415, 'status': 'WARN'},
    {'sensor': 'pm25', 'value': 32, 'status': 'OK'},
    {'sensor': 'voc', 'value': 220, 'status': 'FAIL'}
]

# Misleading preprocessing chain with dead paths
transformed = []
for entry in raw_readings:
    if entry['status'] == 'FAIL':
        transformed.append({'processed_value': 0, 'flagged': True})
    else:
        adjusted = entry['value'] * 0.98 + 0.5
        if entry['sensor'] == 'co2':
            adjusted = min(adjusted, 500)
        normalized = round(adjusted, 2) if isinstance(adjusted, float) else adjusted
        transformed.append({'processed_value': normalized, 'flagged': False})

# Dead code path - never executed due to prior filtering (red herring)
def legacy_conversion(x):
    return (x * 1.05) - 273.15  # Unused function

# Secondary transformation with conditional expressions and distractors
baseline_ref = 20.0
offset_map = {}
for i, item in enumerate(transformed):
    sensor_type = raw_readings[i]['sensor']
    raw_val = raw_readings[i]['value']
    offset_map[sensor_type] = {
        'base': raw_val,
        'deviation': abs(raw_val - baseline_ref),
        'weight': 1.0 if raw_val > baseline_ref else 0.5,
        'timestamp': f"2023-07-21T1{i}:30:00Z"
    }

# Irrelevant aggregation (distractor)
total_warnings = sum(1 for r in raw_readings if r['status'] == 'WARN')
mean_deviation = sum(v['deviation'] for v in offset_map.values()) / len(offset_map)
weighted_sum = sum(v['deviation'] * v['weight'] for v in offset_map.values())

# Complex data structure manipulation
log_entries = []
for reading, proc in zip(raw_readings, transformed):
    log_entries.append({
        'type': reading['sensor'],
        'raw': reading['value'],
        'proc': proc['processed_value'],
        'err': proc['flagged'],
        'meta': offset_map[reading['sensor']]
    })

# Another red herring: unused recursive function
def calculate_depth(data, depth=0):
    if not isinstance(data, dict) or depth >= 3:
        return depth
    return max(calculate_depth(v, depth + 1) for v in data.values() if isinstance(v, (dict, list)))

# Buffer simulation with bit manipulation distraction
buffer_flag = 0b1010
if len(log_entries) > 4:
    buffer_flag |= 0b0101
    buffer_flag ^= 0b0011  # Final flag state irrelevant

# Actual processing pipeline
processed_logs = []
def process_entry(log):
    val = log['proc']
    if log['type'] == 'temp':
        return {'cat': 'thermal', 'score': val * 1.1}
    elif log['type'] == 'humid':
        return {'cat': 'moisture', 'score': val * 0.9}
    elif log['type'] == 'co2':
        base_score = val / 10.0
        penalty = 5 if val > 400 else 0
        return {'cat': 'air', 'score': base_score - penalty}
    else:
        return {'cat': 'other', 'score': max(val - 100, 0) / 15.0}

for entry in log_entries:
    if not entry['err']:
        processed_logs.append(process_entry(entry))

# Decoy analysis function with misleading intermediate output
def dummy_analysis(logs):
    count_by_cat = {}
    for l in logs:
        cat = l['cat']
        count_by_cat[cat] = count_by_cat.get(cat, 0) + 1
    return sum(count_by_cat.values()) * 0.5  # Never called

# Key computation with conditional expression and dictionary reduction
aggregated_scores = {}
for item in processed_logs:
    cat = item['cat']
    score = item['score']
    aggregated_scores[cat] = aggregated_scores.get(cat, 0) + score

overall_factor = 1.25 if len(aggregated_scores) >= 3 else 0.9

# Final diagnostic calculation (target)
def analyze_readings(scores_list):
    total = 0.0
    for s in scores_list:
        category_boost = 1.1 if s['cat'] == 'thermal' or s['cat'] == 'moisture' else 1.0
        total += s['score'] * category_boost
    
    # Apply non-linear correction based on aggregated characteristics
    adjustment = 0.0
    if 'air' in aggregated_scores:
        air_score = aggregated_scores['air']
        adjustment = math.log(abs(air_score) + 1) * 0.5 if air_score != 0 else 0.0
    
    intermediate = total * overall_factor + adjustment
    
    # Final mapping through conditional expression
    final_value = intermediate if intermediate > 0 else abs(intermediate) * 0.5
    return round(final_value, 4)

# Execution point of interest
final_diagnostic = analyze_readings(processed_logs)
print(f"Target result: {final_diagnostic}")