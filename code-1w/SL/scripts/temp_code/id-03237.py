def calculate_final_score(records, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    temp_sum = 0
    debug_trace = []
    
    # Irrelevant preprocessing: string sanitation (distractor)
    sanitized_keys = [k.strip().lower() for k in records.keys() if isinstance(k, str)]
    key_length_sum = sum(len(k) for k in sanitized_keys)

    # Real computation begins
    for key, value in records.items():
        if not isinstance(value, (int, float)):
            continue
        
        # Apply modular arithmetic to simulate cyclical weighting
        weight_index = hash(key) % len(importance_weights)
        applied_weight = importance_weights[weight_index]
        
        # Conditional expression used for dynamic adjustment
        contribution = value * applied_weight if value >= 0 else value * 0.5
        base_score += contribution
        
        # Tracking intermediate values (some used, some not)
        temp_sum += abs(value)
        
        if temp_sum > 100 and penalty_adjustment == 0:
            penalty_adjustment = -5

    # Secondary loop with partial overlap (semi-relevant)
    magnitude_factor = 1.0
    if temp_sum > 0:
        magnitude_factor = (temp_sum / len(records)) ** 0.5

    # Simulate data quality check (mostly irrelevant)
    status_flags = {"valid": True, "sanitized": key_length_sum > 0}
    status_msg = "Valid" if status_flags["valid"] else "Invalid"
    status_msg = status_msg.lower().replace("invalid", "rejected")  # string method (required feature)

    # Final scoring with conditional expression
    scaled_score = base_score * magnitude_factor
    final_score = scaled_score + penalty_adjustment if penalty_adjustment < 0 else scaled_score
    
    return int(final_score)

# Main execution
raw_data = {
    'entry_01': 45,
    'ENTRY_02': -12,
    'Entry::03': 67,
    'item_four': 89,
    'payload': 'ignore_me',
    'count': 34
}

weights = [0.8, 1.2, 0.5, 1.5]

intermediate_total = sum(v for v in raw_data.values() if isinstance(v, int))  # red herring
ignored_list = [x * 2 for x in weights]  # dead code path

final_score = calculate_final_score(raw_data, weights)
print(f"Result: {final_score}")