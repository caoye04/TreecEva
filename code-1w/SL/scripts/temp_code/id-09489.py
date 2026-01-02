import math

# Irrelevant helper function (decoy)
def analyze_quantum_state(state_vector):
    return sum(abs(x) ** 2 for x in state_vector)

# Unused transformation
def transform_legacy_format(data):
    return [x * 1.5 + 2 for x in data if x > 0]  # Dead path

# Simulate sensor noise (never called)
def generate_noise(length, seed=42):
    return [(i * seed) % 7 for i in range(length)]

# Core logic: performance evaluation with multiple distractions
def normalize readings(raw_readings):
    max_val = max(raw_readings)
    return [x / max_val for x in raw_readings]

# Bit manipulation red herring
def check_flag_status(flags):
    flagged = []
    for f in flags:
        if f & 0b1010:  # arbitrary bitmask check
            flagged.append(f ^ 0b1111)
    return flagged  # computed but unused

# Real processing begins here
def filter_outliers(values, threshold=2.0):
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [x for x in values if abs(x - mean) <= threshold * std_dev]

# String-based distractor (simulates config parsing)
def parse_config_tags(tag_string):
    tags = tag_string.upper().split(',')
    valid_tags = {t.strip() for t in tags if t.isalnum()}
    blacklist = {'DEBUG', 'TEMP', 'LEGACY'}
    return valid_tags - blacklist  # used to simulate complexity

# Main scoring logic
def compute_efficiency_ratio(measurements):
    cleaned = filter_outliers(measurements)
    normalized = normalize_readings(cleaned)
    return sum(math.log(x + 1e-5) for x in normalized)  # prevent log(0)

# Secondary metric with misleading intermediate
def calculate_stability_index(log_entries):
    diffs = [abs(log_entries[i+1] - log_entries[i]) for i in range(len(log_entries)-1)]
    smoothed = [d for d in diffs if d < 100]  # artificial cap
    if not smoothed:
        return 0.0
    inverse_variance = 1 / ((sum(smoothed) / len(smoothed)) + 1e-6)
    return inverse_variance * 0.75

# Final evaluation incorporating multiple concepts
def evaluate_performance(metrics, base):
    # Step 1: Filter and normalize primary metric
    primary_stream = metrics.get('readings', [])
    filtered_data = filter_outliers(primary_stream)
    efficiency = compute_efficiency_ratio(filtered_data)
    
    # Step 2: Extract secondary patterns using string methods (distraction)
    event_log_raw = metrics.get('events', '')
    events_clean = event_log_raw.replace('_', ' ').strip()
    event_tokens = [t for t in events_clean.split() if t.isupper()]
    critical_count = len([t for t in event_tokens if 'ERR' in t or 'CRIT' in t])
    
    # Step 3: Use set operations on irrelevant metadata
    labels = metrics.get('labels', 'sensor_A, status_OK, TEMP')
    active_labels = parse_config_tags(labels)
    has_issue = 'FAULT' in active_labels
    
    # Step 4: Bitwise decoy on unrelated control flags
    control_flags = metrics.get('controls', [0b1010, 0b0101, 0b1111])
    suspicious_flags = check_flag_status(control_flags)  # computed but not impactful
    
    # Step 5: Stability analysis from log history
    history = metrics.get('history', [])
    stability = calculate_stability_index(history)
    
    # Step 6: Apply nonlinear transformation to base value
    adjusted_base = base ** 1.5
    if stability > 0.5:
        adjusted_base *= 1.2
    
    # Step 7: Combine efficiency and base with weighting
    raw_score = efficiency * 100 + adjusted_base
    
    # Step 8: Apply penalty if critical events detected
    if critical_count > 0:
        raw_score *= (0.9 ** critical_count)
    
    # Step 9: Round based on arbitrary condition
    if 'CALIBRATED' in active_labels:
        final = round(raw_score)
    else:
        final = int(raw_score)  # truncation
    
    # Step 10: Final adjustment via list comprehension side-effect
    modifiers = [stability * 2, efficiency / 50]
    adjustments = [m * final for m in modifiers if m > 0.1]
    if adjustments:
        final += int(sum(adjustments) / len(adjustments))
    
    return final

# --- Execution Context ---
if __name__ == '__main__':
    # Simulated input data with red herrings
    metric_data = {
        'readings': [120, 130, 125, 1000, 122, 128, 110],  # 1000 is outlier
        'events': 'SYS_INIT, SENSOR_READING_OK, NO_ERR_DETECTED',
        'labels': 'sensor_A, CALIBRATED, DEBUG',
        'controls': [0b1010, 0b0100, 0b1100],
        'history': [5.1, 4.9, 5.0, 5.2, 5.1, 4.8, 5.3]
    }
    baseline = 42
    
    # Dead variables (distractors)
    quantum_reference = [0.3+0.4j, 0.5-0.1j]
    legacy_output = transform_legacy_format([1, -2, 3])
    noise_pattern = generate_noise(10)
    
    # Key execution point
    final_score = evaluate_performance(metric_data, baseline)
    
    # Output result
    print(f"Target result: {final_score}")