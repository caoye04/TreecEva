import math

# Simulated sensor data processing system with red herrings
def collect_telemetry():
    raw_values = [i * 0.77 + 2.1 for i in range(15)]
    timestamps = list(range(15))
    statuses = ['OK'] * 10 + ['ERR'] * 5
    # Irrelevant aggregation (distraction)
    avg_status_len = sum(len(s) for s in statuses) / len(statuses)
    return list(zip(timestamps, raw_values, statuses))

# Unused decoy function (dead code path)
def legacy_calibrate(x):
    return (x * 1.05 - 0.3) ** 2

# Real transformation function
transform_fn = lambda val: round(math.sin(val) * 100, 4) if val > 3 else round(math.cos(val) * 50, 4)

# Data normalizer with misleading intermediate steps
def normalize_sequence(data):
    magnitude = sum(d ** 2 for d in data) ** 0.5
    if magnitude == 0:
        return data
    normalized = [d / magnitude for d in data]
    # Distractor: irrelevant statistical moment
    skew = sum((d - magnitude) ** 3 for d in data) / (len(data) or 1)
    kurtosis = sum((d - magnitude) ** 4 for d in data) / (len(data) or 1) - 3
    return normalized

# Complex configuration with irrelevant fields
config = {
    'threshold': 42.5,
    'debug_mode': True,
    'version': '3.8.1',
    'scaling_factor': -1.5,
    'max_iterations': 99,
    'temporal_window': 7,
    'activation_bias': 0.25,
    'use_legacy': False,
    'fallback_delay': 300
}

# Diagnostic processor combining multiple concepts
def process_metrics(data, cfg):
    # Extract relevant transformed values only
    filtered_vals = [item[1] for item in data if item[2] == 'OK']
    
    # Apply non-linear transformation
    transformed = [transform_fn(v) for v in filtered_vals]
    
    # Introduce bit manipulation distraction
    magic_seed = 0b1101 ^ int(cfg['threshold']) & 0b11111
    shift_offset = (magic_seed >> 2) % 6
    
    # Real computation path
    shifted = [t * (1.1 ** shift_offset) for t in transformed]
    
    # Decoy checksum (never used)
    checksum = sum(shifted[i] * (i+1) for i in range(len(shifted))) % 1024
    
    # Actual aggregation
    base_score = sum(abs(s) for s in shifted)
    
    # Conditional adjustment based on config
    if cfg['scaling_factor'] < 0:
        base_score *= cfg['activation_bias']
    else:
        base_score /= (cfg['scaling_factor'] + 1)
    
    # Integer truncation and modular correction
    truncated = int(base_score)
    corrected = truncated - (truncated % 7)  # Align to nearest lower multiple of 7
    
    # Final adjustment using enumerate (required idiom)
    for i, val in enumerate(shifted):
        if i % 3 == 0 and val > 0:
            corrected += int(val) % 5  # Minor incremental effect
    
    return corrected

# Orchestration with distractor variables
telemetry_data = collect_telemetry()
raw_stream = [x[1] for x in telemetry_data]
diagnostic_log = {"entries": len(telemetry_data), "errors": 5}

# Transform only valid entries
valid_entries = [(ts, val, st) for (ts, val, st) in telemetry_data if st == 'OK']
intermediate_signal = [v for _, v, _ in valid_entries]

# Normalization chain (partially irrelevant)
normalized_signal = normalize_sequence(intermediate_signal)
scaled_input = [ns * 42.0 for ns in normalized_signal]  # Unused downstream

# Core execution point
transformed_data = []
for ts, val, st in valid_entries:
    transformed_val = transform_fn(val)
    transformed_data.append((ts, transformed_val, st))

# Key statement
final_diagnostic = process_metrics(transformed_data, config)

print(f"Result: {final_diagnostic}")