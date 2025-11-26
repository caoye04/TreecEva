def evaluate_performance(data_strings):
    quality_scores = []
    efficiency_values = []
    
    for data_str in data_strings:
        # Calculate quality score based on string length and content
        base_quality = len(data_str.strip())
        vowel_count = sum(1 for char in data_str.lower() if char in 'aeiou')
        quality_score = base_quality * 2 + vowel_count
        quality_scores.append(quality_score)
        
        # Calculate efficiency (distractor - not used in final result)
        digit_count = sum(1 for char in data_str if char.isdigit())
        efficiency = digit_count * 3
        efficiency_values.append(efficiency)
    
    # Process quality scores
    max_quality = max(quality_scores) if quality_scores else 0
    min_quality = min(quality_scores) if quality_scores else 0
    quality_range = max_quality - min_quality
    
    # Calculate final metrics
    quality_score = sum(quality_scores) // len(quality_scores) if quality_scores else 0
    efficiency_bonus = 5 if quality_range > 10 else 2
    multiplier = 3 if max_quality > 25 else 1
    
    # Distractor calculations that don't affect final result
    unused_metric = sum(efficiency_values) * 2
    temp_adjustment = len(data_strings) * 4
    
    # Key calculation
    final_score = (quality_score + efficiency_bonus) * multiplier
    
    print(f"Target result: {final_score}")
    return final_score

# Test data
data_samples = ["Project Alpha", "Task Beta v2", "Operation Gamma 3.0", "Analysis Delta"]
result = evaluate_performance(data_samples)