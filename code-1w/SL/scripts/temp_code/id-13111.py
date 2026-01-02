import math

# System diagnostics simulation with red herrings and complex logic paths
def generate_signature(length, seed=7):
    signature = []
    for i in range(length):
        val = (seed * i * i + 3 * i + 17) % 101
        if i % 5 == 0:
            val = (val + 13) % 101  # Distraction: rarely affects outcome
        signature.append(val)
    return signature

def encrypt_data(data_list):
    # Irrelevant transformation - not used in final path
    encrypted = [((x << 2) ^ 255) % 97 for x in data_list]
    normalized = [e / max(encrypted) for e in encrypted]
    return [round(n * 100) for n in normalized]

def compute_entropy(seq):
    # Dead function - looks important but unused
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def filter_anomalies(raw_data, threshold=42):
    anomalies = []
    for x in raw_data:
        if x > threshold and (x % 3 != 0):  # Partially relevant condition
            anomalies.append(x)
    return set(anomalies)  # Return as set for later operations

def merge_and_validate(primary, secondary):
    # Merges two sequences using symmetric difference (set operation)
    primary_set = set(primary)
    secondary_set = set(secondary)
    merged = list(primary_set ^ secondary_set)  # XOR: elements in either set but not both
    merged.sort(reverse=True)
    return merged

def derive_weights(values):
    # Complex weight calculation with distraction
    weights = []
    base_factor = len(values) / (sum(values) + 1)
    for v in values:
        if v == 0:
            continue
        weight = (v ** 0.5) * base_factor
        if weight > 0.5:
            weight = 0.5  # Cap weight - misleading normalization
        weights.append(round(weight, 3))
    return weights

def analyze_patterns(sequence, ref):
    # Core logic with multiple steps and distractions
    temp_result = 0
    offset = len(sequence) % 7
    
    # Distractor block: complex but irrelevant calculation
    shadow_accum = 0
    for i in range(len(sequence)):
        if sequence[i] % 4 == 0:
            shadow_accum += (sequence[i] // 4) * 3
        elif sequence[i] % 3 == 0:
            shadow_accum -= sequence[i] % 10
    
    # Real logic begins: conditional accumulation based on set membership
    valid_count = 0
    sum_matched = 0
    ref_set = set(ref)  # Redundant conversion - already a set
    
    for idx, num in enumerate(sequence):
        shifted_idx = (idx + offset) % 10
        
        # Key condition: depends on index shift and set inclusion
        if shifted_idx in {1, 3, 5, 7} and num in ref_set:
            sum_matched += num * (shifted_idx + 1)
            valid_count += 1
        
        # Misleading side condition that rarely triggers
        if num > 50 and idx % 4 == 0 and num not in {64, 77, 88}:
            temp_result += num % 11
    
    # Final computation - only sum_matched matters
    diagnostic_score = sum_matched - (valid_count * 3)
    
    # Decoy assignment
    temp_result += shadow_accum % 19
    
    return diagnostic_score

# Main execution flow
if __name__ == '__main__':
    # Generate initial data
    base_sequence = generate_signature(12, seed=7)
    
    # Irrelevant encryption
    encrypted_features = encrypt_data(base_sequence)
    
    # Create reference set via filtering
    candidate_pool = [x * 2 + 5 for x in range(15)]
    filtered_refs = filter_anomalies(candidate_pool, threshold=30)
    
    # Modify base_sequence slightly to create encoded_sequence
    transformed = [x + (i % 3) for i, x in enumerate(base_sequence)]
    masked = [t ^ 5 if i % 4 == 2 else t for i, t in enumerate(transformed)]
    encoded_sequence = merge_and_validate(masked, [10, 20, 30, 40, 50])
    
    # Derive unused weights
    feature_weights = derive_weights(encoded_sequence)
    
    # Critical statement
    final_diagnostic = analyze_patterns(encoded_sequence, filtered_refs)
    
    # Output result
    print(f"Result: {final_diagnostic}")