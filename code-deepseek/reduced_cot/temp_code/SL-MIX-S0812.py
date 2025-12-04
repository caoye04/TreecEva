def analyze_string(text):
    # Distractor: unused character frequency calculation
    char_freq = {}
    for ch in text:
        char_freq[ch] = char_freq.get(ch, 0) + 1
    
    # Relevant: count vowels and consonants
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for ch in text if ch in vowels)
    consonant_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)
    
    # Misleading intermediate calculation
    temp_ratio = vowel_count / (consonant_count + 1) if consonant_count > 0 else 0
    
    # Distractor: unused string manipulation
    reversed_text = text[::-1]
    uppercase_count = sum(1 for ch in text if ch.isupper())
    
    return vowel_count, consonant_count, temp_ratio

def process_data(analysis_result):
    vowels, consonants, ratio = analysis_result
    
    # Distractor: unused lambda function
    square_lambda = lambda x: x * x
    
    # Relevant: bitwise operations and arithmetic
    bit_mask = (vowels << 2) | (consonants & 0b1111)
    
    # Misleading calculation path
    alt_calc = (vowels * 3 + consonants * 2) % 17
    
    # Relevant: logical operations and final computation
    if vowels > consonants:
        base_value = (vowels ^ consonants) + (vowels & consonants)
    else:
        base_value = (vowels | consonants) - (vowels ^ consonants)
    
    # Distractor: unused variable
    dead_result = base_value * ratio
    
    # Key calculation with bitwise XOR
    key_value = base_value ^ bit_mask
    
    # Final transformation
    result = (key_value * 3 - alt_calc) % 256
    
    return result

# Main execution
input_text = "ProgrammingEvaluationBenchmark"

# Distractor: unused processing
word_length = len(input_text)
word_sum = sum(ord(ch) for ch in input_text)

# Key statement
final_result = process_data(analyze_string(input_text))

print(f"Result: {final_result}")