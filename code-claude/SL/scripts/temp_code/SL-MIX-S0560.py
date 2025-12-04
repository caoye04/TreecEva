def normalize_data(values, offset=10):
    """Normalize values by adding offset and scaling"""
    return [(x + offset) / 2 for x in values]

def calculate_adjusted_score(scores, weights):
    """Calculate weighted score with adjustments"""
    # Initialize variables
    base_factor = 0.85
    scaling_factor = 1.25
    penalty = 0
    
    # Create some distractor data
    historical_data = [(85, 0.9), (92, 0.8), (78, 0.95)]
    trend_analysis = lambda x: sum(item[0] * item[1] for item in x) / len(x)
    trend_value = trend_analysis(historical_data)  # Calculated but unused
    
    # Apply weights to scores
    weighted_sum = 0
    total_weight = 0
    
    for score, weight in zip(scores, weights):
        weighted_sum += score * weight
        total_weight += weight
    
    # Some unnecessary operations with slicing
    middle_scores = scores[1:-1]
    if len(middle_scores) > 0:
        middle_avg = sum(middle_scores) / len(middle_scores)
        # This looks important but doesn't affect the result
        if middle_avg < 70:
            penalty = 5
    
    # Calculate raw score
    raw_score = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Process extra factors that seem relevant but most aren't
    bonus_eligible = raw_score > 85
    bonus_factors = [1.05, 1.08, 1.12]
    selected_bonus = bonus_factors[0] if bonus_eligible else 1.0
    
    # More distractor operations
    normalized_weights = normalize_data(weights, offset=5)
    weight_variance = sum((w - sum(normalized_weights)/len(normalized_weights))**2 
                         for w in normalized_weights) / len(normalized_weights)
    
    # The actual calculation that matters
    adjusted_score = int((raw_score * base_factor * selected_bonus) * scaling_factor)
    
    return adjusted_score

# Main execution
scores = [92, 78, 85, 90]
weights = [0.4, 0.2, 0.3, 0.1]

# Calculate various statistics for the scores
min_score = min(scores)
max_score = max(scores)
score_range = max_score - min_score

# Create enumerated version of the data (not directly used)
enumerated_scores = list(enumerate(scores))
position_weighted = sum(i * score for i, score in enumerated_scores) / len(scores)

# This is the key statement
processed_score = calculate_adjusted_score(scores, weights)

# Output the result
print(f"Result: {processed_score}")