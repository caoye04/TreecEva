from collections import defaultdict, Counter

# Irrelevant helper function (decoy)
def compute_entropy(data):
    total = sum(data.values())
    entropy = 0
    for count in data.values():
        if count > 0:
            p = count / total
            entropy -= p * p  # Not actual entropy, misleading
    return round(entropy, 4)

# Distractor: Unused transformation
def mirror_sequence(seq):
    return seq + seq[::-1]

# Core logic disguised among distractions
def count_transitions(seq):
    transitions = 0
    for i in range(len(seq) - 1):
        if seq[i] != seq[i+1]:
            transitions += 1
    return transitions

# Misleading frequency analysis
def assess_balance(chars):
    freq = Counter(chars)
    max_count = max(freq.values())
    min_count = min(freq.values())
    return (max_count - min_count) < 3  # Arbitrary balance threshold

# Heavily distracted main analyzer
def analyze_pattern(seq):
    # Irrelevant preprocessing
    temp_buffer = [c for c in seq if c in 'ACGT']  # DNA red herring
    backup_copy = seq[::-1]  # Unused reverse

    # Real work hidden among noise
    char_map = defaultdict(int)
    for idx, c in enumerate(seq):
        if c.isalpha():
            char_map[c] += (idx + 1) * (1 if ord(c) % 2 else -1)  # Position-weighted sum
    
    # Decoy statistical measures
    avg_position = sum(char_map.values()) / len(char_map) if char_map else 0
    outlier_check = [v for v in char_map.values() if abs(v) > 10]
    stability_flag = len(outlier_check) < 2

    # Critical computation buried in middle
    transition_count = count_transitions(seq)
    balanced = assess_balance(seq)
    
    # Key logic: combine position effects and transitions
    raw_total = sum(char_map.values())
    adjustment = transition_count * (5 if balanced else -5)
    
    # More distractions
    profile = {
        'length': len(seq),
        'unique': len(set(seq)),
        'density': len(seq) / (len(seq) + 1),
        'mirror_match': seq == backup_copy  # Always true, useless
    }
    
    # Final calculation (non-obvious dependency)
    base_score = raw_total + adjustment
    penalty = abs(profile['unique'] - len(temp_buffer))  # Often zero
    final_score = base_score - penalty * 2
    
    # Dead code path (never executed)
    if False:
        fallback = compute_entropy(Counter(seq))
        final_score = int(fallback * 100)
    
    return final_score

# Input with mixed characteristics
sequence = "AbCdEfGhHgFeDcBa"  # Symmetric, alternating case, letter transitions

# Execute key statement
final_score = analyze_pattern(sequence)
print(f"Target result: {final_score}")