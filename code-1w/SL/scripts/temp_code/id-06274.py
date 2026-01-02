from collections import defaultdict

# Simulate student test results with multiple sections
def analyze_performance(raw_data):
    scores = []
    temp_buffer = []
    section_weights = {'math': 0.4, 'logic': 0.3, 'coding': 0.3}
    max_scores = defaultdict(int)
    total_questions = 0

    for category, attempts in raw_data.items():
        correct_count = 0
        for is_correct in attempts:
            if is_correct:
                correct_count += 1
            # Irrelevant accumulation (distractor)
            temp_buffer.append(is_correct)

        accuracy = correct_count / len(attempts) if attempts else 0
        weighted_score = accuracy * section_weights.get(category, 0)
        scores.append(weighted_score)

        # Track max per section (not used later - distractor)
        max_scores[category] = max(max_scores[category], accuracy)

        total_questions += len(attempts)

    # Unused normalization (dead computation)
    normalized_total = sum(max_scores.values()) / len(max_scores) if max_scores else 0

    return scores


def calculate_overall_score(result_list):
    base_scores = [round(s * 100, 2) for s in result_list]
    adjustment_factor = 1.1
    adjusted = []

    for val in base_scores:
        if val >= 85:
            adjusted.append(val * adjustment_factor)
        elif val >= 70:
            adjusted.append(val * 1.05)
        else:
            adjusted.append(val * 0.95)

    # Apply final aggregation
    raw_total = sum(adjusted)
    count_offset = len(adjusted) - 3  # Assume 3 sections
    final_aggregate = raw_total - (count_offset * 2)  # Small correction

    # Dead code: tracking unused stats
    outlier_check = [x for x in adjusted if x > 95]
    warning_flags = len(outlier_check) > 1

    return int(round(final_aggregate))

# Main execution
if __name__ == "__main__":
    # Input data: student responses by category
    response_log = {
        'math':  [True, True, False, True, True, False, True],
        'logic': [True, False, True, True, False, True],
        'coding': [False, True, True, True, False, True, True, False]
    }

    # Intermediate processing with side storage (some irrelevant)
    processing_chain = []
    intermediate_sum = 0
    for key in response_log:
        intermediate_sum += len(response_log[key])
        processing_chain.append(intermediate_sum)

    results = analyze_performance(response_log)
    final_score = calculate_overall_score(results)
    
    # Output target result
    print(f"Result: {final_score}")