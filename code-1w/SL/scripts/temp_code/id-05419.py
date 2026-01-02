def analyze_text_segment(segment):
    char_count = len(segment)
    vowel_count = sum(1 for c in segment.lower() if c in 'aeiou')
    # Irrelevant intermediate calculation
    entropy_approx = char_count * 0.5 if char_count > 0 else 0
    return char_count, vowel_count


def extract_features(text_blocks):
    features = []
    total_chars = 0
    
    for block in text_blocks:
        if len(block) < 5:
            continue  # Skip short blocks
        
        # Process block
        temp_data = block.strip().upper()
        segment_a = temp_data[:len(temp_data)//2]
        segment_b = temp_data[len(temp_data)//2:]
        
        count_a, vowels_a = analyze_text_segment(segment_a)
        count_b, vowels_b = analyze_text_segment(segment_b)
        
        # Semi-relevant aggregation
        block_score = (vowels_a * 2) + (vowels_b * 3)
        features.append(block_score)
        
        # Distractor: accumulating but not used directly
        total_chars += len(block)
        overflow_flag = total_chars > 1000

    return features


def calculate_final_score(data_list):
    base = sum(data_list)
    adjustment = len(data_list) * 1.5
    
    # Extra logic that looks important but doesn't alter final path
    if base > 50:
        adjustment += 10
    elif base > 20:
        adjustment += 5
    else:
        adjustment += 1
    
    # Final computation
    result = base + adjustment
    
    # Dead code path - misleading
    if False:
        result = result ** 0.5
        
    return int(result)

# Main execution
raw_texts = [
    "hello world programming is fun",
    "data analysis with python",
    "complex reasoning required here",
    "short", 
    "artificial intelligence and machine learning"
]

processed_data = extract_features(raw_texts)

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")