def analyze_data_stream():
    raw_signal = [i * 3 + 2 for i in range(15)]
    offset = 7
    shifted_signal = [x - offset for x in raw_signal]
    
    # Irrelevant transformation (distractor)
    inverted = [abs(x - 10) for x in shifted_signal if x > 5]
    temp_buffer = [x ** 0.5 for x in inverted if x > 0]  # Dead-end computation
    
    # Key data path
    mod_flags = [x % 4 == 0 for x in shifted_signal]
    masked_values = [x if flag else 0 for x, flag in zip(shifted_signal, mod_flags)]
    
    # Another distraction: tracking unused stats
    avg_masked = sum(masked_values) / len(masked_values) if masked_values else 0
    outlier_count = sum(1 for x in shifted_signal if abs(x) > 15)
    
    # Core logic with slicing and filtering
    candidate_window = shifted_signal[3:12]  # Focus on subset
    filtered_candidates = [x for x in candidate_window if x > -5]
    padding = [0] * (9 - len(filtered_candidates))
    padded_filtered = filtered_candidates + padding  # Padding has no effect
    
    # Final computation
    relevant_values = [x for x in padded_filtered if x % 3 == 2]
    filtered_sum = sum(relevant_values)
    
    # Output required format
    print(f"Result: {filtered_sum}")

analyze_data_stream()