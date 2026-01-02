def analyze_signal(pattern, threshold=0.7):
    # Irrelevant transformation: scrambles input but unused in final result
    scrambled = [p ^ (i % 256) for i, p in enumerate(pattern)]
    normalized = [p / sum(pattern) for p in pattern if p > 0]
    
    # Distractor: complex-looking but unused metrics
    entropy = 0.0
    for val in normalized:
        if val > 0:
            entropy -= val * __import__('math').log(val)
    
    # Real computation begins: extract peaks
    peaks = [i for i, x in enumerate(normalized) if x > threshold and i % 2 == 0]
    peak_sum = sum(normalized[i] for i in peaks)

    # Simulate diagnostic envelope
    envelope = []
    for i in range(len(normalized)):
        if i < len(normalized) - 1:
            envelope.append(abs(normalized[i+1] - normalized[i]))
        else:
            envelope.append(normalized[i] / 2)
    
    # Unused recursive red herring
    def integrate_recursive(seq, idx=0):
        if idx >= len(seq):
            return 0
        return seq[idx] + 0.9 * integrate_recursive(seq, idx + 1)  # Never called

    # Actual signal metric
    avg_envelope = sum(envelope) / len(envelope)
    return peak_sum, avg_envelope

# Main processing pipeline
raw_input = [120, 85, 140, 60, 135, 90, 150, 70, 130, 80]
noise_floor = [x + (i % 3) * 5 for i, x in enumerate(raw_input)]  # Distractor

# Misleading intermediate: looks important but unused
snapshot = raw_input[::2]
snapshot_zscore = [(x - sum(snapshot)/len(snapshot)) for x in snapshot]

# Key data structures with cross-reference
status_flags = {i: (raw_input[i] > 100) for i in range(len(raw_input))}
trend_data = {k: v for k, v in enumerate(noise_floor) if status_flags[k]}  # Filtered view

baseline = []
for i, val in enumerate(raw_input):
    if i % 3 == 0:
        baseline.append(val * 0.95)

# Decoy function with bit manipulation (unused)
def encrypt_key(data):
    key = 0
    for d in data:
        key ^= (d << 2) | (d >> 6)
    return key % 1000

# Another distractor: set operations that look meaningful
unique_peaks = set([x for x in raw_input if x > 120])
shadow_band = set([x + 10 for x in raw_input if x < 90])
overlap = unique_peaks & shadow_band  # Empty, but looks suspicious

# Real work: call analysis
peak_total, dynamic_base = analyze_signal(raw_input, threshold=0.7)

# Multiple assignment red herring
primary_metric, secondary_metric = peak_total, dynamic_base * 1.5
auxiliary_score = sum(baseline) / 100  # Looks useful, not used

# Adjustment computed from irrelevant logic chain
shift_register = 0
for i in range(5):
    shift_register = (shift_register << 1) | ((sum(noise_floor) + i) % 2)
adjustment_factor = shift_register - 25  # Depends on noise_floor, which is corrupted

# Core answer calculation buried in context
def aggregate_metrics(data_dict, base_list):
    # Use enumerate and zip: required python features
    indexed_vals = list(enumerate(data_dict.values()))
    paired = list(zip(indexed_vals, base_list + [0]*(len(indexed_vals) - len(base_list))))
    
    # Slicing operation: required feature
    window = paired[:len(base_list)][::-1]  # Reverse slice
    
    # Set operation on tuples: required feature
    seen_indices = set()
    filtered = []
    for (idx, val), base_val in window:
        if idx not in seen_indices:
            seen_indices.add(idx)
            filtered.append(val * base_val * 0.01)
    
    return sum(filtered)

# Final statement containing the target variable
final_diagnostic = aggregate_metrics(trend_data, baseline) + adjustment_factor

print(f"Target result: {final_diagnostic}")