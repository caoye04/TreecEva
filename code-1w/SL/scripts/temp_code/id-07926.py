import itertools

# Simulate sensor data from a fusion reactor monitoring system
def generate_sensor_stream(base_value, noise_level, cycles):
    stream = []
    for i in range(cycles):
        noise = (i * 0.01) % noise_level
        stream.append(base_value + noise if i % 3 != 0 else base_value - noise)
    return stream

# Analyze phase coherence in oscillation patterns
def calculate_coherence(data):
    if len(data) < 2:
        return 0.0
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    avg_diff = sum(diffs) / len(diffs)
    return round(1 / (1 + avg_diff), 6)

# Misleading function: looks relevant but unused in final calculation
def deprecated_diagnostic(signal, threshold=0.5):
    count = 0
    for s in signal:
        if s > threshold:
            count += int(s * 10) % 3
    return count * threshold

# Bit manipulation to encode state transitions
def encode_state_sequence(states):
    encoded = 0
    for i, state in enumerate(states):
        if state > 0.7:
            encoded ^= (1 << (i % 8))  # XOR with bit position
        elif state < 0.3:
            encoded |= (1 << ((i + 3) % 8))  # OR with offset bit
    return encoded & 255  # Clamp to 8 bits

# Core evaluation logic
def evaluate_cycle_data(readings):
    # Extract every third reading (critical filtering)
    filtered = [v for i, v in enumerate(readings) if i % 3 == 1]
    
    # Compute moving average over window of 2
    averages = [(filtered[i] + filtered[i+1]) / 2 for i in range(len(filtered)-1)]
    
    # Determine stability bands
    stable_count = sum(1 for a in averages if 0.4 <= a <= 0.6)
    
    # Apply decay factor based on position
    weighted_stable = sum(averages[i] * 0.9**i for i in range(len(averages)))
    
    # Dummy transformation (distraction)
    _ = [x ** 0.5 for x in readings if x > 0.25]
    
    return weighted_stable, stable_count

# Higher-order analysis using itertools
def analyze_pattern_repetition(values, window_size=3):
    chunks = list(itertools.zip_longest(*[iter(values)]*window_size))
    pattern_freq = {}
    for chunk in chunks:
        key = tuple(round(x, 3) for x in chunk if x is not None)
        pattern_freq[key] = pattern_freq.get(key, 0) + 1
    
    # Return max frequency (used later)
    return max(pattern_freq.values()) if pattern_freq else 1

# Main performance evaluator
def evaluate_performance(raw_results, scaling_factor):
    # Step 1: Preprocess raw results
    processed = [round(x * 1.05, 4) for x in raw_results]
    
    # Step 2: Detect repeating sequences
    repetition_index = analyze_pattern_repetition(processed)
    
    # Step 3: Evaluate cycle metrics
    weight, count = evaluate_cycle_data(processed)
    
    # Step 4: Calculate phase coherence
    coherence = calculate_coherence(processed)
    
    # Step 5: Encode internal state (distractor: not used in final score)
    _ = encode_state_sequence([coherence, weight / 100, count / 10])
    
    # Step 6: Apply scaling and repetition bonus
    base_score = weight * scaling_factor
    bonus_score = base_score * (0.1 * repetition_index)
    
    # Final computation
    final = base_score + bonus_score + (coherence * 100)
    
    # Red herring: unused variable that looks important
    diagnostic_flag = deprecated_diagnostic(processed)
    
    return round(final, 4)

# Irrelevant global variables (distractors)
MAX_BUFFER_SIZE = 1024
current_mode = 'diagnostic'
emergency_override = False
temp_log = []

# Generate input data
sensor_data = generate_sensor_stream(base_value=0.5, noise_level=0.2, cycles=18)

# Extract subset for actual processing
working_data = sensor_data[:12]  # Only first 12 used

# Efficiency factor derived from system constants (has real impact)
efficiency_factor = (MAX_BUFFER_SIZE % 13) * 0.01  # evaluates to 0.09

# Execute core logic
cycle_results = working_data

# Critical statement
final_score = evaluate_performance(cycle_results, efficiency_factor)

# Output result
print(f"Result: {final_score}")