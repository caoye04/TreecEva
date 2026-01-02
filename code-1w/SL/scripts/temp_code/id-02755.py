def evaluate_performance(feedback, criteria):
    # Normalize feedback strings
    cleaned = {f.strip().lower() for f in feedback if len(f) > 0}
    
    # Irrelevant distraction: processing unrelated metrics
    temp_stats = []
    for i in range(len(criteria)):
        temp_stats.append(i * 2 + 1)
    temp_stats = [x for x in temp_stats if x % 3 != 0]

    # Distractor computation: unused weight adjustment
    base_weight = 1.5
    adjusted_weight = base_weight * (1 + 0.1 * len(temp_stats))
    scaling_factor = len(cleaned) * 0.5 if len(cleaned) > 2 else 1.0

    # Core logic: count matches with key terms using set operations
    key_terms = {'excellent', 'outstanding', 'exceptional', 'superb'}
    bonus_terms = {'impressive', 'notable'}
    matched_key = cleaned & key_terms
    matched_bonus = cleaned & bonus_terms

    # Scoring with conditional weighting
    base_score = len(matched_key) * 10
    bonus_score = len(matched_bonus) * 3 if 'excellent' in matched_key else 0

    # Secondary condition affecting score
    if 'impressive' in matched_bonus and len(matched_key) >= 2:
        bonus_score += 5

    # Final aggregation
    raw_total = base_score + bonus_score
    final_score = int(raw_total * scaling_factor)

    # Dead code path - never executed under current logic
    if False:
        fallback = sum(ord(c) for c in str(final_score))
        final_score = fallback % 100

    return final_score

# Input data
feedback_input = ["  EXCELLENT  ", "impressive work", "average effort", "OUTSTANDING", ""]
benchmark = ["v1", "v2", "v3"]

# Execute main evaluation
temp_var = sorted(benchmark, key=lambda x: -len(x))
intermediate_result = len(temp_var) * 2
evaluation_snapshot = {k: intermediate_result for k in ['a', 'b']}

final_score = evaluate_performance(feedback_input, benchmark)
print(f"Result: {final_score}")