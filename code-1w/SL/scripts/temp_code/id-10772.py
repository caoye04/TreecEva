import math

# Simulated sensor data processing with red herrings and complex distractions
def collect_telemetry():
    raw_signals = [i * 1.5 for i in range(20)]
    noise_floor = sum([math.sin(x) for x in raw_signals])  # Irrelevant computation
    filtered = [x for x in raw_signals if x > 5]
    scaling_factor = 2.718  # Unused constant (distractor)
    return filtered

# Distractor function - looks important but unused
def legacy_calibrate(data):
    adjusted = []
    for x in data:
        adjusted.append(x * 0.95 if x % 2 else x * 1.05)
    return adjusted

# Another decoy: complex transformation with no downstream use
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Real transformation path begins here
def preprocess_stream(data):
    shifted = [int(x + 7) for x in data]  # Convert to integers + offset
    modified = []
    for val in shifted:
        if val % 3 == 0:
            modified.append(val // 3)
        elif val % 5 == 0:
            modified.append(val // 5)
        else:
            modified.append(val)
    return modified

# Set operation used meaningfully
def filter_anomalies(dataset):
    base_set = set(range(10, 40))
    extra_noise = {x for x in dataset if x % 7 == 0}  # distraction subset
    clean_set = set(dataset) & base_set  # intersection matters
    return sorted(list(clean_set))

# String manipulation as required feature
def generate_diagnostics(code_list):
    labels = []
    for code in code_list:
        binary_rep = bin(code)[2:].zfill(6)
        parity_bit = str(binary_rep.count('1') % 2)
        tag_str = f"ERR{code}X" + parity_bit
        # Use string method meaningfully
        if tag_str.startswith('ERR') and 'X1' in tag_str:
            labels.append(tag_str.strip('X'))
    return labels

# Critical analysis function - actually determines result
def analyze_pattern(values, limit):
    cumulative = 0
    count = 0
    for v in values:
        if v < limit:
            cumulative += v ** 2
            count += 1
        else:
            cumulative -= v
    if count == 0:
        return -1
    # Final logic step combines multiple concepts
    result = int(cumulative / (count or 1))
    return result

# Irrelevant helper - dead code path
def deprecated_merge(a, b):
    return sorted(set(a + b), reverse=True)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect initial data
    signal_data = collect_telemetry()  # [7.5, 9.0, ..., 28.5]
    
    # Step 2: Preprocess — key path
    transformed_data = preprocess_stream(signal_data)
    
    # Step 3: Filter using set logic — relevant
    transformed_data = filter_anomalies(transformed_data)
    
    # Step 4: Generate diagnostic tags — partially relevant
    diagnostics = generate_diagnostics(transformed_data)
    valid_codes = [int(d[3:]) for d in diagnostics if d.startswith('ERR')]  # extract numeric
    
    # Step 5: Introduce misleading alternate path
    phantom_chain = [x * 2 for x in valid_codes if x > 20]  # unused branch
    normalization_key = sum(phantom_chain) % 17 if phantom_chain else 0  # red herring
    
    # Step 6: Compute threshold from string lengths (subtle but valid)
    temp_tags = [tag.replace('ERR', '') for tag in diagnostics]
    length_sum = sum(len(t) for t in temp_tags)
    threshold = (length_sum // len(temp_tags)) if temp_tags else 5  # ~6
    
    # Step 7: Final analysis — this produces the answer
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Step 8: Print result as required
    print(f"Result: {final_diagnostic}")