def analyze_pattern(sequence):
    if not sequence:
        return 0
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        trend.append(1 if sequence[i] > sequence[i-1] else -1)
    
    # Distractor: Analyze trend reversals (not used in final result)
    reversals = 0
    for j in range(1, len(trend)):
        if trend[j] != trend[j-1]:
            reversals += 1
    
    # Relevant logic: count ascending pairs
    asc_count = sum(1 for x in trend if x == 1)
    desc_count = len(trend) - asc_count
    return asc_count - desc_count


def validate_entry(record):
    # Simulate validation with side computation
    valid_fields = sum(1 for k, v in record.items() if v is not None and str(v).strip() != '')
    total_fields = len(record)
    
    # Distractor: Compute completeness ratio (semi-relevant but not decisive)
    completeness = round(valid_fields / total_fields, 3) if total_fields else 0
    
    # Actual rule: must have non-empty 'status' and numeric 'value'
    status_ok = record.get('status') == 'active'
    value_ok = isinstance(record.get('value'), (int, float)) and record['value'] > 0
    return status_ok and value_ok


def process_metrics(data, config):
    baseline = config['base']
    adjustment = 0
    temp_results = []
    outlier_flags = []
    
    for item in data:
        # Extract and validate
        valid = validate_entry(item)
        raw_value = item.get('value', 0)
        
        # Distractor: string-based anomaly tagging
        tag = item.get('tags', [])
        suspicious = any(t for t in tag if isinstance(t, str) and 'suspect' in t.lower())
        outlier_flags.append(suspicious)
        
        if valid:
            # Core transformation chain
            scaled = raw_value * config['multiplier']
            capped = min(scaled, config['cap'])
            
            # Use conditional expression (required feature)
            penalty = 0.5 if raw_value < baseline else 0.1
            adjusted = capped - penalty * baseline
            
            # Feed into pattern analysis (convert to binary-like sequence)
            binary_seq = [1 if adjusted > baseline else 0, int(adjusted % 3), 2]
            pattern_score = analyze_pattern(binary_seq)
            
            # Final per-item score with bitwise twist (simple XOR)
            final_item_score = int(adjusted) ^ abs(pattern_score)
            temp_results.append(final_item_score)
        
    # Aggregate logic
    if not temp_results:
        return 0
    
    # Main result computation
    raw_total = sum(temp_results)
    size_factor = len(temp_results) if len(temp_results) < 10 else 10
    
    # Conditional expression (second required feature)
    bonus = 10 if all(x > 5 for x in temp_results) else 5
    
    # Final score calculation (this is the key line)
    final_score = raw_total + size_factor + bonus
    
    # Dead code path (distractor)
    if len(outlier_flags) > 100:
        fallback = sum(temp_results) // 2
        final_score = max(final_score, fallback)
    
    return final_score

# Input setup
entry_data = [
    {'value': 12, 'status': 'active', 'tags': ['normal', 'v1']},
    {'value': 8, 'status': 'active', 'tags': ['review']},
    {'value': 15, 'status': 'active', 'tags': []},
    {'value': 6, 'status': 'inactive', 'tags': ['suspect']},  # invalid status
    {'value': 20, 'status': 'active', 'tags': ['final']}
]

thresholds = {
    'base': 10,
    'multiplier': 1.5,
    'cap': 25
}

# Execution point
final_score = process_metrics(entry_data, thresholds)
print(f"Result: {final_score}")