def evaluate_performance(data, limit):
    # Irrelevant transformation (distractor)
    normalized = [x * 0.95 for x in data if x > 0]
    filtered = [x for x in data if x >= limit]
    
    # Semi-relevant pre-processing
    squared_values = [x**2 for x in filtered]
    sum_squares = sum(squared_values)
    
    # Core logic: count how many exceed half the limit (actual relevant part)
    mid_threshold = limit / 2
    valid_count = len([x for x in data if x > mid_threshold])
    
    # Red herring computation with no impact
    average_normalized = sum(normalized) / len(normalized) if normalized else 0
    deviation_penalty = 0
    for val in normalized:
        if val < average_normalized * 0.8:
            deviation_penalty += 1

    # Another distraction: character counting in string representation
    str_repr = ''.join(map(str, data))
    digit_count = len(str_repr)  # Not used later

    # Real answer derivation
    base_score = sum(filtered)
    bonus = valid_count * 2
    final = base_score + bonus
    
    # Unnecessary tuple unpacking (meets slicing + destructuring requirement)
    results = (final, base_score, bonus)
    score, _, _ = results
    
    # Slicing operation on list (required Python feature)
    recent_data = data[-3:]  # Last three elements
    spike_count = len([x for x in recent_data if x > limit * 0.75])
    
    # Final adjustment based on spike detection
    if spike_count >= 2:
        score += 5
    
    return score

# Main execution
raw_metrics = [12, 15, 3, 20, 7, 25, 18, 4]
threshold = 10

# Distractor variables
shadow_copy = raw_metrics[:]
duplicate_filtered = [x for x in shadow_copy if x != 7]
placeholder_sum = sum(duplicate_filtered[::2])  # Every other element, irrelevant

# Key statement
final_score = evaluate_performance(raw_metrics, threshold)

print(f"Result: {final_score}")