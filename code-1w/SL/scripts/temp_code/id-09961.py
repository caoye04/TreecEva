def analyze_readings(raw_readings, threshold):
    normalized = [int(x * 1.5) for x in raw_readings if x > 0]
    offset = 10
    adjusted = [x + offset for x in normalized]
    processed_data = [x ** 2 for x in adjusted if x < 50]
    
    base_criteria = {i for i in range(5, 35)}
    extra_flags = {25, 30, 35, 40}
    valid_set = base_criteria.union(extra_flags).difference({15})

    temp_buffer = [x for x in processed_data if x % 2 == 0]
    filtered_sum = sum(filter(lambda x: x in valid_set, processed_data))
    
    correction_factor = 0.9
    final_score = int(filtered_sum * correction_factor)
    
    return final_score

result = analyze_readings([2.0, 3.0, 1.0, 4.0], 2)
print(f"Result: {result}")