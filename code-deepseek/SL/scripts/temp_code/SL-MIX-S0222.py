def analyze_text_complexity(text_samples):
    word_counts = {}
    complexity_scores = {}
    adjusted_ranks = {}
    
    for sample_id, text in enumerate(text_samples):
        words = text.split()
        word_counts[sample_id] = len(words)
        
        # Distractor calculation - not used in final result
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        
        # Main logic - complexity based on word count
        if len(words) > 15:
            complexity_scores[sample_id] = len(words) * 2
        elif len(words) > 8:
            complexity_scores[sample_id] = len(words) + 5
        else:
            complexity_scores[sample_id] = max(len(words) - 2, 0)
    
    # Additional distractor processing
    temp_analysis = [score * 1.5 for score in complexity_scores.values()]
    
    # Core ranking logic
    sorted_samples = sorted(complexity_scores.items(), key=lambda x: x[1], reverse=True)
    
    for rank, (sample_id, score) in enumerate(sorted_samples, 1):
        adjusted_ranks[sample_id] = rank * 3 if score > 20 else rank + 1
    
    # Final calculation
    final_score = sum(adjusted_ranks.values())
    
    # More distractor operations
    debug_check = len(word_counts) + len(complexity_scores)
    
    print(f"Result: {final_score}")

# Test data
text_samples = [
    "The quick brown fox jumps over the lazy dog",
    "Artificial intelligence systems demonstrate remarkable capabilities",
    "Hello world",
    "Machine learning models require extensive training data and computational resources",
    "Python programming language"
]

analyze_text_complexity(text_samples)