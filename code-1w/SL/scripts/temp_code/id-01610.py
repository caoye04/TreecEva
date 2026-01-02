import itertools

# Sensor simulation and diagnostic analysis system
def generate_synthetic_readings():
    # Irrelevant base pattern generation
    base_sequence = [i * 1.5 + (i % 3) for i in range(12)]
    noise_offset = sum([i**0.5 for i in range(5)])  # Distractor computation
    return [round(x + noise_offset, 3) for x in base_sequence]

# Unused function - red herring
def legacy_calibrate(arr):
    scaling_factor = 0.92
    return [x * scaling_factor for x in arr if x > 5]

# Auxiliary transformation with partial relevance
def filter_outliers(data, limit=25.0):
    mean_val = sum(data) / len(data)
    deviated = [x for x in data if abs(x - mean_val) < limit]
    return deviated if len(deviated) > 6 else data[:8]  # Fallback path

# Bit manipulation decoy
def compute_checksum(value_list):
    checksum = 0
    for v in value_list:
        shifted = int(v) << 2
        checksum ^= shifted & 0xFF
    return checksum  # Never used in final result

# Core processing with embedded distractions
def process_sensor_array(raw_readings):
    # Step 1: Normalize readings using offset (relevant)
    offset = raw_readings[0] - 1.5
    normalized = [round(x - offset, 3) for x in raw_readings]
    
    # Step 2: Apply windowed averaging (partially relevant)
    averaged = []
    for i in range(2, len(normalized)):
        window_avg = round(sum(normalized[i-2:i+1]) / 3, 3)
        averaged.append(window_avg)
    
    # Step 3: Inject synthetic padding (distractor)
    padded = [0.111] + averaged + [0.222, 0.333]
    pad_sum = sum(padded[::3])  # Computation on padding - irrelevant
    
    # Step 4: Pairwise diff mask (mixed relevance)
    diffs = [abs(padded[i+1] - padded[i]) for i in range(len(padded)-1)]
    masked_diffs = [d if d > 0.4 else 0.0 for d in diffs]
    
    # Step 5: Tuple-based state tracking (core concept)
    states = []
    for idx, val in enumerate(masked_diffs):
        flag = (idx % 3 == 0)
        states.append((idx, round(val * 1.1, 3), flag))
    
    # Step 6: Filter active states (relevant)
    active_states = [s for s in states if s[2]]
    
    # Step 7: Transform to dictionary structure (key step)
    indexed_map = {s[0]: s[1] for s in active_states}
    
    # Dead code branch - misleading control flow
    if len(indexed_map) > 10:
        fallback = {k: v * 0.5 for k, v in indexed_map.items()}
        return list(fallback.values())
    
    # Actual return path
    return list(indexed_map.values())

# Threshold logic with decoy branching
def build_threshold_profile(base_temp=22.1):
    profile = {}
    
    # Real thresholds
    profile['critical'] = base_temp + 7.3
    profile['warning'] = base_temp + 3.8
    
    # Distractor entries
    profile['calib_min'] = base_temp - 5.0
    profile['tolerance'] = 0.75
    profile['gain'] = 1.08
    
    # Unused derived values
    for key in ['offset_x', 'offset_y', 'offset_z']:
        profile[key] = (base_temp * 0.12) % 1.0
    
    return profile

# Core analysis function with multiple layers
def analyze_readings(readings, thresholds):
    # Initialize counters
    high_count = 0
    mid_count = 0
    total_energy = 0.0
    
    # Primary evaluation loop
    for val in readings:
        total_energy += val ** 1.1  # Accumulate transformed metric
        
        if val > thresholds['critical']:
            high_count += 1
        elif val > thresholds['warning']:
            mid_count += 1
    
    # Compute composite index (intermediate)
    index_raw = (high_count * 13) + (mid_count * 5)
    energy_norm = round(total_energy / (len(readings) or 1), 3)
    
    # Dummy entropy calculation (red herring)
    if energy_norm > 10:
        entropy = 0
        energy_ints = [int(e * 10) for e in readings[:6]]
        for x in energy_ints:
            entropy ^= (x & 7) << (x % 3)
    
    # Final diagnostic formula (actual answer path)
    stability_factor = abs(len(readings) - 7)  # Deviation from expected length
    diagnostic_score = index_raw * 100 - energy_norm * 10 + stability_factor * 3
    
    # Additional distraction: unused tuple unpacking
    extras = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    for a, b, c in extras:
        diagnostic_score -= (a ^ b) & c  # This evaluates but doesn't affect final path
    
    return int(round(diagnostic_score))

# Orchestration with hidden simplicity
if __name__ == "__main__":
    # Generate raw input
    raw_data = generate_synthetic_readings()
    
    # Apply filtering (some steps are distracting)
    filtered_data = filter_outliers(raw_data)
    
    # Process through main pipeline
    processed_data = process_sensor_array(filtered_data)
    
    # Build threshold map (contains decoys)
    threshold_map = build_threshold_profile(base_temp=20.5)
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")