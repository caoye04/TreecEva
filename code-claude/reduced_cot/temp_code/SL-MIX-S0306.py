def calculate_adjusted_score(scores, penalties, bonus):
    # Initialize tracking variables
    valid_scores = []
    penalty_sum = 0
    potential_bonus = 1
    
    # Process scores and apply filtering
    for score in scores:
        # Apply complex filtering logic
        if score > 75:
            valid_scores.append(score)
        elif score < 25:
            # Low scores get special handling
            penalty_sum += 5
            continue
        else:
            # Medium scores are adjusted
            valid_scores.append(score * 0.8)
    
    # Calculate statistics on filtered scores
    max_score = max(valid_scores) if valid_scores else 0
    min_score = min(valid_scores) if valid_scores else 0
    avg_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0
    
    # Process penalties (only odd-indexed ones matter)
    relevant_penalties = [p for i, p in enumerate(penalties) if i % 2 == 1]
    irrelevant_penalties = [p for i, p in enumerate(penalties) if i % 2 == 0]
    
    # Calculate bonus factors
    letter_values = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}
    bonus_word = 'ABCDE'
    letter_sum = sum(letter_values.get(letter, 0) for letter in bonus.upper())
    
    # These calculations are misleading and irrelevant
    misleading_factor = (max_score - min_score) / 2 if max_score > min_score else 10
    distraction_value = sum(irrelevant_penalties) * letter_sum
    red_herring = (avg_score + distraction_value) / 2
    
    # Actual calculation that matters
    base_score = avg_score if avg_score > 60 else 60
    penalty_factor = sum(relevant_penalties) * 0.5
    bonus_factor = len([c for c in bonus.upper() if c in 'AE']) * 2
    
    # Final calculation
    result = base_score - penalty_factor + bonus_factor
    
    # More distraction calculations that aren't used
    alternative_score = (max_score + min_score) / 2 - penalty_sum
    weighted_average = sum(s * (i+1) for i, s in enumerate(valid_scores)) / sum(range(1, len(valid_scores)+1)) if valid_scores else 0
    complex_factor = (weighted_average + red_herring) / 2
    
    return round(result, 2)

# Input data
raw_scores = [82, 45, 91, 15, 63, 87, 22, 29]
penalty_factors = [2, 3, 1, 5, 0, 4]
bonus_multiplier = 'ABBA'

# Unused variables to add complexity
historical_scores = {'Q1': [75, 82, 90], 'Q2': [68, 72, 81], 'Q3': [92, 87, 85]}
trend_analysis = [s for sublist in historical_scores.values() for s in sublist if s > 80]
adjustment_matrix = [[1.1, 0.9, 1.0], [0.8, 1.2, 0.7], [1.0, 1.0, 1.5]]

# Process scores with various methods
def analyze_trend(scores):
    return sum(scores) / len(scores) if scores else 0

def apply_matrix(score, matrix):
    return score * matrix[0][0] * matrix[1][1] * matrix[2][2]

# Calculations that don't affect the final result
trend_value = analyze_trend(trend_analysis)
matrix_factor = apply_matrix(trend_value, adjustment_matrix)
processed_data = {quarter: analyze_trend(scores) for quarter, scores in historical_scores.items()}

# The key calculation
final_score = calculate_adjusted_score(raw_scores, penalty_factors, bonus_multiplier)

print(f"Result: {final_score}")