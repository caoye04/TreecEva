def analyze_text_patterns(text_list):
    char_frequency = {}
    total_chars = 0
    for text in text_list:
        for char in text.lower():
            if char.isalpha():
                char_frequency[char] = char_frequency.get(char, 0) + 1
                total_chars += 1

    # Distractor: Compute average length (not used later)
    lengths = [len(t) for t in text_list]
    avg_length = sum(lengths) / len(lengths) if lengths else 0

    normalized_freq = {k: v / total_chars for k, v in char_frequency.items()}
    return normalized_freq


def filter_relevant_features(freq_dict, threshold=0.05):
    # Use lambda to filter significant characters
    significant = dict(filter(lambda item: item[1] > threshold, freq_dict.items()))
    irrelevant = dict(filter(lambda item: item[1] <= threshold, freq_dict.items()))

    # Distractor: process irrelevant (dead computation)
    penalty_score = 0
    for val in irrelevant.values():
        penalty_score += val * 10

    return significant


def compute_entropy(values):
    import math
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log2(v)
    return entropy


def calculate_final_score(data):
    frequencies = analyze_text_patterns(data)
    relevant = filter_relevant_features(frequencies, threshold=0.08)
    
    # Additional distractor variables
    temp_sum = sum([v * 100 for v in frequencies.values()])
    debug_info = {'total_entries': len(frequencies), 'filtered': len(relevant)}
    
    entropy = compute_entropy(relevant.values())
    score_components = [entropy * 100]
    
    # Secondary scoring via list comprehension (semi-relevant)
    bonuses = [10 for char in relevant.keys() if char in 'aeiou']
    score_components.extend(bonuses)
    
    final_score = sum(score_components) + len(relevant) * 5
    return final_score

# Input data
input_texts = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick daft zebras jump!"
]

# Processing pipeline
processed_data = input_texts
intermediate_result = analyze_text_patterns(processed_data)
filtered_features = filter_relevant_features(intermediate_result)
entropy_value = compute_entropy(filtered_features.values())
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")