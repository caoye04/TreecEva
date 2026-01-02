def process_segments(data, weight_map):
    temp_results = []
    cumulative_shift = 0
    
    for segment in data:
        base_value = len(segment['content'])
        normalized = base_value / (segment['offset'] + 1)
        
        # Irrelevant transformation chain
        shifted = normalized + 2.718
        adjusted = shifted - 2.718  # Neutralizes previous shift
        
        # Distractor: case-insensitive counting with no impact
        char_count = sum(1 for c in segment['content'].upper() if c.isalpha())
        dummy_flag = char_count > 10
        
        # Actual relevant logic
        weight_key = segment['type']
        scaling_factor = weight_map.get(weight_key, 1.0)
        temp_results.append(adjusted * scaling_factor)
        
        # Tracking unrelated state
        cumulative_shift += len(segment['content']) % 3
    
    # Real computation using list comprehension and set operations
    filtered = [val for val in temp_results if val > 1.5]
    unique_floor = list(set(int(x) for x in filtered))
    
    # Secondary distractor: string method chain with no output effect
    metadata_str = "raw_segment_summary"
    formatted = metadata_str.replace('_', '-').title()
    tokens = formatted.split('-')
    
    final_score = sum(unique_floor) * (2 if len(unique_floor) > 2 else 1)
    return final_score

# Input setup
segment_data = [
    {'content': 'sensor_log_01', 'offset': 2, 'type': 'critical'},
    {'content': 'dbg_msg_init', 'offset': 1, 'type': 'debug'},
    {'content': 'status_update_high', 'offset': 3, 'type': 'critical'},
    {'content': 'info_tick', 'offset': 1, 'type': 'info'},
    {'content': 'critical_fault_5', 'offset': 2, 'type': 'critical'}
]

weights = {
    'critical': 2.0,
    'debug': 0.5,
    'info': 1.0
}

# Execution entry point
interim_test = [len(s['content']) for s in segment_data]  # Dead-end analysis
flag_check = any('err' in s['content'] for s in segment_data)  # Always False, irrelevant

final_score = process_segments(segment_data, weights)
print(f"Result: {final_score}")