def analyze_pattern(sequence):
    counts = {}
    for char in sequence:
        counts[char] = counts.get(char, 0) + 1
    return counts


def calculate_entropy(count_dict, total):
    import math
    entropy = 0.0
    for count in count_dict.values():
        if count > 0:
            prob = count / total
            entropy -= prob * math.log2(prob)
    return entropy


def filter_noisy_data(raw_data, min_threshold=2):
    # Simulate filtering out rare characters
    filtered = [item for item in raw_data if len(item) >= min_threshold]
    return filtered


def calculate_final_score(data_list, limits):
    temp_results = []
    total_length = 0
    redundant_sum = 0  # Distractor: not used later

    for i, entry in enumerate(data_list):
        analysis = analyze_pattern(entry)
        length = len(entry)
        total_length += length

        # Irrelevant nested loop (distractor)
        for j in range(min(2, len(entry))):
            if entry[j].isalpha():
                redundant_sum += ord(entry[j]) % 7

        # Semi-relevant computation
        if length > limits['max_len']:
            adjusted = limits['max_len']
        else:
            adjusted = length

        # Use of zip to pair keys and values (Python idiom)
        pairs = list(zip(analysis.keys(), analysis.values()))
        top_freq = max(analysis.values()) if analysis else 0

        # Dummy tracking variable
        snapshot = {"index": i, "size": adjusted, "dominance": top_freq}
        temp_results.append((adjusted, top_freq))
    
    # Core logic hidden among distractions
    raw_score = 0
    for size, freq in temp_results:
        raw_score += size * freq
    
    # Final score calculation — actual answer source
    final_score = raw_score // (len(temp_results) or 1)
    
    # Dead code path (distractor)
    if False:
        backup = sum(redundant_sum for _ in range(3))
        final_score = backup

    return final_score

# Main execution
if __name__ == '__main__':
    input_data = [
        "aabbc", "xxyyz", "hello", "world", "aaabb",
        "zzzxx", "python", "coding", "aaaac", "test"
    ]
    
    config = {
        'max_len': 5,
        'tolerance': 0.1
    }
    
    # Preprocessing step with enumerate (used appropriately)
    processed = []
    for idx, text in enumerate(input_data):
        if idx % 2 == 0:
            processed.append(text.lower())
        else:
            processed.append(text.upper())
    
    cleaned_data = filter_noisy_data(processed)
    
    # Actual target computation
    final_score = calculate_final_score(cleaned_data, config)
    
    # Print result as required
    print(f"Target result: {final_score}")