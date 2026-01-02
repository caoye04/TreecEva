def analyze_pattern(sequence, weights):
    accumulated = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            accumulated += val * weights[i % len(weights)]
        else:
            accumulated -= val // (weights[(i+1) % len(weights)] or 1)
    return accumulated

# Irrelevant auxiliary function (dead path)
def deprecated_normalizer(x):
    return sum(v ** 0.5 for v in x if v > 0) // len(x)

# Unused diagnostic flag
system_status = "STANDBY"

# Simulated sensor inputs (distraction data)
sensor_a_readings = [12, 15, 14, 17, 20]
sensor_b_readings = [8, 10, 13, 9, 11]
baseline_offset = 3

# Weight matrix for pattern analysis (partially relevant)
weight_profile = [2, 3, 1]

# Primary data stream - core to computation
data_stream = [5, 9, 6, 8, 7, 10]

# Misleading intermediate transformation
temp_correction = [x ^ 7 for x in data_stream]  # XOR obfuscation (unused)

# Control thresholds (red herring)
thresholds = {
    'low': 1.5,
    'high': 8.9,
    'critical': 12.0
}

# Actual operational config (key input)
threshold_map = {
    'alpha': 6,
    'beta': 4,
    'gamma': 5
}

# Derived metric with conditional logic
smoothed_avg = sum(x for x in data_stream if x > 6) / len(data_stream)
adjusted_bias = smoothed_avg - baseline_offset if smoothed_avg > 7 else baseline_offset

# Generate signature using bitwise and arithmetic mix
bit_flags = (len(data_stream) << 2) ^ 15
health_signature = (
    analyze_pattern(data_stream, weight_profile) + 
    (bit_flags & 25)  # inject bit manipulation result
)

# Decoy aggregation (never called)
def aggregate_diagnostics(sensors):
    return max(sensors) - min(sensors)

# Core processing function
def process_metrics(signal, config):
    base = signal
    modifier = 0
    
    # Nested conditional expressions with distractor vars
    alpha_mod = config['alpha'] if base > 40 else config['gamma']
    beta_mod = config['beta'] if (base % 3) == 0 else config['alpha']
    
    # Complex multi-step update with irrelevant branches
    if base > 50:
        modifier += base // alpha_mod
    elif base > 30:
        modifier += (base // beta_mod) + 2
    else:
        modifier -= 1
    
    # Additional adjustment using tuple unpacking (meaningful)
    factors = (3, 7, 2)
    x, y, z = factors
    modifier *= (x + z)  # uses tuple values
    
    # Final decision with conditional expression
    final_value = modifier if modifier > 0 else abs(modifier) * 1.5
    
    # Dead code block (misleading)
    debug_trace = []
    for _ in range(3):
        debug_trace.append("NULL")  # unused
    
    return int(final_value)

# Execution point of interest
final_diagnostic = process_metrics(health_signature, threshold_map)

# Print target result
print(f"Target result: {final_diagnostic}")