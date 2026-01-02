import math

# Simulated sensor fusion system for environmental monitoring
def preprocess_input(raw_readings):
    filtered = [x for x in raw_readings if 0 <= x <= 100]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    return [abs(x - baseline) for x in filtered]


def generate_phase_vector(n):
    return [math.sin(i * math.pi / 4) for i in range(n)]


def merge_signals(primary, secondary):
    # Irrelevant padding
    pad_len = max(len(primary), len(secondary))
    extended_primary = primary + [0] * (pad_len - len(primary))
    extended_secondary = secondary + [0] * (pad_len - len(secondary))
    return [a * b for a, b in zip(extended_primary, extended_secondary)]


def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 3)


def shift_cipher(text, shift):
    # Distractor function - not related to main logic
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def detect_anomalies(values, limit):
    anomalies = []
    for i, v in enumerate(values):
        if v > limit:
            anomalies.append(i)
    return set(anomalies)  # Use of set operation


def compute_checksum(sequence):
    # Decoy computation
    checksum = 0
    for i, val in enumerate(sequence):
        checksum += val * (i + 1)
    return checksum % 1000


def temporal_filter(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed


def evaluate_stability(profile):
    diffs = [abs(profile[i] - profile[i-1]) for i in range(1, len(profile))]
    return all(d < 5 for d in diffs)


def analyze_signal(data_stream, criteria):
    # Core logic begins
    stage1 = preprocess_input(data_stream)
    phase_mod = generate_phase_vector(len(stage1))
    mixed = merge_signals(stage1, phase_mod)
    
    # Key transformation
    processed = temporal_filter(mixed)
    
    # Threshold filtering based on input criteria
    thresholded = [x for x in processed if x >= criteria[0]]
    
    # Red herring: unused branching
    if len(thresholded) > 10:
        summary_stats = {
            'peak': max(thresholded),
            'avg': sum(thresholded) / len(thresholded),
            'size': len(thresholded)
        }
        # This block is never executed due to data size
        encrypted_report = shift_cipher(str(summary_stats), 7)
    
    # Actual critical path
    entropy_score = calculate_entropy([round(x, 1) for x in thresholded])
    anomaly_set = detect_anomalies(thresholded, criteria[1])
    stability = evaluate_stability(thresholded)
    
    # Final diagnostic calculation
    base_value = sum(thresholded) * entropy_score
    if stability:
        base_value *= 1.25
    if len(anomaly_set) == 0:
        base_value += 23.7
    
    final_diagnostic = int(round(base_value))
    
    # Dead code - irrelevant output
    debug_log = f"Anomalies found: {len(anomaly_set)}"
    log_entry = {'type': 'DIAGNOSTIC', 'value': final_diagnostic}
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data
    sensor_readings = [88, 12, 45, 67, 23, 78, 34, 89, 14, 67, 23, 77, 31, 84]
    config_thresholds = [0.5, 1.0]  # activation and anomaly thresholds
    
    # Irrelevant precomputations
    normalized = [x / 100 for x in sensor_readings]
    squared_errors = [(x - 50)**2 for x in sensor_readings]
    feature_hash = sum(x * (i+1) for i, x in enumerate(sensor_readings)) % 500
    
    # Unused data structures
    history_buffer = [{'timestamp': t, 'val': v} for t, v in enumerate(sensor_readings[:5])]
    lookup_table = {i: math.cos(i * 0.1) for i in range(20)}
    
    # Trigger key computation
    final_diagnostic = analyze_signal(sensor_readings, config_thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")