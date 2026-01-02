def calculate_final_score(entries, importance_weights):
    base_total = 0
    bonus_factor = 0.0
    penalty_offset = 0
    temp_result = []
    
    # Preprocess entries using list comprehension with filtering
    filtered_entries = [e for e in entries if e['value'] > 0 and e['active']]
    
    # Irrelevant aggregation - distractor
    avg_value = sum(e['value'] for e in entries) / len(entries) if entries else 0
    max_timestamp = max((e['timestamp'] for e in entries), default=0)
    
    # Core logic: weighted sum with modular adjustments
    for item in filtered_entries:
        weight = importance_weights.get(item['category'], 1)
        contribution = item['value'] * weight
        
        # Apply conditional bonus based on timestamp (semi-relevant)
        if item['timestamp'] % 7 == 0:
            bonus_factor += 0.1 * weight  # Minor influence
        
        # Apply penalty for late entries (modular arithmetic)
        age = (max_timestamp - item['timestamp']) % 5
        if age > 3:
            penalty_offset += 1
        
        base_total += contribution
    
    # Secondary processing with tuple unpacking
    modifiers = [(1.2, 'early'), (0.9, 'late')]  # Unused path - dead code
    status_flags = {flag: False for _, flag in modifiers}  # Distractor state
    
    # Compute final score with adjustment chain
    adjusted_total = base_total * (1 + bonus_factor)
    adjusted_total = max(adjusted_total - penalty_offset * 5, 0)
    
    # Final normalization via integer division
    normalized_score = int(adjusted_total // 1)  # Simulate discrete scoring
    
    # Red herring computation (unused)
    projected_growth = sum(item['value'] * 1.05 for item in filtered_entries)  # Not used
    volatility_index = sum(1 for e in entries if e['value'] < avg_value)  # Distractor metric
    
    final_score = normalized_score + 10  # Final adjustment
    return final_score

# Input data setup
data = [
    {'value': 8, 'category': 'A', 'active': True, 'timestamp': 14},
    {'value': 12, 'category': 'B', 'active': True, 'timestamp': 21},
    {'value': -5, 'category': 'A', 'active': True, 'timestamp': 7},  # filtered out by value
    {'value': 10, 'category': 'C', 'active': True, 'timestamp': 28},
    {'value': 15, 'category': 'B', 'active': False, 'timestamp': 35}, # filtered out by active
    {'value': 7, 'category': 'A', 'active': True, 'timestamp': 42}
]

weights = {'A': 1, 'B': 2, 'C': 3}

result = calculate_final_score(data, weights)
print(f"Result: {result}")