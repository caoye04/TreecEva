def analyze_frequency(text):
    frequency_map = {}
    for char in text.lower():
        if char.isalpha():
            frequency_map[char] = frequency_map.get(char, 0) + 1
    return frequency_map


def normalize_values(raw_dict):
    total = sum(raw_dict.values())
    normalized = {k: v / total for k, v in raw_dict.items()}
    return normalized


def filter_relevant_chars(freq_dict, threshold=0.05):
    # Only keep characters that appear above threshold
    return {k: v for k, v in freq_dict.items() if v > threshold}


def calculate_entropy(probabilities):
    import math
    entropy = 0.0
    for p in probabilities.values():
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy


def calculate_final_score(log_data, limits):
    # Step 1: Analyze character frequency
    freq_analysis = analyze_frequency(log_data)
    
    # Step 2: Normalize frequencies to probabilities
    norm_probs = normalize_values(freq_analysis)
    
    # Step 3: Filter out low-frequency characters
    filtered = filter_relevant_chars(norm_probs, limits['freq_threshold'])
    
    # Step 4: Calculate entropy of remaining distribution
    entropy_value = calculate_entropy(filtered)
    
    # Step 5: Apply bitwise adjustment based on length of filtered keys
    key_length_factor = len(''.join(filtered.keys()))
    masked_entropy = int(entropy_value * 100) ^ (key_length_factor << 2)
    
    # Step 6: Accumulate secondary score from character pattern
    bonus_accumulator = 0
    temp_string = ''.join(sorted(filtered.keys()))
    for i, c in enumerate(temp_string):
        bonus_accumulator += (i + 1) * (ord(c) % 7)
    
    # Misleading intermediate calculation (distractor)
    dummy_score = 0
    for ch in temp_string:
        if ch in 'aeiou':
            dummy_score += 3
        else:
            dummy_score += 1
    dummy_score = (dummy_score * 17) % 19  # Irrelevant to final result
    
    # Final composition
    adjustment_factor = limits['adjustment']
    preliminary_score = masked_entropy + bonus_accumulator
    final_score = preliminary_score * adjustment_factor
    
    # Extra unused variables (distraction)
    unused_metrics = {
        'peak': max(norm_probs.values(), default=0),
        'spread': len(norm_probs),
        'rare_count': sum(1 for v in norm_probs.values() if v < 0.02)
    }
    
    # Dead code path (never executed)
    if False:
        fallback = sum(ord(x) for x in unused_metrics.keys())
        final_score = fallback
    
    return int(final_score)

# Main execution
log_input = "DynamicAnalysisEngine::Initiated|DataFlowTracingEnabled|XRayModeActive"
thresholds = {
    'freq_threshold': 0.045,
    'adjustment': 3
}

intermediate_result = normalize_values({'x': 1, 'y': 1, 'z': 1})  # Unused normalization

final_score = calculate_final_score(log_input, thresholds)
print(f"Result: {final_score}")