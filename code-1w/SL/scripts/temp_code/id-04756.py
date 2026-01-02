from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant fields
data = [
    {'temp': 23.5, 'hum': 65, 'press': 1013.25, 'err': 0, 'meta': {'seq': 1, 'valid': True}},
    {'temp': -999, 'hum': 70, 'press': 1012.9, 'err': 1, 'meta': {'seq': 2, 'valid': False}},
    {'temp': 24.1, 'hum': -999, 'press': 1011.8, 'err': 0, 'meta': {'seq': 3, 'valid': True}},
    {'temp': 22.8, 'hum': 68, 'press': 1014.1, 'err': 0, 'meta': {'seq': 4, 'valid': True}}
]

# Irrelevant historical baseline (distractor)
historical_avg = defaultdict(float)
historical_avg['temp'] = 22.0
historical_avg['hum'] = 60.0
historical_avg['press'] = 1013.0

# Weight configuration for processing (some weights are misleading)
weights = {
    'temp': 0.4,
    'hum': 0.3,
    'press': 0.2,
    'err_corr': 0.1,  # unused weight (red herring)
    'dummy': 0.0       # explicitly zero (decoy)
}

# Auxiliary functions (some irrelevant)
def validate_entry(entry):
    return entry['meta']['valid'] and entry['err'] == 0

# Unused function - dead code path
def legacy_normalize(val, key):
    if key == 'temp':
        return max(0, min(100, (val - 10) / 2))
    return val

# Core processing pipeline
def clean_data(raw):
    cleaned = []
    missing_counter = Counter()
    
    for item in raw:
        if item['temp'] == -999:
            missing_counter['temp'] += 1
            item['temp'] = 23.0  # impute
        if item['hum'] == -999:
            missing_counter['hum'] += 1
            item['hum'] = 65.0
        cleaned.append(item)
    
    # Log missing stats (not used later)
    total_missing = sum(missing_counter.values())
    debug_ratio = total_missing / (len(raw) * 2) if len(raw) > 0 else 0
    
    return cleaned

# Higher-order function with lambda abstraction
def create_scaler(ref):
    base = ref['temp']
    return lambda x: x['temp'] * math.sin(math.pi / 6) + (x['hum'] - ref['hum']) * 0.1

# Main metric processor
def process_metrics(dataset, config):
    # Step 1: Filter valid entries
    valid_entries = [e for e in dataset if validate_entry(e)]
    
    # Step 2: Clean data (impute missing values)
    processed = clean_data(valid_entries)
    
    # Step 3: Compute derived features
    temp_sum = sum(p['temp'] for p in processed)
    hum_avg = sum(p['hum'] for p in processed) / len(processed) if processed else 0
    press_trend = sum(processed[i+1]['press'] - processed[i]['press'] 
                     for i in range(len(processed)-1))

    # Step 4: Apply weighting (only temp and hum contribute)
    weighted_temp = temp_sum * config['temp']
    weighted_hum = hum_avg * config['hum']
    pressure_effect = abs(press_trend) * config['press']

    # Step 5: Apply non-linear correction using lambda scaler
    reference_point = processed[0] if processed else {'temp': 20, 'hum': 50}
    scaler = create_scaler(reference_point)
    scaled_value = sum(scaler(p) for p in processed)

    # Step 6: Conditional adjustment based on error count (always zero here)
    error_count = sum(1 for d in dataset if d['err'] != 0)
    if error_count > 1:
        adjustment = -5
    elif error_count == 1:
        adjustment = -2
    else:
        adjustment = 3  # bonus for clean data

    # Step 7: Accumulate final score
    raw_score = weighted_temp + weighted_hum + pressure_effect + adjustment
    
    # Step 8: Apply obscure scaling (simulates calibration factor)
    calibration = math.log(2 + abs(scaled_value) * 0.01 + 1)
    final_score = int(raw_score * calibration)

    # Irrelevant secondary computation (distractor)
    entropy = 0.0
    freq = Counter([int(p['temp']) for p in processed])
    total = sum(freq.values())
    for count in freq.values():
        prob = count / total
        entropy -= prob * math.log2(prob)

    # Debug print that doesn't affect result
    outlier_flag = any(p['press'] < 1012 for p in processed)

    return final_score

# Misleading pre-computation (dead code)
baseline_metric = 0
if len(data) > 3:
    baseline_metric = (data[0]['temp'] + data[-1]['temp']) * 0.5

# Key execution point
final_score = process_metrics(data, weights)

# Output result as required
print(f"Result: {final_score}")