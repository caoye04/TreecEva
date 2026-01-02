def analyze_text_patterns(text_list):
    char_frequency = {}
    total_chars = 0
    for text in text_list:
        for char in text.lower():
            if char.isalpha():
                char_frequency[char] = char_frequency.get(char, 0) + 1
                total_chars += 1

    # Irrelevant computation: counts vowels but not used later
    vowel_count = sum(char_frequency.get(v, 0) for v in 'aeiou')
    average_frequency = total_chars / (len(char_frequency) or 1)

    normalized_scores = {
        ch: round((count / total_chars) * 100, 3)
        for ch, count in char_frequency.items()
    }
    return normalized_scores, average_frequency


def filter_relevant_entries(data_map, threshold=0.5):
    # Some entries are filtered based on arbitrary score
    filtered = {k: v for k, v in data_map.items() if sum(v.values()) > threshold}
    sorted_keys = sorted(filtered.keys())
    reindexed_data = {i: filtered[k] for i, k in enumerate(sorted_keys)}
    return reindexed_data


def compute_entropy(scores):
    import math
    entropy = 0.0
    total = sum(scores)
    if total == 0:
        return 0.0
    for s in scores:
        if s > 0:
            prob = s / total
            entropy -= prob * math.log(prob + 1e-9)
    return round(entropy, 4)


def calculate_final_score(dataset):
    all_scores = []
    temp_offsets = []
    for idx, entry in dataset.items():
        values = list(entry.values())
        all_scores.extend(values)
        if idx % 2 == 0:
            temp_offsets.append(sum(values) * 0.1)
    
    # Core logic contribution
    base_sum = sum(all_scores)
    offset_correction = sum(temp_offsets)
    
    # Dummy transformation chain
    intermediate = base_sum + offset_correction
    adjusted = intermediate * 0.95
    
    # Final decision gate
    if adjusted > 100:
        final_score = int(adjusted - 42)
    else:
        final_score = int(adjusted + 18)
    
    return final_score

# Main execution
raw_texts = [
    "Structure enhances clarity.",
    "Logic requires precision and focus.",
    "Reasoning chains build understanding."
]

# Step 1: Analyze character patterns
frequency_map, avg_freq = analyze_text_patterns(raw_texts)

# Step 2: Simulate multiple processing paths (some irrelevant)
dummy_transform = {k: {c: v.get(c, 0)*2 for c in 'xyz'} for k, v in frequency_map.items()}
dummy_vector = [sum(d.values()) for d in dummy_transform.values()]

# Only this path leads to result
processed_data = filter_relevant_entries({i: freq for i, (k, freq) in enumerate(frequency_map.items())}, threshold=0.35)

# Introduce side computation that looks important but isn't used
side_entropy = compute_entropy([v for d in processed_data.values() for v in d.values()])

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")