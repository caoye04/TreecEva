def process_metrics(entries, limits):
    filtered = [e for e in entries if e[1] > limits['min_val'] and e[2] < limits['max_age']]
    temp_sum = 0
    count = 0
    debug_info = []
    
    # Irrelevant aggregation for distraction
    total_weight = sum([e[3] for e in entries])
    avg_weight = total_weight / len(entries) if entries else 0
    
    scale_factor = 1.5 if avg_weight > 50 else 0.8
    
    intermediate_results = []
    for item in filtered:
        name, metric, age, weight = item
        adjusted_metric = metric * (1 + (weight / 100))
        
        # String-based filtering condition (uses string method)
        if name.lower().startswith('x') or 'test' in name.lower():
            continue  # Exclude certain names
        
        cap = limits['max_metric']
        clamped = min(adjusted_metric, cap)
        
        # Additional irrelevant transformation
        squared_error = (clamped - 90) ** 2
        debug_info.append(squared_error)
        
        temp_sum += clamped
        count += 1
        intermediate_results.append(clamped)
    
    # More red herring variables
    outlier_count = sum(1 for r in intermediate_results if r > 95)
    penalty = outlier_count * 0.5
    
    raw_average = temp_sum / count if count > 0 else 0
    
    # Final computation path
    variance_proxy = sum((r - raw_average) ** 2 for r in intermediate_results) / count if count > 0 else 0
    stability_bonus = 10 if variance_proxy < 25 else 0
    
    final_score = (raw_average + stability_bonus) * scale_factor
    
    # Dead code branch (never executed due to data)
    if False and len(entries) > 100:
        fallback = sum(e[1] for e in entries)
        final_score = fallback / 10
    
    return final_score

# Main execution
config = {
    'min_val': 45,
    'max_age': 65,
    'max_metric': 98
}

data = [
    ('Alice', 50, 30, 60),
    ('Bob', 70, 45, 75),
    ('Xavier', 85, 50, 80),  # filtered out by string condition
    ('Christine', 65, 70, 55), # filtered out by age
    ('David', 90, 55, 90),
    ('Eve', 40, 40, 45),   # filtered out by metric
    ('Fiona', 80, 60, 70)
]

result = process_metrics(data, config)
print(f'Result: {result}')