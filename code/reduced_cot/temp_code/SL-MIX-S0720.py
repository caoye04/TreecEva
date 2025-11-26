def text_processor(input_string):
    temp_upper = input_string.upper()
    temp_lower = input_string.lower()
    char_count = len(input_string)
    
    vowel_count = 0
    consonant_count = 0
    processed_chars = []
    
    for char in input_string:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel_count += 1
                processed_chars.append(char.upper())
            else:
                consonant_count += 1
                processed_chars.append(char.lower())
        else:
            processed_chars.append('*')
    
    unused_var = len(temp_upper) + len(temp_lower)
    
    return vowel_count, consonant_count, ''.join(processed_chars)

def main_processor(text_data):
    vowels, consonants, processed = text_processor(text_data)
    
    vowel_diff = abs(vowels - consonants)
    ratio_calc = vowels * 2 + consonants // 2
    
    intermediate_sum = vowels + consonants + len(processed)
    
    unused_computation = (vowels * consonants) % 7
    
    final_result = (vowel_diff * 3) + (consonants - vowels) + len(text_data)
    
    return final_result

text_data = "PythonProgramming2024"
final_count = main_processor(text_data)
print(f"Result: {final_count}")