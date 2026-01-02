def analyze_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    return freq

# Irrelevant helper function (distractor)
def compute_entropy(values):
    import math
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Semi-relevant transformation (misleading path)
def normalize_counts(count_dict):
    total = sum(count_dict.values())
    normalized = {k: v / total for k, v in count_dict.items()}
    scaled = {k: int(v * 100) for k, v in normalized.items()}  # Lossy scaling
    return scaled

# Core logic disguised among distractions
def calculate_complexity_score(freq_dict):
    score = 0
    weights = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    vowel_count = 0
    consonant_weight = 0.7
    
    for letter, count in freq_dict.items():
        if letter in weights:
            vowel_count += count
            score += count * 2
        else:
            score += count * consonant_weight
    
    # Apply non-linear adjustment
    if vowel_count > 0:
        score = score * (1.5 - 0.02 * vowel_count)
    
    return int(score)

# Main scoring function
def calculate_final_score(raw_data, limits):
    temp_result = 0
    intermediate_values = []
    
    for idx, entry in enumerate(raw_data):
        # Use of enumerate and zip (required Python features)
        chars = [c for c in entry if c.isalnum()]
        pos_chars = list(zip(chars, [i for i in range(len(chars))]))
        
        # Extract just the characters, ignore positions (semi-relevant)
        clean_text = ''.join([pc[0] for pc in pos_chars])
        
        # Real work begins
        freq_map = analyze_frequency(clean_text)
        
        # Distraction: normalize but don't use
        normalized_freq = normalize_counts(freq_map)  # dead-end computation
        entropy_proxy = compute_entropy(list(freq_map.values()))  # unused
        
        base_score = calculate_complexity_score(freq_map)
        
        # Conditional modification based on external thresholds
        length_bonus = len(clean_text) if len(clean_text) > limits['min_len'] else 0
        complexity_penalty = 0
        
        if base_score > limits['max_score']:
            complexity_penalty = 5
        
        adjusted = base_score + length_bonus - complexity_penalty
        intermediate_values.append(adjusted)
    
    # Aggregate with weighted emphasis on later entries
    final = 0
    for i, val in enumerate(intermediate_values):
        weight = 1 + i * 0.1  # increasing importance
        final += val * weight
    
    # Final threshold clamp
    max_cap = limits['hard_cap']
    final = min(final, max_cap)
    
    # Key variable assignment
    final_score = int(round(final))
    
    # Unrelated cleanup (distractor)
    garbage_collect = [0] * 100
    del garbage_collect
    
    return final_score

# Simulated dataset
log_entries = [
    "UserLogin: Alice@host1",
    "DataAccess: FileXYZ, Mode=R",
    "SystemAlert: HighMemoryUsage",
    "NetworkEvent: IP=192.168.1.1"
]

tuning_params = {
    'min_len': 10,
    'max_score': 30,
    'hard_cap': 88
}

# Execute
result = calculate_final_score(log_entries, tuning_params)
print(f"Target result: {result}")