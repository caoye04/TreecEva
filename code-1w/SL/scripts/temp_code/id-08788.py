def analyze_performance(records):
    base_weights = [0.2, 0.3, 0.5]
    adjustments = [0.05, -0.03, 0.02]
    total_entries = len(records)
    temp_sum = 0
    weighted_total = 0
    
    # Misleading normalization pass (not used in final logic)
    normalized_records = []
    max_value = max(max(rec) for rec in records)
    for record in records:
        norm_rec = [x / max_value for x in record]
        normalized_records.append(norm_rec)
    
    # Actual computation with distractor variables
    temp_debug_log = []
    intermediate_results = []
    for i, record in enumerate(records):
        entry_total = sum(record)
        if entry_total > 100:
            adjustment_factor = adjustments[i % 3]
        else:
            adjustment_factor = 0  # neutral adjustment
        
        # Core weight application using enumerate and zip
        weighted_entry = 0
        for idx, (value, base) in enumerate(zip(record, base_weights)):
            weighted_entry += value * (base + adjustment_factor)
        
        intermediate_results.append(weighted_entry)
        temp_debug_log.append(f'Entry {i}: {weighted_entry:.4f}')
    
    # Secondary processing with red herring condition
    filtered_results = [val for val in intermediate_results if val > 20]
    dummy_aggregate = sum(filtered_results) / len(filtered_results) if filtered_results else 0
    
    # Distractor: unused combinatoric calculation
    combination_count = 0
    for a in range(len(intermediate_results)):
        for b in range(a + 1, len(intermediate_results)):
            if intermediate_results[a] + intermediate_results[b] > 50:
                combination_count += 1
    
    # Final aggregation logic (what actually matters)
    final_score = 0
    for val in intermediate_results:
        if val >= 25:
            final_score += val * 1.1
        else:
            final_score += val * 0.9
    
    return int(final_score)

# Input data
data_log = [
    [40, 50, 60],
    [30, 45, 70],
    [55, 40, 50],
    [20, 35, 40]
]

# Execution
result_var = analyze_performance(data_log)
final_score = result_var
print(f"Result: {final_score}")