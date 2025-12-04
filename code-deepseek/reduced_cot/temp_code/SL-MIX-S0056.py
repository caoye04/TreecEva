def process_coordinates(coords):
    valid_count = 0
    temp_sum = 0
    processed = []
    
    for i, (x, y) in enumerate(coords):
        if x > 0 and y > 0:
            valid_count += 1
            processed.append((x * 2, y // 2))
        temp_sum += x + y  # Distractor: not used in final result
    
    quadrant_analysis = {}
    for idx, (a, b) in enumerate(processed):
        if a + b > 10:
            quadrant_analysis[idx] = 'high'
        else:
            quadrant_analysis[idx] = 'low'
    
    final_count = sum(1 for val in quadrant_analysis.values() if val == 'high')
    print(f"Result: {final_count}")
    return final_count

coord_pairs = [(3, 8), (5, 12), (2, 4), (7, 9), (1, 2)]
result_analysis = process_coordinates(coord_pairs)