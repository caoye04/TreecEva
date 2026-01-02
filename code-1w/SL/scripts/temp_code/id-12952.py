def process_sensor_array(raw_readings, config):
    # Irrelevant preprocessing block (dead code path)
    temp_cache = {}
    for idx, val in enumerate(raw_readings):
        if val < 0:
            temp_cache[idx] = abs(val) ** 0.5

    # Distractor: complex but unused transformation
    normalized = [max(0, min(100, (x - config['min_val']) * 10)) for x in raw_readings]
    stats_summary = {
        'peak': max(normalized),
        'trough': min(normalized),
        'span': len([n for n in normalized if n > 50])
    }

    # Actual relevant data filtering
    filtered_data = []
    for i, reading in enumerate(raw_readings):
        if i % 2 == 0 and reading > config['filter_floor']:
            filtered_data.append(reading * config['gain'])

    # Misleading secondary processing (never called)
    def compute_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        return -sum((count / len(data)) * log(count / len(data)) for count in freq.values())

    # Another red herring: builds a structure but doesn't use it
    decoy_matrix = [[i + j for j in range(3)] for i in range(len(raw_readings))]
    checksum = sum(sum(row) for row in decoy_matrix) % 1000

    # Real logic begins: build threshold map based on config
    base_threshold = config['base_threshold']
    threshold_map = {}
    for index, value in enumerate(filtered_data):
        if value > base_threshold * 2:
            threshold_map[index] = base_threshold + (value // 100)
        elif value > base_threshold:
            threshold_map[index] = base_threshold
        else:
            threshold_map[index] = base_threshold - 5

    # Critical function call
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Final output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic


def analyze_readings(data, thresholds):
    # Core analysis with conditional branching and early exits
    if len(data) == 0:
        return -1
    
    cumulative_score = 0
    adjustment_factor = 1.5
    
    for idx, val in enumerate(data):
        # Case conversion analog: simulate mode switching
        mode = 'aggressive' if val > 150 else 'conservative'
        
        # Character counting analog: digit-based weighting
        digit_count = len(str(abs(val)))
        
        threshold = thresholds.get(idx, 100)
        
        if mode == 'aggressive':
            if val > threshold * 1.3:
                cumulative_score += (val - threshold) * adjustment_factor
            elif val > threshold:
                cumulative_score += (val - threshold) * 0.8
            else:
                cumulative_score -= 10  # penalty
                break  # early termination on failure
        else:
            if val >= threshold:
                cumulative_score += (val - threshold) * 1.1
            else:
                # Use of zip to align with dummy correction factors
                corrections = [0.1, 0.2, 0.3, 0.4]
                indices = list(range(len(corrections)))
                for pos, corr in zip(indices, corrections):
                    if idx == pos:
                        cumulative_score -= corr * 100

    # Additional distraction: bitwise manipulation (unused)
    debug_flag = (cumulative_score << 2) ^ 0xFF
    
    # Final adjustment based on data length parity (actual effect)
    if len(data) % 2 == 1:
        cumulative_score = int(cumulative_score * 1.2)
    
    return int(cumulative_score)

# Execution entry point
if __name__ == "__main__":
    sensor_input = [89, 167, 45, 201, 78, 234, 112]
    system_config = {
        'min_val': 20,
        'filter_floor': 90,
        'gain': 1.3,
        'base_threshold': 120
    }
    process_sensor_array(sensor_input, system_config)