def analyze_character_pattern(sequence, offset=3):
    char_count = {}
    for char in sequence:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Extract frequencies and apply modular arithmetic with offset
    frequencies = [count * offset for count in char_count.values()]
    sum_with_offset = sum(frequencies)
    modulus = len(sequence) % 7 or 5
    total_mod = sum_with_offset % modulus
    
    return total_mod

# Main execution
data_stream = "abccbaa"
diagnostic_mode = True

if diagnostic_mode:
    result = analyze_character_pattern(data_stream, offset=2)
    Result: {result}