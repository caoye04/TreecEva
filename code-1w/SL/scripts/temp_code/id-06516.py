import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [127, 255, 192, 64, 224, 32, 160, 96]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

# Irrelevant utility - distractor function (dead path)
def compress_data(data):
    if len(data) == 0:
        return []
    compressed = []
    for i in range(0, len(data), 2):
        pair_sum = sum(data[i:i+2])
        compressed.append(pair_sum // 2)
    return compressed  # Never used

# Signal transformation with red herring operations
def filter_noise(signal):
    filtered = []
    noise_floor = 45.0
    suppression_factor = 0.1
    temp_accumulator = 0  # Misleading variable
    
    for val in signal:
        if val > noise_floor:
            val = val * (1 - suppression_factor)
        else:
            val = val * suppression_factor  # Distraction: not actually needed
        
        # Bit manipulation decoy
        int_val = int(val)
        flipped = int_val ^ 255  # Bitwise XOR with no real impact
        temp_accumulator += flipped % 10  # Accumulates noise digits
        
        filtered.append(round(val, 3))
    
    # Dummy checksum that isn't used
    dummy_checksum = sum(int(x) for x in filtered) % 1000
    return filtered

# Data windowing - relevant but with extra logic
def segment_window(data, size=4):
    windows = []
    for i in range(0, len(data) - size + 1, size//2):
        window = data[i:i+size]
        avg = sum(window) / len(window)
        variance = sum((x - avg)**2 for x in window) / len(window)
        coherence = math.exp(-variance / 100.0)  # Scientific-sounding but unused
        windows.append({'data': window, 'avg': avg})
    
    # Unused metadata generation
    metadata_log = [{'index': i, 'length': len(w['data'])} for i, w in enumerate(windows)]
    return [w['avg'] for w in windows]  # Only averages matter

# String-based identifier processing - adds distraction using string methods
def generate_id(base_num):
    hex_str = hex(base_num)[2:].upper()
    padded = hex_str.rjust(6, '0')
    formatted = f"SIG-{padded[:3]}-{padded[3:]}"
    reversed_id = formatted[::-1]  # Looks important
    checksum_char = chr((sum(ord(c)) for c in formatted) % 26 + 65)  # More misdirection
    return formatted  # Value not used anywhere

# Core analysis with key computation buried in distractions
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 5)

# Main processing chain with decoys
def analyze_signal(data_chunk):
    # Multiple assignment red herring
    a, b, c = 10, 20, 30
    temp_x = a * b + c  # Unused arithmetic
    
    # Distractor: string manipulation with no effect
    id_tag = generate_id(42)
    id_parts = id_tag.split('-')
    if 'SIG' in id_parts:
        id_parts[1] = id_parts[1].lower()
    
    # Actual work hidden among noise
    clean_data = [x for x in data_chunk if x > 50.0]
    baseline = sum(clean_data) / len(clean_data)
    
    # Decoy list comprehension
    _ = [math.sin(x) for x in clean_data if x % 10 == 0]
    
    # Critical calculation: counting oscillations above threshold
    threshold = baseline * 0.9
    crossings = 0
    for i in range(1, len(clean_data)):
        if clean_data[i-1] < threshold < clean_data[i]:
            crossings += 1
    
    # Fake transformation chain
    fake_weights = [0.1, 0.2, 0.3]
    fake_result = sum(w * crossings for w in fake_weights)  # Looks like weighting
    
    # Final diagnostic based on entropy and crossings
    entropy_score = compute_entropy(clean_data)
    final_diagnostic = int((entropy_score * 1000) + crossings)  # Key result
    
    # Dead code paths below
    if False:
        debug_dump = {'raw': data_chunk, 'clean': clean_data}
        log_entry = str(debug_dump)
    
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    # Step 1: Collect raw readings
    raw_data = collect_readings()
    
    # Step 2: Apply filtering (relevant)
    processed_data = filter_noise(raw_data)
    
    # Step 3: Window segmentation (relevant)
    window_averages = segment_window(processed_data)
    
    # Step 4: Analyze signal - this is where final_diagnostic is computed
    final_diagnostic = analyze_signal(processed_data)
    
    # Print required output
    print(f"Result: {final_diagnostic}")