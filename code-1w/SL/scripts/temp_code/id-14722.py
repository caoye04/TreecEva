def evaluate_performance(output, faults):
    base_score = 100
    penalty = 0

    # Analyze productivity using slicing and transformations
    peak_days = output[1:6:2]  # Not used in final logic, distraction
    avg_output = sum(output) / len(output)

    # Distraction: Irrelevant set operations
    unique_faults = set(faults)
    fault_clusters = {f % 3 for f in unique_faults}  # Group by modulo (not used)

    # Real logic begins: performance bands
    if avg_output > 8:
        base_score += 20
    elif avg_output > 5:
        base_score += 10
    else:
        base_score -= 15

    # Fault impact with dictionary-based severity mapping
    severity_map = {0: 0, 1: 5, 2: 12, 3: 20, 4: 30, 5: 45}
    total_severity = 0
    for f in faults:
        if f in severity_map:
            total_severity += severity_map[f]

    # Additional distraction: unused data structure transformation
    inverted_map = {v: k for k, v in severity_map.items()}
    rare_cases = [k for k, v in severity_map.items() if v < 10]

    # Apply penalty based on total severity
    if total_severity > 50:
        penalty = 40
    elif total_severity > 30:
        penalty = 25
    else:
        penalty = 10

    # Final score computation
    debug_info = {'input_avg': avg_output, 'total_penalty': penalty}  # dead variable
    final_score = base_score - penalty

    return final_score

# Main execution context
productivity = [7, 9, 6, 10, 8, 7]
errors = [2, 1, 3, 2, 1, 0, 2]

# Irrelevant pre-processing (distractor)
buffered_data = productivity[:]
duplicate_count = len(buffered_data) - len(set(buffered_data))

# Key statement
final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")