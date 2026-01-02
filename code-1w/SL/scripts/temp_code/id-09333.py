import math

def analyze_noise_floor(received_signal, threshold=0.05):
    """Irrelevant function: Analyzes signal noise (dead code path)."""
    if not received_signal:
        return 0
    avg_power = sum(x ** 2 for x in received_signal) / len(received_signal)
    return avg_power > threshold

def validate_checksum(frame):
    """Irrelevant function: Validates data frame checksum (distractor)."""
    return sum(frame) % 256 == 0

def dummy_encryption(data, key=17):
    """Misleading transformation: Simulates encryption but unused in logic."""
    return [(x + key) % 256 for x in data]

def decode_modulation(signal, modulation='QAM'):
    """Distractor function: Simulates decoding but result not used."""
    if modulation == 'QAM':
        return [math.sqrt(abs(x)) * 2 for x in signal]
    else:
        return [abs(x) for x in signal]

def calculate_entropy(data):
    """Red herring: Computes character entropy from string representation."""
    s = ''.join(map(str, data))
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return -sum((count / len(s)) * math.log2(count / len(s)) for count in freq.values())

def optimize_transmission(buffer, ratio):
    """Core function: Correctly computes optimized bandwidth."""
    # Step 1: Filter valid amplitudes above threshold
    filtered = [x for x in buffer if x > 0.1]
    
    # Step 2: Apply logarithmic scaling to dynamic range
    scaled = [math.log(y) for y in filtered]
    
    # Step 3: Accumulate and compute base throughput
    total = sum(scaled)
    
    # Step 4: Use string representation of ratio to extract digits
    ratio_str = str(ratio).replace('.', '')
    digit_sum = sum(int(d) for d in ratio_str if d.isdigit())
    
    # Step 5: Count occurrences of '3' in ratio string (irrelevant but looks meaningful)
    decoy_count = ratio_str.count('3')
    
    # Step 6: Compute adjustment factor using tuple unpacking
    factors = (digit_sum, len(filtered), decoy_count + 1)
    a, b, c = factors
    adjustment = (a * b) / max(c, 1)
    
    # Step 7: Apply adjustment only if entropy threshold met (but entropy not actually used)
    temp_string = f"{total:.2f}_{ratio}".upper()
    char_count = len(temp_string.replace('X', ''))  # Irrelevant cleanup
    
    # Step 8: Final bandwidth calculation — depends only on total and adjustment
    base = total * 100
    final = base + adjustment
    
    # Misleading debug prints (no effect)
    debug_info = {
        'entries': len(buffer),
        'filtered_count': b,
        'noise_flag': False,
        'checksum_valid': True
    }
    return int(final)

# Main execution with mixed data types and distractors
raw_data = [0.01, 0.45, 0.92, 0.03, 1.33, 0.71, 2.01, 0.07, 1.15]
signal_buffer = [x * 1.8 for x in raw_data]
compression_ratio = 3.7

# Decoy operations: create multiple irrelevant variables
modulated = decode_modulation(signal_buffer, 'QAM')
encrypted_frame = dummy_encryption([int(x * 10) for x in signal_buffer])
noise_level = analyze_noise_floor(raw_data)
frame_checksum = validate_checksum(encrypted_frame)
entropy_metric = calculate_entropy(signal_buffer)

# Key statement: this is where the answer is determined
final_bandwidth = optimize_transmission(signal_buffer, compression_ratio)

# Print target result
print(f"Result: {final_bandwidth}")