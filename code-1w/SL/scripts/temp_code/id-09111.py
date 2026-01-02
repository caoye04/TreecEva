from collections import defaultdict, Counter

def analyze_text_patterns(text_blocks):
    char_freq = defaultdict(int)
    bigram_count = Counter()
    total_chars = 0
    
    for block in text_blocks:
        cleaned = block.strip().lower()
        total_chars += len(cleaned)
        
        for i in range(len(cleaned) - 1):
            bigram = cleaned[i:i+2]
            if bigram.isalpha():
                bigram_count[bigram] += 1

        for char in cleaned:
            if char.isalpha():
                char_freq[char] += 1

    return char_freq, bigram_count, total_chars

def normalize_scores(raw_freq, total):
    normalized = {}
    for k, v in raw_freq.items():
        normalized[k] = round(v / total, 5) if total else 0
    return normalized

def filter_relevant_features(freq_dict, threshold=0.01):
    return {k: v for k, v in freq_dict.items() if v >= threshold}

def compute_entropy(values):
    import math
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log2(v)
    return round(entropy, 4)

def calculate_complexity_index(data_list):
    size_metric = len(data_list)
    variance_proxy = sum((i - size_metric/2)**2 for i in range(size_metric))
    complexity = size_metric * 2 + int(variance_proxy % 77)
    return complexity

def calculate_final_score(processed_data):
    base_score = sum(processed_data.values()) * 100
    adjustment = len(processed_data) * 1.5
    raw_score = base_score - adjustment
    
    # Irrelevant transformation
    temp_transform = [ord(k[0]) * v for k, v in processed_data.items() if isinstance(k, str)]
    dummy_reduction = sum(temp_transform) / 1000 if temp_transform else 0
    
    final_score = int(raw_score - dummy_reduction)  # Final assignment point
    return final_score

# Main execution
if __name__ == '__main__':
    input_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Pack my box with five dozen liquor jugs.",
        "How vexingly quick daft zebras jump!"
    ]

    frequencies, bigrams, total_length = analyze_text_patterns(input_texts)

    # Normalize character frequencies
    normalized_freq = normalize_scores(frequencies, total_length)
    
    # Filter to keep only meaningful characters
    filtered_features = filter_relevant_features(normalized_freq, threshold=0.02)
    
    # Compute auxiliary metrics (not used in final score but look relevant)
    entropy_value = compute_entropy(list(filtered_features.values()))
    complexity_index = calculate_complexity_index(list(filtered_features.keys()))
    
    # Simulate feature weighting
    weighted_contributions = {}
    for ch, score in filtered_features.items():
        weight = 1 + (ord(ch) % 5)
        weighted_contributions[ch] = score * weight
    
    # This line has no effect on final_score but looks important
    shadow_copy = {k.upper(): v for k, v in weighted_contributions.items()}
    
    # Key statement: final_score computation
    final_score = calculate_final_score(weighted_contributions)
    
    print(f"Result: {final_score}")