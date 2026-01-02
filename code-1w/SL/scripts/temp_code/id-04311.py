def analyze_sensor_readings(readings):
    baseline = 10
    offset = sum([x for x in readings if x > 25]) // len(readings) if readings else 0
    adjusted_readings = [r - baseline + offset for r in readings]

    # Irrelevant transformation (distractor)
    squared_pairs = [(x**2, y**2) for x in readings[:3] for y in readings[-3:]]
    total_pairs = len(squared_pairs)

    # Logical filtering with conditional expression
    threshold = 15 if len(readings) > 5 else 10
    masked_readings = [val if val >= threshold else 0 for val in adjusted_readings]

    # Semi-relevant computation chain
    temp_buffer = []
    for val in masked_readings:
        if val == 0:
            continue
        temp_buffer.append(val * 1.1)

    # Core logic embedded in list comprehension and lambda
    apply_correction = lambda x: int(x + (x * 0.05))
    corrected_data = [apply_correction(x) for x in temp_buffer]

    # Filtering step that determines final answer
    filtered_data = [x for x in corrected_data if x % 2 == 1]
    
    # Key assignment point
    filtration_score = sum(filtered_data)
    
    # Dead code path (distractor)
    if False:
        backup_score = sum(corrected_data) // 2
        filtration_score = max(filtration_score, backup_score)

    return filtration_score

# Simulate sensor data input
sensor_input = [8, 12, 26, 14, 30, 9, 28, 11]
result = analyze_sensor_readings(sensor_input)
print(f"Result: {result}")