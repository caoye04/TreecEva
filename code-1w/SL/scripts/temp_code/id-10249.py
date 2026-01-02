from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
def fetch_sensor_data():
    raw_signals = [3, 5, 7, 11, 13, 17, 19, 23]
    timestamps = [100, 101, 102, 105, 108, 110, 115, 120]
    metadata_map = defaultdict(str)
    for t in timestamps:
        metadata_map[t] = f'status_ok_{t}'
    return list(zip(raw_signals, timestamps)), metadata_map

# Irrelevant preprocessing: spectral decomposition (not used in final result)
def perform_spectral_analysis(signal):
    transformed = []
    for x in signal:
        transformed.append(x * math.sin(math.pi / 4) + math.cos(x))
    return transformed

# Real preprocessing: filter primes and square them
def preprocess_signal(data):
    signals, _ = data
    filtered = [x for x in signals if all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))]
    squared = [x ** 2 for x in filtered]
    return squared

# Misleading feature extraction (dead end)
def extract_temporal_features(timestamps):
    diffs = []
    for i in range(1, len(timestamps)):
        diffs.append(timestamps[i] - timestamps[i-1])
    avg_diff = sum(diffs) / len(diffs)
    return {'mean_interval': avg_diff, 'total_duration': timestamps[-1] - timestamps[0]}

# Core logic: count frequency of digits in processed values
def compute_digit_frequency(values):
    digit_count = Counter()
    for val in values:
        for digit in str(val):
            digit_count[int(digit)] += 1
    return digit_count

# Secondary analysis: sum of even-position digits (distraction)
def calculate_positional_weight(values):
    total_weight = 0
    for val in values:
        s = str(val)
        for i in range(len(s)):
            if i % 2 == 0:
                total_weight += int(s[i])
    return total_weight

# Actual critical function: computes checksum based on digit counts
def generate_diagnostic_code(freq_counter):
    checksum = 0
    for digit, count in freq_counter.items():
        if digit % 2 == 1:
            checksum += count * digit
        else:
            checksum -= count
    return checksum * 3

# Final analysis pipeline
processed_cache = {}
def analyze_signal(data):
    key = hash(tuple(data))
    if key in processed_cache:
        return processed_cache[key]
    
    # Step 1: digit frequency
    freq = compute_digit_frequency(data)
    
    # Step 2: apply diagnostic formula
    result = generate_diagnostic_code(freq)
    
    # Step 3: obscure adjustment (only applies if condition met, which it isn't)
    outlier_digits = [d for d, c in freq.items() if c > 10]
    if outlier_digits:
        adjustment = sum(outlier_digits) // len(outlier_digits)
        result += adjustment
    else:
        result -= 7  # This always executes
    
    processed_cache[key] = result
    return result

# Orchestration with red herrings
if __name__ == '__main__':
    # Fetch real data
    sensor_data, meta_info = fetch_sensor_data()
    
    # Irrelevant spectral analysis
    spectral_components = perform_spectral_analysis([x[0] for x in sensor_data])
    
    # Extract fake temporal features
    temporal_stats = extract_temporal_features([x[1] for x in sensor_data])
    
    # REAL processing path
    processed_data = preprocess_signal(sensor_data)
    
    # More distractions
    weight_score = calculate_positional_weight(processed_data)
    normalized_weights = [w / (weight_score + 1e-8) for w in [1, 2, 3]]
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_data)
    
    # Output required result
    print(f"Result: {final_diagnostic}")