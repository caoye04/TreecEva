def calculate_rating(converged, data):
    base = len(data['readings'])
    offset = sum([x % 2 for x in data['factors']])
    adjustment = 0
    
    # Irrelevant string processing (distractor)
    status_msg = "System active" if converged else "Inactive"
    log_entry = f"[LOG] {status_msg.upper().replace(' ', '_')}: Run complete."
    entry_length = len(log_entry)
    
    # Semi-relevant filtering
    filtered = [v for v in data['readings'] if v > 0]
    positive_count = len(filtered)
    
    # Core logic hidden among distractions
    if converged and positive_count > 3:
        adjustment = 10
    else:
        adjustment = -5
    
    # Dummy loop with no effect on result (dead code path)
    temp_values = []
    for i in range(3):
        temp_values.append(i ** 3)  # Unused later
    
    # Actual computation
    scaling_factor = data['config'][0] * 0.5
    raw_score = (base + offset) * scaling_factor
    final_rating = raw_score + adjustment
    
    # Key statement
    final_score = int(final_rating)
    return final_score

# Setup inputs
convergence = True
metrics = {
    'readings': [12, -5, 8, 15, 0, 7],
    'factors': [4, 9, 2, 7],
    'config': [4.0],  # Used in scaling
    'version': '2.1'
}

# Call function and print result
result = calculate_rating(convergence, metrics)
print(f"Result: {result}")