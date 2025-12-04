import collections

def analyze_text_quality(text_samples):
    # Red herring calculations
    char_count = sum(len(sample) for sample in text_samples)
    vowel_count = sum(sum(1 for c in sample.lower() if c in 'aeiou') for sample in text_samples)
    
    # Misleading intermediate results
    irrelevant_metric = (char_count * 3) - (vowel_count * 2) + 17
    distraction_value = irrelevant_metric % 23
    
    # Dead code path (never executed due to condition)
    if distraction_value > 100:
        unused_result = distraction_value * 2 + 5
    
    # Actual quality analysis
    word_lengths = [len(word) for sample in text_samples for word in sample.split()]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # More distractions
    temp_calc = (distraction_value + 7) * 3
    misleading_score = temp_calc // 2
    
    # Core quality calculation
    quality_score = round(avg_length * 10, 2)
    return quality_score

def filter_text_samples(texts):
    # Multiple irrelevant operations
    total_chars = sum(len(text) for text in texts)
    char_frequency = collections.Counter(''.join(texts))
    
    # Distracting intermediate steps
    most_common_count = char_frequency.most_common(1)[0][1] if char_frequency else 0
    ratio_calc = (total_chars * 3) // (most_common_count + 1)
    
    # Actual filtering logic
    filtered = [text for text in texts if len(text.split()) >= 2]
    
    # More red herrings
    unused_filter_metric = ratio_calc % 15
    distraction_list = [i * 2 for i in range(5)]
    
    return filtered

# Main execution with heavy interference
sample_texts = ["Python programming", "Code analysis", "Machine learning models", "A", "Data processing pipelines"]

# Irrelevant preprocessing
initial_lengths = [len(text) for text in sample_texts]
sum_initial = sum(initial_lengths)
product_initial = 1
for length in initial_lengths:
    product_initial *= (length + 1)

# Dead variable (never used)
unused_complex_metric = (sum_initial * product_initial) % 47

# Actual processing chain
filtered_text = filter_text_samples(sample_texts)
processed_quality = analyze_text_quality(filtered_text)

# Final calculation with distractions
intermediate_value = processed_quality * 1.5
temp_adjustment = (len(filtered_text) * 3) - 2
final_quality_score = round(intermediate_value + temp_adjustment, 2)

# More irrelevant computations that don't affect final result
final_distraction = (sum_initial + 15) * 2
another_unused = final_distraction // 3

print(f"Target result: {final_quality_score}")