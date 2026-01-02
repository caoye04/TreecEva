def analyze_data_stream():
    raw_values = [3, 7, 2, 9, 4, 8, 1, 6]
    processed = []
    temp_sum = 0
    
    for val in raw_values:
        if val % 2 == 0:
            processed.append(val ** 2)
        else:
            processed.append(val + 1)
    
    # Irrelevant statistical tracking (distractor)
    mean_val = sum(raw_values) / len(raw_values)
    variance_tracker = 0
    for v in raw_values:
        variance_tracker += (v - mean_val) ** 2
    
    # Secondary processing with conditional expression
    adjusted = [x * 0.9 if x > 20 else x * 1.1 for x in processed]
    
    # Destructuring assignment (relevant)
    first_half, second_half = adjusted[:4], adjusted[4:]
    
    # Red herring: unused helper function
    def unused_normalization(data):
        max_val = max(data)
        return [d / max_val for d in data]
    
    # Simulate noise filtering (partially relevant)
    filtered = []
    threshold = 5.5
    for x in adjusted:
        if x >= threshold:
            filtered.append(x)
    
    # State tracking with misleading counters
    high_count = 0
    low_count = 0
    for f in filtered:
        if f > 10:
            high_count += 1
        else:
            low_count += 1  # This will be used indirectly
    
    # Core logic disguised among distractions
    base_metric = sum(filtered)
    penalty_factor = 0.1 * low_count
    bonus_granted = True if high_count >= 3 else False
    bonus = 15 if bonus_granted else 0
    
    # Final metric calculation (key step)
    final_score = int(base_metric - (penalty_factor * base_metric) + bonus)
    
    # Dead code path (distractor)
    if False:
        final_score *= 1.5
        print("This will never execute")
    
    return final_score

def calculate_performance_metric():
    return analyze_data_stream()

# Execution entry point
result = calculate_performance_metric()
print(f"Result: {result}")