def analyze_sequence_overlap(seq_a, seq_b):
    position_map_a = {val: idx for idx, val in enumerate(seq_a)}
    position_map_b = {val: idx for idx, val in enumerate(seq_b)}
    
    common_values = set(position_map_a.keys()) & set(position_map_b.keys())
    
    common_positions = []
    for val in common_values:
        pos_a = position_map_a[val]
        pos_b = position_map_b[val]
        if abs(pos_a - pos_b) <= 2:
            common_positions.append((pos_a, pos_b))
    
    overlap_count = len(common_positions)
    return overlap_count

sequence_x = [10, 25, 30, 45, 50, 60]
sequence_y = [25, 40, 30, 45, 70, 10]

result = analyze_sequence_overlap(sequence_x, sequence_y)
print(f"Result: {result}")