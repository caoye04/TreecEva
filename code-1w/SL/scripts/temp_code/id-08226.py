from collections import defaultdict, Counter

# Simulated network packet analysis with red herrings
def analyze_packet_flow(packets):
    flow_stats = defaultdict(int)
    temporal_gaps = []
    for pkt in packets:
        flow_stats[pkt['src']] += 1
        if 'timestamp' in pkt:
            temporal_gaps.append(1)  # dummy placeholder
    return flow_stats

# Irrelevant helper: computes byte entropy (not used in final result)
def compute_entropy(data):
    freq = Counter(data)
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # fake simplified entropy
    return round(entropy, 6)

# Misleading transformation chain
def transform_sequence(seq):
    temp = [x ** 2 for x in seq if x % 2 == 0]
    shifted = [x >> 1 for x in temp]
    filtered = [x for x in shifted if x > 10]
    return filtered if len(filtered) > 5 else [sum(shifted)]

# Core logic disguised among distractors
def extract_signatures(payloads):
    sig_map = {}
    for i, p in enumerate(payloads):
        key = ''.join([chr(b % 97 + 33) for b in p[:3]]) if p else ''
        sig_map[key] = i % 7
    return sig_map

# Decoy function: looks important but unused
def validate_checksum(chunk):
    return sum(chunk) % 256 == 0

# Real processing function with nested logic
def process_segments(data, config):
    # Step 1: Preprocess using slicing and filtering
    raw_segments = data[::config.get('stride', 2)]
    cleaned = [x for x in raw_segments if x > 0]
    
    # Step 2: Build frequency map with defaultdict
    count_map = defaultdict(int)
    for val in cleaned:
        bucket = val // config.get('bucket_size', 10)
        count_map[bucket] += 1
    
    # Step 3: Apply conditional transformations
    intermediate = 0
    for k, v in count_map.items():
        if k % 2 == 0 and v >= 2:
            intermediate += k * v
        elif k > 5:
            intermediate -= v

    # Step 4: Use string manipulation as control trigger
    mode_flag = config.get('mode', '')[::-1].lower()
    if 'xyz' in mode_flag:
        intermediate *= 2
    
    # Step 5: Simulate segment reassembly
    reassembled = []
    for i in range(len(cleaned)):
        if i % 3 == 0:
            reassembled.append(cleaned[i] + intermediate % 10)
    
    # Step 6: Aggregate final signal
    signal_strength = sum(reassembled) % 10000
    
    # Step 7: Apply bitmask from config (bit manipulation red herring)
    mask = config.get('mask', 0xFF)
    masked_signal = signal_strength & mask
    
    # Step 8: Final adjustment based on dictionary size
    signature_dict = extract_signatures(data)
    final_offset = len(signature_dict) * config.get('scale', 1)
    
    # Critical assignment
    final_output = masked_signal + final_offset
    
    # Dead code path (never reached due to prior logic)
    if False and len(temporal_gaps) > 10:
        backup = compute_entropy(flattened_data)
        return int(backup * 1000)
        
    return final_output

# Generate input data deterministically
base_data = [i * 3 + 2 for i in range(50)]
flattened_data = [x ^ 0x5A for x in base_data]  # unused distraction

# Configuration with misleading keys
config_params = {
    'stride': 3,
    'bucket_size': 7,
    'mode': 'zyX_tun1ng',
    'mask': 0x3FF,  # 10-bit mask
    'scale': 4,
    'debug': True,
    'timeout': 1500,
    'retries': 3
}

# Simulated packet stream (unused but plausible)
network_packets = [
    {'src': '192.168.1.10', 'size': 150, 'timestamp': t} for t in range(0, 1000, 100)
]
packet_analysis = analyze_packet_flow(network_packets)

# Key execution point
final_output = process_segments(flattened_data, config_params)
print(f"Target result: {final_output}")