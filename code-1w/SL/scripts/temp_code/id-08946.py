def analyze_metrics(data_map):
    temp_results = {}
    for key, values in data_map.items():
        if len(values) == 0:
            temp_results[key] = 0
            continue
        avg = sum(values) / len(values)
        max_val = max(values)
        min_val = min(values)
        # Irrelevant transformation
        transformed = [v ** 0.5 for v in values if v > 0]
        temp_results[key] = (avg + max_val - min_val) / 3
    
    # Dead code path with misleading logic
    outlier_count = 0
    for v_list in data_map.values():
        for v in v_list:
            if v > 1000:
                outlier_count += 1
    
    return temp_results


def normalize_keys(raw_keys):
    # String processing - using string methods
    cleaned = [k.strip().lower().replace('_', '-') for k in raw_keys]
    return {k: idx for idx, k in enumerate(cleaned)}


def calculate_performance(log_entries):
    stats = {}
    total_entries = 0
    valid_tags = ['critical', 'important', 'standard']
    
    # Dictionary and string operations mixed with distractors
    tag_frequency = {tag: 0 for tag in valid_tags}
    length_distribution = {}
    
    for entry in log_entries:
        total_entries += 1
        tag = entry.get('tag', '').strip().lower()
        content = entry.get('content', '')
        
        # Relevant accumulation
        if tag in tag_frequency:
            tag_frequency[tag] += 1
        
        # Length analysis - semi-relevant
        cont_len = len(content)
        if cont_len not in length_distribution:
            length_distribution[cont_len] = 0
        length_distribution[cont_len] += 1
        
        # Dummy state tracking
        warning_flag = False
        if 'error' in content.lower() or 'fail' in content.lower():
            warning_flag = True
        
    # Compute base performance metric
    critical_weight = tag_frequency['critical'] * 3
    important_weight = tag_frequency['important'] * 2
    standard_weight = tag_frequency['standard']
    total_weight = critical_weight + important_weight + standard_weight
    
    # Normalize by total entries (only this affects final result)
    if total_entries > 0:
        normalized_metric = total_weight / total_entries
    else:
        normalized_metric = 0
    
    # Distractor: unused complex structure
    histogram_summary = {}
    for length, count in length_distribution.items():
        if count >= 2:
            histogram_summary[length] = count * 1.5
    
    # Final score based only on normalized weight
    final_score = int(round(normalized_metric * 10))
    
    # Additional irrelevant computation
    entropy_proxy = 0
    for freq in tag_frequency.values():
        if freq > 0:
            entropy_proxy -= freq * (freq / total_entries)
    
    return final_score

# Main execution
log_data = [
    {'tag': ' CRITICAL ', 'content': 'System failure at node 3'},
    {'tag': 'important', 'content': 'High memory usage detected'},
    {'tag': 'standard', 'content': 'Routine health check passed'},
    {'tag': 'critical', 'content': 'Authentication timeout'},
    {'tag': 'standard', 'content': 'Backup completed successfully'}
]

# Extract keys for normalization (not used later - red herring)
raw_labels = ['Status_Code', ' Error_Type ', ' Subsystem '] 
normalized_index = normalize_keys(raw_labels)

# Analyze metrics (used but only partially relevant)
data_metrics = analyze_metrics({'values': [10, 20, 30], 'scores': [5, 15]})

# Core calculation
final_score = calculate_performance(log_data)

# Print result
print(f"Result: {final_score}")