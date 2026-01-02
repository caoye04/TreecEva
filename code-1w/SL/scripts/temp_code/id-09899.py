def analyze_distribution(data_sequence):
    temp_buffer = []
    cumulative_shift = 0
    equilibrium_score = 0
    base_threshold = len(data_sequence) // 2
    
    for index, value in enumerate(data_sequence):
        shifted_value = value << 1
        temp_buffer.append(shifted_value)
        
        if index % 2 == 0:
            cumulative_shift += value
        else:
            adjustment_factor = value >> 1
            cumulative_shift -= adjustment_factor

    # Irrelevant aggregation - red herring
    redundant_sum = sum(x ** 0.5 for x in temp_buffer if x > 10)
    spike_count = len([x for x in data_sequence if x > base_threshold])

    intermediate_stats = {}
    for i, val in enumerate(temp_buffer):
        intermediate_stats[i] = val % 13
    
    # Distractor loop - computes but doesn't impact main result
    outlier_flags = []
    for k in intermediate_stats:
        if intermediate_stats[k] in [1, 3, 5]:
            outlier_flags.append(k * 2)

    # Real computation chain begins
    filtered_data = [x for x in data_sequence if x % 3 != 0]
    filtered_sum = sum(filtered_data)
    
    checksum = 0
    for num in filtered_data:
        checksum ^= num
    
    # Key state variables
    validation_key = checksum & 0xFF
    activation_level = len(filtered_data) + validation_key
    
    # Secondary distractor: complex but unused structure
    metadata_map = dict(zip(range(len(temp_buffer)), temp_buffer))
    sliced_view = list(temp_buffer[::2])
    
    # Core logic embedded with noise
    trend_vector = [filtered_sum, activation_level, cumulative_shift]
    trend_vector.append(sum(sliced_view[:3]))  # Semi-relevant injection

    final_tally = trend_vector[0] + trend_vector[1] - trend_vector[2]
    
    # Critical statement
    equilibrium_score = final_tally // (index + 1)
    
    # Final print required
    print(f"Result: {equilibrium_score}")

# Input data
input_sequence = [7, 4, 9, 12, 5, 8, 11]
analyze_distribution(input_sequence)