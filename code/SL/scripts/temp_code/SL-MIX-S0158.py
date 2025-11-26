from collections import Counter

def analyze_text_patterns(text_data):
    words = text_data.lower().split()
    word_counts = Counter(words)
    
    # Distractor operations
    total_chars = sum(len(word) for word in words)
    avg_length = total_chars / len(words) if words else 0
    
    # Core logic with conditional expressions
    target_words = ['data', 'analysis', 'processing']
    matching_count = sum(word_counts[word] for word in target_words if word in word_counts)
    
    # Additional distractor processing
    unique_ratio = len(word_counts) / len(words) if words else 0
    processed_count = matching_count * 2 if matching_count > 0 else 1
    
    # More distraction with bitwise operations
    bit_check = processed_count & 3
    adjustment = 5 if bit_check == 1 else 2
    
    final_result = processed_count + adjustment
    print(f"Target result: {final_result}")

# Test data
text_sample = "Data analysis requires careful data processing and thorough data validation"
analyze_text_patterns(text_sample)