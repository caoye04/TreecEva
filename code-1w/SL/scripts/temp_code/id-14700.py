def analyze_text_metrics(text_blocks):
    char_count = 0
    word_count = 0
    line_count = len(text_blocks)
    temp_ratio = 0.0
    
    stats = []
    for i, block in enumerate(text_blocks):
        words = block.split()
        block_words = len(words)
        block_chars = sum(len(w) for w in words)
        char_count += block_chars
        word_count += block_words
        
        if block_words > 0:
            avg_char_per_word = round(block_chars / block_words, 3)
        else:
            avg_char_per_word = 0
            
        # Distractor: irrelevant transformation
        case_swapped = ''.join(c.lower() if c.isupper() else c.upper() for c in block)
        swap_entropy = sum(1 for c in case_swapped if c.isalpha())
        
        stats.append({'index': i, 'words': block_words, 'chars': block_chars, 'avg': avg_char_per_word})
    
    # Distractor: unused intermediate calculation
    if char_count > 0:
        temp_ratio = round(word_count * 1.0 / char_count, 4)
    
    return stats, char_count, word_count, line_count


def filter_relevant_entries(raw_stats):
    filtered = []
    total_entries = len(raw_stats)
    cumulative_chars = 0
    
    for entry in raw_stats:
        if entry['words'] >= 2 and entry['avg'] >= 3.0:
            filtered.append(entry)
            cumulative_chars += entry['chars']
        else:
            # Dead code path with misleading logic
            dummy_value = entry['words'] ** 2 + 10
            continue
    
    # Distractor: semi-relevant aggregation
    indices = [e['index'] for e in filtered]
    index_sum = sum(indices)
    
    return filtered, cumulative_chars


def calculate_final_score(filtered_stats):
    base_score = 0
    penalty = 0
    
    # Use of zip and enumerate together
    for idx, (stat1, stat2) in enumerate(zip(filtered_stats, filtered_stats[1:])):
        diff = stat2['chars'] - stat1['chars']
        base_score += stat1['words'] * stat1['avg']
        if diff < 0:
            penalty += abs(diff) // 2
    
    # Final computation using last element
    if filtered_stats:
        last_entry = filtered_stats[-1]
        base_score += last_entry['avg'] * 10
    
    final_raw = int(base_score - penalty)
    
    # Distractor: extra transformations not affecting result
    checksum = sum([ord(c) for c in 'score']) % 100
    validation_key = (final_raw + checksum) % 97
    
    return final_raw

# Main execution
if __name__ == '__main__':
    input_texts = [
        "The quick brown fox jumps over the lazy dog",
        "Hello world in Python is simple and clean",
        "AI reasoning evaluation requires complex logic",
        "Short ok",
        "Another valid segment with sufficient length here",
        "X Y Z",  # Minimal words
        "Final block contains enough characters to qualify"
    ]
    
    # Step 1: Extract metrics
    all_stats, total_chars, total_words, lines = analyze_text_metrics(input_texts)
    
    # Step 2: Filter relevant ones based on criteria
    processed_data, effective_char_total = filter_relevant_entries(all_stats)
    
    # Step 3: Compute final score
    final_score = calculate_final_score(processed_data)
    
    print(f"Result: {final_score}")