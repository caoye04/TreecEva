from collections import defaultdict, Counter
import math

def generate_frequency_map(pattern):
    # Irrelevant helper: builds char frequency (not used in final result)
    return Counter(pattern)

def deprecated_filter(sequence):
    # Dead code path: never called
    return [x for x in sequence if x % 3 != 0]

def transform_sequence(raw_seq, key_offset):
    # Applies bit manipulation and arithmetic transformations
    shifted = [(x << 1) + key_offset for x in raw_seq]
    masked = [y ^ 0b1010 for y in shifted]  # XOR mask
    return [z for z in masked if z > 0]  # Remove negatives (none here)

def accumulate_with_damping(values, damping_factor=0.93):
    # Summation with decay – red herring, not used in critical path
    total = 0.0
    for i, v in enumerate(values):
        total += v * (damping_factor ** i)
    return total

def extract_features(data_stream):
    # Extracts statistical features, some irrelevant
    lengths = defaultdict(int)
    for item in data_stream:
        lengths[len(item)] += 1
    
    # Misleading intermediate: looks important but unused
    entropy_proxy = 0
    for count in lengths.values():
        if count > 0:
            entropy_proxy -= count * math.log(count + 1e-8)
    
    # Actual relevant transformation
    flat = ''.join(data_stream).lower()
    digit_chars = [c for c in flat if c.isdigit()]
    digits = list(map(int, digit_chars))
    return digits

def validate_checksum(tokens):
    # Complex validation with unused branches
    if len(tokens) < 5:
        return False
    weighted = sum((i + 1) * t for i, t in enumerate(tokens[:8]))
    checksum = weighted % 256
    return checksum == 127  # Rare condition, not satisfied here

def normalize_readings(readings):
    # Unused normalization function (decoy)
    mean_val = sum(readings) / len(readings)
    return [r - mean_val for r in readings]

def process_signal_packet(packet_list):
    # Main processing with distractions
    temp_results = []
    decoy_state = 0
    
    for pkt in packet_list:
        # Simulate parsing
        if pkt.startswith('DAT'):
            raw_nums = [ord(c) % 25 for c in pkt]  # Generate numbers
            transformed = transform_sequence(raw_nums, key_offset=7)
            temp_results.extend(transformed)
            
            # Distractor: accumulates but unused
            running_max = max(transformed)
            decoy_state ^= running_max
        elif pkt.startswith('META'):
            continue  # Skip metadata
        else:
            # Fallback with no impact
            temp_results.append(hash(pkt) % 100)
    
    # Real use: filter only even-positioned results
    filtered = [temp_results[i] for i in range(0, len(temp_results), 2)]
    return filtered

def analyze_signal(cleaned_signal):
    # Final analysis: computes diagnostic from signal peaks
    if not cleaned_signal:
        return -1
    
    # Identify local maxima (peaks)
    peaks = []
    for i in range(1, len(cleaned_signal) - 1):
        if cleaned_signal[i-1] < cleaned_signal[i] > cleaned_signal[i+1]:
            peaks.append(cleaned_signal[i])
    
    # Add edge values if they are high enough
    if len(cleaned_signal) > 1:
        if cleaned_signal[0] > cleaned_signal[1]:
            peaks.append(cleaned_signal[0])
        if cleaned_signal[-1] > cleaned_signal[-2]:
            peaks.append(cleaned_signal[-1])
    
    # Compute diagnostic as sum of peak XOR patterns
    accumulator = 0
    for p in peaks:
        # Bit manipulation chain
        step1 = (p ^ 0xF0F) & 0xFFFF
        step2 = (step1 >> 2) | (step1 << 14)
        step3 = step2 & 0x7FFF  # Ensure positive
        accumulator += step3
    
    # Final transformation
    diagnostic = int((accumulator * 0.87) + 33)
    return diagnostic

# Entry point with realistic dataset
if __name__ == '__main__':
    # Input data – mixed valid and invalid packets
    signal_packets = [
        'DAT9M2K', 'DAT3X1L', 'META:CFG:7', 'DAT7P4N',
        'DAT5Q8M', 'JUNK99', 'DAT2Z7T', 'DAT8B1W'
    ]
    
    # Step 1: Extract embedded digits (red herring path)
    fake_features = extract_features(signal_packets)
    
    # Step 2: Process actual signal (critical path)
    processed_data = process_signal_packet(signal_packets)
    
    # Step 3: Validate (fails, but condition not met)
    is_valid = validate_checksum(fake_features)
    
    # Step 4: Analyze signal to get final result
    final_diagnostic = analyze_signal(processed_data)
    
    # Print result
    print(f"Result: {final_diagnostic}")