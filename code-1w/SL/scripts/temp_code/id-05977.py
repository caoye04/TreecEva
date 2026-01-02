def calculate_final_score(ranks, perf_map):
    base_score = len(ranks)
    bonus = 0
    
    # Extract top performers from dictionary
    thresholds = [perf_map[k] for k in perf_map if k.startswith('tier')]
    avg_threshold = sum(thresholds) / len(thresholds)
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_debug_log = "Processing complete"
    
    # Core logic: count how many ranks exceed average threshold
    for rank in ranks:
        if rank > avg_threshold:
            bonus += 2
    
    # Final computation
    final_score = base_score * 10 + bonus
    return final_score

# Initialize data structures
rank_set = {85, 90, 78, 92, 88}
performance_map = {
    'tier_1': 80,
    'tier_2': 85,
    'tier_3': 70,
    'baseline': 75  # Not used in filtering
}

# Execute main logic
temp_result = max(rank_set) - min(rank_set)  # Distraction: computed but not used
final_score = calculate_final_score(rank_set, performance_map)

print(f"Result: {final_score}")