def calculate_text_complexity(text_data):
    word_counts = {}
    total_letters = 0
    uppercase_chars = 0
    
    # Distractor: Irrelevant vowel counting
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    
    for word in text_data:
        # Main logic: count word frequencies
        word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1
        
        # Distractor: Character analysis (partially used)
        total_letters += len(word)
        uppercase_chars += sum(1 for char in word if char.isupper())
        
        # Dead code path: vowel analysis (unused result)
        vowel_count += sum(1 for char in word if char in vowels)
    
    # Calculate frequency score (used in final result)
    frequency_score = sum(count * len(word) for word, count in word_counts.items())
    
    # Distractor: Misleading intermediate calculations
    complexity_index = (total_letters * 2) - (uppercase_chars // 3)
    unused_metric = vowel_count * 0.75  # Never used
    
    # Core logic: normalization and adjustment
    normalized_total = frequency_score // len(text_data)
    adjustment_factor = (uppercase_chars % 7) * 2
    
    # Final calculation
    final_score = normalized_total + adjustment_factor
    
    # Print result
    print(f"Result: {final_score}")

# Input data
text_samples = ["Python", "Programming", "Benchmark", "Evaluation", "Programming", "PYTHON", "benchmark"]

# Execute function
calculate_text_complexity(text_samples)