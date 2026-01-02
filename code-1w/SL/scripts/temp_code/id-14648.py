from collections import defaultdict, Counter
import math

# Simulated sensor data processing with noise filtering and pattern analysis
def acquire_signal():
    raw_samples = [i * 0.5 for i in range(80) if i % 2 == 0]
    noise_floor = [math.sin(x / 3) for x in raw_samples]
    return [s + n for s, n in zip(raw_samples, noise_floor)]

def filter_outliers(data, limit=50):
    # Irrelevant filtering path - never used
    return [x for x in data if x < limit]

def rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values) - window + 1):
        smoothed.append(sum(values[i:i+window]) / window)
    return smoothed

def extract_features(dataset):
    feature_map = defaultdict(float)
    total_peaks = 0
    for val in dataset:
        if val > 15 and val < 25:
            total_peaks += 1
    feature_map['peak_count'] = total_peaks

    # Distractor computation - looks important but unused
    squared_sums = sum(x ** 2 for x in dataset if x > 10)
    temp_normalization = math.sqrt(squared_sums) if squared_sums else 1
    
    # Real feature
    feature_map['avg'] = sum(dataset) / len(dataset)
    return feature_map

def generate_combinations(n):
    # Dead recursive function - no impact on result
    if n <= 1:
        return 1
    return n * generate_combinations(n - 1)

def transform_sequence(seq):
    # Bit manipulation red herring
    masked_values = [int(x) & 0xFF for x in seq if x > 0]
    shifted = [v << 1 for v in masked_values]
    
    # Actual transformation
    adjusted = [round(x * 1.5, 2) for x in seq]
    reversed_chunk = adjusted[::-1][:len(adjusted)//2]
    return adjusted + reversed_chunk

def analyze_pattern(data, cutoff):
    stats = Counter()
    segment_a = data[:len(data)//2]
    segment_b = data[len(data)//2:]
    
    # Meaningful logic
    avg_a = sum(segment_a) / len(segment_a)
    avg_b = sum(segment_b) / len(segment_b)
    
    trend_score = (avg_b - avg_a) * 1.75
    
    # Decoy logic with string operations
    status_flags = ['normal', 'caution', 'alert']
    flag_summary = ''.join(status_flags).upper().replace('A', 'X')
    
    # Critical decision
    if trend_score > cutoff:
        return int(trend_score * 2)
    else:
        return int(trend_score // 1.5)

# Orchestration pipeline
if __name__ == '__main__':
    signal_data = acquire_signal()  # Base physical measurement
    
    # Apply smoothing - relevant
    processed = rolling_average(signal_data, 4)
    
    # Extract metadata - partially irrelevant
    features = extract_features(processed)
    
    # Generate decoy combinatorics
    dummy_perms = generate_combinations(7)  # Unused
    
    # Transform for pattern engine
    transformed_data = transform_sequence(processed)
    
    # Phantom set operation
    unique_caps = set('Result'.upper()) & set('Target'.lower())
    
    # Threshold calibrated from domain knowledge
    threshold = features['avg'] * 0.3
    
    # Key execution point
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output requirement
    print(f"Target result: {final_diagnostic}")