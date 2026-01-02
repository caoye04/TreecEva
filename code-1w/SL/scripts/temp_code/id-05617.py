import itertools

# Simulated sensor data processing pipeline with diagnostic analysis
raw_readings = [0.8, 1.2, -0.4, 1.9, 0.1, -0.8, 2.1, -1.3]

def apply_noise_filter(data, threshold=0.5):
    # Irrelevant filtering function (not used in main path)
    return [x for x in data if abs(x) > threshold]

def generate_frequency_map(data):
    # Creates frequency buckets - partially relevant
    freq_map = {}
    for val in data:
        bucket = int(abs(val) * 2)
        freq_map[bucket] = freq_map.get(bucket, 0) + 1
    return freq_map

def compute_moving_average(data, window=3):
    # Dead code path - not used
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        averages.append(avg)
    return averages

def extract_peaks(signal, sensitivity=1.0):
    # Extracts peaks above threshold - this is critical
    peak_threshold = max(signal) * sensitivity / 2
    peaks = [x for x in signal if x > peak_threshold]
    normalized_peaks = list(map(lambda x: round(x * 1.5, 3), peaks))
    return normalized_peaks

def calculate_entropy(values):
    # Misleading complex calculation - unused
    from math import log2
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * log2(p) for p in probabilities)
    return round(entropy, 4)

def transform_coordinates(peaks):
    # Unused geometric transformation
    coords = [(i, val) for i, val in enumerate(peaks)]
    rotated = [(y * 0.707 - x * 0.707, x * 0.707 + y * 0.707) for x, y in coords]
    return rotated

def integrate_signals(primary, secondary):
    # Fake fusion function - distractor
    return [a + b for a, b in zip(primary, secondary)]

def preprocess_signal(raw):
    # Adds noise then removes it - red herring process
    amplified = [x * 2.1 for x in raw]
    clipped = [min(max(x, -1.5), 2.5) for x in amplified]
    restored = [x / 2.1 for x in clipped]  # Inverse op cancels effect
    return restored

def encode_diagnostic_code(value):
    # Complex but irrelevant encoding
    binary_rep = bin(int(abs(value) * 1000))[2:]
    flipped = ''.join('1' if b == '0' else '0' for b in binary_rep)
    return int(flipped, 2) % 97

def analyze_signal(data):
    # Core logic hidden among distractions
    freq_analysis = generate_frequency_map(data)
    peak_list = extract_peaks(data, sensitivity=0.8)
    
    # Critical intermediate computation
    base_score = sum(peak_list) * 100
    
    # Distractor: multiple unused transforms
    dummy_transform = [encode_diagnostic_code(p) for p in peak_list]
    dummy_freq_op = list(itertools.accumulate(freq_analysis.values()))
    
    # Real logic continues here
    adjustment_factor = len(freq_analysis) * 1.25
    raw_diagnostic = base_score + adjustment_factor
    
    # Final manipulation using itertools on trivial sequence
    padding = list(itertools.repeat(1, len(peak_list)))
    offset = sum(padding) * 0.75
    
    final_diagnostic = raw_diagnostic - offset
    return final_diagnostic

# Main execution flow
processed_data = preprocess_signal(raw_readings)

# Several irrelevant computations to obscure the real path
unused_smoothed = compute_moving_average(raw_readings)
unused_entropy = calculate_entropy(raw_readings)
dummy_fusion = integrate_signals(raw_readings[:4], raw_readings[4:])

# Key statement containing the answer
final_diagnostic = analyze_signal(processed_data)

print(f"Target result: {final_diagnostic}")