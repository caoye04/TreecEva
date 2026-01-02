from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (irrelevant but realistic)
sensor_readings = [120, 135, 142, 118, 150, 130, 127, 145, 138, 132]
noise_floor = 110
calibration_offset = 8

# Irrelevant signal processing chain
denoised_signal = [max(0, x - noise_floor - calibration_offset) for x in sensor_readings]
frequency_bins = defaultdict(int)
for val in denoised_signal:
    freq_bin = val // 10
    frequency_bins[freq_bin] += 1

# Phantom diagnostic thresholds (distractor)
phantom_thresholds = {
    'critical': 95,
    'warning': 70,
    'normal': 50
}

# Real threshold logic disguised among red herrings
def compute_adaptive_base(x):
    if x < 125:
        return x * 0.8
    elif x < 140:
        return x * 0.85 + 5
    else:
        return x * 0.9 + 10

# Unused recursive function (dead code path)
def recursive_dampen(n, depth=0):
    if depth >= 3 or n <= 10:
        return n
    return recursive_dampen(n * 0.7, depth + 1)

# Core data used in actual computation
health_data = [
    {'metric': 'vital_a', 'value': 132, 'weight': 0.6},
    {'metric': 'vital_b', 'value': 145, 'weight': 0.9},
    {'metric': 'vital_c', 'value': 118, 'weight': 0.4},
    {'metric': 'vital_d', 'value': 138, 'weight': 0.7}
]

# Threshold map with misleading entries
temp_correction = 1.08
threshold_map = defaultdict(lambda: 120)
threshold_map.update({
    'vital_a': 128,
    'vital_b': compute_adaptive_base(145) // 1,  # Evaluate to 130
    'vital_c': 122,
    'vital_d': 130
})

# Decoy statistical analysis
mean_reading = sum(sensor_readings) / len(sensor_readings)
variance = sum((x - mean_reading) ** 2 for x in sensor_readings) / len(sensor_readings)
std_dev = math.sqrt(variance)

# Irrelevant combinatorics (distractor)
def count_valid_pairs(lst, limit):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] <= limit:
                count += 1
    return count

pair_count = count_valid_pairs(sensor_readings, 250)

# Real processing function buried in complexity
def evaluate_metric(value, base_threshold, weight):
    adjusted = value * weight
    required = base_threshold * weight
    return adjusted >= required

# Complex accumulator with mixed logic
def process_metrics(data, thresholds):
    result_counter = Counter()
    total_weighted = 0.0
    met_conditions = 0
    
    for entry in data:
        key = entry['metric']
        val = entry['value']
        wt = entry['weight']
        
        # Real logic step 1: weighted accumulation
        total_weighted += val * wt
        
        # Real logic step 2: threshold comparison
        if val >= thresholds[key]:
            result_counter['passed'] += 1
        else:
            result_counter['failed'] += 1
        
        # Real logic step 3: conditional promotion
        if wt >= 0.6 and val >= thresholds[key]:
            met_conditions += 1
    
    # Real logic step 4: final computation
    base_score = result_counter['passed'] * 25
    adjustment = met_conditions * 12
    
    # Real logic step 5: final formula
    final_score = base_score + adjustment - int(total_weighted // 10)
    
    # Dead branch (never taken, distractor)
    if result_counter['failed'] > 100:
        final_score = 0
    
    return final_score

# Misleading post-processing
aggregated_diagnostics = []
for i in range(3):
    shifted = process_metrics(health_data, threshold_map) - i * 5
    aggregated_diagnostics.append(shifted)

# Key execution point
final_diagnostic = process_metrics(health_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")