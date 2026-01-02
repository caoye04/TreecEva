def analyze_signal(samples, window_size=4):
    smoothed = []
    for i in range(len(samples) - window_size + 1):
        segment = samples[i:i+window_size]
        avg = sum(segment) / window_size
        smoothed.append(avg)
    return [round(x, 2) for x in smoothed]


def extract_features(data_stream):
    features = {}
    magnitude = sum(abs(x) for x in data_stream)
    peaks = [i for i, x in enumerate(data_stream) if x > 0.5 * max(data_stream)]
    energy = sum(x**2 for x in data_stream)
    features['magnitude'] = round(magnitude, 3)
    features['peak_count'] = len(peaks)
    features['energy'] = round(energy, 3)
    features['entropy'] = 0.0  # placeholder, not used
    return features


def validate_checksum(sequence):
    # Irrelevant validation function (dead-end logic)
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 100) % 256
    return checksum == 127


def transform_coordinates(x_vals, y_vals):
    # Distractor: unused coordinate mapping
    coords = list(zip(x_vals, y_vals))
    rotated = [(y * 0.7, x * 1.3) for x, y in coords]
    return rotated


def compute_histogram(data, bins=5):
    # Red herring: computes distribution but not used in final result
    min_val, max_val = min(data), max(data)
    bin_width = (max_val - min_val) / bins
    histogram = [0] * bins
    for val in data:
        idx = min(int((val - min_val) / bin_width), bins - 1)
        histogram[idx] += 1
    return histogram


def process_metrics(diagnostics, thresholds):
    base_score = 0
    adjustment = 0
    
    for i, (key, value) in enumerate(diagnostics.items()):
        if key == 'magnitude' and value > thresholds['mag_th']:
            base_score += 15
        elif key == 'energy' and value < thresholds['eng_th']:
            adjustment -= 5
        elif key == 'peak_count':
            base_score += value * 2
    
    # Complex conditional with nested bit manipulation (relevant path)
    if base_score > 20:
        temp = base_score ^ 255  # Bit flip lower byte
        temp = (temp << 2) & 1023  # Shift and mask
        adjustment += (temp >> 4)
    
    # Dead branch: never taken due to fixed condition
    emergency_override = False
    if validate_checksum([1.1, 2.2, 3.3]):
        emergency_override = True  # This block is unreachable logically
    
    final_score = base_score + adjustment
    
    # Final transformation using case conversion simulation and summation
    tag = "DIAGNOSTIC"
    shift_factor = sum(ord(c.lower()) - ord('a') for c in tag) % 7  # sum of letter positions
    final_diagnostic = final_score * 3 + shift_factor
    
    return final_diagnostic

# Main execution flow
raw_samples = [0.1, 0.8, 0.3, 0.9, 0.2, 0.7, 0.4]
smoothed_signal = analyze_signal(raw_samples)
features = extract_features(smoothed_signal)

# Unused computations - distractors
x_axis = [1, 2, 3, 4]
y_axis = [0.5, 0.6, 0.4, 0.8]
transformed_coords = transform_coordinates(x_axis, y_axis)
hist = compute_histogram(smoothed_signal, bins=6)

# Thresholds for decision logic
thresholds = {
    'mag_th': 1.5,
    'eng_th': 1.0
}

# Critical execution point
final_diagnostic = process_metrics(features, thresholds)
print(f"Result: {final_diagnostic}")