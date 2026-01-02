def calculate_final_score(raw_data):
    # Preprocessing: filter and transform valid entries
    processed = [x for x in raw_data if x > 0]
    
    # Irrelevant distraction: statistical summary (not used)
    mean_val = sum(processed) / len(processed) if processed else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in processed) / len(processed) if processed else 0

    # Key transformation chain
    squared_filtered = [x**2 for x in processed if x % 2 == 1]  # Only odd values, squared
    
    # Distractor: unused path with lambda
    analyze = lambda arr: sum(x * 1.5 for x in arr if x > 10)
    temp_analysis = analyze(squared_filtered)  # Computed but not used

    # Conditional scaling based on size (actual logic branch)
    base_score = sum(squared_filtered)
    adjustment = 10 if len(squared_filtered) > 3 else 5
    
    # Multi-step calculation with conditional expression
    penalty = 0
    penalty += 7 if any(x > 100 for x in squared_filtered) else 0
    penalty += 3 if all(x < 50 for x in squared_filtered) else 0

    # Final composition
    intermediate = (base_score + adjustment) // 2
    final_score = intermediate - penalty

    # Dead code: irrelevant state tracking
    status_log = []
    status_log.append('processed')
    status_log.append('adjusted')

    return final_score

# Input data with mixed characteristics
data = [3, -5, 4, 7, 0, 9, 2, 11]

# Execute main computation
final_score = calculate_final_score(data)

# Output result as required
print(f"Result: {final_score}")