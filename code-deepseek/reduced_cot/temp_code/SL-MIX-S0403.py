def score_processor(data, cutoff):
    irrelevant_data = [i**2 for i in range(10)]
    misleading_sum = sum(irrelevant_data)
    
    temp_scores = [x for x in data if x >= cutoff]
    dead_code = [x*2 for x in data if x < cutoff]
    
    score_filter = lambda x: x > 0
    filtered_scores = list(filter(score_filter, temp_scores))
    
    redundant_calc = max(data) - min(data) if len(data) > 1 else 0
    if len(filtered_scores) == 0:
        return -1
    
    average_score = sum(filtered_scores) / len(filtered_scores)
    
    misleading_adjustment = (misleading_sum % 100) / 10
    intermediate = average_score + misleading_adjustment
    
    final_multiplier = 1.5 if len(filtered_scores) > 2 else 0.8
    final_score = intermediate * final_multiplier
    
    print(f"Target result: {final_score}")

scores = [85, 92, 78, 65, 88, 95, 42, 73]
threshold = 70
final_score = score_processor(scores, threshold)