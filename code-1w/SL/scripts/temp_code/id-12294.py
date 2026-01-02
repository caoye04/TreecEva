import itertools

# Sensor simulation and diagnostic analysis system
def generate_raw_signal(baseline, noise_factor, length):
    return [baseline + ((i % 7) - 3) * noise_factor for i in range(length)]

# Irrelevant helper - distractor
def smooth_data(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append(sum(signal[i-1:i+2]) / 3)
    smoothed.append(signal[-1])
    return smoothed

# Data windowing - partially relevant but overcomplicated
def create_windows(data, size=4):
    windows = []
    for i in range(len(data) - size + 1):
        windows.append(data[i:i+size])
    return windows

# Core transformation pipeline
def preprocess_signal(raw):
    # Normalize by mean
    mean_val = sum(raw) / len(raw)
    normalized = [x - mean_val for x in raw]
    
    # Apply artificial gain (red herring)
    amplified = [x * 1.7 for x in normalized]  # Not actually used
    
    # Actual relevant processing path
    filtered = [x for x in normalized if abs(x) > 0.5]  # Threshold filter
    return filtered

# Advanced pattern detection using itertools
def detect_anomalies(readings):
    if len(readings) < 3:
        return 0
    
    # Use itertools to find increasing triplets (real logic)
    count = 0
    for triplet in itertools.combinations(readings, 3):
        if triplet[0] < triplet[1] < triplet[2]:
            count += 1
    
    # Decoy computation with no effect
    decoy_sum = sum([x**2 for x in readings if x < 0]) * 0.1
    
    return count

# Secondary analysis - looks important but unused
def compute_entropy(data):
    from math import log
    if not data:
        return 0.0
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 3)

# Main diagnostic engine
def analyze_readings(cleaned):
    # Real computation: count values above threshold
    critical_count = len([x for x in cleaned if x > 1.0])
    
    # Complex-looking but irrelevant block
    if len(cleaned) > 5:
        windowed = create_windows(cleaned, 3)
        long_pattern = 0
        for win in windowed:
            if all(w > 0 for w in win):
                long_pattern += 1
        # This value is never used
    
    # Another red herring: sorting and median calculation
    sorted_vals = sorted(cleaned)
    median_offset = 0
    if sorted_vals:
        mid = len(sorted_vals) // 2
        median_offset = abs(sorted_vals[mid])
    
    # Key actual logic: combine anomaly count and critical readings
    anomaly_score = detect_anomalies(cleaned)
    base_diagnostic = critical_count * 100
    final_diagnostic = base_diagnostic + anomaly_score  # Final answer depends on this
    
    # Dead code path - unreachable
    if False:
        backup = sum(cleaned) / len(cleaned)
        final_diagnostic = int(backup * 10)
    
    return final_diagnostic

# Simulate sensor array readings
raw_sensor_data = generate_raw_signal(baseline=25.4, noise_factor=1.8, length=12)

# Process through pipeline
processed_signals = preprocess_signal(raw_sensor_data)

# Perform diagnostic analysis
final_diagnostic = analyze_readings(processed_signals)

# Output result as required
print(f"Result: {final_diagnostic}")