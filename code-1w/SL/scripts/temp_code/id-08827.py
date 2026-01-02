def process_results(data):
    scaling_factor = 1.5
    bonus_threshold = 75
    base_adjustment = 10

    # Convert string scores to integers and apply case normalization
    numeric_scores = {k.lower(): int(v) for k, v in data.items()}

    # Calculate average score
    avg_score = sum(numeric_scores.values()) / len(numeric_scores)

    # Determine performance category using lambda
    categorize = lambda x: 'excellent' if x >= bonus_threshold else 'standard'
    perf_category = categorize(avg_score)

    # Apply scaling based on category
    if perf_category == 'excellent':
        scaled_score = avg_score * scaling_factor
    else:
        scaled_score = avg_score + base_adjustment

    # Minor irrelevant computation (distractor at intervention level 5)
    temp_result = len(numeric_scores.keys()) * 2  # Not used in final result

    # Final scoring with fixed offset
    final_score = int(scaled_score + 5)
    return final_score

# Input data with mixed-case keys and string values
assessment_data = {'Math': '88', 'Physics': '92', 'Chemistry': '76', 'Biology': '81'}

result = process_results(assessment_data)
print(f"Target result: {result}")