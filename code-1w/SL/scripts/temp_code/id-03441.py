import math

# Simulated sensor data from wind turbine array
turbine_ids = [101, 102, 103, 104, 105]
sensor_readings = [
    [120.5, 135.2, 140.1, 138.7, 142.3],
    [119.8, 136.0, 139.5, 137.9, 141.8],
    [121.0, 134.8, 141.2, 138.5, 143.0],
    [119.0, 135.5, 138.9, 138.0, 140.5],
    [120.0, 135.0, 140.0, 137.5, 142.0]
]

# Irrelevant auxiliary data (distractor)
legacy_system_codes = ['A7', 'B9', 'C3', 'D1', 'E5']
reliability_weights = {tid: round(1 / (1 + abs(tid - 103)), 3) for tid in turbine_ids}

# Fault detection thresholds (real logic)
thresh_high = 140.0
thresh_low = 135.0

# Simulated timestamp matrix (unused but plausible)
timestamps = [[f'2023-07-01T{i}:{j:02d}:00' for j in range(5)] for i in range(8, 13)]

# Misleading intermediate calculation (dead path)
avg_temporal = [sum(row)/len(row) for row in sensor_readings]

# Real-time drift correction factor (distractor, not used later)
drift_correction = sum([abs(read[2] - read[3]) for read in sensor_readings]) / len(sensor_readings)

# Flag potential faults based on sustained threshold breaches
def detect_faults(readings_matrix):
    flags = []
    for idx, readings in enumerate(readings_matrix):
        high_count = sum(1 for r in readings if r > thresh_high)
        low_count = sum(1 for r in readings if r < thresh_low)
        # Only flag if both extremes occur (complex condition)
        flags.append(high_count >= 2 and low_count >= 1)
    return flags

# Auxiliary function that looks important but is unused
def compute_efficiency_score(data):
    base = sum([max(row) - min(row) for row in data])
    return round(base * 0.87, 2)

# Bitwise alignment check for system sync (red herring)
sync_mask = 0b11111
activation_pattern = 0
for i, readings in enumerate(sensor_readings):
    if sum(1 for r in readings if r > 130) == 5:
        activation_pattern |= (1 << i)

# Unused combinatorial analysis (distractor)
from itertools import combinations
cross_turbine_pairs = list(combinations(turbine_ids, 2))
coherence_score = len([c for c in cross_turbine_pairs if abs(c[0]-c[1]) < 3])

# Core processing function with relevant logic
def analyze_stability(metrics, flags):
    stable_count = 0
    variance_pool = []
    
    for i, (data, flag) in enumerate(zip(metrics, flags)):
        if flag:  # Skip faulty turbines
            continue
            
        # Compute rolling variance over consecutive pairs
        variances = []
        for j in range(len(data) - 1):
            diff = data[j+1] - data[j]
            variances.append(diff * diff)
            
        turbine_var = sum(variances) / len(variances) if variances else 0
        variance_pool.append(turbine_var)
        
        if turbine_var < 12.0:
            stable_count += 1
    
    # Use enumerate to find best-performing segment
    best_segment = 0
    for seg_idx, segment in enumerate(sensor_readings):
        seg_avg = sum(segment) / len(segment)
        if seg_idx == 0 or seg_avg > best_segment:
            best_segment = seg_avg
    
    # Final stability index combines multiple factors
    base_index = stable_count * 100
    if variance_pool:
        base_index += int(sum(variance_pool) / len(variance_pool))
    
    # Inject result from bitwise pattern (irrelevant)
    decoy_factor = activation_pattern & 0b1010
    final_index = base_index - decoy_factor * 5  # Minor obfuscation
    
    return final_index

# Data normalization function (looks critical but partially irrelevant)
def normalize_readings(raw_data):
    normalized = []
    global_max = max(max(row) for row in raw_data)
    global_min = min(min(row) for row in raw_data)
    
    for row in raw_data:
        norm_row = []
        for val in row:
            norm_val = (val - global_min) / (global_max - global_min) * 100
            norm_row.append(round(norm_val, 3))
        normalized.append(norm_row)
    return normalized

# Another decoy: historical baseline comparison
historical_averages = [120.0, 135.5, 140.2, 138.0, 142.0]
deviation_vector = [abs(sensor_readings[i][2] - historical_averages[i]) for i in range(5)]
consistency_metric = 100 - sum(deviation_vector)

# Main aggregation function (key logic path)
def aggregate_metrics(turbine_data, fault_flags):
    # Normalize data (used)
    processed_data = normalize_readings(turbine_data)
    
    # Analyze stability on original scale (uses raw data)
    stability_score = analyze_stability(turbine_data, fault_flags)
    
    # Spurious entropy calculation (distractor)
    entropy = 0.0
    for row in processed_data:
        for x in row:
            if x > 0:
                entropy -= x * math.log(x/100) * 0.01
    
    # Critical decision: only use first three turbines for final diagnosis
    primary_turbines = [row[:3] for row in turbine_data[:3]]
    primary_sum = sum(sum(row) for row in primary_turbines)
    
    # Combine with stability score using integer division
    rough_estimate = primary_sum // 3
    
    # Final diagnostic blends multiple sources, but only some matter
    final_value = stability_score + (rough_estimate % 89)
    
    # Dead code branch (never executed due to constant)
    debug_mode = False
    if debug_mode:
        print(f'Diagnostic trace: {entropy=}, {consistency_metric=}')
    
    return int(final_value)

# Execute core pipeline
fault_flags = detect_faults(sensor_readings)
final_diagnostic = aggregate_metrics(turbine_data=sensor_readings, fault_flags=fault_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")