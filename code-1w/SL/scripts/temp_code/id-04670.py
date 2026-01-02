def analyze_sequence(raw_values):
    offset = 7
    shifted = raw_values[2:] + raw_values[:2]
    transformed = [x * 2 for x in shifted]
    filtered = [v for v in transformed if v > 10]
    processed_data = tuple(filtered)
    temp_sum = sum(processed_data[:2])
    final_offset = len(processed_data) * 3
    result = processed_data[1] + final_offset
    return result

values = [1, 5, 3, 8, 4]
output = analyze_sequence(values)
print(f"Result: {output}")