def analyze_crop_patterns(field_data, threshold=3):
    pattern_count = 0
    temp_sum = 0
    for row in field_data:
        if len(row) > threshold:
            center = len(row) // 2
            left_part = row[:center]
            right_part = row[center:]
            temp_sum += sum(left_part) - sum(right_part)
            if left_part.count(1) == right_part.count(1):
                pattern_count += 1
    return pattern_count

def sanitize_input(raw_input):
    cleaned = raw_input.strip().upper()
    if 'ERROR' in cleaned:
        return ''
    return cleaned.replace(',', ';')

def calculate_harvest_efficiency(data, config):
    total_yield = 0
    efficiency_factor = config.get('efficiency', 1.0)
    decay_rate = config.get('decay', 0.95)
    base_multiplier = config.get('multiplier', 2)
    
    # Irrelevant string processing (distractor)
    input_trace = "data_source_001.log"
    file_extension = input_trace.split('.')[-1]
    is_valid_format = file_extension in ['log', 'txt']
    
    anomaly_score = 0
    stable_fields = 0
    
    for i, field in enumerate(data):
        field_id_str = f"F{i:03}"
        if field_id_str.startswith('F'):
            pass  # dummy check
        
        # Real logic begins
        if sum(field) > config.get('threshold', 10):
            adjusted = [x * efficiency_factor for x in field]
            capped = [min(x, 15) for x in adjusted]
            
            # Modular arithmetic core step
            field_yield = sum(capped) % 97
            
            # String slicing distractor
            metadata_tag = field_id_str[1:] + "X"
            tag_value = int(metadata_tag[:-1]) % 10
            
            if tag_value > 5:
                anomaly_score += 1
            else:
                total_yield += field_yield
                stable_fields += 1
        else:
            # Dead code path (distractor)
            backup_yield = 0
            for val in field:
                backup_yield = (backup_yield * 2 + val) % 100
    
    # Secondary distractor computation
    avg_stable = stable_fields / len(data) if data else 0
    diagnostic_flag = sanitize_input("status_ok")
    
    # Final calculation with early return avoided
    if stable_fields == 0:
        final_efficiency = 0
    else:
        final_efficiency = (total_yield * base_multiplier) * decay_rate
    
    # Key result
    final_yield = int(final_efficiency + 0.5)  # round to nearest int
    return final_yield

# Main execution
field_data = [
    [4, 5, 6, 7],
    [2, 8, 3, 9],
    [5, 5, 5, 5],
    [1, 1, 10, 12],
    [7, 1, 1, 1]
]

diag_mode = True
config = {
    'efficiency': 1.1,
    'decay': 0.98,
    'multiplier': 3,
    'threshold': 15
}

# Call function
final_yield = calculate_harvest_efficiency(field_data, config)
print(f"Result: {final_yield}")