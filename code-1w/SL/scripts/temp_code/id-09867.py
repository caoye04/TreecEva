def analyze_entry(entry):
    base_value = entry['value'] * 0.85
    adjustment = 1.1 if entry['category'] == 'premium' else 0.9
    # Irrelevant computation (distractor)
    temp_debug = base_value + adjustment  
    adjusted = base_value * adjustment
    return adjusted

# Misleading data structure with unused fields
tags_reference = {'urgent': 10, 'normal': 1, 'low': -5}

threshold_map = [20, 45, 60]

def evaluate_threshold(score):
    for i, t in enumerate(threshold_map):
        if score < t:
            return i
    return len(threshold_map)

# Unused helper (dead code path - distractor)
def legacy_normalize(x):
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0] * len(x)

# Main processing function
def calculate_final_score(entries):
    scores = []n    total_weight = 0.0
    debug_logs = []  # Collected but unused
    
    for idx, entry in enumerate(entries):
        raw_score = analyze_entry(entry)
        weight = entry.get('weight', 1.0)
        total_weight += weight
        
        # Conditional expression used
        category_bonus = 5 if entry['category'] == 'premium' and raw_score > 30 else 0
        
        final_raw = raw_score + category_bonus
        
        # Tracking unnecessary info
        debug_logs.append(f"Step {idx}: {final_raw}")
        
        scores.append(final_raw)
    
    # Sorting used (suggested paradigm)
    sorted_scores = sorted(scores, reverse=True)
    
    # Key: Only top 3 contribute to final score
    top_contributions = sum(sorted_scores[:3])
    
    # Dummy computation with zip and enumerate (partially relevant)
    offset = 0
    for i, (a, b) in enumerate(zip(sorted_scores, sorted_scores[1:])):
        offset += (b - a) * i  # Diminishing impact
    
    # Final score calculation
    final_score = top_contributions + offset * 0.1
    
    # Additional irrelevant transformation
    normalized_offset = offset / (len(sorted_scores) or 1)
    _ = round(normalized_offset, 3)  # Not used
    
    return final_score

# Input data
entries_data = [
    {'value': 40, 'category': 'premium', 'weight': 1.2},
    {'value': 35, 'category': 'standard', 'weight': 1.0},
    {'value': 50, 'category': 'premium', 'weight': 1.5},
    {'value': 20, 'category': 'standard', 'weight': 0.8},
    {'value': 60, 'category': 'premium', 'weight': 1.3}
]

# Execution point
final_score = calculate_final_score(entries_data)
print(f"Result: {final_score}")