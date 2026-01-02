def calculate_efficiency(data):
    base_efficiency = 0.85
    penalty_factor = 0.1
    bonus_factor = 0.2
    size_threshold = 100
    adjustment = 0.0

    # Irrelevant tracking variables (distractors)
    total_iterations = 0
    temp_result_log = []
    
    for i, entry in enumerate(data):
        total_iterations += 1
        if len(entry['buffer']) > size_threshold:
            adjustment -= penalty_factor
        elif entry['status'] == 'optimal':
            adjustment += bonus_factor
        
        # Dead computation: used nowhere
        intermediate_calc = (i + 1) * base_efficiency % 0.5
        temp_result_log.append(intermediate_calc)

    # Semi-relevant but not critical transformation
    adjustment = max(-0.3, min(adjustment, 0.3))  # Clamp adjustment

    return int((base_efficiency + adjustment) * 100)

# Simulated sensor data processing pipeline
raw_packets = [
    {'id': 1, 'buffer': list(range(80)), 'status': 'normal'},
    {'id': 2, 'buffer': list(range(120)), 'status': 'normal'},
    {'id': 3, 'buffer': list(range(90)), 'status': 'optimal'},
    {'id': 4, 'buffer': list(range(150)), 'status': 'critical'}
]

# Data preprocessing with slicing and lambda (required Python features)
filter_valid = lambda x: x['status'] != 'critical'
filtered_packets = [p for p in raw_packets if filter_valid(p)]

processed_data = []
for packet in filtered_packets:
    # Extract summary using slicing
    sample_window = packet['buffer'][10:20]  # Slice irrelevant to final logic
    avg_sample = sum(sample_window) / len(sample_window)
    
    # Add processed entry
    processed_data.append({
        'packet_id': packet['id'],
        'status': packet['status'],
        'window_avg': avg_sample
    })

# Additional distraction: unused helper function
unused_helper = lambda arr: sum(x ** 0.5 for x in arr if x > 50)
irrelevant_sum = unused_helper(raw_packets[0]['buffer'])

# Key computational step
efficiency_score = calculate_efficiency(processed_data)

# Output result as required
print(f"Target result: {efficiency_score}")