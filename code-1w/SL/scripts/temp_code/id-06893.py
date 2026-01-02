from collections import defaultdict

# Simulate employee review data with mixed metrics
def generate_feedback():
    raw_scores = [4.2, 3.8, 4.5, 4.0, 3.9]
    comments = ['excellent', 'good', 'excellent', 'satisfactory', 'good']
    categories = ['leadership', 'teamwork', 'innovation', 'punctuality', 'adaptability']
    
    feedback = defaultdict(list)
    for i, score in enumerate(raw_scores):
        category = categories[i % len(categories)]
        feedback[category].append(score)
    
    # Distractor computation: average comment length (not used)
    avg_comment_len = sum(len(c) for c in comments) / len(comments)
    growth_potential = 0.7 * len([s for s in raw_scores if s >= 4.0])
    
    return feedback, growth_potential

# Weighting function for performance dimensions
get_weight = lambda dim: 1.2 if dim in ['leadership', 'innovation'] else 1.0

# Core evaluation logic
def evaluate_performance(feedback_map):
    base_score = 0.0
    bonus_credit = 0
    penalty = 0
    
    dimension_averages = {}
    
    for dimension, scores in feedback_map.items():
        avg = sum(scores) / len(scores)
        dimension_averages[dimension] = avg
        
        # Apply weighted contribution
        weight = get_weight(dimension)
        base_score += avg * weight
        
        # Bonus condition: high consistency in feedback
        if max(scores) - min(scores) < 0.5:
            bonus_credit += 0.3
        
        # Track low performers for penalty (distractor: not fully used)
        low_performers = [s for s in scores if s < 3.8]
        if len(low_performers) > 0:
            penalty += 0.1  # Minimal impact
    
    # Secondary distractor: unused efficiency metric
    efficiency_ratio = len(dimension_averages) / (len(dimension_averages) + bonus_credit + 1)
    
    # Final aggregation with normalization
    normalized_base = base_score / len(feedback_map)
    final_score = round(normalized_base + bonus_credit - penalty, 4)
    
    # Additional red herring: modify final_score in a branch that never executes
    if False:
        final_score *= 1.1
    
    return final_score

# Unused helper: simulates training progress (dead code path)
def calculate_training_progress(records):
    return sum(r * 0.8 for r in records if r > 3.0)

# Main execution
feedback_data, potential = generate_feedback()
dummy_map = {'test': [1,2,3]}
scratch_result = sum(potential for _ in range(2))  # Irrelevant accumulation

final_score = evaluate_performance(feedback_data)
print(f"Target result: {final_score}")