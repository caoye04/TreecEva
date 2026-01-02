def analyze_performance(records):
    total_score = 0
    temp_buffer = []
    points_multiplier = 3
    base_offset = len(records) % 4
    
    for i, record in enumerate(records):
        if i % 2 == 0:
            temp_buffer.append(record['value'] ** 0.5)
        else:
            temp_buffer.append(record['value'] // 4)
    
    backup_data = [x * 2 for x in temp_buffer if x > 5]  # Distractor: not used later
    adjustment_factor = sum(temp_buffer) / (len(temp_buffer) or 1)
    
    status_flags = {k: False for k in range(len(records))}
    for idx, item in enumerate(records):
        confidence = item.get('confidence', 1)
        index = idx + base_offset
        raw_points = item['value'] * confidence
        
        if raw_points > 10:
            capped_points = 10
        else:
            capped_points = raw_points
        
        # Key computation chain
        if index % 3 == 0:
            points_multiplier += 1
        elif index % 3 == 1:
            points_multiplier -= 1
        
        if item['active']:
            points_multiplier = max(1, points_multiplier)
            total_score += points_multiplier * (index + 1)

    # Irrelevant post-processing
    final_buffer = []
    for val in temp_buffer:
        final_buffer.append(val * adjustment_factor)
    
    # Output target result
    print(f"Result: {total_score}")

# Input data
input_records = [
    {'value': 16, 'active': True, 'confidence': 1.2},
    {'value': 8, 'active': False, 'confidence': 0.8},
    {'value': 25, 'active': True, 'confidence': 1.5},
    {'value': 12, 'active': True, 'confidence': 0.9},
    {'value': 36, 'active': False, 'confidence': 1.1}
]

analyze_performance(input_records)