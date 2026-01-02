import itertools

# Simulated sensor frame data with noise and metadata
def generate_frames():
    base_signal = [i * i for i in range(15) if i % 3 != 0]
    noise_profile = [(i % 7) - 3 for i in range(15)]
    frames = []
    for i in range(15):
        frame = {
            'id': i,
            'raw': base_signal[i] + noise_profile[i],
            'timestamp': i * 100 + 50,
            'checksum': (i * 11) % 17,
            'flagged': False
        }
        if i % 4 == 0:
            frame['redundant_copy'] = frame.copy()  # Red herring: nested copy
        frames.append(frame)
    return frames

# Irrelevant helper - looks important but unused in critical path
def validate_checksum(frame_list):
    total = 0
    for f in frame_list:
        total += f['checksum'] * f['id']
    return total % 19 == 0

# Distractor function: appears useful but not part of main logic
def apply_filter(data, mode='lowpass'):
    if mode == 'lowpass':
        return [x * 0.9 for x in data]
    else:
        return [x * 1.1 for x in data]

# Unused transformation path - dead code branch
def legacy_transform(seq):
    acc = 1
    result = []
    for x in seq:
        acc *= (x % 5 + 1)
        result.append(acc % 100)
    return result

# Core processing: extracts and cleans signal
def extract_signal(frames):
    raw_values = [f['raw'] for f in frames]
    adjusted = [v + 2 for v in raw_values]  # Compensate for calibration offset
    return adjusted

# Secondary processing with list comprehension and filtering
def clean_noise(signal_seq):
    threshold = sum(signal_seq) / len(signal_seq) * 0.6
    filtered = [x for x in signal_seq if x > threshold]
    padding = [0] * (len(signal_seq) - len(filtered))
    return filtered + padding  # Preserves length, adds zeros at end

# Data aggregation with distractors
def aggregate_chunks(data):
    chunk_size = 4
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    aggregated = []
    for chunk in chunks:
        if len(chunk) == chunk_size:
            val = sum(x * (i+1) for i, x in enumerate(chunk))  # Weighted sum
        else:
            val = sum(chunk) * 10  # Different rule for incomplete
        aggregated.append(val)
    
    # Decoy operation: modifies copy only
    temp_agg = [x - 5 for x in aggregated]
    temp_agg.reverse()
    
    return aggregated

# Main analysis with bit manipulation red herring
def analyze_signal(data):
    # Real computation
    base_score = sum(data) // len(data)
    
    # Irrelevant bitwise decoy chain
    magic_offset = 0
    temp = base_score
    for _ in range(3):
        temp = (temp ^ 21) + 7
        temp = (temp & 127) | 15
        magic_offset += temp % 50
    
    # Another distraction: unused product chain
    product_chain = 1
    for x in data[::3]:
        product_chain *= (x % 10 + 1)
        if product_chain > 1000:
            product_chain //= 5
    
    # Actual answer contribution: linear search for first over threshold
    threshold = 85
    first_high_idx = -1
    for i, x in enumerate(data):
        if x > threshold:
            first_high_idx = i
            break
    
    # Final computation combines real elements
    stability_factor = len([x for x in data if x > 50])
    final_value = base_score + first_high_idx * 10 + (stability_factor // 3)
    
    # Critical assignment - this is the target
    final_diagnostic = final_value
    
    # More distractions below
    diagnostics_log = []
    for i in range(3):
        dummy = (final_diagnostic * i) % 97
        diagnostics_log.append(f'entry_{dummy}')
    
    return final_diagnostic

# Orchestration with misleading structure
def main_pipeline():
    frames = generate_frames()
    
    # Looks important but stored in unused var
    checksum_status = validate_checksum(frames)
    
    raw_sequence = extract_signal(frames)
    cleaned = clean_noise(raw_sequence)
    processed_frames = aggregate_chunks(cleaned)
    
    # Dead branch - never executed but looks like error handling
    if len(processed_frames) > 100:
        fallback = legacy_transform([len(frames)])
        return sum(fallback)
    
    # Key execution point
    final_diagnostic = analyze_signal(processed_frames)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Execute
main_pipeline()