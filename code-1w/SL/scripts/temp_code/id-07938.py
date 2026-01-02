def preprocess_sensor(x):
    return (x * 1.8) + 32


def filter_noise(values):
    smoothed = []
    for i in range(1, len(values) - 1):
        avg = (values[i-1] + values[i] + values[i+1]) / 3
        smoothed.append(avg)
    return smoothed


def generate_synthetic_data(n):
    # Irrelevant function - decoy
    return [i**2 for i in range(n)]


def calculate_entropy(arr):
    # Misleading computation - not used in final result
    from math import log
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    total = len(arr)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)


def extract_features(data):
    features = []
    for idx, val in enumerate(data):
        if idx % 2 == 0:
            features.append(val * 2)
    return features


def shift_window(sequence, window_size=3):
    # Dead code path - never invoked in main logic
    result = []
    for i in range(len(sequence) - window_size + 1):
        result.append(sum(sequence[i:i+window_size]))
    return result


def validate_calibration(signal):
    # Distractor: performs checks but doesn't affect outcome
    threshold = 50
    status = True
    for s in signal:
        if abs(s) > threshold:
            status = False
    return status


def accumulate_segments(bands):
    # Relevant transformation
    cumulative = [0]
    for b in bands:
        cumulative.append(cumulative[-1] + b % 7)
    return cumulative


def analyze_readings(peaks):
    score = 0
    for i, p in enumerate(peaks):
        if i % 3 == 0:
            score += p
        elif p > 0:
            score += p // 2
        else:
            score -= p // 4
    return score * 2

# Main execution with high interference
raw_readings = [-5, 12, 8, -3, 20, 15, -10, 7]

# Irrelevant preprocessing chain
converted = [preprocess_sensor(x) for x in raw_readings]
synthetic = generate_synthetic_data(10)
noise_check = validate_calibration(raw_readings)

# Real signal processing begins here
filtered = filter_noise(raw_readings + [0])  # Add dummy to allow filtering

# Feature extraction with slicing distraction
segment_a = filtered[1:5]
segment_b = filtered[2:6]
merged = []
for a, b in zip(segment_a, segment_b):
    merged.append((a + b) / 2)

enhanced = extract_features(merged)

# Decoy data structure
log_entry = {
    'timestamp': '2023-01-01T00:00:00',
    'readings_count': len(raw_readings),
    'processed_length': len(enhanced),
    'system_status': 'OK'
}

# Critical relevant computation path
modulated = [x % 9 for x in enhanced if x != 0]
dilated = []
for i, val in enumerate(modulated):
    dilated.append(val * (i + 1))

accumulated_levels = accumulate_segments(dilated)
trimmed = accumulated_levels[1:]  # Remove initial zero

# Final analysis using enumerate and slicing (required features)
processed_signals = []
for index, level in enumerate(trimmed):
    if index % 2 == 0:
        processed_signals.append(level - 5)
    else:
        processed_signals.append(level + 3)

# This is the key statement
final_diagnostic = analyze_readings(processed_signals)

# Print target result
print(f"Target result: {final_diagnostic}")