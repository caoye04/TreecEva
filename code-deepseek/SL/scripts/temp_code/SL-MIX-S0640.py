def analyze_text_patterns(text_samples):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_count = 0
    irrelevant_counter = 0
    
    for char in text_samples.lower():
        if char.isalpha():
            irrelevant_counter += 1 if char in {'x', 'y', 'z'} else 0
            consonant_count += 1 if char not in vowels else 0
    
    # Misleading intermediate calculation
    temp_value = consonant_count * 3 + irrelevant_counter
    return consonant_count if consonant_count > 5 else consonant_count + 2

def process_numerical_data(base_value, modifier):
    bit_operations = base_value & 15 | (modifier << 2)
    intermediate_result = bit_operations ^ 7
    
    # Distractor operations that don't affect final result
    dead_calc = (intermediate_result * 2) // 3
    misleading_var = dead_calc + 10
    
    return intermediate_result if intermediate_result % 2 == 0 else intermediate_result - 1

def compute_final_value(data_source):
    text_analysis = analyze_text_patterns(data_source)
    numerical_processing = process_numerical_data(text_analysis, 3)
    
    # Key conditional expression using python feature
    adjustment = 5 if text_analysis > numerical_processing else 8
    
    # More irrelevant computations
    unused_var = (numerical_processing * adjustment) // 2
    red_herring = unused_var + 100
    
    final_result = (text_analysis + numerical_processing) * adjustment
    return final_result

# Main execution
sample_text = "ProgrammingEvaluationBenchmark"
processed_data = sample_text
final_output = compute_final_value(processed_data)

# Additional distracting operations that don't affect the answer
distraction_1 = len(sample_text) * 2
distraction_2 = distraction_1 - 15

print(f"Target result: {final_output}")