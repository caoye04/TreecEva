import itertools

def analyze_signal(pattern):
    if len(pattern) < 3:
        return 0
    magnitude = sum(x ** 2 for x in pattern)
    noise_floor = max(pattern) - min(pattern)
    return magnitude // (noise_floor + 1)

def generate_sequence(base, count):
    seq = [base]
    for i in range(1, count):
        seq.append(seq[-1] * 2 + (i % 5))
    return seq

def filter_anomalies(data_stream):
    clean = []
    for val in data_stream:
        if val < 0 or val > 999:
            continue
        if val % 7 == 0 and val % 11 == 0:
            continue
        clean.append(val)
    return clean

def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)

def merge_diagnostics(d1, d2, d3):
    # Irrelevant fusion logic (distractor)
    peak = max(d1, d2, d3)
    avg = (d1 + d2 + d3) / 3
    score = (peak * 0.6) + (avg * 0.4)
    return int(score)

def main_pipeline():
    # Simulated sensor data generation (partially irrelevant)
    raw_signals = [
        generate_sequence(3, 7),
        generate_sequence(5, 6),
        generate_sequence(8, 5)
    ]
    
    # Process each signal (some relevant)
    signal_metrics = [analyze_signal(sig) for sig in raw_signals]
    
    # Inject decoy operations
    temp_cache = {f'key_{i}': pow(i, 3) for i in range(12)}
    _ = [x for x in temp_cache.values() if x % 2 == 0]  # dead computation

    # Real data path begins
    base_input = [18, 24, 36, 48, 54, 72, 81, 96]
    filtered = [x for x in base_input if x % 12 == 0]  # only multiples of 12
    derived_values = [x // 3 for x in filtered]  # divide by 3
    
    # Use set operations (required feature)
    valid_set = set(derived_values)
    control_set = set(range(5, 20))
    intersection_size = len(valid_set & control_set)  # relevant
    
    # Use itertools (required feature)
    paired = list(itertools.combinations([2, 4, 6], 2))
    combo_sum = sum(a * b for a, b in paired)  # red herring
    
    # Create distraction with multiple unused diagnostics
    diag_a = compute_entropy([1, 2, 2, 3, 3, 3])
    diag_b = compute_entropy([4, 4, 5, 5, 6])
    diagnostic_shadow = merge_diagnostics(
        int(diag_a * 10), int(diag_b * 10), combo_sum % 100
    )
    
    # Core logic: construct consolidated data
    consolidated_data = {
        'samples': derived_values,
        'quality': 94,
        'mode': 'turbo',
        'flags': [0, 1, 1, 0],
        'version': 2
    }
    
    # Thresholds matter
    thresholds = {
        'min_valid': 4,
        'max_entries': 10,
        'critical_level': 45
    }
    
    # Decoy function calls
    _ = analyze_signal([1, 1, 1, 2])
    _ = filter_anomalies(list(range(990, 1005)))
    
    # Actual key computation
    def process_metrics(data, limits):
        entries = data['samples']
        if len(entries) > limits['max_entries']:
            return -1
        above_min = [e for e in entries if e >= limits['min_valid']]
        if not above_min:
            return 0
        total = sum(e for e in above_min if e < limits['critical_level'])
        adjustment = len(entries) - intersection_size  # uses earlier set op
        return total - adjustment
    
    final_diagnostic = process_metrics(consolidated_data, thresholds)
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main_pipeline()