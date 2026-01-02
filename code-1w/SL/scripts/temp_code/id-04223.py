def analyze_performance(raw_marks, weight_factor):
    adjusted_marks = [mark * weight_factor for mark in raw_marks]
    total = sum(adjusted_marks)
    averages = [round(x / len(adjusted_marks), 2) for x in adjusted_marks]
    normalized_scores = [avg / (total / 100) for avg in averages]
    
    # Irrelevant tracking variable (minor distractor)
    record_count = len(raw_marks)
    
    threshold_score = max(normalized_scores)
    return threshold_score

# Main execution
raw_data = [88, 92, 76, 85, 89]
scaling = 1.1
result = analyze_performance(raw_data, scaling)
threshold_score = result
print(f"Result: {threshold_score}")