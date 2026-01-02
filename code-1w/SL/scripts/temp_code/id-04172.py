import math

# Simulated sensor array diagnostics with noise filtering and health scoring
def analyze_sensor_health(raw_readings, threshold=0.75):
    normal_count = sum(1 for x in raw_readings if abs(x) < 1.0)
    total_sensors = len(raw_readings)
    health_ratio = normal_count / total_sensors if total_sensors else 0

    # Irrelevant transformation (distractor)
    squared_norms = [x**2 for x in raw_readings]
    avg_squared = sum(squared_norms) / len(squared_norms) if squared_norms else 0
    decay_factor = math.exp(-avg_squared)

    return health_ratio > threshold

# Legacy function - unused but looks relevant (dead code path)
def legacy_calibrate(sequence):
    return [x * 0.98 + 0.5 for x in sequence]

# Signal preprocessing with multiple steps and red herrings
def preprocess_signal(amplitudes):
    # Apply windowing (seemingly important, actually irrelevant)
    windowed = [amp * (0.54 - 0.46 * math.cos(2 * math.pi * i / len(amplitudes))) 
                for i, amp in enumerate(amplitudes)]
    
    # Compute FFT-like magnitude approx (distractor computation)
    real_parts = [sum(windowed[j] * math.cos(2 * math.pi * k * j / len(windowed)) 
                       for j in range(len(windowed))) for k in range(5)]
    magnitudes = [math.sqrt(r**2 + 0.1) for r in real_parts]
    avg_magnitude = sum(magnitudes) / len(magnitudes)

    # Actual relevant processing: clip and normalize
    clipped = [max(min(x, 1.5), -1.5) for x in amplitudes]
    normalized = [x / 1.5 if x >= 0 else x / 2.0 for x in clipped]
    
    return normalized

# Core data pipeline
raw_input = [0.1, -0.3, 1.8, -2.1, 0.5, 0.7, -1.2, 0.4, 3.2, -0.8]

# Distractor variables (misleading intermediate results)
dropped_sensors = [i for i, x in enumerate(raw_input) if abs(x) > 3.0]
redundant_stats = {
    'peak': max(raw_input, default=0),
    'truncated_sum': sum(x for x in raw_input if x > 0.5),
    'legacy_score': sum(1 for x in raw_input if x != 0) * 0.77
}

# Filter logic with conditional expression (key feature)
filtered_data = [x for x in raw_input if -2.5 <= x <= 2.5] if len(raw_input) > 5 else raw_input[:3]

# Secondary filter based on health (adds nesting and complexity)
system_healthy = analyze_sensor_health([x for x in raw_input if x < 1.0])
if system_healthy:
    filtered_data = [x for x in filtered_data if x >= -1.5]

    # Nested conditional with lambda (required feature)
    transform = lambda z: z * 1.25 if z > 0 else z * 0.8
    processed_filtered = [transform(x) for x in filtered_data]

    # Another layer of irrelevant computation (distractor)
    entropy_proxy = -sum(x * math.log(abs(x) + 1e-8) for x in processed_filtered)
    compression_estimate = len(processed_filtered) / (entropy_proxy + 1)

    def process_readings(data):
        # Complex multi-step reasoning
        base_score = sum(math.sin(x) for x in data)
        adjustment = 0
        
        for i, val in enumerate(data):
            if i % 2 == 0:
                adjustment += math.cos(val) * 0.5
            else:
                adjustment -= math.tan(0.1 * val) * 0.3
        
        # Combinatorics-inspired weighting (simple combinatorics)
        pair_interactions = 0
        n = len(data)
        if n > 1:
            pair_interactions = n * (n - 1) // 2 * 0.01
        
        # Character counting distractor (counts 'e' in function names - meaningless)
        e_count = sum(func_name.count('e') for func_name in ['process_readings', 'analyze_sensor_health'])
        phantom_offset = e_count * 0.05

        # Final computation chain
        raw_total = base_score + adjustment
        scaled_total = raw_total * (1 + pair_interactions)
        final_diagnostic = int(scaled_total * 100 + phantom_offset)  # Key output
        
        # Dead code - never executed but looks important
        if False:
            final_diagnostic = math.gamma(final_diagnostic + 10)
        
        return final_diagnostic

    # Execute key statement
    final_diagnostic = process_readings(processed_filtered)
else:
    final_diagnostic = -999  # fallback (not taken due to data)

# Additional red herring: tuple-based status tracking (unused)
current_state = ('diagnostic_phase', 'sensor_array_7', 3.14159)
state_metadata = {
    'version': current_state[2],
    'active': True if current_state[0] == 'diagnostic_phase' else False
}

# Print result as required
print(f"Result: {final_diagnostic}")