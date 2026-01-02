import math

# Simulated sensor fusion system for environmental anomaly detection
def collect_samples(base_freq, duration):
    samples = []
    for t in range(1, duration + 1):
        raw = math.sin(base_freq * t) * math.exp(-0.1 * t) + 0.5 * math.cos(3 * base_freq * t)
        samples.append(round(raw * 1000) / 1000)
    return samples

# Irrelevant transformation - dead code path (distractor)
def legacy_filter(data):
    return [x for x in data if abs(x) > 0.3]

# Unused auxiliary function (red herring)
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Signal conditioning with multiple irrelevant steps
def preprocess_signal(raw_data):
    normalized = [round(x + 0.1, 3) for x in raw_data]  # minor shift
    amplified = [x * 1.5 for x in normalized]           # amplification
    clipped = [max(-1.0, min(x, 1.0)) for x in amplified]  # clip to range
    
    # Decoy statistical computation (irrelevant)
    mean_val = sum(clipped) / len(clipped) if clipped else 0
    variance = sum((x - mean_val) ** 2 for x in clipped) / len(clipped) if clipped else 0
    
    # This transformation is actually used later
    quantized = [int(x * 10) for x in clipped]
    return quantized

# Core analysis logic
def detect_peaks(signal_seq, sensitivity=5):
    peaks = []
    for i in range(1, len(signal_seq) - 1):
        if signal_seq[i] > signal_seq[i-1] and signal_seq[i] > signal_seq[i+1]:
            if signal_seq[i] >= sensitivity:
                peaks.append(i)
    return peaks

# Set-based interference pattern matching (uses set operations)
def match_interference_patterns(clean_seq):
    even_positions = {i for i in range(0, len(clean_seq), 2)}
    high_values = {i for i, val in enumerate(clean_seq) if val >= 8}
    negative_vals = {i for i, val in enumerate(clean_seq) if val < 0}
    
    # Meaningful intersection: positions that are even-indexed AND have high values
    critical_nodes = even_positions & high_values
    
    # Irrelevant symmetric difference (distractor)
    anomaly_mask = negative_vals ^ {x+1 for x in even_positions}
    
    return critical_nodes

# Main diagnostic engine
def analyze_signal(trace, thresholds):
    # Linear search through thresholds (relevant)
    active_level = 0
    for level in sorted(thresholds):
        if len(trace) > level:
            active_level = level
            break

    # Real processing path
    peak_indices = detect_peaks(trace, sensitivity=7)
    interference_sites = match_interference_patterns(trace)

    # Complex conditional with early exit (short-circuit)
    if not peak_indices and len(interference_sites) == 0:
        return -1
    
    # Key calculation: weighted impact score
    base_score = sum(trace[i] for i in peak_indices if i in interference_sites)
    
    # Multiple distractor variables (irrelevant)
    temp_offset = sum(1 for x in trace if x in {3, 6, 9})
    shadow_factor = len({x % 7 for x in trace})
    phantom_count = len([x for x in trace if x < 0])

    # Final computation - only base_score and active_level matter
    final_impact = base_score * 100 + active_level
    
    # Dead branch (never reached due to structure)
    if temp_offset > 100:
        final_impact += shadow_factor * 2

    return int(final_impact)

# Orchestration script
if __name__ == "__main__":
    # Generate realistic input
    raw_trace = collect_samples(base_freq=0.4, duration=12)
    processed_trace = preprocess_signal(raw_trace)
    
    # Threshold set (used in linear search)
    threshold_set = {5, 10, 15, 20}
    
    # Irrelevant data structures (distractors)
    audit_log = [{'step': 'init', 'status': 1}, {'step': 'proc', 'status': 0}]
    metadata_cache = {"version": "2.1", "mode": "diagnostic"}
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_trace, threshold_set)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")