import math

# Simulated sensor array diagnostics with mixed computational paradigms
def collect_readings():
    raw_signals = [127, 255, 192, 64, 224, 31, 88, 176]
    noise_floor = 15
    adjusted = [(x ^ 42) + noise_floor for x in raw_signals]  # Bit manipulation red herring
    return adjusted

# Irrelevant signal smoothing (dead path)
def smooth_signal(data):
    smoothed = []
    for i in range(len(data)):
        window = data[max(0, i-1):min(len(data), i+2)]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Unused checksum validator
def validate_checksum(arr):
    checksum = 0
    for val in arr:
        checksum = (checksum + val) % 256
    return checksum == 0

# Core transformation with meaningful logic buried in distractions
def transform_readings(readings):
    transformed = []
    base_offset = 10
    scale_factor = 0.75

    # Distractor: unused frequency analysis
    frequencies = {}
    for r in readings:
        freq_key = r % 16
        frequencies[freq_key] = frequencies.get(freq_key, 0) + 1

    # Actual transformation
    for idx, val in enumerate(readings):
        if idx % 2 == 0:
            transformed.append(int((val - base_offset) * scale_factor))
        else:
            transformed.append(int((val + base_offset) * (scale_factor + 0.1)))
    return transformed

# Misleading diagnostic flag generator (partially used)
def generate_flags(data):
    flags = []
    for d in data:
        if d > 200:
            flags.append('CRITICAL')
        elif d > 150:
            flags.append('ELEVATED')
        else:
            flags.append('NORMAL')
    return flags  # Not used in final result

# Real processing chain
threshold_map = {
    'low': 85,
    'high': 180,
    'critical': 210
}

# Decoy aggregation function
def aggregate_patterns(seq):
    pattern_count = 0
    for a, b in zip(seq, seq[1:]):
        if (a + b) % 2 == 1:
            pattern_count += 1
    return pattern_count

# Main analyzer - key logic hidden among distractors
def analyze_metrics(data, thresholds):
    score = 0
    
    # Irrelevant enumeration with side computation
    indices = []
    for i, x in enumerate(data):
        if x > thresholds['low']:
            indices.append(i)
    
    # Real scoring logic
    for i, reading in enumerate(data):
        if reading > thresholds['critical']:
            score += reading // (i + 1)
        elif reading > thresholds['high']:
            score -= reading % 17
        else:
            score += int(math.sin(math.pi * i / 4) * 10)
    
    # Dead branch with misleading output
    if score > 100:
        anomaly_ref = sum([i*r for i, r in enumerate(data) if r < 100])
        # This is never accessed downstream
    
    return score

# --- Execution Sequence ---
raw_data = collect_readings()
processed_data = transform_readings(raw_data)

# Unused intermediate results (distractors)
diag_flags = generate_flags(processed_data)
smoothed_raw = smooth_signal(raw_data)
pattern_metric = aggregate_patterns(processed_data)

# Key statement
final_diagnostic = analyze_metrics(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")