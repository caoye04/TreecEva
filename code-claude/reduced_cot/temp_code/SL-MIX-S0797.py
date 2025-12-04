import itertools

def analyze_student_performance(scores, threshold=65):
    # Calculate some statistics that aren't directly used
    avg_score = sum(scores) / len(scores) if scores else 0
    max_possible = 100 * len(scores)
    performance_ratio = sum(scores) / max_possible if max_possible else 0
    
    # Generate some additional data
    bonus_points = [5 if x > 90 else 3 if x > 80 else 0 for x in scores]
    penalty_points = [2 if x < 60 else 1 if x < 70 else 0 for x in scores]
    
    # Apply transformations to original scores
    adjusted_scores = [s + b - p for s, b, p in zip(scores, bonus_points, penalty_points)]
    
    # These operations don't affect the final result
    score_pairs = list(itertools.combinations(scores, 2))
    pair_differences = [abs(a - b) for a, b in score_pairs[:3]]
    
    # Core logic that determines the answer
    passing_scores = [score for score in adjusted_scores if score >= threshold]
    failing_scores = [score for score in adjusted_scores if score < threshold]
    
    # Create a set of unique scores and perform operations
    unique_scores = set(adjusted_scores)
    score_product = 1
    for score in list(unique_scores)[:2]:
        score_product *= score
    
    # Extract values based on conditions
    values = []
    for i, score in enumerate(passing_scores):
        if i % 2 == 0:
            values.append(score + 10)
        else:
            values.append(score - 5)
    
    # This sorting doesn't affect the final result
    sorted_values = sorted(values, reverse=True)
    
    # Filter values based on a condition
    filtered_values = [v for v in values if v % 3 != 0]
    
    # Calculate final result using slicing
    final_score = sum(filtered_values[::-2])
    
    # Additional calculations that don't affect the result
    alternative_score = sum(failing_scores) if failing_scores else score_product
    
    print(f"Result: {final_score}")
    return final_score

# Test with student scores
student_scores = [72, 85, 90, 63, 77]
result = analyze_student_performance(student_scores, threshold=70)