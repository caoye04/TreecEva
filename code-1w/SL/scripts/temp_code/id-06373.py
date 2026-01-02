from collections import defaultdict

def calculate_final_score(responses, weights):
    score = 0
    category_count = defaultdict(int)
    
    for response in responses:
        category = response['category']
        value = response['value']
        category_count[category] += 1
        if category_count[category] <= 2:  # Only count first two responses per category
            weight = weights.get(category, 1)
            score += value * weight
    
    bonus = 0
    total_categories = len(category_count)
    if total_categories > 3:
        bonus = 10
    
    # Irrelevant distraction below (minimal interference)
    debug_info = {'processed': len(responses), 'bonus_applied': bonus > 0}
    
    score += bonus
    return score

# Input data
responses = [
    {'category': 'logic',     'value': 5},
    {'category': 'arithmetic', 'value': 4},
    {'category': 'logic',      'value': 6},
    {'category': 'boolean',    'value': 7},
    {'category': 'control',    'value': 3},
    {'category': 'arithmetic', 'value': 8},  # This will be ignored due to limit
]

weights = {
    'logic': 2,
    'arithmetic': 1.5,
    'boolean': 1,
    'control': 3
}

final_score = calculate_final_score(responses, weights)
print(f"Result: {final_score}")