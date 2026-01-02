import itertools

# Simulate sensor data stream with noise and valid segments
def generate_signal():
    raw_values = [x * 0.5 for x in range(20)]
    noise = [0.1, -0.2, 0.3, -0.1, 0.0, 0.2, -0.3, 0.1]
    signal = []
    for i in range(len(raw_values)):
        noise_val = noise[i % len(noise)]
        signal.append(round(raw_values[i] + noise_val, 2))
    return signal

# Extract contiguous segments above threshold
def extract_segments(data, thresh):
    segments = []
    current_seg = []
    for val in data:
        if val > thresh:
            current_seg.append(val)
        else:
            if len(current_seg) > 0:
                segments.append(current_seg)
                current_seg = []
    if len(current_seg) > 0:
        segments.append(current_seg)
    return segments

# Misleading auxiliary function (not used in final computation)
def calculate_entropy(data):
    from math import log
    freq = {}
    total = len(data)
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Process segments to compute score based on length and average
def process_segments(segments, limits):
    valid_count = 0
    total_avg = 0.0
    size_bonus = 0
    # Irrelevant tracking variables
    max_segment_length = 0
    total_elements = 0
    
    for seg in segments:
        seg_len = len(seg)
        max_segment_length = max(max_segment_length, seg_len)
        total_elements += seg_len
        avg = sum(seg) / seg_len
        
        # Core logic: count segments within dynamic threshold bounds
        if limits[0] <= seg_len <= limits[1] and avg > 4.0:
            valid_count += 1
            total_avg += avg
        
        # Distractor: bonus not actually used
        if seg_len >= 5:
            size_bonus += 10
    
    # Final score calculation (only valid_count and total_avg matter)
    final_score = int(valid_count * 100 + (total_avg * 10))
    
    # Dead code path: never executed due to logic
    if max_segment_length == 0:
        final_score = -1
        
    return final_score

# Main execution
if __name__ == '__main__':
    # Generate base signal
    sensor_data = generate_signal()
    
    # Apply slicing to focus on middle portion (simulate windowing)
    windowed_data = sensor_data[5:18]
    
    # Extract segments above threshold 3.0
    segment_data = extract_segments(windowed_data, 3.0)
    
    # Thresholds for valid segment length
    thresholds = (2, 6)
    
    # Unused entropy metric (distraction)
    flat_data = list(itertools.chain.from_iterable(segment_data)) if segment_data else []
    entropy_metric = calculate_entropy(flat_data) if flat_data else 0.0
    
    # Key statement
    final_score = process_segments(segment_data, thresholds)
    
    # Print result
    print(f"Result: {final_score}")