def evaluate_performance():
    raw_scores = [88, 92, 76, 94, 85, 90, 70]
    ranks = sorted(raw_scores, reverse=True)
    offset = 3
    adjusted_ranks = [rank - offset for rank in ranks]
    index_map = {i: val for i, val in enumerate(adjusted_ranks)}
    
    # Extract every second element starting from index 1
    sliced_ranks = adjusted_ranks[1::2]
    
    # Filter ranks above threshold
    filtered_ranks = [x for x in sliced_ranks if x > 80]
    
    # Irrelevant variable (minor distraction)
    temp_result = sum([1 for x in raw_scores if x < 80])
    
    final_score = sum(filtered_ranks)
    print(f"Result: {final_score}")

evaluate_performance()