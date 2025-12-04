import itertools

def analyze_text_complexity(text_samples):
    # Distractor: Complex preprocessing that doesn't affect final calculation
    word_counts = [len(sample.split()) for sample in text_samples]
    avg_word_lengths = [sum(len(word) for word in sample.split()) / len(sample.split()) for sample in text_samples]
    
    # Relevant calculation: Find longest word across all samples
    all_words = list(itertools.chain(*[sample.split() for sample in text_samples]))
    max_word_length = max(len(word) for word in all_words) if all_words else 0
    
    # Distractor: Unused complexity metrics
    sentence_complexity = sum(1 for word in all_words if len(word) > 6)
    vocabulary_richness = len(set(all_words)) / len(all_words) if all_words else 0
    
    # Key calculation: Process data with logical operations
    base_score = max_word_length * 3
    has_long_words = any(len(word) > 10 for word in all_words)
    
    # Conditional processing
    if has_long_words and base_score > 15:
        processed_data = base_score - 2
    else:
        processed_data = base_score + 1
    
    # Final calculation with distractor
    penalty_factor = 0.85 if len(text_samples) > 2 else 1.0
    readability_index = sum(word_counts) * 0.5  # Unused distractor
    
    final_score = processed_data * penalty_factor
    print(f"Target result: {final_score}")
    return final_score

# Test data
text_samples = [
    "The quick brown fox jumps over the lazy dog",
    "Programming languages require precise syntax and logical structure",
    "Complex algorithms demonstrate computational thinking processes"
]

analyze_text_complexity(text_samples)