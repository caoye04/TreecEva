def analyze_performance(scores, threshold=75):
    # Irrelevant transformation: convert to uppercase (distractor for string handling)
    score_labels = ["Pass" if s >= threshold else "Fail" for s in scores]
    label_set = set(label.upper() for label in score_labels)  # Distractor set operation

    # Semi-relevant preprocessing: normalize scores to 0-1 scale
    max_score = max(scores)
    normalized = [s / max_score for s in scores]

    # Key metric: count how many are above normalized 0.8
    high_performers = len([n for n in normalized if n > 0.8])

    # Distractor: unused statistical computation
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    variance_proxy = sum((n - avg_normalized) ** 2 for n in normalized) / len(normalized) if normalized else 0

    return high_performers


def calculate_final_score(raw_data, bonus_factor=1.5):
    # Extract numeric scores from mixed data using lambda (required feature)
    get_numeric = lambda x: x['score'] if isinstance(x, dict) and 'score' in x else 0
    numeric_scores = [get_numeric(item) for item in raw_data]

    # Remove zero entries (could be noise)
    filtered_scores = [s for s in numeric_scores if s > 0]

    # Distractor: reverse list but don't use it
    reversed_order = filtered_scores[::-1]
    temp_sum = sum(reversed_order[:2]) * 0.1  # Minor red herring

    # Conditional expression (required feature): apply curve based on length
    adjustment = 10 if len(filtered_scores) >= 4 else 5

    # Analyze performance tier
    performance_tier = analyze_performance(filtered_scores, threshold=70)

    # Core logic chain
    base_score = sum(filtered_scores) // len(filtered_scores)  # Integer average
    bonus_points = performance_tier * bonus_factor
    curve_applied = base_score + adjustment

    # Final nonlinear transformation
    final_score = int(curve_applied + bonus_points + temp_sum // 2)

    # Critical execution point
    return final_score

# Input data with mixed types (realistic structure)
data_mixture = [
    {'score': 85, 'subject': 'math'},
    {'score': 92, 'subject': 'physics'},
    'invalid_entry',
    {'score': 78, 'subject': 'chemistry'},
    {'score': 96, 'subject': 'biology'},
    {'score': 88, 'subject': 'literature'},
    None,
    {'score': 65, 'subject': 'history'}  # Below threshold
]

# Execution entry point
target_result = calculate_final_score(data_mixture, bonus_factor=1.5)
print(f"Result: {target_result}")