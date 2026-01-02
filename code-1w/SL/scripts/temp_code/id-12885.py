def calculate_similarity(a, b):
    return sum(1 for x, y in zip(a, b) if x == y)

# Simulate a tournament ranking system with noise data
def evaluate_performance(logs):
    total_errors = 0
    for log in logs:
        total_errors += 'ERROR' in log
    return total_errors

# Main processing pipeline
def process_tournament_results(results, thresholds):
    processed = []
    temp_accumulator = 0
    
    for i, result in enumerate(results):
        rank = i + 1
        score = len(result['team_name']) * 2 + result['wins'] * 10
        
        # Irrelevant transformation (distractor)
        normalized_name = ''.join([c.lower() for c in result['team_name'] if c.isalpha()])
        name_entropy = sum(ord(c) for c in normalized_name)
        
        # Actual logic contribution
        if score > thresholds['min_qualifying_score']:
            processed.append({'rank': rank, 'score': score, 'team': result['team_name']})
        
        # Dead computation (interference)
        temp_accumulator += name_entropy % 7
    
    return processed

# Final scoring with combinatorics adjustment
def calculate_final_score(rankings, bonus_multiplier):
    base_total = sum(entry['score'] for entry in rankings)
    rank_bonus = 0
    
    # Apply rank-based incremental bonus
    for j, entry in enumerate(rankings):
        if j < 3:
            rank_bonus += (3 - j) * 5
    
    # Combinatorics factor: number of ways to choose 2 from top 4 ranks (only computed, not critical)
    top_four_count = min(4, len(rankings))
    combination_value = 0
    if top_four_count >= 2:
        combination_value = (top_four_count * (top_four_count - 1)) // 2
    
    # Misleading floating point adjustment (not used in final path)
    dummy_adjustment = round(combination_value * 0.777, 3)
    
    # Real final calculation
    adjusted_score = base_total + rank_bonus
    final_weighted = int(adjusted_score * bonus_multiplier)
    
    return final_weighted

# Input data
results_data = [
    {'team_name': 'Apex Predators', 'wins': 7},
    {'team_name': 'Quantum Flux', 'wins': 5},
    {'team_name': 'Binary Hawks', 'wins': 8},
    {'team_name': 'Logic Masters', 'wins': 6},
    {'team_name': 'Syntax Knights', 'wins': 4}
]

thresholds_config = {
    'min_qualifying_score': 40,
    'max_name_length': 20
}

# Auxiliary logs with irrelevant content
system_logs = [
    'INFO: Startup complete',
    'ERROR: Failed to load asset',
    'DEBUG: Loop iteration 3',
    'WARNING: High latency',
    'ERROR: Timeout in module X'
]

# Execute workflow
error_count = evaluate_performance(system_logs)
filtered_rankings = process_tournament_results(results_data, thresholds_config)
bonus_multiplier = 1.2 if error_count < 3 else 1.0

final_score = calculate_final_score(filtered_rankings, bonus_multiplier)
print(f"Result: {final_score}")