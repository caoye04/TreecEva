def process_data(data_sequence):
    # Initial processing with string operations
    text_data = ''.join([str(x) for x in data_sequence if x % 2 == 0])
    
    # Intermediate calculations (some not directly used)
    char_count = len(text_data)
    digit_sum = sum(int(c) for c in text_data if c.isdigit())
    
    # Main logic with slicing and filtering
    relevant_chars = text_data[1:-1] if len(text_data) > 2 else text_data
    filtered_values = [ord(c) for c in relevant_chars if c.isalpha()]
    
    # Distractor: Unused intermediate calculation
    avg_value = sum(filtered_values) / len(filtered_values) if filtered_values else 0
    
    # Core processing with modulo and arithmetic
    processing_result = sum(filtered_values) % 100
    
    # Additional unused operation
    backup_calc = (digit_sum + char_count) // 3
    
    return processing_result

# Data preparation with mixed operations
raw_data = [8, 3, 12, 7, 16, 5, 4, 11]
clean_data = [x * 2 for x in raw_data if x > 4]

# Function call and result storage
final_analysis = process_data(clean_data)
print(f"Target result: {final_analysis}")