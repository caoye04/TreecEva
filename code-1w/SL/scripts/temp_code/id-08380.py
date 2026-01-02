def analyze_text_patterns(text_blocks):
    char_frequency = {}
    total_chars = 0
    for block in text_blocks:
        for char in block.lower():
            if char.isalpha():
                char_frequency[char] = char_frequency.get(char, 0) + 1
                total_chars += 1

    frequency_scores = []
    for freq in char_frequency.values():
        score = (freq / total_chars) * 100
        frequency_scores.append(round(score, 3))

    return char_frequency, frequency_scores, total_chars


def filter_relevant_pairs(keys, values, threshold=2):
    # Misleading function - not used in final computation
    result = {}
    for k, v in zip(keys, values):
        if v > threshold:
            result[k] = v * 1.5
    return result


def compute_entropy(scores):
    import math
    entropy = 0.0
    for s in scores:
        if s > 0:
            p = s / 100
            entropy -= p * math.log2(p)
    return round(entropy, 4)


def compute_final_score(data_list):
    running_sum = 0
    temp_offset = len(data_list) % 7  # Distractor computation
    adjustment_factor = 0
    
    for i, item in enumerate(data_list):
        if i % 2 == 0:
            running_sum += item ** 0.5
        else:
            running_sum -= item // 4
        
        # Dead code path - never executed due to prior condition
        if i % 5 == 0 and False:
            adjustment_factor += item * 0.1

    # Additional irrelevant logic
    outlier_count = 0
    for val in data_list:
        if val > 50:
            outlier_count += 1

    # Core calculation
    base_score = running_sum + temp_offset
    final_score = int(base_score * 3.7) % 999
    
    # Unused state tracking
    log_entries = [f"Step {i}: {val}" for i, val in enumerate(data_list)]
    
    return final_score

# Main execution
raw_texts = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick daft zebras jump!"
]

freq_map, scores, total_len = analyze_text_patterns(raw_texts)

# Generate auxiliary data (some irrelevant)
unique_chars = set(freq_map.keys())
sorted_freq = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
enumerated_ranks = list(enumerate(sorted_freq))

# Extract values for processing
raw_values = [item[1] for item in sorted_freq]
high_freq_only = [v for v in raw_values if v > 4]

# Simulate signal noise (unused)
noise_sequence = []
for idx, val in enumerate(raw_values):
    noise_sequence.append(val * (idx % 3 + 1) - 2)

# Key data for final computation
processed_data = [x * 2 + 1 for x in high_freq_only]
processed_data.append(len(unique_chars))
processed_data.append(sum(raw_values[:3]))

# Misleading conditional block (no effect)
if len(processed_data) > 5:
    processed_data = processed_data[:-1]  # This doesn't execute as length is exactly 5

final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")