import itertools

# Simulated sensor fusion system for environmental monitoring
base_threshold = 0.67
scaling_factor = 2.3
dummy_offset = -1.05

sensor_a_readings = [0.45, 0.72, 0.51, 0.83, 0.62]
sensor_b_readings = [0.39, 0.77, 0.54, 0.69, 0.81]
sensor_c_readings = [0.48, 0.68, 0.59, 0.74, 0.66]

# Irrelevant pre-processing: dummy normalization (unused later)
normalized_a = [x * scaling_factor + dummy_offset for x in sensor_a_readings]
normalized_b = [y * scaling_factor + dummy_offset for y in sensor_b_readings]

# Decoy transformation chain
transformed_b = []
for val in sensor_b_readings:
    if val > 0.7:
        transformed_b.append(val ** 1.5)
    else:
        transformed_b.append(val * 0.9)

# Real processing begins: cross-sensor correlation analysis
correlation_pairs = list(itertools.product(sensor_a_readings, sensor_b_readings))
strong_correlations = [pair for pair in correlation_pairs if abs(pair[0] - pair[1]) < 0.1]

# Compute confidence-weighted consensus from three sensors
def compute_consensus(a_vals, b_vals, c_vals):
    consensus = []
    for i in range(len(a_vals)):
        avg = (a_vals[i] + b_vals[i] + c_vals[i]) / 3
        weight = 1.0
        if abs(a_vals[i] - b_vals[i]) < 0.05:
            weight += 0.2
        if abs(b_vals[i] - c_vals[i]) < 0.05:
            weight += 0.2
        consensus.append(avg * weight)
    return consensus

consensus_values = compute_consensus(sensor_a_readings, sensor_b_readings, sensor_c_readings)

# Spurious secondary calculation (dead path)
avg_transformed = sum(transformed_b) / len(transformed_b) if transformed_b else 0.0
auxiliary_metric = avg_transformed * scaling_factor  # Unused downstream

# Flag generation based on threshold crossings
elevated_flags = []
for idx, val in enumerate(consensus_values):
    flags = 0
    if val > base_threshold:
        flags |= 1
    if sensor_a_readings[idx] > 0.7:
        flags |= 2
    if sensor_c_readings[idx] > 0.7:
        flags |= 4
    elevated_flags.append(flags)

# Decoy state machine (never invoked)
def analyze_hysteresis(seq):
    state = 0
    transitions = 0
    for x in seq:
        if x > 0.7 and state == 0:
            state = 1
            transitions += 1
        elif x <= 0.5 and state == 1:
            state = 0
            transitions += 1
    return transitions

# Diagnostic aggregation with red herring variables
intermediate_fusion = []
buffer_cache = []  # Distractor: looks important but unused

for i in range(len(consensus_values)):
    raw = consensus_values[i]
    flag_code = elevated_flags[i]
    
    # Apply conditional correction based on flag pattern
    if flag_code & 1:
        corrected = raw * 1.1
    elif flag_code & 2:
        corrected = raw * 0.95
    else:
        corrected = raw
        
    # Secondary adjustment based on position parity (subtle but relevant)
    if i % 2 == 0:
        corrected = max(corrected, base_threshold)
        
    intermediate_fusion.append(round(corrected, 6))

# Simulated diagnostic severity levels (mostly irrelevant)
diag_severity_map = {0: 'LOW', 1: 'MEDIUM', 2: 'HIGH', 3: 'CRITICAL'}
index_weights = [1.0, 0.95, 1.1, 0.85, 1.0]  # Position-based weighting

# Core diagnostic log construction (key step)
diagnostics_log = []
for j, fused_val in enumerate(intermediate_fusion):
    weighted_val = fused_val * index_weights[j]
    if weighted_val > base_threshold * 1.05:
        diagnostics_log.append(weighted_val * 1.2)
    else:
        diagnostics_log.append(weighted_val * 0.85)

# Dead code block: complex but unused spectral analysis
def perform_spectral_analysis(data):
    spec_result = 0.0
    for k in range(len(data)):
        for m in range(k+1, len(data)):
            spec_result += abs(data[k] - data[m]) * (k + m)
    return spec_result / (len(data) ** 2) if data else 0.0

spectral_index = perform_spectral_analysis(sensor_a_readings)  # Unused

# Final aggregation function with misleading complexity
def aggregate_diagnostics(log):
    if not log:
        return 0.0
    
    # Red herring: sort and take middle (but actually full sum matters)
    sorted_log = sorted(log)
    median_candidate = sorted_log[len(sorted_log)//2]
    
    # Actual computation: sum with outlier suppression
    total = 0.0
    for x in log:
        if x < 2.0:  # Filter extreme values (none present)
            total += x
        else:
            total += 1.5  # Fallback cap
    
    # Final scaling based on length (relevant)
    adjustment = len(log) * 0.15
    return round(total + adjustment, 6)

final_diagnostic = aggregate_diagnostics(diagnostics_log)

# Extraneous logging (distractor)
log_metadata = {
    'entries': len(diagnostics_log),
    'max_raw': max(sensor_a_readings + sensor_b_readings + sensor_c_readings),
    'timestamp': '2023-11-05T10:30:00Z',
    'aux': auxiliary_metric
}

print(f"Target result: {final_diagnostic}")