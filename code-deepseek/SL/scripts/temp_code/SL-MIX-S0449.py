def analyze_text_scores(text_samples):
    # Initialize base metrics
    base_scores = [len(sample) for sample in text_samples]
    processed_scores = []
    
    # Process each score with some intermediate calculations
    for score in base_scores:
        # Some intermediate calculations that don't affect final result
        temp_adj = score * 1.5
        normalized = temp_adj / 2
        irrelevant_calc = normalized + 100
        
        # Actual relevant processing
        if score > 10:
            processed = score - 5
        else:
            processed = score + 3
        processed_scores.append(processed)
    
    # More intermediate operations
    total_sum = sum(processed_scores)
    avg_length = total_sum / len(processed_scores)
    
    # Unused variable that looks relevant
    weighted_avg = avg_length * 1.2
    
    # Final relevant calculation
    processed_data = {
        'total': total_sum,
        'average': avg_length,
        'max': max(processed_scores)
    }
    
    # Key execution point
    final_score = processed_data.get('total', 0)
    print(f"Result: {final_score}")
    return final_score

# Test data
text_samples = ['hello', 'world', 'python', 'programming', 'language']
result = analyze_text_scores(text_samples)