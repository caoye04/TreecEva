def calculate_final_score(data, thresh):
    # Preprocessing: filter and transform ranking data
    filtered_ranks = [x for x in data if x > 0]
    rank_sum = sum(filtered_ranks)
    rank_count = len(filtered_ranks)
    average_rank = rank_sum / rank_count if rank_count else 0

    # Auxiliary computation - not directly used in final score
    outlier_count = 0
    for val in filtered_ranks:
        if val > 100:
            outlier_count += 1
    adjusted_outliers = outlier_count * 0.5  # Distractor variable

    # Set-based filtering using threshold set
    valid_ranks = set(filtered_ranks) - thresh
    unique_valid_count = len(valid_ranks)

    # Scoring logic with conditional weighting
    base_score = 0
    bonus_multiplier = 1.0
    for i, val in enumerate(filtered_ranks):
        if val in thresh:
            base_score += val // 3
        else:
            base_score += val % 7
        if i % 4 == 0:
            bonus_multiplier *= 1.1  # Compounding effect on early indices

    # Secondary unused scoring branch (dead logic path)
    temp_score = 0
    for a, b in zip(filtered_ranks, reversed(filtered_ranks)):
        temp_score += (a - b) ** 2
    normalized_temp = temp_score / len(filtered_ranks) if filtered_ranks else 0

    # Final composition
    penalty = 0
    if unique_valid_count < 5:
        penalty = 10
    elif unique_valid_count > 10:
        penalty = 5

    final_score = int((base_score * bonus_multiplier) - penalty)
    return final_score

# Main execution context
rank_data = [12, 15, 7, 22, 3, 8, 100, 101, 6, 14, 19]
threshold_set = {3, 7, 100, 22, 101}

# Key assignment statement
final_score = calculate_final_score(rank_data, threshold_set)
print(f"Result: {final_score}")