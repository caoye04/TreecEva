import itertools

# System calibration and diagnostic evaluation for quantum sensor array
def generate_calibration_sequence(base_seed, iterations):
    sequence = [base_seed]
    for i in range(1, iterations):
        if i % 5 == 0:
            sequence.append((sequence[-1] + i) * 2)
        elif i % 3 == 0:
            sequence.append(sequence[-1] - (i * 2))
        else:
            sequence.append(sequence[-1] + (i ** 2))
    return sequence

# Irrelevant helper: simulates thermal drift (dead code path)
def simulate_thermal_drift(temp_base, cycles):
    drift_values = []
    for cycle in range(cycles):
        adjustment = (temp_base * 0.87) + cycle % 7
        drift_values.append(int(adjustment))
    return drift_values  # Never used

# Decoy function: power optimization (not called in main logic)
def optimize_power_levels(levels):
    adjusted = []
    for level in levels:
        if level > 40:
            adjusted.append(level * 0.75)
        else:
            adjusted.append(level + 10)
    return adjusted

# Core processing with distractors
def analyze_phase_shifts(raw_data):
    shifted = []
    multiplier = 1.5
    for idx, val in enumerate(raw_data):
        if idx % 4 == 0:
            shifted.append(val * multiplier)
        elif idx % 4 == 1:
            shifted.append(val + 5)
        else:
            shifted.append(val - 3)
    # Misleading intermediate
    temp_normalization = sum(shifted) / len(shifted) if shifted else 0
    return shifted

# Main metric processor
def process_metrics(seq, config_map):
    # Extract relevant thresholds
    threshold_a = config_map['threshold_a']
    threshold_b = config_map['threshold_b']
    offset = config_map.get('offset', 0)
    
    # Distractor variables (unused in final logic)
    safety_margin = threshold_a * 0.15
    recalibration_factor = 1.07
    stability_log = []
    anomaly_count = 0
    
    cumulative_score = 0
    
    # Complex transformation with conditional expressions
    transformed = [
        x * 1.1 if x > threshold_a else \
        (x * 0.95 if x < threshold_b else x * 1.02) \
        for x in seq
    ]
    
    # Additional irrelevant list comprehension
    audit_trail = [f"Item_{i}: {val:.1f}" for i, val in enumerate(transformed) if val > 50]
    
    # Real logic: apply modular weighting based on index parity
    for index, value in enumerate(transformed):
        weight = 1.25 if index % 2 == 0 else 0.88
        adjusted_val = value * weight
        
        # Red herring: this block modifies unused variable
        if adjusted_val > 100:
            stability_log.append(True)
            anomaly_count += 1  # Distractor counter
        
        # Actual accumulation
        if index % 4 != 3:  # Skip every fourth element
            cumulative_score += int(adjusted_val)

    # Secondary manipulation using dictionary operations
    stats_summary = {
        'count': len(transformed),
        'sum_raw': sum(transformed),
        'weighted_total': cumulative_score
    }
    
    # Final computation with bit manipulation decoy
    decoy_hash = 0
    for val in transformed[:5]:
        decoy_hash ^= int(val) & 255  # Bitwise red herring
    
    # Real final result
    scaling_factor = config_map['scaling']['primary']
    base_correction = config_map['scaling']['offset']
    intermediate = (cumulative_score * scaling_factor) + base_correction
    
    # Apply final nonlinear correction
    final_diagnostic = int(intermediate - (intermediate * 0.11))
    
    return final_diagnostic

# Setup configuration map with nested structure
config = {
    'threshold_a': 65,
    'threshold_b': 35,
    'offset': 5,
    'scaling': {
        'primary': 1.08,
        'secondary': 0.92,
        'offset': -12
    }
}

# Generate sequence
calibration_sequence = generate_calibration_sequence(base_seed=23, iterations=18)

# Apply phase analysis (result not used - misleading call)
diagnostic_phases = analyze_phase_shifts(calibration_sequence)

# Create full diagnostic map
metric_weights = {k: v * 1.05 for k, v in config.items() if isinstance(v, (int, float))}
diagnostic_map = {**config, 'weights': metric_weights}

# Critical execution point
final_diagnostic = process_metrics(calibration_sequence, diagnostic_map)

# Output result
print(f"Result: {final_diagnostic}")