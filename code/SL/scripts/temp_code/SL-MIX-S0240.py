def process_cipher_text(text_data):
    # Irrelevant string processing (distractor)
    temp_chars = list(text_data)
    char_codes = [ord(c) for c in temp_chars]
    sum_codes = sum(char_codes)  # Dead code path - unused
    
    # Main encryption calculation
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_count = 0
    vowel_positions = []
    
    for idx, char in enumerate(text_data.lower()):
        if char.isalpha():
            if char in vowels:
                vowel_positions.append(idx)
            else:
                consonant_count += 1
    
    # Misleading intermediate calculations
    position_product = 1
    for pos in vowel_positions:
        position_product *= (pos + 1)  # +1 to avoid zero
    
    # Relevant calculation path
    base_score = consonant_count * len(vowel_positions)
    shift_value = position_product % 100  # Modulo to keep reasonable
    
    # Distractor operations
    fake_checksum = sum(ord(c) for c in text_data[:3])  # Unused
    redundancy_check = len(text_data) * 2 - 5  # Dead code
    
    # Core encryption logic
    if len(vowel_positions) > 0:
        encryption_score = base_score + shift_value
    else:
        encryption_score = base_score - 10  # Unreachable path
    
    # Final adjustment with bitwise operations
    adjustment_value = (encryption_score & 0b1111) | 0b1000
    
    # Target statement
    final_output = encryption_score + adjustment_value
    
    # Irrelevant final operations (distractors)
    verification_code = final_output % 37  # Unused
    debug_value = final_output * 2 - 15  # Dead code
    
    print(f"Target result: {final_output}")

# Execute with test data
process_cipher_text("CryptographicAnalysis")