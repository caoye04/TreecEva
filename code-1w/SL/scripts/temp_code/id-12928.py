def process_sensor_array(raw_stream, config):
    # Irrelevant preprocessing block (dead path)
    if len(raw_stream) == 0:
        return [0] * 10

    temp_cache = []
    for val in raw_stream:
        if val > 100:
            temp_cache.append(val // 3)
        elif val < -50:
            temp_cache.append(-val % 7)
        else:
            temp_cache.append(val + 2)

    # Distractor: complex-looking but unused transformation
    shadow_normalized = [round((x - min(temp_cache)) / (max(temp_cache) - min(temp_cache) + 1e-8) * 100) for x in temp_cache]
    inverted_map = {i: shadow_normalized[-(i+1)] for i in range(len(shadow_normalized)) if i % 3 == 0}

    # Actual relevant data filtering
    valid_range = config.get('range', (-30, 80))
    filtered_data = [x for x in raw_stream if valid_range[0] <= x <= valid_range[1]]

    # Misleading statistical decoy
    mean_val = sum(temp_cache) / len(temp_cache) if temp_cache else 0
    outlier_score = sum(1 for x in temp_cache if abs(x - mean_val) > 2 * (sum((y - mean_val)**2 for y in temp_cache)/len(temp_cache))**0.5)

    # Unused recursive red herring
    def explore_anomaly(seq, depth):
        if depth <= 0 or len(seq) < 2:
            return seq[0] if seq else 0
        mid = len(seq) // 2
        left = explore_anomaly(seq[:mid], depth - 1)
        right = explore_anomaly(seq[mid:], depth - 1)
        return (left ^ right) + depth

    # Early exit distraction (never reached due to logic)
    if config.get('debug_mode') and len(filtered_data) > 100:
        checksum = sum(explore_anomaly(filtered_data[i:i+10], 3) for i in range(0, len(filtered_data), 10))
        return [checksum]

    # Key control flow with slicing and conditional expression
    window_size = config.get('window', 5)
    sliding_windows = [filtered_data[i:i+window_size] for i in range(0, max(1, len(filtered_data) - window_size + 1))]
    
    # Decoy aggregation with bitwise distraction
    mask = 0
    for w in sliding_windows:
        if len(w) == window_size:
            mask ^= int(sum(w) / len(w)) & 0xF

    # Real computation path begins here
    threshold = config.get('sensitivity', 10) * 1.5

    def analyze_readings(data, limit):
        if not data:
            return -999
        
        # Conditional expression + slicing mix
        primary_segment = data[len(data)//3 : ] if len(data) > limit else data[:len(data)//2]
        secondary_slice = data[::-1][:len(primary_segment)]
        
        # Core arithmetic-boolean fusion
        base_score = 0
        for i, (a, b) in enumerate(zip(primary_segment, secondary_slice)):
            diff = abs(a - b)
            contribution = (diff * (i + 1)) if (diff > 2 and (a | b) & 1) else (diff // (i + 1) if i > 0 else 0)
            base_score += contribution
            
            # Early break on logical condition (not always triggered)
            if base_score > limit * 10 and i > len(primary_segment) // 2:
                break

        # Final adjustment using distractor variables in non-impactful way
        adjustment = 5 if mask > 10 else -3
        return int(base_score) + adjustment  # adjustment is irrelevant due to masking below

    final_diagnostic = analyze_readings(filtered_data, threshold)
    
    # Redundant override based on unused recursion result (distraction)
    anomaly_probe = explore_anomaly([final_diagnostic], 2)
    if anomaly_probe != 42:  # Always true
        final_diagnostic = final_diagnostic  # No-op

    # Irrelevant sorting of decoy structure
    sorted_inverted = sorted(inverted_map.values())
    pivot = sorted_inverted[len(sorted_inverted)//2] if sorted_inverted else 0

    # Critical output
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# Execution entry point with deterministic input
sensor_input = [12, -5, 23, 67, -14, 34, 8, 55, -22, 41, 9, 66, -8]
settings = {'range': (-25, 70), 'sensitivity': 8, 'window': 4, 'debug_mode': False}
process_sensor_array(sensor_input, settings)