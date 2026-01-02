from collections import defaultdict
from itertools import combinations

# System health monitoring simulation with diagnostic interference

def generate_frequencies(base_signal, noise_level=3):
    return [base_signal * (i + 1) + (i % noise_level) for i in range(6)]

def validate_checksum(sequence):
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum += val * (idx + 1)
    return checksum % 17

def analyze_pattern(seq):
    if len(seq) < 4:
        return False
    # Irrelevant pattern check (distractor)
    for i in range(len(seq) - 2):
        if seq[i] + seq[i+1] == seq[i+2]:
            return True
    return False

def compute_entropy(values):
    freq_map = defaultdict(int)
    for v in values:
        freq_map[v] += 1
    entropy = 0.0
    total = len(values)
    for count in freq_map.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Simplified pseudo-entropy
    return round(entropy, 4)

def extract_diagnostic_flags(raw_data):
    flags = []
    for item in raw_data:
        if item & 1:
            flags.append(item ^ 5)
        elif item > 10:
            flags.append(item >> 2)
    return flags  # Unused in final logic

def evaluate_stability(rtt_list, tolerance=0.15):
    avg = sum(rtt_list) / len(rtt_list)
    deviations = [(abs(x - avg) / avg) for x in rtt_list]
    return all(d < tolerance for d in deviations)

def derive_key_vector(signal_group):
    vector = []
    for group in signal_group:
        if sum(group) % 2 == 0:
            vector.append(len([x for x in group if x % 3 == 0]))
        else:
            vector.append(sum(group) % 7)
    return vector  # Dead path - not used later

# Core processing function with embedded distractions
def process_metrics(signature, thresholds):
    # Step 1: Initial unpacking and transformation
    raw_samples = signature['samples']
    metadata = signature['meta']
    
    # Distractor computation 1: Frequency analysis (partially irrelevant)
    frequencies = generate_frequencies(metadata['base'], noise_level=5)
    checksum_valid = validate_checksum(frequencies)
    
    # Distractor computation 2: Pattern detection (never used)
    has_pattern = analyze_pattern(frequencies)
    
    # Step 2: Real computation begins - entropy from samples
    sample_entropy = compute_entropy(raw_samples)
    
    # Step 3: Extract operational mode
    mode = metadata['mode']
    adjustment_factor = 1.0
    if mode == 'turbo':
        adjustment_factor = 1.25
    elif mode == 'eco':
        adjustment_factor = 0.85
    
    # Step 4: Apply threshold logic using dictionary mapping
    category = metadata['category']
    category_weight = thresholds.get(category, 1.0)
    
    # Step 5: Conditional override based on bit properties
    primary_sample = raw_samples[0]
    if primary_sample & (primary_sample - 1) == 0:  # Power of two check
        category_weight *= 1.1
    
    # Step 6: Compute weighted risk index
    risk_index = 0
    for i, val in enumerate(raw_samples):
        if i % 3 == 0:
            risk_index += val * 0.1
        elif i % 3 == 1:
            risk_index += val * 0.05
        else:
            risk_index += abs(val - 5) * 0.02
    
    # Step 7: Normalize risk with adjustment
    normalized_risk = risk_index * adjustment_factor * category_weight
    
    # Step 8: Final diagnostic via conditional expression
    stability_check = evaluate_stability(raw_samples[1:4])
    final_diagnostic = int(normalized_risk * 100) if stability_check else int((normalized_risk + 2.5) * 100)
    
    # Dead code paths below (red herrings)
    if final_diagnostic > 1000:
        derived_vector = derive_key_vector([[1,2,3], [4,5]])
        flags = extract_diagnostic_flags([final_diagnostic])
    
    return final_diagnostic

# Simulated input data with meaningful structure
threshold_map = {
    'A': 0.9,
    'B': 1.1,
    'C': 1.3
}

health_signature = {
    'samples': [8, 12, 14, 7, 5, 9, 11],
    'meta': {
        'base': 7,
        'mode': 'turbo',
        'category': 'B'
    }
}

# Execution point of interest
final_diagnostic = process_metrics(health_signature, threshold_map)
print(f"Result: {final_diagnostic}")