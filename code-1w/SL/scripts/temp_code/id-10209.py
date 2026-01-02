from collections import defaultdict
import itertools

# Simulate sensor data with noise and metadata
raw_readings = [14, 17, 23, 14, 19, 23, 14, 28, 17, 23]
noise_profile = {'offset': 3, 'jitter': [1, -2, 1], 'gain': 1.1}
sensor_metadata = {
    'calibration': [1.0, 0.98, 1.02],
    'location': 'Zone-C',
    'last_reset': '2023-09-01'
}

# Irrelevant helper that is never called
def legacy_calibrate(x):
    return [val * 0.95 for val in x]

# Decoy transformation with unused intermediate
buffer_cache = []
for _ in range(3):
    buffer_cache.append(sum(noise_profile['jitter']) * noise_profile['gain'])

# Apply gain and offset correction (relevant)
corrected_readings = [(x + noise_profile['offset']) * noise_profile['gain'] for x in raw_readings]

# Introduce misleading statistical summary
decoy_mean = sum(corrected_readings) / len(corrected_readings)
decoy_variance = sum((x - decoy_mean) ** 2 for x in corrected_readings) / len(corrected_readings)

# Bucket readings by original value (before correction) using defaultdict
bucketed = defaultdict(list)
for val in raw_readings:
    bucketed[val].append(val)

# Compute frequency map (used later)
frequency_map = {k: len(v) for k, v in bucketed.items()}

# Simulate time-series windows using itertools
windowed_pairs = list(itertools.pairwise(raw_readings))
transition_count = defaultdict(int)
for a, b in windowed_pairs:
    transition_count[(a, b)] += 1

# Phantom clustering attempt (dead code path)
clusters = {}
if len(raw_readings) > 50:  # Never true
    clusters = {'group1': [], 'group2': []}
else:
    temp_key = tuple(set(noise_profile['jitter']))
    clusters[temp_key] = 'placeholder'

# Core evaluation logic hidden among distractors
def assess_stability(freq_dict, base_threshold=3):
    frequent_values = [k for k, v in freq_dict.items() if v >= base_threshold]
    if not frequent_values:
        return 0
    # Use lambda to compute weighted impact
    impact_func = lambda x: x * freq_dict[x]
    return sum(map(impact_func, frequent_values))

# Secondary metric: detect repetitive patterns
repetition_penalty = 0
for count in frequency_map.values():
    if count > 2:
        repetition_penalty -= 2  # Small penalty

# Baseline computation from corrected signals
baseline = sum(corrected_readings) / len(corrected_readings)

# Metric data construction with red herring fields
metric_data = {
    'readings': corrected_readings,
    'freq_snapshot': frequency_map.copy(),
    'transitions': dict(transition_count),
    'system_noise': buffer_cache[:],  # Unused field
    'version': '2.1-alpha'  # Irrelevant metadata
}

# UNUSED function - looks important but isn't called
def finalize_report(data, sig_digits=4):
    return {"digest": hash(str(data)[:sig_digits])}

# Main scoring function - only this matters
def evaluate_performance(metrics, base):
    readings = metrics['readings']
    freq_data = metrics['freq_snapshot']
    
    # Step 1: stability score from high-frequency originals
    stability = assess_stability(freq_data)
    
    # Step 2: average of top 4 corrected readings
    sorted_corrected = sorted(readings, reverse=True)
    top_average = sum(sorted_corrected[:4]) / 4
    
    # Step 3: combine with baseline offset
    adjusted_base = base * 1.05
    
    # Step 4: apply stability as multiplier if above threshold
    if stability > 10:
        contribution = stability * 0.3
    else:
        contribution = 10
    
    # Step 5: final composition
    score = top_average + contribution - abs(adjusted_base - top_average)
    
    # Dead branch: never executes due to data
    if len(metrics.get('system_noise', [])) > 100:
        score *= 0.9
        
    return int(round(score))

# Critical execution point
final_score = evaluate_performance(metric_data, baseline)
print(f"Target result: {final_score}")