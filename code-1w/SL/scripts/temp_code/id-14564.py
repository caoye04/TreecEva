import math

# Simulated sensor readings over time (irrelevant: some are noise)
sensor_raw = [102.3, 98.7, 105.1, 100.5, 110.2, 95.8, 103.4, 99.9, 107.6, 101.8]
noise_filter = [x for x in sensor_raw if 97 < x < 108]  # Only use plausible values

# Historical baseline (distractor data)
historical_avg = sum([99.1, 100.3, 98.9, 101.2, 97.6]) / 5

# Calibration coefficients (some are decoys)
coeff_a = 0.89
coeff_b = 1.02
coeff_c = 2.1  # unused coefficient (red herring)
decoherence_factor = lambda x: x * 0.001  # never called

# Real-time calibration data (used)
calibration_data = {
    'baseline': 100.0,
    'sensitivity': 1.05,
    'drift_compensation': -0.15,
    'window_size': 3
}

# Auxiliary monitoring (dead code path)
def monitor_stability(data):
    return all(abs(data[i] - data[i+1]) < 2.0 for i in range(len(data)-1))

# Secondary validation (unused function)
def validate_redundancy(checksums):
    return sorted(checksums)[-1] if checksums else 0

# Core processing pipeline
def preprocess_stream(raw, window=3):
    """Apply moving average filter."""
    smoothed = []
    for i in range(len(raw) - window + 1):
        window_avg = sum(raw[i:i+window]) / window
        smoothed.append(round(window_avg, 2))
    return smoothed

# Irrelevant transformation (string manipulation distractor)
status_flags = ['OK', 'STABLE', 'CALIBRATED', 'ACTIVE']
flag_summary = ''.join([f[0] for f in status_flags]).lower()  # yields 'osca'

# Noise-filtered and smoothed signal
filtered_readings = preprocess_stream(noise_filter)

# Simulated packet metadata (decoy structure)
packet_log = [
    {'id': 'A7', 'size': 512, 'ts': 1678881234},
    {'id': 'B2', 'size': 256, 'ts': 1678881235},
    {'id': 'C9', 'size': 1024, 'ts': 1678881236}
]

# Critical calculation engine
def calculate_optimal_flow(readings, config):
    base = config['baseline']
    sensitivity = config['sensitivity']
    drift = config['drift_compensation']
    
    # Apply sensitivity correction and drift compensation
    adjusted = [base + (r - base) * sensitivity + drift for r in readings]
    
    # Identify peak deviation (distraction logic)
    deviations = [abs(a - base) for a in adjusted]
    max_deviation_index = deviations.index(max(deviations))
    
    # Dummy sort (misleading operation)
    sorted_adjusted = sorted(adjusted, reverse=True)
    
    # Key logic: harmonic mean of top 3 adjusted values
    top_three = sorted_adjusted[:3]
    harmonic_mean = len(top_three) / sum(1/v for v in top_three)
    
    # Final adjustment using trigonometric weighting (arcane but deterministic)
    angle_weight = math.cos(math.pi / len(top_three))
    final_rate = harmonic_mean * angle_weight
    
    # Dead comparison (never used)
    is_optimal = final_rate > 102.0
    
    return final_rate

# Execute core logic
sensor_readings = filtered_readings  # Aligned with preprocessing
optimized_flow_rate = calculate_optimal_flow(sensor_readings, calibration_data)

# Print result as required
print(f"Result: {optimized_flow_rate}")