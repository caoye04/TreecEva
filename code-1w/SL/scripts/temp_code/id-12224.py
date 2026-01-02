def analyze_pattern(sequence):
    frequency = {}
    for char in sequence:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def filter_noise(frequency_map, threshold=2):
    cleaned = {}
    total_count = 0
    for k, v in frequency_map.items():
        if v >= threshold:
            cleaned[k] = v
            total_count += v
    return cleaned, total_count


def compute_entropy(counts):
    import math
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 4)


def compute_final_score(data, weights):
    # Step 1: Analyze character frequencies
    freq_map = analyze_pattern(data)
    
    # Distractor: Calculate entropy (not used in final score)
    entropy = compute_entropy(freq_map)
    
    # Step 2: Filter out low-frequency characters
    filtered_map, valid_total = filter_noise(freq_map, threshold=1)
    
    # Distractor: Unused transformation
    squared_weights = {k: w**2 for k, w in weights.items()}
    adjusted_data = ''.join([ch for ch in data if ch in filtered_map])
    
    # Step 3: Apply weights to remaining characters
    raw_score = 0
    for char in adjusted_data:
        if char in weights:
            raw_score += weights[char]

    # Step 4: Normalize by length (only if non-empty)
    normalization_factor = len(adjusted_data) if adjusted_data else 1
    normalized_score = raw_score / normalization_factor
    
    # Step 5: Apply bonus if all weight keys are present
    coverage_bonus = 1.0
    for key in weights:
        if key in filtered_map:
            coverage_bonus += 0.1
    
    # Final computation
    final_score = int(normalized_score * coverage_bonus * 10)
    
    # Irrelevant tracking
    debug_log = f'Score computed with {len(filtered_map)} unique chars, entropy={entropy}'
    
    return final_score

# Main execution
if __name__ == '__main__':
    input_sequence = "aabbcddddeeeeeffggggg"
    importance_weights = {'a': 2, 'b': 3, 'c': 1, 'd': 4, 'e': 5, 'x': 99, 'z': 100}  # Some weights not in data
    
    # Unused preprocessing
    reversed_seq = input_sequence[::-1]
    token_chunks = [input_sequence[i:i+3] for i in range(0, len(input_sequence), 3)]
    chunk_lengths = [len(chunk) for chunk in token_chunks]
    
    final_score = compute_final_score(input_sequence, importance_weights)
    print(f"Result: {final_score}")