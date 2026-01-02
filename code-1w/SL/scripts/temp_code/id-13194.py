from collections import defaultdict, Counter

# Simulated sensor network diagnostic system
def acquire_signal():
    return [i * 1.5 for i in range(80) if i % 3 != 0]

# Irrelevant signal processing branch (dead path)
def legacy_calibration(signal):
    adjusted = []
    for x in signal:
        if x > 40:
            adjusted.append(x * 0.85)
        else:
            adjusted.append(x * 1.05)
    return adjusted

# Distractor: Unused transformation
def frequency_shift(data, shift=2.5):
    return [d + shift for d in data if d % 4 != 0]

# Real pipeline starts here
def filter_anomalies(readings):
    normal_range = [x for x in readings if 5 <= x <= 90]
    outliers = [x for x in readings if x < 5 or x > 90]
    
    # Red herring: counting but not using
    stats = defaultdict(int)
    for r in readings:
        if r < 5: stats['low'] += 1
        elif r > 90: stats['high'] += 1
    
    # Actual filtering logic
    if len(outliers) > 5:
        return normal_range[:len(normal_range) // 2]
    return normal_range[::2]  # Return every second reading

# Bit manipulation decoy (never called)
def encrypt_channel(data):
    result = 0
    for d in data:
        result ^= int(d) << 1
    return result

# Misleading intermediate transform
def normalize_amplitude(signal):
    max_val = max(signal)
    return [round(s / max_val, 6) for s in signal]

# Core processing with conditional exit
def process_readings(cleaned):
    readings_map = defaultdict(list)
    for i, val in enumerate(cleaned):
        bucket = i % 7
        readings_map[bucket].append(val)
    
    # Compute multiple unused metrics
    entropy_score = sum([len(v) for v in readings_map.values()]) / 7
    peak_group = max(readings_map.keys(), key=lambda k: sum(readings_map[k]))
    
    # Decoy statistical analysis
    flat = [item for sublist in readings_map.values() for item in sublist]
    counter_stats = Counter(flat)
    mode_approx = counter_stats.most_common(1)[0][1]
    
    # Real computation path
    primary_band = readings_map.get(3, [])
    if not primary_band:
        return sum(flat) / len(flat)
    
    # Conditional early termination based on bit check
    control_flag = len(primary_band) & 1
    if control_flag:
        secondary = readings_map.get(5, [])
        if secondary:
            adjustment = secondary[0] % 3
            primary_band = [p - adjustment for p in primary_band]
        else:
            return sum(primary_band) * 0.95
    
    # Final deterministic calculation
    base_value = sum(primary_band)
    correction_factor = len(cleaned) % 4
    final_adjustment = base_value - (correction_factor * 2.75)
    
    # Critical execution point
    final_diagnostic = round(final_adjustment, 4)
    
    # Dead code below (never reached due to return)
    if final_diagnostic < 0:
        return abs(final_diagnostic) * 2
    
    return final_diagnostic

# Orchestration with red herring calls
raw_data = acquire_signal()
legacy_data = legacy_calibration(raw_data)  # Unused
shifted_data = frequency_shift(raw_data)     # Unused

# Key statement
final_diagnostic = process_readings(filter_anomalies(raw_data))

# Output result
print(f"Result: {final_diagnostic}")