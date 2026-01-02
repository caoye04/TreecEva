import math

# Simulated sensor array diagnostics with signal processing
# Irrelevant helper function (decoy)
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data] if max_val > 0 else data

def detect_anomalies(seq, limit):
    anomalies = []
    for i, val in enumerate(seq):
        if val < 0:
            anomalies.append(i)
    return anomalies if len(anomalies) < limit else [len(seq)]

# Unused transformation (dead code path)
def shift_sequence(s, steps):
    return s[steps:] + s[:steps]

# Core analysis logic
def evaluate_entropy(signal):
    signal_set = set(signal)
    total = len(signal)
    entropy = 0.0
    for val in signal_set:
        p = signal.count(val) / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

# Misleading intermediate: looks important but unused later
def compute_checksum(arr):
    checksum = 0
    for i, v in enumerate(arr):
        checksum ^= (v + i) * 3
    return checksum

def filter_signals(raw_inputs, criteria):
    filtered = []
    for idx, reading in enumerate(raw_inputs):
        if idx % 2 == 0 and sum(reading) > criteria['sum_threshold']:
            filtered.append(reading)
    return filtered

def analyze_signal(pattern_list, levels):
    # Step 1: Filter relevant patterns
    valid_patterns = []
    for p in pattern_list:
        if len(p) >= levels['min_length']:
            valid_patterns.append(p)
    
    # Step 2: Find repeating motifs using set operations
    all_values = []
    for p in valid_patterns:
        all_values.extend(p)
    unique_vals = set(all_values)
    frequent_vals = {v for v in unique_vals if all_values.count(v) > 2}
    
    # Step 3: Compute entropy for each valid pattern
    entropies = []
    for pat in valid_patterns:
        entropies.append(evaluate_entropy(pat))
    
    # Step 4: Use enumerate and zip to correlate with threshold bands
    adjusted_scores = []
    for i, (ent, pat) in enumerate(zip(entropies, valid_patterns)):
        base_score = ent * (i + 1)
        length_factor = len(pat) / 10.0
        adjusted = base_score * length_factor
        adjusted_scores.append(adjusted)
    
    # Step 5: Apply conditional weighting based on frequency overlap
    final_score = 0.0
    for score, pattern in zip(adjusted_scores, valid_patterns):
        common_with_freq = set(pattern).intersection(frequent_vals)
        if len(common_with_freq) >= 2:
            final_score += score * 1.5
        else:
            final_score += score * 0.7
    
    # Step 6: Disruptive but irrelevant normalization attempt (distractor)
    temp_normalized = [math.sin(x) for x in all_values[:5]]
    dummy_metric = sum(temp_normalized) / 5 if temp_normalized else 0
    
    # Final diagnostic calculation — only this matters
    adjustment = len(frequent_vals) * 0.3
    final_diagnostic = int((final_score * 100) + adjustment)
    
    return final_diagnostic

# Simulated input data
patterns = [
    [4, 4, 2, 8, 2],
    [4, 8, 4, 8, 2, 2],
    [2, 8, 8, 4, 4, 2, 8],
    [1, 1, 1, 1],           # Too short, will be filtered out
    [8, 2, 4, 8, 4, 2, 2, 8]
]

thresholds = {
    'sum_threshold': 10,
    'min_length': 5
}

# Dead variable assignment (red herring)
optimized_set = compute_checksum([3, 5, 7, 9])

# Unused filtering result (misdirection)
processed_signals = filter_signals(patterns, thresholds)

# Key execution point
final_diagnostic = analyze_signal(patterns, thresholds)

# Output the required result
print(f"Result: {final_diagnostic}")