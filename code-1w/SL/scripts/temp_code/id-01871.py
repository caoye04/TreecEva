def evaluate_performance(records, limit):
    # Track active and inactive categories using sets
    active_set = set()
    inactive_set = set()
    
    for val in records:
        if val > limit * 0.5:
            active_set.add(val)
        else:
            inactive_set.add(val)
    
    # Misleading computation: unused trend analysis
    trend_values = [records[i+1] - records[i] for i in range(len(records)-1)]
    avg_trend = sum(trend_values) / len(trend_values) if trend_values else 0
    
    # Simulate correction factor based on set sizes (not actually used)
    size_diff = len(active_set) - len(inactive_set)
    correction_factor = size_diff * 0.1  # Dead code path influence
    
    # Core logic: count how many exceed the strict threshold
    compliant_count = 0
    for val in records:
        if val > limit:
            compliant_count += 1
    
    # Secondary filter: only those divisible by 3 contribute fully
    bonus_weight = 0
    for val in active_set:
        if val % 3 == 0:
            bonus_weight += 1
    
    # Final score calculation - only depends on compliant_count and bonus_weight
    base_score = compliant_count * 10
    final_score = base_score + (bonus_weight * 5)
    
    # Red herring: modify final_score with irrelevant condition
    if len(inactive_set) > len(active_set):
        final_score -= 2  # This does not trigger in this case
    
    return final_score

# Main execution context
productivity_data = [12, 15, 9, 20, 7, 18, 5]
threshold = 10

# Unused statistical summary
mean_value = sum(productivity_data) / len(productivity_data)
std_deviation = (sum((x - mean_value) ** 2 for x in productivity_data) / len(productivity_data)) ** 0.5

# Key data structure transformation
productivity_set = set(productivity_data)

# Critical statement
final_score = evaluate_performance(productivity_set, threshold)

print(f"Result: {final_score}")