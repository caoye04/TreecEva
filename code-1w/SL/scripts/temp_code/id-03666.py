def process_results(data, threshold):
    # Irrelevant transformation (distractor)
    normalized = [x * 1.05 for x in data if x > 0]
    adjusted = [int(x) for x in normalized]

    # Core logic begins
    filtered = [score for score in data if score >= threshold]
    unique_scores = set(filtered)
    sorted_scores = sorted(unique_scores, reverse=True)

    # Secondary filtering based on parity (semi-relevant)
    even_suppressed = [val for val in sorted_scores if val % 2 != 0] or [0]

    # Weighted contribution calculation
    weights = [0.5 ** i for i in range(len(even_suppressed))]
    weighted_sum = sum(even_suppressed[i] * weights[i] for i in range(len(even_suppressed)))

    # Dummy state tracking (distractor)
    stats = {
        'max_raw': max(data),
        'min_raw': min(data),
        'count_above': len([x for x in data if x > threshold]),
        'fake_metric': sum(1 for x in data if x % 7 == 0)
    }

    # Decision logic with conditional expression
    base_result = weighted_sum if len(even_suppressed) > 1 else even_suppressed[0] * 1.5

    # Final adjustment using bitwise masking (obscure but deterministic)
    masked_result = int(base_result) & 0xFF  # Keep only last 8 bits

    # Key assignment
    final_score = masked_result + 10
    return final_score

# Input data
assessment_data = [88, 91, 76, 91, 45, 67, 88, 73, 95, 54, 67, 88, 76]
passing_threshold = 75

# Execute
final_score = process_results(assessment_data, passing_threshold)
print(f"Result: {final_score}")