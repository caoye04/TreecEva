from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion (real and decoy)
sensor_readings = [14, 17, 14, 23, 17, 14, 26, 23, 17, 14, 29, 26, 23, 17, 14]
noise_floor = 12
detected_peaks = []
baseline_shift = 0

# Irrelevant statistical tracking (distractor)
reading_frequencies = Counter(sensor_readings)
mode_value = reading_frequencies.most_common(1)[0][0]

# Signal preprocessing with red herring transformations
corrected_readings = [x - noise_floor for x in sensor_readings]
filtered_readings = [x for x in corrected_readings if x > 3]
sorted_peaks = sorted(filtered_readings, reverse=True)

# Decoy analysis path (dead code - never called)
def legacy_analysis(data):
    return sum([math.sqrt(x) for x in data if x > 5])

# Unused transformation matrices (distractor variables)
transform_matrix_a = [[1, -1], [1, 1]]
weight_vector = [0.5, 0.5]

# Real processing begins: group by magnitude bands
band_mapping = defaultdict(list)
for val in sorted_peaks:
    band = val // 5
    band_mapping[band].append(val)

# Threshold policy setup (mixed relevant/irrelevant)
temporal_weights = {'morning': 0.7, 'evening': 1.3}
threshold_map = {k: v * 2.5 for k, v in Counter(band_mapping).items()}

# Phantom normalization function (unused)
def normalize_signal(seq):
    mean_val = sum(seq) / len(seq)
    return [round((x - mean_val) / mean_val, 3) for x in seq]

# Critical data restructuring
processed_data = []
for band, values in band_mapping.items():
    avg_val = sum(values) / len(values)
    if avg_val > 4.0:
        processed_data.append({'band': band, 'strength': avg_val, 'count': len(values)})

# Secondary filter based on structural criteria
valid_entries = [entry for entry in processed_data if entry['count'] >= 2]
pruned_data = [entry for entry in valid_entries if entry['band'] > 1]

# Simulate diagnostic rules
rule_triggered = False
if len(pruned_data) >= 2:
    total_strength = sum(entry['strength'] for entry in pruned_data)
    max_band_gap = max(pruned_data, key=lambda x: x['band'])['band'] - min(pruned_data, key=lambda x: x['band'])['band']
    if max_band_gap >= 2:
        rule_triggered = True

# Auxiliary computation with misleading intermediate (distractor)
entropy_score = 0.0
if len(band_mapping) > 1:
    probabilities = [len(v) / len(sensor_readings) for v in band_mapping.values()]
    entropy_score = -sum(p * math.log2(p) for p in probabilities if p > 0)

# Core analysis function with conditional logic
def analyze_signal(data_list, thresholds):
    if not data_list:
        return -1
    
    # Weighted scoring with threshold modulation
    score = 0
    for item in data_list:
        band = item['band']
        strength = item['strength']
        count = item['count']
        
        # Conditional boost (relevant logic)
        boost = 1.0
        if count > 2:
            boost += 0.5
        if strength > 8.0:
            boost *= 1.2
        
        base_contribution = strength * count * boost
        threshold_key = band
        dynamic_threshold = thresholds.get(threshold_key, 5.0)
        
        # Only contribute if above adaptive threshold
        if strength > dynamic_threshold:
            score += int(base_contribution)
    
    # Final adjustment based on rule activation (cross-concept linkage)
    global rule_triggered
    if rule_triggered:
        score = int(score * 1.75)  # 75% boost when pattern detected
    
    # Red herring final check (never executed due to condition)
    if entropy_score > 3.0:
        score = int(score * 0.8)
    
    return score + 10  # Base offset

# Execute critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")