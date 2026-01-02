def analyze_signal_pattern(raw_samples):
    filtered_samples = [x for x in raw_samples if x > 0]
    window_size = 3
    smoothed_values = []
    
    for i in range(len(filtered_samples) - window_size + 1):
        window_avg = sum(filtered_samples[i:i+window_size]) / window_size
        smoothed_values.append(round(window_avg))
    
    # Irrelevant transformation (distractor)
    inverted_map = {i: val for i, val in enumerate(reversed(smoothed_values))}
    temp_offset = len(smoothed_values) // 2
    
    # Key data paths
    forward_pass = [smoothed_values[i] * (i + 1) for i in range(len(smoothed_values))]
    backward_pass = [smoothed_values[-(i+1)] * (i + 1) for i in range(len(smoothed_values))]
    
    # Dummy computation (dead logic path)
    cumulative_drift = 0
    for j in range(len(forward_pass)):
        if j % 2 == 0:
            cumulative_drift += forward_pass[j] * 0.1  # Not used later
    
    # Noise buffer (irrelevant variable)
    noise_buffer = [0] * len(smoothed_values)
    for idx in range(len(noise_buffer)):
        noise_buffer[idx] = (idx + 1) * 0.05
    
    equilibrium_score = abs(sum(forward_pass) - sum(backward_pass))
    
    # Additional misleading metric
    symmetry_ratio = (sum(forward_pass) + 1) / (sum(backward_pass) + 1) if sum(backward_pass) != 0 else 0
    
    # Final output
    print(f"Result: {equilibrium_score}")

# Input data
input_data = [4, -2, 6, 0, 8, -1, 5, 3]
analyze_signal_pattern(input_data)