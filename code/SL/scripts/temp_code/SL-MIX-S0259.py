def analyze_string_patterns(text_input):
    vowel_count = sum(1 for char in text_input if char.lower() in 'aeiou')
    consonant_count = sum(1 for char in text_input if char.lower() in 'bcdfghjklmnpqrstvwxyz')
    ratio_analysis = vowel_count / consonant_count if consonant_count > 0 else 0
    
    text_length = len(text_input)
    length_factor = text_length * 2 if text_length > 10 else text_length * 3
    
    sample_data = "processing completed"
    status_check = sample_data.upper() if ratio_analysis > 0.5 else sample_data.lower()
    
    final_computation = (vowel_count * length_factor) - (consonant_count * 2)
    computation_result = final_computation
    
    print(f"Target result: {computation_result}")

analyze_string_patterns("algorithmic computation")