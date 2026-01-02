from collections import defaultdict
import math

# Simulated sensor data processing with red herrings and complex logic

def preprocess_segment(data_slice, mode='legacy'):
    if mode == 'legacy':
        return [x * 1.05 for x in data_slice]
    else:
        return [x * 0.98 for x in data_slice]


def generate_checksum(sequence):
    # Irrelevant function - not used in main logic
    chk = 0
    for val in sequence:
        chk ^= int(val) & 255
    return chk


def normalize_stream(raw_values):
    mean_val = sum(raw_values) / len(raw_values)
    std_dev = (sum((x - mean_val) ** 2 for x in raw_values) / len(raw_values)) ** 0.5
    return [(x - mean_val) / std_dev for x in raw_values], mean_val, std_dev


def evaluate_coherence(signal, reference):
    score = 0
    for i in range(min(len(signal), len(reference))):
        if abs(signal[i] - reference[i]) < 0.1:
            score += 1
    return score / len(signal)


def extract_features(dataset):
    # Dead code path - never actually called
    features = defaultdict(int)
    for i, val in enumerate(dataset):
        if val > 0:
            features['positive_count'] += 1
        if i % 2 == 0:
            features['even_index_sum'] += val
    return features


def filter_anomalies(buffer, sensitivity=0.95):
    filtered = []
    for i in range(1, len(buffer) - 1):
        prev, curr, next_val = buffer[i-1], buffer[i], buffer[i+1]
        trend = (next_val - curr) * (curr - prev)
        if trend >= 0:
            filtered.append(curr)
    return filtered


def compute_entropy(values):
    counts = defaultdict(int)
    for v in values:
        counts[round(v, 1)] += 1
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p)
    return entropy


def analyze_signal(patterns, thresholds):
    # Core relevant logic starts here
    temp_store = []
    for key in sorted(thresholds.keys()):
        if key in patterns:
            temp_store.append(patterns[key] * thresholds[key])
    
    # Apply slicing to focus on central segment
    mid_point = len(temp_store) // 2
    analysis_window = temp_store[mid_point-1:mid_point+2]  # 3-element slice

    # Bit manipulation decoy
    magic_flag = 0b1010
    for val in analysis_window:
        magic_flag ^= int(val) & 0b1111
    
    # Conditional branching with misleading path
    if magic_flag > 10:
        adjustment = 0.75
    else:
        adjustment = 1.25  # This branch is always taken

    # Actual answer computation
    base_value = sum(analysis_window) * adjustment
    
    # Decoy operations
    dummy_calc = base_value
    for _ in range(3):
        dummy_calc = (dummy_calc * 1.01) % 1000
    
    final_score = int(round(base_value))
    
    # Critical assignment
    final_diagnostic = final_score ^ 0xABCD  # XOR with fixed pattern
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Initialize sensor buffers (mix of relevant and irrelevant data)
    raw_input = [2.1, 3.4, 1.8, 4.2, 5.1, 3.9, 2.7, 4.6]
    processed, m, s = normalize_stream(raw_input)
    legacy_processed = preprocess_segment(raw_input, mode='legacy')
    enhanced_processed = preprocess_segment(raw_input, mode='quantum')

    # Construct pattern buffer (only this part matters)
    pattern_buffer = {
        'p1': 15,
        'p3': 8,
        'p2': 12,
        'p5': 20
    }

    # Threshold map - critical input
    threshold_map = {
        'p1': 2.0,
        'p2': 1.5,
        'p3': 3.0,
        'p4': 0.8
    }

    # Filtering anomaly (red herring)
    cleaned = filter_anomalies(legacy_processed)
    entropy_metric = compute_entropy(cleaned)

    # Evaluate coherence with fake reference (unused)
    ref_pattern = [1.0, 1.0, 1.0]
    coherence = evaluate_coherence(cleaned[:3], ref_pattern)

    # Key computation
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")