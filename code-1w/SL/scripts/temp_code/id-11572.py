def analyze_pattern(seq, threshold):
    # Irrelevant transformation: character frequency analysis
    char_freq = {}
    for c in seq:
        char_freq[c] = char_freq.get(c, 0) + 1
    
    # Distractor: unused entropy calculation
    import math
    entropy = 0.0
    total = len(seq)
    for count in char_freq.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * math.log2(prob)
    
    # Relevant: pattern-based scoring using bitwise and logical ops
    score = 0
    shift_key = len(seq) % 7
    
    # Decoy list comprehension with no side effects
    [i ** 2 for i in range(len(seq) // 2)]
    
    # Real logic begins: scanning n-grams
    n = 3
    patterns_found = 0
    for i in range(len(seq) - n + 1):
        segment = seq[i:i+n]
        if 'ATG' in segment:
            patterns_found += 1
            # Complex condition with short-circuit logic
            if (len(segment) == 3 and segment[0] == 'A') or (segment[-1] == 'G' and len(segment) > 2):
                base_val = sum(ord(c) for c in segment)
                masked = base_val & (0xFF >> (shift_key % 4))
                score += masked ^ (patterns_found << 2)
    
    # Secondary irrelevant computation: palindrome check (unused)
    palindromes = [seq[i:j] for i in range(len(seq)) for j in range(i+3, len(seq)+1) if seq[i:j] == seq[i:j][::-1]]
    
    # Lambda-based filtering (partially relevant)
    weight_fn = lambda x, t: x * 1.75 if x > t else x * 0.8
    adjusted_score = weight_fn(score, threshold)
    
    # Final adjustment using boolean logic chain
    modifier = 1
    if score > threshold and (patterns_found % 2 == 1) or (shift_key & 3 == 2):
        modifier = -1
    elif entropy > 2.0:  # This will never trigger due to string structure
        modifier = 2
    
    # Critical assignment
    filtration_score = int(adjusted_score * modifier)
    return filtration_score

# Initialization data
base_sequence = 'CATGATGTAGCTATGGCTATGTT'
filter_threshold = 42

# Dead code path: unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Unused variable (distractor)
consensus_motif = 'TATA'

# Key execution point
filtration_score = analyze_pattern(base_sequence, filter_threshold)

# Print result as required
print(f"Target result: {filtration_score}")