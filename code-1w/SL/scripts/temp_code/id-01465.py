def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    temp_offset = 0.0  # unused distraction
    final_score = 0
    
    for entry in data:
        raw_value = entry['metric'] * base_multiplier
        if entry['anomaly_flag']:
            raw_value *= penalty_factor
        
        # Distractor block: irrelevant computation
        debug_checksum = 0
        for c in entry['tag']:
            debug_checksum += ord(c) % 7
        debug_checksum = debug_checksum ** 2 if debug_checksum > 10 else 0
        
        # Conditional expression used
        adjustment = 5.0 if raw_value > bonus_threshold else (2.5 if raw_value > 70 else 0)
        
        # Accumulate score
        final_score += raw_value + adjustment
        
        # Early exit red herring (never triggered due to data)
        if raw_value < 0:
            return -1  # dead code path

    # Another distraction: string processing with no impact
    metadata_log = "Processed entries: " + str(len(data))
    metadata_log = metadata_log.upper().replace("PROCESSED", "COMPLETE")
    
    scaling_constant = 1.1
    final_score = int(final_score * scaling_constant)  # final meaningful assignment
    
    return final_score

# Input data
benchmark_data = [
    {'metric': 60, 'anomaly_flag': False, 'tag': 'A1'},
    {'metric': 70, 'anomaly_flag': True, 'tag': 'B2'},
    {'metric': 90, 'anomaly_flag': False, 'tag': 'C3'},
    {'metric': 80, 'anomaly_flag': False, 'tag': 'D4'}
]

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")