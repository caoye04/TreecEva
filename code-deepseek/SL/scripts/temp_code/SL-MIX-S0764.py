def analyze_string(text):
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = len(text) - vowel_count
    length_factor = len(text) * 0.5
    return vowel_count, consonant_count, length_factor

def process_data(input_text, limit):
    v_count, c_count, factor = analyze_string(input_text)
    
    # Relevant calculations
    ratio = v_count / max(c_count, 1)
    weighted_sum = v_count * 2 + c_count * 1.5
    
    # Distractor calculations that don't affect final result
    temp_multiplier = len(input_text.strip()) * 0.3
    unused_calc = (v_count + c_count) ** 1.2
    
    if ratio > 0.5:
        result = weighted_sum * factor
    else:
        result = weighted_sum / factor
    
    # Filter based on threshold
    if result > limit:
        result = result - (limit * 0.2)
    
    return round(result, 2)

sample_text = "DataAnalyticsPipeline"
threshold = 25
final_metric = process_data(sample_text, threshold)
print(f"Target result: {final_metric}")