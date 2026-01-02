def analyze_sequence(data_stream):
    raw_length = len(data_stream)
    filtered_data = [x for x in data_stream if x % 3 == 0]
    temp_flags = set()
    for item in filtered_data:
        if item < 0:
            temp_flags.add('negative')
        if item > 50:
            temp_flags.add('high_range')
    
    # Distractor: complex but unused transformation
    encoded = ''.join([chr((i % 26) + 97) for i in range(len(temp_flags))])
    reversed_encoded = encoded[::-1].upper()  # Dead path
    dummy_sum = sum([ord(c) for c in reversed_encoded]) * 0.1  # Irrelevant calculation
    
    # Real computation begins
    base_total = 0
    for i, val in enumerate(filtered_data):
        if i % 2 == 0:
            base_total += val ** 2
        else:
            base_total -= val // 2
    
    # Another red herring: unused recursive function
    def explore_paths(seq):
        if len(seq) <= 1:
            return seq
        mid = len(seq) // 2
        return explore_paths(seq[mid:]) + explore_paths(seq[:mid])
    
    sorted_chunks = []
    chunk_size = 3
    for i in range(0, len(filtered_data), chunk_size):
        chunk = filtered_data[i:i+chunk_size]
        sorted_chunk = sorted(chunk, reverse=True)
        sorted_chunks.append(sorted_chunk)
    
    # Distractor: character frequency map with no impact
    char_map = {}
    for c in 'diagnostic_report':
        char_map[c] = char_map.get(c, 0) + 1
    vowel_count = sum(1 for k in char_map.keys() if k in 'aeiou')
    
    # Core logic hidden among noise
    aggregate_score = base_total
    adjustment_log = []
    for chunk in sorted_chunks:
        if len(chunk) >= 2:
            diff = abs(chunk[0] - chunk[1])
            adjustment_log.append(diff)
    
    if adjustment_log:
        avg_adjustment = sum(adjustment_log) / len(adjustment_log)
        correction_factor = int(avg_adjustment * 0.75)
    else:
        correction_factor = 5
    
    final_diagnostic = aggregate_score + correction_factor
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution entry point
signal_input = [12, -6, 81, 45, -15, 3, 99, 27, 33]
analyze_sequence(signal_input)