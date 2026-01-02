def analyze_sensor_data(raw_readings, threshold=0.75):
    # Simulate preprocessing pipeline for environmental sensor network
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in normalized if x > 0.1]
    
    # Irrelevant transformation: frequency domain simulation (distraction)
    fft_simulated = []
    for i in range(len(filtered)):
        accum = 0
        for j in range(len(filtered)):
            import math
            accum += filtered[j] * math.cos(2 * math.pi * i * j / len(filtered))
        fft_simulated.append(accum)
    
    # Decoy function that's never called (dead code path)
    def calibrate_noise_floor(data, alpha=0.9):
        return [x * alpha + (1 - alpha) * 0.05 for x in data]
    
    # Identify high-confidence readings
    high_confidence = [x for x in filtered if x > threshold]
    
    # Compute rolling average (irrelevant to final result)
    window_size = 3
    rolling_averages = []
    for i in range(len(filtered) - window_size + 1):
        rolling_averages.append(sum(filtered[i:i+window_size]) / window_size)
    
    # Create diagnostic summary (distractor variables)
    spike_count = 0
    for i in range(1, len(filtered)):
        if filtered[i] > 1.8 * filtered[i-1]:
            spike_count += 1
    
    # Core logic disguised among distractions
    candidate_sets = []
    for start in range(len(high_confidence)):
        for end in range(start + 1, len(high_confidence) + 1):
            subset = high_confidence[start:end]
            if len(subset) >= 2 and max(subset) - min(subset) < 0.25:
                candidate_sets.append(set(round(x, 3) for x in subset))
    
    # Use set operations to find most consistent group
    consensus = set()
    if candidate_sets:
        consensus = candidate_sets[0]
        for s in candidate_sets[1:]:
            consensus = consensus.intersection(s)
        if not consensus:
            consensus = candidate_sets[-1]  # fallback
    
    # Apply slicing to derive refinement set (relevant operation)
    sorted_candidates = sorted([sum(cs) for cs in candidate_sets if cs])
    refined_candidates = sorted_candidates[::2]  # take every other (slicing distractor)
    
    # Final decision logic
    if len(high_confidence) == 0:
        optimal_set = set()
    else:
        # Find set with minimal variance (key computation)
        best_var = float('inf')
        optimal_set = set()
        for cs in candidate_sets:
            values = list(cs)
            mean_val = sum(values) / len(values)
            var = sum((x - mean_val) ** 2 for x in values) / len(values)
            if var < best_var and len(cs) >= 2:
                best_var = var
                optimal_set = cs.copy()
    
    # Critical execution point
    filtration_score = len(optimal_set)
    
    # More red herrings: simulate transmission overhead
    overhead_bits = 0
    for item in optimal_set:
        overhead_bits += len(f'{int(item * 1000):b}')
    
    # Additional decoy: attempt reverse mapping (unused)
    reverse_map = {round(v, 3): idx for idx, v in enumerate(raw_readings)}
    
    # Output required result
    print(f"Result: {filtration_score}")

# Execute with sample data
data_input = [120, 234, 98, 450, 231, 129, 904, 321, 654, 876]
analyze_sensor_data(data_input)