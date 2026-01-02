from collections import Counter
def calculate_final_score():
    scores = [85, 90, 78, 90, 82, 85, 93]
    score_count = Counter(scores)
    
    # Find most common score
    most_common_score = score_count.most_common(1)[0][0]
    
    # Calculate average
    average = sum(scores) / len(scores)
    
    # Apply adjustment: if mode > average, add difference to average
    adjusted_average = average + (most_common_score - average) if most_common_score > average else average
    
    # Final result is ceiling of adjusted average without using math.ceil for simplicity
    result = int(adjusted_average + 0.999)
    
    return result

# Irrelevant auxiliary variable (minimal distraction)
temp_log = "Processing complete"

result = calculate_final_score()
print(f"Target result: {result}")