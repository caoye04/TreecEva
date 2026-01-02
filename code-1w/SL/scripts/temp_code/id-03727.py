def analyze_data_stream(raw_input):
    tokens = raw_input.split(',')
    parsed_numbers = [float(x.strip()) for x in tokens if x.strip().isdigit() or (x.strip()[1:].isdigit() and x.strip().startswith('-'))]
    
    # Irrelevant transformation: reverse and join string (distractor)
    reversed_str = ''.join([t[::-1] for t in tokens])
    dummy_checksum = sum([ord(c) for c in reversed_str]) % 17
    
    # State tracking with intermediate variables
    temp_results = []
    outlier_threshold = 100
    scaling_factor = 2.5
    
    for num in parsed_numbers:
        scaled = num * scaling_factor
        if abs(scaled) < outlier_threshold:
            temp_results.append(scaled)
    
    # Secondary filter based on modulo pattern
    candidate_values = [val for val in temp_results if val % 3 == 2]
    
    # More distraction: simulate a frequency count (not used in final result)
    freq_map = {}
    for v in candidate_values:
        rounded = round(v)
        freq_map[rounded] = freq_map.get(rounded, 0) + 1
    
    adjustment_offset = len(freq_map) * 0.5
    
    # Final filtering: only values greater than computed offset
    relevant_values = [v for v in candidate_values if v > adjustment_offset]
    
    filtered_sum = sum(relevant_values)
    
    # Extra unused computation to increase interference
    max_possible_triplet_product = 0
    for i in range(len(relevant_values)):
        for j in range(i+1, len(relevant_values)):
            for k in range(j+1, len(relevant_values)):
                product = relevant_values[i] * relevant_values[j] * relevant_values[k]
                if product > max_possible_triplet_product:
                    max_possible_triplet_product = product

    return filtered_sum

# Simulate input data stream
data_stream = "12, -5, 40, 8, abc, 3, 9, 25, 7"
result = analyze_data_stream(data_stream)
print(f"Result: {result}")