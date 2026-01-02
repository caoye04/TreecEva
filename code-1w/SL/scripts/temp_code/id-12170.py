def analyze_signal(pattern, threshold=0.7):
    """ Analyze binary signal pattern for coherence anomalies (distraction function) """
    ones_count = sum(pattern)
    total_length = len(pattern)
    if total_length == 0:
        return 0.0
    density = ones_count / total_length
    segments = [pattern[i:i+4] for i in range(0, len(pattern), 4)]
    coherent_segments = sum(1 for s in segments if sum(s) >= 3)
    coherence_rate = coherent_segments / len(segments)
    return coherence_rate if density > threshold else 0.0


def compute_entropy(data):
    """ Compute Shannon entropy of a byte sequence (distraction function) """
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return entropy

def extract_features(sequence):
    """ Extract various statistical features from numeric sequence """
    n = len(sequence)
    mean_val = sum(sequence) / n if n > 0 else 0
    variance = sum((x - mean_val) ** 2 for x in sequence) / n if n > 0 else 0
    std_dev = __import__('math').sqrt(variance)
    max_val, min_val = max(sequence), min(sequence)
    
    # Distractor: unused advanced stats
    skewness = 0.0
    kurtosis = 0.0
    if std_dev > 0:
        skewness = sum(((x - mean_val) / std_dev) ** 3 for x in sequence) / n
        kurtosis = sum(((x - mean_val) / std_dev) ** 4 for x in sequence) / n - 3
    
    # Real feature subset
    return {
        'mean': mean_val,
        'std': std_dev,
        'range': max_val - min_val,
        'median': sorted(sequence)[n//2] if n > 0 else 0
    }

def transform_sequence(seq, key=3):
    """ Apply Caesar-style shift to sequence with wraparound """
    shifted = [(x + key) % 256 for x in seq]
    reversed_half = shifted[::-1][:len(shifted)//2]
    return shifted + reversed_half  # Augment with reverse half

def validate_checksum(buffer):
    """ Simple XOR checksum validation (distractor with partial use) """
    if len(buffer) == 0:
        return True
    checksum = 0
    for b in buffer:
        checksum ^= b
    return checksum == 0

def aggregate_metrics(timing_log, status_flags):
    """ Core metric aggregation: combines timing percentiles and flag patterns """
    if not timing_log:
        return 0
    
    # Sort and extract percentiles
    sorted_times = sorted(timing_log)
    n = len(sorted_times)
    p25 = sorted_times[n//4]
    p75 = sorted_times[3*n//4]
    iqr = p75 - p25
    
    # Flag analysis
    critical_count = sum(1 for f in status_flags if f == 'CRITICAL')
    warning_count = sum(1 for f in status_flags if f == 'WARNING')
    
    # Real logic path
    base_score = p75 * 1.5
    penalty = 0
    if critical_count > 0:
        penalty += critical_count * 100
    if iqr > 50:
        penalty += 50
    if warning_count > 3:
        penalty += 20
    
    # Key intermediate (misleading)
    raw_heuristic = base_score - penalty
    
    # Final adjustment based on specific condition
    if critical_count == 0 and iqr <= 40:
        final_adjustment = 0.8
    elif warning_count == 0:
        final_adjustment = 0.9
    else:
        final_adjustment = 1.1
    
    return int((base_score - penalty) * final_adjustment)

# Simulated system telemetry data
raw_bytes = list(range(10, 25)) + [5, 12, 18, 18, 21]
decoded_stream = transform_sequence(raw_bytes, key=7)

# Distractor: signal analysis on bit pattern
bit_pattern = [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0]
signal_quality = analyze_signal(bit_pattern, threshold=0.6)

# Distractor: entropy computation
entropy_value = compute_entropy(decoded_stream)

# Feature extraction (partially used)
features = extract_features(decoded_stream)

# Timing simulation with realistic jitter
import random
random.seed(42)
timing_data = [round(__import__('math').sin(i/10)*100 + 75 + random.uniform(-5, 5), 2) for i in range(30)]

# Status flags with mixed severity
flags = ['OK', 'OK', 'WARNING', 'OK', 'CRITICAL', 'OK', 'WARNING', 'WARNING', 'OK']

# Dead code path (never called)
unused_buffer = [0xAA, 0x55, 0xFF, 0x00]
valid = validate_checksum(unused_buffer)

# Slicing operation (required python feature): filter timing outliers using slice
filtered_times = sorted(timing_data)[1:-1]  # Remove min and max

# Update timing data to use filtered version
timing_data = filtered_times

# Key statement
final_diagnostic = aggregate_metrics(timing_data, flags)

print(f"Result: {final_diagnostic}")