import itertools

def preprocess_sequence(raw_data):
    filtered = [x for x in raw_data if x > 0]
    normalized = [x / sum(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]

def generate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum += val * (i + 1)
    return checksum % 17

def evaluate_stability(ratio):
    if ratio < 0.1:
        return "CRITICAL"
    elif ratio < 0.5:
        return "WARNING"
    else:
        return "STABLE"

def build_threshold_map(keys, base_offset):
    # Irrelevant mapping used to distract
    return {k: (base_offset + i) ** 2 for i, k in enumerate(keys)}

def analyze_signal(pattern, config):
    state_log = []
    accumulator = 0
    temp_snapshot = []
    
    for idx, chunk in enumerate(pattern):
        segment_sum = sum(chunk)
        if segment_sum == 0:
            continue
        
        # Real logic starts here
        norm_factor = config.get(len(chunk), 1)
        adjusted = segment_sum / norm_factor
        
        # Distractor: complex but unused calculation
        entropy_proxy = 0
        for x in chunk:
            if x > 0:
                entropy_proxy -= x * __import__('math').log(x + 1e-8)
        
        # Actual contribution to result
        if adjusted > 5:
            accumulator += int(adjusted)
        else:
            accumulator -= 1
        
        temp_snapshot.append(entropy_proxy)  # Dead storage
        
    # More distractors
    snapshot_stats = {
        'max_entropy': max(temp_snapshot) if temp_snapshot else 0,
        'length': len(temp_snapshot)
    }
    
    # Real final computation
    modifier = len(state_log) - len(temp_snapshot)  # Always negative
    final_score = accumulator + modifier
    
    # Key transformation
    final_diagnostic = abs(final_score) * 2
    return final_diagnostic

# Main execution
if __name__ == "__main__":
    raw_sensor_data = [0.1, -0.5, 0.3, 0.6, 0.0, 0.2]
    processed = preprocess_sequence(raw_sensor_data)
    
    # Irrelevant checksum
    chksum = generate_checksum(processed)
    
    # Build dummy structures for distraction
    labels = ['A', 'B', 'C']
    threshold_map = build_threshold_map(labels, 3)
    
    # Unused stability check
    status = evaluate_stability(processed[0] if processed else 0)
    
    # Core data structure - pattern buffer is key
    pattern_buffer = [
        [1, 2],
        [3, 0, 4],
        [5, 1, 1, 1],
        [0, 0],
        [2, 2]
    ]
    
    # Modify threshold_map with irrelevant updates
    for k in threshold_map:
        threshold_map[k] *= 2
    
    # Unused combinatorics
    combo_pool = list(itertools.combinations([1, 2, 3], 2))
    perm_count = len(list(itertools.permutations(['x','y'])))
    
    # Critical assignment - this is where answer is determined
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)
    
    # Final output
    print(f"Result: {final_diagnostic}")