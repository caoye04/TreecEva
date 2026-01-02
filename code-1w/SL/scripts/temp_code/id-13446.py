def evaluate_performance(base_points, penalty_rate, is_eligible):
    if is_eligible:
        adjusted = base_points * (1 - penalty_rate)
    else:
        adjusted = base_points * 0.5
    return int(adjusted + 0.5)

# Simulate historical data for irrelevant analysis
temp_log = []
for i in range(5):
    temp_log.append((i, i**3 - 2*i + 1))

# Core ranking logic
rank_map = {'alpha': 85, 'beta': 90, 'gamma': 87}
bonus_multiplier = 1.2
penalty_flag = False

def apply_correction(value, mode='add'):
    shift = 3 if mode == 'add' else -3
    return value + shift

def process_rankings(ranks, multiplier):
    total = 0
    bonus_accrued = 0
    
    # Real processing with conditional expression
    for key, score in ranks.items():
        normalized = score // 10 * 10  # Round down to nearest 10
        contribution = normalized * multiplier
        
        # Conditional expression used here
        adjustment = apply_correction(contribution, 'add') if contribution > 90 else apply_correction(contribution, 'subtract')
        
        total += int(adjustment)
        
        # Irrelevant tracking (distractor)
        if 'a' in key:
            bonus_accrued += 5
    
    # Additional interference: unused transformation
    transformed_ranks = {k.upper(): v ** 0.5 for k, v in ranks.items()}
    avg_sqrt = sum(transformed_ranks.values()) / len(transformed_ranks)
    
    # Final calculation influenced only by main loop
    final = total + (10 if penalty_flag else 5)
    
    # Dead code path (never executed but looks relevant)
    if False:
        fallback = sum(ranks.values()) * 0.8
        final = max(final, fallback)
    
    return final

# Secondary irrelevant computation
entropy_proxy = 0
for val in [2, 3, 5, 7, 11]:
    entropy_proxy += (val % 4) * 0.1

# Main execution flow
base_score = evaluate_performance(100, 0.15, True)
rank_map['gamma'] = base_score  # Update one value based on prior logic

final_score = process_rankings(rank_map, bonus_multiplier)

# Output required format
print(f"Result: {final_score}")