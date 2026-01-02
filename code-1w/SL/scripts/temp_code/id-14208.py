import itertools

# Sensor simulation and analysis system for environmental monitoring
base_offsets = [0.1, -0.2, 0.3, -0.4]
raw_readings = [127, 255, 64, 192, 32]

def apply_calibration(values, offset_sequence):
    """Apply non-linear calibration to sensor values."""
    calibrated = []
    for i, val in enumerate(values):
        # Complex but irrelevant transformation chain
        temp_a = val ^ 0xFF  # Invert bits for some readings
        temp_b = (temp_a + i * 17) % 256
        if i % 2 == 0:
            temp_b = int(temp_b * 0.9)
        calibrated.append(temp_b + offset_sequence[i % len(offset_sequence)] if i < len(offset_sequence) else temp_b)
    return calibrated

def generate_combinations(data):
    """Generate all possible pairs (distractor function - not used in final path)"""
    return list(itertools.combinations(data, 2))

def filter_anomalies(dataset):
    """Remove extreme outliers using moving threshold (partially relevant)"""
    cleaned = []
    threshold = sum(dataset) / len(dataset) * 1.1
    for x in dataset:
        if x < threshold and x > 50:  # Only keep mid-to-high range valid signals
            cleaned.append(x)
    return cleaned

def transform_coordinates(x):
    """Irrelevant geospatial mapping (dead code path)"""
    lat = (x / 256.0) * 180 - 90
    lon = ((x % 128) / 128.0) * 360 - 180
    return lat, lon

def rolling_window_avg(seq, window_size=3):
    """Compute rolling average with fixed window (unused distractor)"""
    if len(seq) < window_size:
        return seq
    averages = []
    for i in range(len(seq) - window_size + 1):
        averages.append(sum(seq[i:i+window_size]) / window_size)
    return averages

def compute_entropy(data):
    """Calculate Shannon entropy of signal distribution (red herring)"""
    from math import log2
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def phase_shift_correction(arr):
    """Apply FFT-like shift (irrelevant to final result)"""
    n = len(arr)
    shifted = [0] * n
    for i in range(n):
        shifted[(i + n//2) % n] = arr[i]
    return shifted

def preprocess_signal(raw):
    """Main preprocessing pipeline"""
    step1 = [x & 0x7F for x in raw]  # Mask highest bit
    step2 = [x for x in step1 if x % 2 == 1]  # Keep only odd values
    enhanced = list(map(lambda y: y * 1.25, step2))  # Amplify remaining
    return enhanced

def integrate_signals(signals):
    """Accumulate weighted signal strength"""
    weights = [0.8, 1.0, 1.2, 1.4][:len(signals)]
    integral = 0.0
    for i, s in enumerate(signals):
        integral += s * weights[i % len(weights)]
    return integral

def analyze_readings(clean_signals):
    """Final diagnostic analyzer"""
    # Key processing steps
    base_sum = sum(int(x) for x in clean_signals)
    checksum = 0
    for i, val in enumerate(clean_signals):
        if i % 2 == 0:
            checksum ^= int(val)  # XOR every other value
        else:
            checksum += int(val) // 3
    
    # Final composite metric
    metric_a = base_sum * 0.7
    metric_b = checksum * 2.3
    final_score = metric_a + metric_b
    
    # Decoy intermediate calculations
    avg_val = sum(clean_signals) / len(clean_signals) if clean_signals else 0
    peak = max(clean_signals) if clean_signals else 0
    entropy_val = compute_entropy([int(x) for x in clean_signals])
    
    # The real answer is embedded here
    return int(round(final_score))

# Irrelevant setup
all_pairs = generate_combinations(raw_readings)
geo_refs = [transform_coordinates(x) for x in raw_readings[:3]]
window_avgs = rolling_window_avg(raw_readings, 2)

# Main execution flow
adjusted_readings = apply_calibration(raw_readings, base_offsets)
filtered_signals = filter_anomalies(adjusted_readings)
processed_signals = preprocess_signal(filtered_signals)
signal_integral = integrate_signals(processed_signals)
final_diagnostic = analyze_readings(processed_signals)

# Spurious entropy calculation (distraction)
_ = compute_entropy([int(x) for x in processed_signals])

# Critical output
print(f"Result: {final_diagnostic}")