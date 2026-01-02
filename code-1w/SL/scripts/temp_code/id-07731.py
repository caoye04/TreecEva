import itertools

# Simulated sensor data processing with noise filtering and scoring logic
def preprocess_sensor_data(raw_data):
    filtered = [x for x in raw_data if x > -100]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) * 100 for x in filtered]
    return normalized

# Irrelevant helper: converts numeric levels to descriptive strings
def level_to_string(level):
    mapping = {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Critical'}
    return mapping.get(round(level), 'Unknown')

# Dead function: never called but looks relevant
def legacy_calibrate(values):
    adjustment = sum([v % 7 for v in values if v > 10])
    return [v - adjustment for v in values]

# Complex transformation with red herring variables
def transform_signal_sequence(signal):
    shifted = [(s << 2) ^ 0xAA for s in signal]  # Bit manipulation distraction
    aggregated = 0
    for i, val in enumerate(shifted):
        if i % 3 == 0:
            aggregated += val % 100
        elif i % 5 == 0:
            aggregated -= val // 50
    return aggregated + len(signal)

# Misleading intermediate computation with unused result
def compute_apparent_magnitude(stream):
    magnitude = 0
    for idx, val in enumerate(stream):
        if idx < 10:
            magnitude += abs(val) * (0.9 ** idx)
        else:
            break
    scaling_factor = 2.718  # Unused but plausible
    adjustment_curve = [magnitude / (i + 1) for i in range(1, 6)]  # Dead computation
    return magnitude

# Core scoring logic buried among distractions
def evaluate_consistency(measurements):
    diffs = [abs(a - b) for a, b in zip(measurements, measurements[1:])]
    threshold = sum(diffs) / len(diffs) if diffs else 0
    stable_count = sum(1 for d in diffs if d < threshold)
    return stable_count > len(diffs) * 0.6

# Main computation path with conditional logic and distractors
def compute_final_score(data_stream):
    # Real preprocessing
    cleaned = preprocess_sensor_data(data_stream)
    
    # Distractor variables
    peak_level = max(cleaned) if cleaned else 0
    baseline_offset = min(cleaned) if cleaned else 0
    anomaly_flags = [c > 85 or c < 5 for c in cleaned]  # Not actually used
    
    # Real consistency check
    is_consistent = evaluate_consistency(cleaned)
    
    # Red herring: complex bit operation on length
    metadata_hash = (len(cleaned) ^ 0xFFFF) >> 4
    temp_adjustment = transform_signal_sequence([len(cleaned)])  # Uses length only
    
    # Another decoy score
    apparent_strength = compute_apparent_magnitude(cleaned)
    strength_category = level_to_string(round(apparent_strength / 25))  # Unused
    
    # Key calculation chain
    base_score = sum(cleaned) / len(cleaned) if cleaned else 0
    bonus_multiplier = 1.5 if is_consistent and peak_level > 50 else 1.0
    
    # Conditional expression (required python feature)
    penalty = 25 if any(x < 10 for x in cleaned[-5:]) else 0
    adjusted_score = base_score * bonus_multiplier - penalty
    
    # Final transformation using itertools (required feature): group by threshold
    groups = [list(g) for k, g in itertools.groupby(cleaned, key=lambda x: x > 40)]
    longest_high_streak = max((len(g) for g in groups if g[0] > 40), default=0)
    streak_bonus = 10 if longest_high_streak >= 3 else 0
    
    final_score = int(adjusted_score + streak_bonus)
    
    # Critical output
    return final_score

# Simulated input - deterministic
raw_input_stream = [105, -150, 200, 180, 190, 210, 205, 195, 185, 170, 160, 150, 140]

# Execution point of interest
data_stream = raw_input_stream.copy()
final_score = compute_final_score(data_stream)
print(f"Result: {final_score}")