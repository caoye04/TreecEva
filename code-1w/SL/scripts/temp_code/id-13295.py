import math

# Simulated sensor array data (irrelevant initial setup)
base_frequency = 50.0
harmonic_noise = [0.1, 0.3, 0.2, 0.7, 0.4]
dummy_weights = [0.9, 0.1, 0.8, 0.2]  # Unused in final calculation

# Core signal parameters
def generate_raw_signals():
    return [45, 82, 29, 67, 53, 74, 36, 88, 42, 59]

# Irrelevant transformation (dead path)
def deprecated_filter(x):
    return [val for val in x if val > 60]

# Preprocessing with red herring operations
def preprocess_signal(raw):
    offset = 12
    adjusted = [val + offset for val in raw]  # Simple shift
    squared_errors = [math.pow(x, 2) for x in harmonic_noise]  # Distractor computation
    filtered = [val for val in adjusted if val % 2 == 0]  # Partial filter (misleading)
    return adjusted  # Critical: returns full adjusted, not filtered

# Secondary analysis with decoy logic
def compute_entropy(data):
    total = sum(data)
    probabilities = [d / total for d in data]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy  # Computed but unused

# Bit manipulation layer (combined relevant & irrelevant)
def flag_analysis(val):
    bit_flags = val ^ 255  # Invert bits (used in processing)
    parity = bin(bit_flags).count('1') % 2
    if parity == 0:
        return bit_flags >> 1
    else:
        return bit_flags << 1  # Not triggered in this case

# Main processing chain
def analyze_readings(data):
    temp_results = []
    for d in data:
        if d < 70:
            temp_results.append(d * 1.1)
        else:
            temp_results.append(d * 0.95)
    
    # Key transformation using bitwise and arithmetic
    processed = [flag_analysis(int(tr)) for tr in temp_results]
    
    # Decoy aggregation
    avg_temp = sum(temp_results) / len(temp_results)  # Computed but ignored
    peak = max(processed)  # Mentioned but not used
    
    # Critical nested conditional (depends on specific threshold)
    diagnostic_score = 0
    for p in processed:
        if p > 200 and p < 300:
            diagnostic_score += 3
        elif p > 100:
            diagnostic_score += 1
        else:
            diagnostic_score -= 2
    
    # Final adjustment based on pattern count
    high_flags = len([x for x in processed if x > 250])
    if high_flags >= 2:
        diagnostic_score *= 2
    
    return diagnostic_score

# Execution flow
raw_signals = generate_raw_signals()
processed_signals = preprocess_signal(raw_signals)
entropy_value = compute_entropy(processed_signals)  # Dead call
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")