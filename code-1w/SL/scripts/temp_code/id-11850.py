from collections import defaultdict

def calculate_final_score(scores, modifiers):
    base_total = sum(scores)
    adjustment_factor = 1.0
    
    # Apply multiplier if any score exceeds threshold
    if max(scores) > 85:
        adjustment_factor *= 1.1
    
    # Use defaultdict to count adjustment types
    adj_count = defaultdict(int)
    for adj in modifiers:
        adj_count[adj['type']] += 1
    
    # Additional logic based on adjustment distribution
    if adj_count['bonus'] >= 2:
        adjustment_factor += 0.05
    if adj_count['penalty'] == 0:
        adjustment_factor += 0.03

    temp_result = base_total * adjustment_factor
    
    # Normalize case of comment before final rounding
    comment = "Final computation complete"
    normalized_comment = comment.lower()
    
    # Final score rounded to nearest integer
    return round(temp_result)

# Input data
raw_scores = [78, 85, 92, 88]
adjustments = [
    {'type': 'bonus', 'value': 5},
    {'type': 'bonus', 'value': 3},
    {'type': 'note', 'value': 0}
]

final_score = calculate_final_score(raw_scores, adjustments)
print(f"Result: {final_score}")