from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing with red herrings
def fetch_raw_readings():
    return [17, 23, 17, 45, 23, 59, 61, 45, 17, 61]

def compute_legacy_checksum(data):
    # Irrelevant legacy function (dead path)
    checksum = 0
    for x in data:
        checksum = (checksum + x * 11) % 257
    return checksum

def normalize_signal(values):
    mean = sum(values) / len(values)
    return [round(x - mean, 2) for x in values]

def extract_frequency_profile(raw_seq):
    freq = defaultdict(int)
    for val in raw_seq:
        freq[val] += 1
    return freq

def apply_noise_filter(seq):
    # Misleading filter that doesn't actually get used
    return [x for x in seq if x > 15]

def generate_temporal_windows(data):
    windows = []
    for i in range(len(data) - 2):
        windows.append(data[i:i+3])
    return windows

def transform_sequence(signal):
    # Real transformation: map to prime factors count
    def count_prime_factors(n):
        if n <= 1:
            return 0
        count = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                count += 1
                n //= d
            d += 1
        if n > 1:
            count += 1
        return count
    
    return [count_prime_factors(x) for x in signal]

def build_reference_map(freq_dist):
    # Creates a normalized weight map based on frequency
    total = sum(freq_dist.values())
    return {k: round(v / total, 3) for k, v in freq_dist.items()}

def evaluate_coherence(window_list, weights):
    # Unused coherence metric (decoy)
    score = 0.0
    for window in window_list:
        for val in window:
            if val in weights:
                score += weights[val] ** 2
    return round(score, 4)

def analyze_pattern(transformed, ref_map):
    # Core logic: weighted sum of transformed indices using frequency-based weights
    cumulative = 0
    temp_lookup = list(ref_map.keys())
    
    # Irrelevant sorting distraction
    temp_lookup.sort(reverse=True)
    
    weight_index = {val: idx for idx, val in enumerate(temp_lookup)}
    
    for i, val in enumerate(transformed):
        # Only use mapping if original value exists in ref_map
        original_val = fetch_raw_readings()[i]  # Recompute to simulate lookup
        if original_val in ref_map:
            position_weight = ref_map[original_val]
            cumulative += val * position_weight * (i + 1)  # index-weighted contribution
    
    # Decoy intermediate variables
    debug_trace = f"Processed {len(transformed)} elements"
    anomaly_flag = cumulative > 100
    
    final_score = int(round(cumulative))
    
    # Dead code block: never executed due to constant condition
    if False:
        fallback = 0
        for k in ref_map:
            fallback += hash(str(k)) % 10
        final_score = fallback
    
    return final_score

# Main execution flow
raw_data = fetch_raw_readings()
legacy_hash = compute_legacy_checksum(raw_data)  # Distractor variable

normalized_data = normalize_signal(raw_data)
frequency_map = extract_frequency_profile(raw_data)
windowed_chunks = generate_temporal_windows(raw_data)

# Apply actual transformation
transformed_data = transform_sequence(raw_data)

# Build weighting system
reference_map = build_reference_map(frequency_map)

# Unused decoy analysis
coherence_metric = evaluate_coherence(windowed_chunks, reference_map)

# Key statement
final_diagnostic = analyze_pattern(transformed_data, reference_map)

# Output result
print(f"Result: {final_diagnostic}")