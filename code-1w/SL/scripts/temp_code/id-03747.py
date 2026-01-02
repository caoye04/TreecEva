from collections import defaultdict, Counter
from itertools import zip_longest, cycle
import math

def analyze_frequency(pattern):
    # Distractor: unused function (red herring)
    freq = defaultdict(int)
    for p in pattern:
        freq[p] += 1
    return freq

def generate_checksum(seq):
    # Another red herring - looks important but not used in final result
    checksum = 0
    for i, val in enumerate(seq):
        checksum += val * (i + 1)
    return checksum % 1000

def decode_sequence(signal):
    # Irrelevant transformation
    decoded = []
    for s in signal:
        if s % 3 == 0:
            decoded.append(s // 3)
        elif s % 2 == 0:
            decoded.append(s // 2)
        else:
            decoded.append(s)
    return decoded

def evaluate_threshold(values, limit=50):
    # Dead code path - never actually used
    count = 0
    for v in values:
        if v > limit:
            count += 1
    return count > len(values) // 2

def compute_entropy(data):
    # Misleading scientific computation
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [d / total for d in data if d > 0]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return round(entropy, 6)

def filter_anomalies(dataset):
    mean_val = sum(dataset) / len(dataset)
    std_dev = (sum((x - mean_val) ** 2 for x in dataset) / len(dataset)) ** 0.5
    lower, upper = mean_val - 2*std_dev, mean_val + 2*std_dev
    # This filtering does nothing because we don't use cleaned_data elsewhere
    cleaned_data = [x for x in dataset if lower <= x <= upper]
    return cleaned_data

def extract_features(temporal_data):
    features = []
    window_size = 3
    for i in range(len(temporal_data) - window_size + 1):
        window = temporal_data[i:i+window_size]
        avg = sum(window) / len(window)
        trend = window[-1] - window[0]
        features.append(avg + trend)
    return features

def build_lookup(keys, values):
    # Unused mapping construction (decoy)
    lookup = {}
    for k, v in zip(keys, values):
        lookup[k] = v * 2
    return lookup

def process_pipeline(input_stream):
    # Core relevant logic begins here
    stage1 = [x * 2 for x in input_stream if x % 2 == 1]  # Double odd numbers
    
    temp_buffer = []
    for idx, val in enumerate(stage1):
        if idx % 2 == 0:
            temp_buffer.append(val + 5)
        else:
            temp_buffer.append(val - 3)
    
    # Simulate interleaving with dummy data (some distraction)
    padded = list(zip_longest(temp_buffer, [100, 200, 300], fillvalue=0))
    flattened = [item for pair in padded for item in pair]
    
    # Actual critical transformation
    accumulated = 0
    for num in flattened:
        if num > 50:
            accumulated += num // 4
        elif num > 20:
            accumulated += num // 5
        else:
            accumulated += num
    
    # Secondary real operation: count how many original odds were > 15 after doubling
    count_qualifying = sum(1 for x in stage1 if x > 15)
    
    # Real answer depends on both accumulated and count_qualifying
    intermediate = accumulated * 3
    correction = abs(intermediate - count_qualifying * 10)
    final_output = int(intermediate - correction)  # Final deterministic result
    
    # These variables look important but are irrelevant
    dummy_stats = {
        'peak': max(flattened),
        'length': len(flattened),
        'anomaly_ratio': 0.05
    }
    
    return final_output

# Main execution block
if __name__ == '__main__':
    raw_signal = [7, 8, 12, 9, 11, 14, 6, 13]
    metadata_log = ['init', 'start', 'run']
    timestamp_sequence = [1623, 1624, 1625]
    
    # Distractor: multiple unused preprocessing steps
    filtered_raw = [x for x in raw_signal if x < 15]
    extended_data = list(zip_longest(raw_signal, timestamp_sequence, fillvalue=1))
    repeated_cycle = list(cycle([0]))[:0]  # Empty, meaningless
    
    processed_features = extract_features(filtered_raw)
    potential_keys = ['a', 'b', 'c']
    fake_lookup = build_lookup(potential_keys, filtered_raw)
    
    # Actual input to pipeline
    data_stream = [x + 2 for x in filtered_raw]  # [9, 11, 13] from odds and evens <15
    
    # Key statement
    final_output = process_pipeline(data_stream)
    
    # Print result as required
    print(f"Target result: {final_output}")