import itertools

def analyze_team_performance(team_data):
    irrelevant_counter = 0
    misleading_total = 0
    
    # Distractor: irrelevant team analysis
    for i in range(len(team_data)):
        misleading_total += team_data[i] * 2  # Misleading calculation
        irrelevant_counter += i ** 2
    
    # Main logic: analyze performance patterns
    performance_sets = set()
    for combo in itertools.combinations(team_data, 3):
        if sum(combo) > 15:  # Relevant threshold
            performance_sets.add(tuple(sorted(combo)))
    
    # Dead code path (never executed)
    unused_result = misleading_total - irrelevant_counter
    if unused_result < -1000:
        return -999  # Never reached
    
    # Core calculation
    valid_patterns = len(performance_sets)
    base_score = sum(team_data)
    
    # Distractor: misleading intermediate
    temp_metric = base_score * 2 + irrelevant_counter
    
    # Final calculation chain
    adjustment = valid_patterns * 3
    final_metric = base_score + adjustment - (temp_metric % 7)
    
    result = final_metric
    print(f"Target result: {result}")
    return result

# Main execution
team_performance = [4, 8, 6, 12, 3, 7]
result = analyze_team_performance(team_performance)