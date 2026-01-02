import itertools
from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings and complex routing
def fetch_raw_stream():
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def apply_noise_filter(data):
    # Irrelevant transformation: shifts values but not used in final path
    shifted = [(x + 7) % 10 for x in data]
    normalized = [x / sum(shifted) for x in shifted]
    return [int(x * 100) for x in normalized]

def generate_combinatorial_pairs(lst):
    # Distractor: generates pairs but unused
    return list(itertools.combinations(lst, 2))

def compute_entropy(values):
    # Dead-end function: looks important but unused
    counter = Counter(values)
    total = len(values)
    entropy = 0
    for count in counter.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, misleading
    return round(entropy, 6)

def extract_frequency_map(seq):
    # Useful but indirect: builds frequency map used later
    freq = defaultdict(int)
    for item in seq:
        freq[item] += 1
    return freq

def derive_sequence_signature(freq_map, threshold=2):
    # Extracts recurring elements — contributes to transformation
    return sorted([k for k, v in freq_map.items() if v >= threshold])

def transform_sequence(raw, signature):
    # Core transformation: maps raw data using signature as mask
    result = []
    sig_set = set(signature)
    for i, val in enumerate(raw):
        if val in sig_set:
            result.append(val * 2)
        elif i % 2 == 0:
            result.append(val + 1)
        else:
            result.append(val - 1)
    return result

def evaluate_health_metrics(diag_data):
    # Heavily obfuscated metrics — all irrelevant
    stats = defaultdict(float)
    n = len(diag_data)
    for i in range(n):
        stats['metric_a'] += diag_data[i] * (i + 1)
        stats['metric_b'] += diag_data[n - i - 1] ** 0.5
        stats['metric_c'] *= 1.01  # Decoy accumulation
    return {k: round(v, 4) for k, v in stats.items()}

def analyze_pattern(processed, cfg):
    # Final analysis: computes weighted sum based on config
    weight = cfg.get('weight', 1)
    offset = cfg.get('offset', 0)
    base_sum = sum(x for x in processed if x > 0)
    adjustment = 0
    
    # Complex conditional logic with misleading branches
    if len(processed) > 10:
        adjustment += cfg.get('bonus', 5)
    if sum(processed) % 7 == 0:
        adjustment -= 3  # Never triggers due to prior steps
    if any(x > 20 for x in processed):
        adjustment += 2
    
    # Critical computation path
    raw_score = base_sum * weight + offset + adjustment
    
    # Secondary validation check (looks important, doesn't alter logic)
    validation_trace = []
    for x in processed:
        if x % 2 == 0:
            validation_trace.append(x // 2)
        else:
            validation_trace.append(x * 2 + 1)
    
    # Final diagnostic is deterministic
    return int(raw_score)

# Main execution flow
if __name__ == "__main__":
    # Primary data source
    sensor_readings = fetch_raw_stream()
    
    # Irrelevant operations (red herrings)
    noisy_profile = apply_noise_filter(sensor_readings)
    pair_combinations = generate_combinatorial_pairs(sensor_readings)
    entropy_value = compute_entropy(sensor_readings)
    
    # Key processing path begins here
    frequency_map = extract_frequency_map(sensor_readings)
    recurrence_signature = derive_sequence_signature(frequency_map, threshold=2)
    transformed_data = transform_sequence(sensor_readings, recurrence_signature)
    
    # Unused side analysis
    health_diagnostics = evaluate_health_metrics(transformed_data)
    
    # Configuration affecting final result
    config = {
        'weight': 3,
        'offset': -10,
        'bonus': 5  # Won't apply since length condition fails
    }
    
    # Critical statement: this produces the answer
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Output result
    print(f"Result: {final_diagnostic}")