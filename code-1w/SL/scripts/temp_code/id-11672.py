def analyze_performance(raw_data, min_pass, bonus_eligible):
    # Irrelevant preprocessing (distractor)
    cleaned_data = [x for x in raw_data if isinstance(x, int) and x >= 0]
    outlier_count = 0
    temp_sum = 0
    for val in cleaned_data:
        if val > 100:
            outlier_count += 1
    
    # Semi-relevant stats (some used later)
    avg_raw = sum(raw_data) / len(raw_data)
    above_avg = [x for x in cleaned_data if x > avg_raw]
    adjustment_factor = 0.9 if len(above_avg) > 3 else 1.1
    
    # Core logic embedded with noise
    scaled_scores = []
    for score in cleaned_data:
        adjusted = score * adjustment_factor
        if adjusted > 100:
            adjusted = 100
        elif adjusted < 0:
            adjusted = 0
        scaled_scores.append(int(adjusted))
    
    # Distraction: unused transformation
    rank_map = {i: s for i, s in enumerate(sorted(scaled_scores, reverse=True))}
    max_rank = len(rank_map)
    
    # Bonus logic that looks important but only applies conditionally
    bonus_applied = False
    if bonus_eligible and min_pass <= 50:
        bonus_applied = True
        for i in range(len(scaled_scores)):
            if scaled_scores[i] >= 90:
                scaled_scores[i] = min(100, scaled_scores[i] + 5)
    
    return scaled_scores, avg_raw, bonus_applied


def process_results(log_entries, threshold):
    # Simulate result processing with red herrings
    status_flags = set()
    cumulative = 0
    count_passed = 0
    penalty = 0.0
    
    for entry in log_entries:
        if entry >= threshold:
            count_passed += 1
            cumulative += entry
        else:
            status_flags.add('fail')
    
    # Distracting control flow
    if count_passed == 0:
        final_avg = 0
    else:
        final_avg = cumulative / count_passed if cumulative > 0 else 0
    
    # Extra computation that doesn't affect output
    efficiency_ratio = (count_passed / len(log_entries)) * 100 if log_entries else 0
    normalized = round(final_avg * 1.05)  # Slight adjustment
    
    # Final scoring with misleading rounding
    base_score = int(round(normalized))
    extra_credit = 10 if 'special' in status_flags else 0  # never added
    final_score = base_score  # This is the actual result
    
    return final_score

# Main execution
raw_input = [88, 76, 92, 'N/A', -5, 94, 81, 73, 99, 105]
passing_threshold = 75

# Call analysis (intermediate step)
processed_scores, average_raw, bonus_used = analyze_performance(
    raw_input, min_pass=passing_threshold, bonus_eligible=False
)

# Key statement
final_score = process_results(processed_scores, passing_threshold)

print(f"Result: {final_score}")