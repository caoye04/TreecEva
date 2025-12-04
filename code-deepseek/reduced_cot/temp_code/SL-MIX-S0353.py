from collections import Counter

def analyze_text_patterns(text_data):
    # Distractor: String processing that doesn't affect final result
    words = text_data.split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(3)
    
    # Misleading intermediate calculations
    temp_sum = sum(len(word) for word in words)
    avg_length = temp_sum / len(words) if words else 0
    
    # Dead code path - never executed
    if avg_length > 10:
        unused_var = "long_words"
    else:
        unused_var = "short_words"
    
    # Relevant numeric processing
    numeric_values = [ord(char) for char in text_data if char.isalpha()]
    
    # Key statement with bitwise operations and lambda
    processed_data = list(map(lambda x: (x[0] ^ x[1]) & 0xFF, zip(numeric_values, reversed(numeric_values))))
    
    # More distractor operations
    max_val = max(processed_data) if processed_data else 0
    min_val = min(processed_data) if processed_data else 0
    range_val = max_val - min_val
    
    # Actual target calculation
    final_result = sum(processed_data) % 256
    
    # Print irrelevant values for distraction
    print(f"Word analysis: {most_common}")
    print(f"Average length: {avg_length:.2f}")
    print(f"Range of processed data: {range_val}")
    
    # Final answer
    print(f"Result: {final_result}")
    return final_result

# Main execution with realistic data
sample_text = "Programming evaluation benchmark for LLM reasoning capabilities"
analyze_text_patterns(sample_text)