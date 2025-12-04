def final_time_calculation(log_data, cutoff, multiplier):
    irrelevant_buffer = [x * 2 for x in range(10)]  # Dead code path
    backup_calc = sum(irrelevant_buffer) * 3.14  # Misleading intermediate
    
    valid_entries = [entry for entry in log_data if entry['duration'] > cutoff]
    sorted_entries = sorted(valid_entries, key=lambda x: x['timestamp'], reverse=True)
    
    timing_offset = multiplier * 1000
    redundant_check = timing_offset // 2  # Unused calculation
    
    if len(sorted_entries) > 0:
        primary_timestamp = sorted_entries[0]['timestamp']
        secondary_check = sorted_entries[-1]['timestamp'] if len(sorted_entries) > 1 else 0
        
        adjustment_factor = len(log_data) - len(valid_entries)
        misleading_total = primary_timestamp + secondary_check + backup_calc  # Red herring
        
        result = primary_timestamp - (adjustment_factor * multiplier) + timing_offset
        debug_trace = result * 0.5  # Dead end calculation
    else:
        result = timing_offset * 2
    
    return result

log_entries = [
    {'timestamp': 1654321000, 'duration': 45, 'type': 'api'},
    {'timestamp': 1654321500, 'duration': 12, 'type': 'batch'},
    {'timestamp': 1654322000, 'duration': 28, 'type': 'api'},
    {'timestamp': 1654322500, 'duration': 8, 'type': 'cron'},
    {'timestamp': 1654323000, 'duration': 52, 'type': 'batch'}
]

threshold = 15
offset_factor = 2.5
shadow_calc = threshold * offset_factor * 100  # Irrelevant variable
backup_time = 1654323500  # Misleading constant

processing_timestamp = final_time_calculation(log_entries, threshold, offset_factor)
print(f"Result: {processing_timestamp}")