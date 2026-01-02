def process_metrics(entries, limit):
    filtered = [e for e in entries if e['value'] > limit]
    
    # Irrelevant tracking variables (distractors)
    total_entries = len(entries)
    outlier_count = 0
    temp_sum = 0
    
    for e in entries:
        temp_sum += e['value']
        if e['value'] < 10 or e['value'] > 90:
            outlier_count += 1

    # Misleading precomputation
    avg_temp = temp_sum / total_entries if total_entries else 0
    adjusted_values = []
    
    for item in filtered:
        raw_val = item['value']
        weight = 1.0
        
        # Conditional weighting based on metadata
        if item['type'] == 'A':
            weight = 1.2
        elif item['type'] == 'B':
            weight = 0.9
        
        # Case conversion distraction
        name_upper = item['name'].upper()
        name_lower = item['name'].lower()
        name_title = item['name'].title()
        
        # Bitwise flag check (semi-relevant)
        flags = item['flags']
        has_flag_x = flags & 1
        has_flag_y = (flags >> 1) & 1
        
        # Only add if both flags are set (critical logic)
        if has_flag_x and has_flag_y:
            adjusted_values.append(raw_val * weight)
    
    # Real computation path
    base_score = sum(adjusted_values)
    penalty = len(filtered) * 0.5
    bonus = 10 if len(adjusted_values) >= 3 else 0
    
    # Final score calculation
    final_score = base_score - penalty + bonus
    
    return final_score

# Input data
input_data = [
    {'name': 'sensor_x', 'value': 45, 'type': 'A', 'flags': 3},
    {'name': 'sensor_y', 'value': 67, 'type': 'B', 'flags': 3},
    {'name': 'sensor_z', 'value': 88, 'type': 'A', 'flags': 1},
    {'name': 'sensor_w', 'value': 92, 'type': 'A', 'flags': 3},
    {'name': 'sensor_v', 'value': 76, 'type': 'B', 'flags': 3}
]
threshold = 40

# Execute
final_score = process_metrics(input_data, threshold)
print(f"Target result: {final_score}")