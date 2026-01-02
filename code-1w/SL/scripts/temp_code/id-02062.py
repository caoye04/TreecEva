import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_values = [x * 1.7 for x in range(15)]
    offset = 4.2
    calibrated = [round(v + offset, 2) for v in raw_values]
    return calibrated

# Irrelevant helper: audio normalization (dead path)
def normalize_audio(signal):
    peak = max(abs(x) for x in signal)
    return [x / peak for x in signal] if peak > 0 else signal

# Data transformation pipeline
def transform_signal(data, factor=1.1):
    shifted = [(math.sin(x) * factor) + 0.5 for x in data]
    # Apply windowing function (only some values used later)
    windowed = [shifted[i] * (0.54 - 0.46 * math.cos(2 * math.pi * i / (len(shifted)-1))) for i in range(len(shifted))]
    filtered = [x for x in windowed if x > 0.25]
    return filtered

# Auxiliary calculation: battery efficiency (decoy)
def estimate_battery(level, usage_hours):
    base_rate = 0.87
    drain = level * (1 - base_rate ** usage_hours)
    projected = level - drain
    return round(projected, 2)

# Core pattern analyzer with red herring conditions
def analyze_pattern(seq, limit):
    # Decoy counters
    temp_sum = 0
    dummy_flag = False
    for val in seq:
        temp_sum += val * 1.1
        if temp_sum > 5 and not dummy_flag:
            dummy_flag = True
            temp_sum = 0  # Reset for no reason

    # Actual logic: count oscillations above threshold
    cross_count = 0
    prev_above = seq[0] > limit
    for reading in seq[1:]:
        curr_above = reading > limit
        if curr_above != prev_above:
            cross_count += 1
        prev_above = curr_above

    # Secondary metric: sum of squares (unused)
    sq_total = sum(x**2 for x in seq)

    # Tertiary logic: detect symmetry (irrelevant)
    mid = len(seq) // 2
    mirrored = seq[:mid] == seq[-mid:][::-1]

    # Final result based on crossing behavior only
    score = cross_count * 100 + (50 if mirrored else 0)
    return int(score)

# Unused recursive validation (distractor)
def validate_sequence(items, index=0):
    if index >= len(items) - 1:
        return True
    if items[index] >= items[index + 1]:
        return False
    return validate_sequence(items, index + 1)

# Main execution flow
if __name__ == "__main__":
    # Collect real data
    sensor_log = collect_readings()
    
    # Transform for analysis
    transformed_data = transform_signal(sensor_log, factor=1.3)
    
    # Compute auxiliary metrics (some irrelevant)
    avg_val = sum(transformed_data) / len(transformed_data) if transformed_data else 0
    max_val = max(transformed_data) if transformed_data else 0
    
    # Threshold derived from average and constant
    dynamic_cap = avg_val * 1.15
    threshold = min(max_val * 0.6, dynamic_cap)
    
    # Call target function
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
