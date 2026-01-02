import math

# Simulated sensor data processing with diagnostic flags
def collect_samples(duration, sample_rate=10):
    samples = []
    for t in range(0, int(duration * sample_rate)):
        time_val = t / sample_rate
        raw_value = math.sin(2 * math.pi * 3 * time_val) + 0.5 * math.cos(2 * math.pi * 7 * time_val)
        samples.append(round(raw_value * 1000) / 1000)
    return samples

# Irrelevant auxiliary function – decoy for noise filtering
def apply_noise_filter(data, threshold=0.1):
    return [x for x in data if abs(x) > threshold]  # Unused in final logic

# Signal conditioning with red herring operations
def precondition_signal(raw_data):
    offset_compensated = [x - 0.1 for x in raw_data]
    amplified = [x * 1.2 for x in offset_compensated]  # Distractor: not used later
    normalized = [max(min(x, 1.0), -1.0) for x in raw_data]
    return normalized

# Frame segmentation with misleading counters
def segment_into_frames(signal, frame_size=8):
    frames = []
    temp_frame = []
    index_counter = 0
    overflow_buffer = []  # Dead variable – never used

    for val in signal:
        temp_frame.append(val)
        index_counter += 1
        if len(temp_frame) == frame_size:
            frames.append(temp_frame)
            temp_frame = []
    
    # Leftover handling (not triggered due to exact size)
    if temp_frame:
        overflow_buffer.append(temp_frame)
    
    # Add dummy padding frames – irrelevant but looks important
    for _ in range(2):
        frames.append([0.0] * frame_size)
    
    return frames

# Core transformation using list comprehension and enumerate
def encode_frames(frames):
    encoded = []
    for i, frame in enumerate(frames):
        if i % 2 == 0:
            transformed = [round(math.tanh(x), 3) for x in frame]
        else:
            transformed = [round(math.copysign(abs(x)**0.5, x), 3) for x in frame]
        parity_flag = sum(1 for x in transformed if x > 0) >= len(transformed) / 2
        encoded.append({'data': transformed, 'seq_id': i, 'positive_dominant': parity_flag})
    return encoded

# Decoy checksum function – looks critical but unused
def compute_checksum(data_list):
    total = 0
    for item in data_list:
        if isinstance(item, dict) and 'data' in item:
            for val in item['data']:
                total ^= int(val * 1000) % 256
    return total

# Analyze only frames with even sequence ID using zip and conditional logic
def analyze_signal(encoded_frames):
    relevant = [f for f in encoded_frames if f['seq_id'] % 2 == 0]
    metrics = []
    
    # Use of enumerate and zip to pair adjacent frame stats (with wrap-around)
    for i, frame in enumerate(relevant):
        flat_data = frame['data']
        positive_count = sum(1 for x in flat_data if x > 0)
        negative_count = sum(1 for x in flat_data if x < 0)
        net_polarity = positive_count - negative_count
        
        # Modular arithmetic on index
        shift = (i * 3) % 7
        shifted_polarity = (net_polarity + shift) % 5
        
        # Integer division and rounding
        avg_magnitude = round(sum(abs(x) for x in flat_data) / len(flat_data), 3)
        
        metrics.append({
            'index': i,
            'polarity_score': net_polarity,
            'shifted': shifted_polarity,
            'magnitude': avg_magnitude
        })
    
    # Final aggregation using complex conditional expression
    base_score = sum(m['shifted'] for m in metrics)
    adjustment = sum(int(m['magnitude'] * 10) for m in metrics if m['polarity_score'] > 0)
    
    # Real answer computation path
    final_diagnostic = base_score * adjustment
    
    # Multiple red herring variables below
    debug_trace = [m['index'] for m in metrics if m['shifted'] > 2]
    validation_key = ''.join(str(int(m['magnitude'] * 100))[-1] for m in metrics)
    auxiliary_flag = len(debug_trace) > 0 and validation_key.startswith('5')
    
    # Unused recursive attempt – dead code path
    def recursive_blend(data, depth=0):
        if depth >= 3 or len(data) <= 1:
            return data[0] if data else 0
        mid = len(data) // 2
        left = recursive_blend(data[:mid], depth + 1)
        right = recursive_blend(data[mid:], depth + 1)
        return (left + right) / 2
    
    return final_diagnostic

# Entry point
if __name__ == '__main__':
    # Generate synthetic input
    raw_sensor_data = collect_samples(duration=1.6, sample_rate=10)  # Exactly 16 samples
    
    # Preprocess signal
    cleaned_signal = precondition_signal(raw_sensor_data)
    
    # Segment into frames (each of size 8 -> yields 2 real frames)
    segmented = segment_into_frames(cleaned_signal, frame_size=8)
    
    # Encode frames with metadata
    processed_frames = encode_frames(segmented)
    
    # Apply actual analysis function
    final_diagnostic = analyze_signal(processed_frames)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")