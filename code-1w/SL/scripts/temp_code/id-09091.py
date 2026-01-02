import itertools

# Simulated sensor data processing with embedded logic chain
def collect_samples(raw_data, threshold=5.0):
    filtered = [x for x in raw_data if abs(x) > threshold]
    return filtered[::2]  # Return every second sample above threshold

def enhance_resolution(data, factor=2):
    expanded = []
    for a, b in zip(data, data[1:]):
        expanded.append(a)
        expanded.append((a + b) / factor)
    expanded.append(data[-1])
    return expanded

def compress_frame(frame, method='xor'):
    if method == 'xor':
        result = 0
        for val in frame:
            result ^= int(abs(val)) % 256
        return result
    elif method == 'sum':
        return sum(int(x) for x in frame) % 1000  # Irrelevant alternate path
    return -1

def validate_sequence(seq):
    if len(seq) < 3:
        return False
    for i in range(2, len(seq)):
        if seq[i] < seq[i-1] and seq[i-1] >= seq[i-2]:
            return True
    return False

def generate_reference_map(depth):
    # Distractor function - generates unused pattern map
    return {i: (i ** 2) % 7 for i in range(depth)}

def accumulate_diagnostics(signals):
    records = []
    for s in signals:
        temp = 0
        for digit in str(int(abs(s) * 1000)):
            temp = temp * 2 + (int(digit) % 2)
        records.append(temp)
    return records

def analyze_signal(frames):
    baseline = frames[0] if frames else 0
    adjustments = []
    for f in frames[1:]:
        delta = f - baseline
        if delta != 0:
            # Bit manipulation embedded in logic
            adjusted = (abs(delta) ^ 42) & 255
            if delta < 0:
                adjusted = -adjusted
            adjustments.append(adjusted)
    aggregate = sum(adjustments) if adjustments else 0
    return abs(aggregate) + 100  # Final transformation

def main():
    # Initial raw input
    signal_stream = [-2.3, 8.7, -6.1, 4.2, 9.6, -8.3, 7.4, 3.9, -5.8]
    
    # Step 1: Filtering relevant samples
    critical_samples = collect_samples(signal_stream, threshold=5.0)
    
    # Step 2: Enhance resolution for detailed analysis
    high_res_signal = enhance_resolution(critical_samples, factor=2)
    
    # Step 3: Frame compression using XOR method
    processed_frames = []
    window_size = 3
    for i in range(0, len(high_res_signal) - window_size + 1, window_size):
        window = high_res_signal[i:i+window_size]
        compressed_val = compress_frame(window, method='xor')
        processed_frames.append(compressed_val)
    
    # Distractor: Unused validation check
    sequence_valid = validate_sequence([len(str(f)) for f in high_res_signal])
    
    # Distractor: Generate reference map (never used)
    ref_map = generate_reference_map(len(high_res_signal))
    
    # Distractor: Accumulate diagnostics but don't use directly
    diagnostics_log = accumulate_diagnostics(high_res_signal)
    temp_summary = list(map(lambda x: x % 89, diagnostics_log))  # Red herring
    
    # Real computation continues independently
    secondary_enhancement = [x * 1.5 for x in processed_frames if x % 2 == 0]
    refined_set = enhance_resolution(secondary_enhancement, factor=3)[:4]
    
    # Key intervention point
    final_diagnostic = analyze_signal(processed_frames)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

if __name__ == "__main__":
    main()