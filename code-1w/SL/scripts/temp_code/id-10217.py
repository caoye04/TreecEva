from collections import defaultdict, Counter

# Simulated sensor data ingestion and processing pipeline
def collect_sensor_data():
    raw_signals = [3, 5, 7, 11, 13, 17, 19, 23]
    timestamps = list(range(100, 180, 10))
    labeled_readings = {f'sensor_{i}': raw_signals[i] for i in range(len(raw_signals))}
    return raw_signals, timestamps, labeled_readings

def filter_anomalies(signal_list):
    # Irrelevant filtering (dead code path)
    filtered = [x for x in signal_list if x > 4]
    stats = {'count': len(filtered), 'sum': sum(filtered)}
    return stats  # Not used in main logic

def generate_lookup(signals):
    # Creates a decoy mapping that looks important but isn't used
    lookup = {}
    for idx, val in enumerate(signals):
        key = (val * 2) ^ (idx + 1)
        lookup[key] = val % 5
    return lookup

def compute_derivatives(signal_seq):
    derivatives = []
    for i in range(1, len(signal_seq)):
        derivatives.append(signal_seq[i] - signal_seq[i-1])
    smoothed = [d * 0.9 for d in derivatives]
    return smoothed

def extract_features(raw, labels_dict):
    # Extracts character count from sensor names (red herring)
    name_lengths = [len(name) for name in labels_dict.keys()]
    char_count_total = sum(name_lengths)
    
    # Real feature: prime frequency
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    prime_hits = sum(1 for x in raw if x in primes)
    
    # Decoy accumulation
    dummy_accum = 0
    for k, v in labels_dict.items():
        if 'sensor_3' in k or 'sensor_5' in k:
            dummy_accum += v * 2
    
    return {'prime_frequency': prime_hits, 'char_sum': char_count_total}

def aggregate_diagnostics(features, deriv_seq):
    report = defaultdict(float)
    report['base_score'] = features['prime_frequency'] * 10
    report['trend_bias'] = sum(deriv_seq[:3]) if len(deriv_seq) > 3 else 0
    
    # Irrelevant normalization
    max_deriv = max(deriv_seq) if deriv_seq else 1
    normalized_trend = [d / max_deriv for d in deriv_seq]
    
    report['normalization_offset'] = sum(normalized_trend) * 0.1
    
    return report

def calculate_entropy(seq):
    # Dead-end function — not part of critical path
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, just looks complex
    return round(entropy, 4)

def process_metrics(diag_report, threshold):
    # Core logic hidden among distractions
    score = diag_report['base_score']
    bias = diag_report['trend_bias']
    offset = diag_report['normalization_offset']
    
    # Actual computation chain
    intermediate = score + (bias * 12) - (offset * 5)
    
    # Conditional mutation (depends on threshold)
    flags = [True if bias > 2 else False, offset < 1.0]
    if all(flags):
        intermediate = int(intermediate) ^ 15  # Bitwise red herring
    else:
        intermediate = abs(intermediate - 7)  # This branch actually taken
    
    # Final adjustment based on case conversion of string constant
    magic_str = "DiagX9"
    uppercase_count = sum(1 for c in magic_str if c.isupper())
    final_value = intermediate + (uppercase_count * 3)
    
    return int(final_value)

# Main execution with multiple diversions
if __name__ == '__main__':
    data, times, labels = collect_sensor_data()
    
    # Distractor calls
    anomaly_stats = filter_anomalies(data)
    fake_lookup = generate_lookup(data)
    entropy_metric = calculate_entropy(data)
    
    # Real signal path begins here
    derivatives = compute_derivatives(data)
    features = extract_features(data, labels)
    diagnostics = aggregate_diagnostics(features, derivatives)
    
    # Key control variable — appears arbitrary but affects logic
    activation_threshold = len([x for x in data if x < 15])  # evaluates to 4
    
    # Critical statement
    final_diagnostic = process_metrics(diagnostics, activation_threshold)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")