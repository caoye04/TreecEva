from collections import Counter

def analyze_text_patterns(text_samples):
    # Irrelevant text processing setup
    sample_sizes = [len(sample) for sample in text_samples]
    avg_size = sum(sample_sizes) / len(sample_sizes) if sample_sizes else 0
    
    # Misleading character frequency analysis (distractor)
    char_counter = Counter()
    for sample in text_samples:
        char_counter.update(sample.lower())
    most_common_chars = char_counter.most_common(3)
    
    # Actual relevant computation
    vowel_counts = []
    vowels = set('aeiou')
    for sample in text_samples:
        vowel_count = sum(1 for char in sample.lower() if char in vowels)
        vowel_counts.append(vowel_count)
    
    # More irrelevant calculations
    consonant_ratio = sum(len(s) - vc for s, vc in zip(text_samples, vowel_counts)) / sum(len(s) for s in text_samples) if text_samples else 1.0
    
    # Dead code path - never executed
    if len(text_samples) > 100:
        scaling_factor = 2.5
    else:
        scaling_factor = 1.0
    
    # Key logic chain
    base_metric = sum(vowel_counts) * 3
    quality_adjustment = max(vowel_counts) * 2 if vowel_counts else 0
    
    # Misleading intermediate variable
    processing_overhead = base_metric // 4 + len(text_samples) * 7
    
    # Final computation chain
    processed_data_tracker = base_metric - processing_overhead
    correction_factor = 1.5 if avg_size > 10 else 2.0
    
    # Target statement
    final_analysis_result = processed_data_tracker * correction_factor - quality_adjustment
    
    # Print irrelevant results (distraction)
    print(f"Character analysis: {most_common_chars}")
    print(f"Consonant ratio: {consonant_ratio:.3f}")
    print(f"Processing overhead: {processing_overhead}")
    
    return final_analysis_result

# Test data
text_corpus = ["algorithmic complexity", "data structures", "computational thinking", "programming paradigms"]

# Unused variables (distractors)
backup_corpus = ["machine learning", "neural networks"]
temp_buffer_size = len(text_corpus) * 25
cache_hit_ratio = 0.85

# Main execution
result = analyze_text_patterns(text_corpus)

# More irrelevant computations
validation_check = sum(len(s) for s in text_corpus) * 0.1
performance_metric = validation_check * 3.2

print(f"Result: {result}")