from collections import defaultdict

# Simulate student test results with multiple sections
def evaluate_performance(raw_data):
    scores = {}
    bonus_points = 0
    total_submissions = 0

    for section, attempts in raw_data.items():
        correct_count = 0
        max_attempts = len(attempts)
        total_submissions += max_attempts

        # Compute section accuracy
        for outcome in attempts:
            if outcome == 'pass':
                correct_count += 1

        accuracy = correct_count / max_attempts if max_attempts > 0 else 0
        scaled_score = int(accuracy * 100)

        # Award bonus for perfect sections (distractor logic)
        if scaled_score == 100:
            bonus_points += 2  # Not actually used later

        scores[section] = scaled_score

    return scores

# Apply weighting and compute composite score
def compute_final_score(section_scores, weight_map):
    weighted_sum = 0.0
    total_weight = 0.0
    penalty = 0.0

    # Misleading normalization step
    normalized_scores = {k: v / 100.0 for k, v in section_scores.items()}

    for sec, score in normalized_scores.items():
        if sec in weight_map:
            weight = weight_map[sec]
            weighted_sum += score * weight
            total_weight += weight

            # Artificial penalty for low performance (never triggered here)
            if score < 0.5:
                penalty += 5

    # Final computation
    final_raw = (weighted_sum / total_weight) * 100 if total_weight > 0 else 0
    return int(final_raw + 0.5)  # Round to nearest integer

# Main execution flow
if __name__ == '__main__':
    # Input data: student outcomes per test section
    submission_log = {
        'algebra': ['pass', 'pass', 'fail', 'pass'],
        'geometry': ['pass', 'pass', 'pass', 'pass'],
        'calculus': ['fail', 'pass', 'pass', 'fail', 'pass']
    }

    # Weighting schema for final evaluation
    section_weights = {
        'algebra': 3,
        'geometry': 2,
        'calculus': 4
    }

    # Irrelevant aggregation (distractor)
    all_results = []
    for k, v in submission_log.items():
        all_results.extend(v)
    unique_outcomes = set(all_results)  # Unused downstream

    # Step 1: Evaluate per-section performance
    results = evaluate_performance(submission_log)

    # Tracking auxiliary metrics (dead code path)
    summary_stats = defaultdict(int)
    for key, val in results.items():
        if val >= 75:
            summary_stats['high'] += 1
        else:
            summary_stats['low'] += 1

    # Step 2: Compute final weighted score
    final_score = compute_final_score(results, section_weights)

    # Print result as required
    print(f"Result: {final_score}")