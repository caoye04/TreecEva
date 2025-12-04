from collections import defaultdict

def analyze_pattern(text_data):
    char_freq = defaultdict(int)
    temp_sum = 0
    for char in text_data:
        char_freq[char] += 1
        temp_sum += ord(char)  # Misleading calculation
    
    # Irrelevant processing
    normalized = lambda x: x * 2 - 1
    processed = [normalized(ord(c)) for c in text_data[:3]]
    
    return len(char_freq), temp_sum

def validate_input(input_data):
    checksum = 0
    for item in input_data:
        checksum = (checksum << 3) | (ord(item) % 8)
    
    # Dead code path
    if checksum > 1000:
        backup_calc = sum(ord(c) for c in input_data[::-1])
        return backup_calc
    
    return checksum

def process_data(data_stream):
    pattern_result, _ = analyze_pattern(data_stream)
    validation_hash = validate_input(data_stream)
    
    # Misleading intermediate variables
    interim_value = pattern_result * 7
    adjustment = (validation_hash >> 2) & 0xF
    
    # Distractor calculation
    noise_factor = sum(1 for c in data_stream if c.isupper())
    if noise_factor > 2:
        interim_value -= 5  # Never executed with given input
    
    # Key logic
    core_metric = pattern_result + (interim_value % 13)
    result = core_metric - adjustment
    
    # Final adjustment with bitwise operations
    final_metric = (result ^ 0b1010) & 0x1F
    
    return final_metric

# Main execution with distractor variables
validation_set = "abc123XYZ"
prelim_check = validate_input(validation_set[:4])
backup_analysis = analyze_pattern(validation_set[3:])

# Irrelevant processing chain
secondary_metric = (prelim_check * 3) // 2
if secondary_metric > 50:
    tertiary_adjust = secondary_metric % 11
else:
    tertiary_adjust = secondary_metric // 3

final_metric = process_data(validation_set)
print(f"Result: {final_metric}")