from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with diagnostic analysis
def preprocess_sensor_readings(raw_samples):
    filtered = [x for x in raw_samples if -50 <= x <= 50]
    normalized = [round(x / max(filtered), 6) for x in filtered]
    return normalized

# Irrelevant helper - dead code path (distractor)
def legacy_calibrate(signal):
    return [s * 0.98 for s in signal]

# Key transformation: frequency compression via logarithmic scaling
def compress_frequency_domain(signal):
    compressed = []
    for s in signal:
        if s > 0:
            compressed.append(math.log(s) * 100)
        elif s < 0:
            compressed.append(-math.log(abs(s)) * 100)
        else:
            compressed.append(0)
    return [round(c, 4) for c in compressed]

# Misleading intermediate analysis (distractor)
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = -sum((freq / total) * math.log2(freq / total) for freq in counts.values())
    return round(entropy, 4)

# Threshold classification system based on dynamic baselines
def generate_threshold_map(signal_part):
    avg = sum(signal_part) / len(signal_part)
    std_dev = (sum((x - avg) ** 2 for x in signal_part) / len(signal_part)) ** 0.5
    return {
        'low': avg - 1.5 * std_dev,
        'medium': avg,
        'high': avg + 2.0 * std_dev
    }

# Decoy function: looks important but unused (distractor)
def validate_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= int(val * 100) % 255
    return checksum == 42

# Core diagnostic logic with set operations and lambda filtering
def analyze_signal(compressed_data, threshold_map):
    above_high = set(filter(lambda x: x > threshold_map['high'], compressed_data))
    below_low = set(filter(lambda x: x < threshold_map['low'], compressed_data))
    normal_range = set(compressed_data) - above_high - below_low
    
    # Compute weighted anomaly score
    high_penalty = sum(map(lambda x: (x - threshold_map['high']) * 1.5, above_high))
    low_penalty = sum(map(lambda x: (threshold_map['low'] - x) * 1.2, below_low))
    
    base_score = len(above_high) * 10 + len(below_low) * 8
    adjustment = round(high_penalty + low_penalty, 4)
    
    # Complex conditional scoring
    if len(above_high) > len(below_low) and adjustment > 50:
        base_score += 25
    elif len(below_low) > len(above_high):
        base_score += 15
    
    # Final adjustment using modular arithmetic
    if len(normal_range) % 7 == 0:
        adjustment = abs(adjustment) % 37
    else:
        adjustment = abs(adjustment) % 29
    
    final_score = base_score + adjustment
    
    # Red herring: unused complex structure (distractor)
    diagnostics_log = defaultdict(dict)
    diagnostics_log['anomalies']['spikes'] = list(above_high)
    diagnostics_log['anomalies']['drops'] = list(below_low)
    diagnostics_log['metrics']['entropy'] = compute_entropy(compressed_data)
    diagnostics_log['status'] = 'CALIBRATED' if len(compressed_data) % 5 == 0 else 'STANDBY'
    
    return int(final_score)

# Entry point with extensive irrelevant setup
if __name__ == '__main__':
    raw_sensor_stream = [
        3.45, -2.1, 8.99, 0.0, 12.5, -7.3, 4.2, 9.8, -1.05, 6.7,
        15.2, -4.8, 2.9, 11.1, -6.4, 5.3, 13.7, -3.2, 7.8, 10.4
    ]
    
    # Process pipeline
    cleaned = preprocess_sensor_readings(raw_sensor_stream)
    processed_signal = compress_frequency_domain(cleaned)
    
    # Unused transformations (distractors)
    sorted_forward = sorted(processed_signal)
    sorted_reverse = sorted(processed_signal, reverse=True)
    median_val = sorted_forward[len(sorted_forward) // 2]
    
    # Actual used components
    threshold_map = generate_threshold_map(processed_signal[:15])
    final_diagnostic = analyze_signal(processed_signal, threshold_map)
    
    # Print required result
    print(f"Result: {final_diagnostic}")