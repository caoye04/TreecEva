import itertools

def analyze_frequency(data):
    # Irrelevant function: analyzes frequency but not used in main logic
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return {k: v for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)}

def decode_signal(stream):
    # Dead code path — never called
    return [x ^ 255 for x in stream if x % 2 == 0]

def validate_checksum(frame):
    # Misleading validation that looks important but isn't used
    return sum(frame) % 256 == frame[-1]

def shift_window(arr, offset):
    # Unused helper with complex indexing
    return arr[offset:] + arr[:offset]

def process_frame(data, config):
    size = len(data)
    mode = config.get('mode', 'standard')
    mask = config.get('mask', 0xFF)
    threshold = config.get('threshold', 10)
    
    # Distractor variables
    temp_buffer = [0] * size
    history_log = []
    debug_flag = False
    accumulator = 0
    
    for i in range(size):
        temp_buffer[i] = data[i] & mask
        if temp_buffer[i] > threshold:
            accumulator += temp_buffer[i]
    
    # Conditional expression (required feature)
    scaling_factor = 1.5 if mode == 'boost' else 0.8
    
    # Early termination red herring
    if accumulator == 0:
        return -1
    
    # Real computation begins here — non-obvious due to noise
    filtered = [x for x in temp_buffer if x > 0]
    paired = list(itertools.zip_longest(filtered[::2], filtered[1::2], fillvalue=0))  # itertools basics
    
    weighted_sum = 0
    for a, b in paired:
        weighted_sum += (a * 3) + (b * 2)
    
    # Key transformation
    checksum = (weighted_sum ^ 0xAAAA) & 0xFFFF
    
    # More distractions below
    post_processed = [(x ^ checksum) % 251 for x in filtered]
    if len(post_processed) > 5:
        history_log.append(sum(post_processed))
    
    # Final red herring
    if debug_flag and history_log:
        print(f'Debug: {history_log}')
        return None
        
    return checksum

# Main execution with decoy data
if __name__ == '__main__':
    raw_stream = [170, 85, 200, 45, 130, 90, 255, 10, 60]
    buffer = [x << 1 for x in raw_stream]  # Bit manipulation distraction
    buffer = [x & 0xFF for x in buffer]   # Normalize to byte range
    
    # Unused alternate configurations
    alt_configs = [
        {'mode': 'safe', 'mask': 0xF0, 'threshold': 20},
        {'mode': 'turbo', 'mask': 0x0F, 'threshold': 5}
    ]
    
    flags = {
        'mode': 'standard',
        'mask': 0xFF,
        'threshold': 10
    }
    
    # Decoy processing steps
    snapshot = buffer[::3]
    baseline = sum(snapshot) // len(snapshot)
    
    # Critical statement
    checksum = process_frame(buffer, flags)
    
    # Output result as required
    print(f'Result: {checksum}')