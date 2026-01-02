def analyze_text_segments(text_blocks):
    word_frequencies = {}
    total_chars = 0
    segment_count = len(text_blocks)
    
    for i, block in enumerate(text_blocks):
        clean_block = block.strip().lower()
        words = clean_block.split()
        
        # Irrelevant statistic: track average word length (not used later)
        total_word_length = sum(len(word) for word in words)
        avg_word_length = total_word_length / len(words) if words else 0
        
        # Update frequency map using set logic to avoid duplicates per block
        unique_words_in_block = set(words)
        for word in unique_words_in_block:
            if word.isalpha():
                word_frequencies[word] = word_frequencies.get(word, 0) + 1
        
        # Distractor: accumulate character count across blocks (semi-relevant)
        total_chars += len(clean_block.replace(' ', ''))
    
    # Intermediate transformation with zip for alignment
    sorted_freqs = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    ranks = range(1, len(sorted_freqs) + 1)
    ranked_data = list(zip(ranks, sorted_freqs))
    
    # Return both meaningful and irrelevant data
    return word_frequencies, ranked_data, total_chars, segment_count


def filter_relevant_terms(freq_dict, min_occurrence=2):
    # Use set operations to isolate high-frequency terms
    valid_keys = {k for k, v in freq_dict.items() if v >= min_occurrence}
    filtered = {k: freq_dict[k] for k in valid_keys}
    
    # Dead code path - never accessed
    if False:
        debug_info = "Filtering complete."
        redundant_check = len(debug_info)
    
    return filtered


def calculate_final_score(data_list):
    base_value = 0
    adjustment_factor = 0.5
    
    for item in data_list:
        key = item[0]
        count = item[1]
        contribution = len(key) * count * adjustment_factor
        base_value += contribution
    
    # Additional logic that looks important but only minor impact
    if base_value > 10:
        base_value *= 1.1
    
    return int(base_value)

# Main execution
raw_segments = [
    "The signal integrity must be maintained.",
    "Integrity checking ensures signal quality.",
    "Quality assurance prevents signal degradation.",
    "Degradation analysis helps maintain integrity."
]

# Step 1: Analyze text segments
freq_map, ranked_info, char_total, seg_count = analyze_text_segments(raw_segments)

# Step 2: Filter terms appearing at least twice
relevant_terms = filter_relevant_terms(freq_map, min_occurrence=2)

# Step 3: Prepare data list from filtered items
processed_data = []
for term, count in relevant_terms.items():
    processed_data.append((term, count))

# Step 4: Calculate final score
final_score = calculate_final_score(processed_data)

# Output result
print(f"Result: {final_score}")