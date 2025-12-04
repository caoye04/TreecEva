def process_data(data_string, min_length):
    # Process text data and count valid entries
    temp_words = data_string.split(',')
    word_list = [word.strip().lower() for word in temp_words]
    
    # Distractor: Unused intermediate calculation
    total_chars = sum(len(word) for word in word_list)
    
    # Main processing logic
    valid_words = [word for word in word_list if len(word) >= min_length]
    processed_count = len(valid_words)
    
    # Distractor: Additional unused operation
    avg_length = total_chars / len(word_list) if word_list else 0
    
    return processed_count

# Sample data processing
sample_data = "python, code, benchmark, test, ai, language, model"
threshold = 4

# Main execution
final_result = process_data(sample_data, threshold)
print(f"Result: {final_result}")