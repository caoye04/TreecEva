from itertools import combinations, cycle

# System health monitoring simulation with diagnostic filtering

def simulate_sensor_drift(base_value, noise_factor, iterations):
    """Simulate noisy sensor readings over time (irrelevant distractor)"""
    import math
    readings = []
    for i in range(iterations):
        noise = math.sin(i * 0.5) * noise_factor
        readings.append(base_value + noise + (i * 0.01))
    return readings

def generate_phase_shifts(n):
    """Generate phase shifts for signal processing (unused red herring)"""
    return [i * 360 / n for i in range(n)]
def calculate_entropy(seq):
    """Calculate Shannon entropy of a sequence (distractor function)"""
    from collections import Counter
    import math
    counts = Counter(seq)
    total = len(seq)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def detect_anomalies(logs, sensitivity=0.95):
    """Detect anomalies in system logs (dead path - never called)"""
    thresholds = [sensitivity * 100 for _ in range(5)]
    alerts = []
    for entry in logs:
        if sum(entry) > thresholds[0]:
            alerts.append(True)
    return alerts

def rolling_average(data, window_size):
    """Compute rolling average for smoothing (partially relevant distractor)"""
    result = []
    for i in range(len(data) - window_size + 1):
        result.append(sum(data[i:i+window_size]) / window_size)
    return result

def validate_checksum(sequence):
    """Validate data checksum using XOR folding (misleading intermediate)"""
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 100) % 256
    return checksum == 42  # Magic number check (red herring)

# Irrelevant data generation block
temp_calibration = [round(25 + 5 * ((i % 7) - 3), 2) for i in range(20)]
humidity_buffer = list(combinations([60, 65, 70, 75], 2))

# Core signal processing parameters (some used, some not)
baseline_cycles = 8
reference_amplitude = 12.0
harmonic_series = [reference_amplitude / (i+1) for i in range(baseline_cycles)]
phase_angles = generate_phase_shifts(8)  # Computed but unused

# Simulated telemetry data stream (real input source)
raw_telemetry = [
    [3, 7, 2, 8, 1],
    [5, 1, 6, 3, 9],
    [4, 9, 3, 7, 2],
    [8, 2, 5, 1, 6]
]

# Signal transformation chain (distractor pipeline)
processed_stream = []
for segment in raw_telemetry:
    amplified = [x * 1.5 for x in segment]
    normalized = [x / max(amplified) for x in amplified]
    discrete = [int(x * 10) for x in normalized]
    processed_stream.append(discrete)

# Decoy state variables (never used in final calculation)
current_state_vector = [0.85, 0.72, 0.91, 0.63]
failure_mode_pattern = list(cycle([1, 0, 1]))[:10]

# Real computational core disguised among distractions
def extract_signatures(data_blocks):
    signatures = []
    for block in data_blocks:
        # Actual relevant computation: sum of squares modulo prime
        sig = sum(x**2 for x in block) % 101  # Prime modulus
        signatures.append(sig)
    return signatures

def build_threshold_map(config_level):
    """Create threshold mapping based on configuration level"""
    config_map = {
        'critical': {'limit': 85, 'grace': 5},
        'high': {'limit': 70, 'grace': 8},
        'medium': {'limit': 50, 'grace': 10}
    }
    # Only 'high' is used; others are distractors
    return config_map['high']

def aggregate_metrics(cycle_data, threshold_profile):
    """Main aggregation logic - computes final diagnostic score"""
    # Step 1: Extract numeric signatures from each telemetry cycle
    sig_list = extract_signatures(cycle_data)
    
    # Step 2: Apply dynamic weighting based on threshold grace period
    weights = []
    base_weight = 0.8
    for sig in sig_list:
        if sig > threshold_profile['limit']:
            weights.append(base_weight)
        else:
            weights.append(base_weight + 0.3)  # Lower risk gets higher weight
    
    # Step 3: Weighted contribution calculation
    contributions = [sig * wgt for sig, wgt in zip(sig_list, weights)]
    
    # Step 4: Apply harmonic damping from earlier parameter
    damped_contributions = []
    for i, cont in enumerate(contributions):
        damping_factor = harmonic_series[i % len(harmonic_series)] / reference_amplitude
        damped_contributions.append(cont * damping_factor)
    
    # Step 5: Final integration via ceiling of mean
    raw_mean = sum(damped_contributions) / len(damped_contributions)
    import math
    final_score = math.ceil(raw_mean * 100) / 100  # Round up to nearest 0.01
    
    # Step 6: Validate against decoy checksum (result ignored)
    _ = validate_checksum(damped_contributions)  # Side effect only
    
    return final_score

# Generate actual inputs for the real computation
cycle_data = [[x % 10 + y % 7 for x in range(y, y+5)] for y in range(4, 12, 2)]
threshold_map = build_threshold_map('high')

# Execute main diagnostic
final_diagnostic = aggregate_metrics(cycle_data, threshold_map)

# Print final result as required
print(f"Result: {final_diagnostic}")