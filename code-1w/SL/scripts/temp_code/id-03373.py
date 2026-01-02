import math

# Simulated sensor data processing system with diagnostic logic
def collect_samples(base_freq, duration, noise_level=0.1):
    samples = []
    for t in range(1, duration + 1):
        signal = math.sin(base_freq * t) + noise_level * math.cos(7 * t)
        samples.append(round(signal * 1000) / 1000)
    return samples

# Irrelevant helper: used to mislead with frequency analysis
def compute_harmonic_series(n):
    return sum(1 / i for i in range(1, n + 1))

# Distractor function: looks important but unused in critical path
def generate_checksum(data_list):
    checksum = 0
    for val in data_list:
        checksum ^= int(abs(val) * 100) % 256
    return checksum

# Signal filtering - only some outputs are actually used
def filter_anomalies(raw_data, sensitivity):
    cleaned = []
    anomalies = []
    threshold = sensitivity * 1.8
    for x in raw_data:
        if abs(x) > threshold:
            anomalies.append(x)
        else:
            cleaned.append(x)
    # Dead code branch - never accessed in execution path
    if len(anomalies) > 100:
        fallback = [x for x in raw_data if x > 0]
        return sorted(fallback)
    return cleaned

# Core transformation: applies envelope detection
def apply_envelope(signal):
    envelope = []
    for i in range(len(signal)):
        prev = signal[i-1] if i > 0 else 0
        curr = signal[i]
        next_val = signal[i+1] if i < len(signal)-1 else 0
        env_val = max(abs(prev), abs(curr), abs(next_val))
        envelope.append(round(env_val, 3))
    return envelope

# Diagnostic engine - processes logs into metrics
pattern_log = set()
def register_pattern(code, desc, score_factor):
    pattern_log.add((code, desc))
    # Side effect ignored; score_factor not used
    return len(desc) % 4

# Misleading accumulation (looks like scoring but isn't)
cumulative_bias = 0
for i in range(3):
    cumulative_bias += (-1)**i * (i + 1) * 17

# Generate primary data stream
raw_readings = collect_samples(base_freq=0.45, duration=12)
filtered_readings = filter_anomalies(raw_readings, sensitivity=0.6)
enveloped = apply_envelope(filtered_readings)

# Simulate historical comparison set (unused red herring)
historical_peak = max(collect_samples(0.33, 8, 0.15))
baseline_offset = math.log(historical_peak + 10, 2)

# Extract features from enveloped signal
feature_vector = []
for v in enveloped:
    if v > 0.5:
        feature_vector.append(int(v * 10))
    elif v < 0.2:
        feature_vector.append(-1)
    else:
        feature_vector.append(0)

# Register multiple patterns including decoys
register_pattern('SIG-9', 'attenuated carrier', 0.8)
register_pattern('CLK-12', 'clock drift detected', 1.1)
register_pattern('ENV-5', 'envelope symmetry breach', 0.9)
register_pattern('CAL-0', 'calibration stable', 1.0)

# Threshold bank with irrelevant entries
thresholds = {
    'alpha': 0.45,
    'beta': 0.71,
    'gamma': 0.33,
    'delta': 0.88,  # unused
    'epsilon': 0.21  # unused
}

# Critical diagnostic analyzer
# This function contains the actual answer computation
def analyze_signal(log_set, limits):
    size_impact = len(log_set) * 10
    
    # Compute ratio-based metric from feature vector (defined in outer scope)
    above_threshold = sum(1 for x in feature_vector if x > 2)
    below_noise = sum(1 for x in feature_vector if x == -1)
    total_valid = len([x for x in feature_vector if x != 0])
    
    if total_valid == 0:
        density_ratio = 0
    else:
        density_ratio = above_threshold / total_valid
    
    # Use only alpha and gamma thresholds
    sensitivity_score = (limits['alpha'] + limits['gamma']) * 100
    
    # Incorporate set cardinality and computed ratio
    intermediate = size_impact + int(density_ratio * 100)
    
    # Final computation
    result = intermediate * int(sensitivity_score)
    
    # Decoy mutation - doesn't affect outer scope
    log_set.add(('TMP-99', 'transient spike'))
    
    return result

# Execute critical statement
final_diagnostic = analyze_signal(pattern_log, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")