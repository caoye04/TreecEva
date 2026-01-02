from collections import defaultdict

# Simulate student assessment scoring with weighted components
def calculate_final_score(weights, scores):
    weighted_total = 0.0
    normalization_factor = sum(weights.values())
    
    for component, weight in weights.items():
        if component in scores:
            weighted_total += weight * scores[component]
    
    return weighted_total / normalization_factor

# Irrelevant auxiliary data (minimal distraction, intervention level 5)
student_records = defaultdict(int)
student_records['temp_id'] = 999

# Core input data
exam_weights = {
    'midterm': 0.3,
    'final_exam': 0.5,
    'project': 0.2
}

raw_scores = {
    'midterm': 85,
    'final_exam': 92,
    'project': 78
}

# Computation of interest
final_score = calculate_final_score(exam_weights, raw_scores)

# Print result as required
print(f"Result: {final_score}")