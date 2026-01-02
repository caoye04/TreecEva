import math

# Simulated network packet analyzer with decoy transformations
def decode_header(raw_header):
    # Irrelevant base64-like transformation (dead end)
    decoded = ''.join([chr((ord(c) % 16) + 97) for c in raw_header])
    checksum = sum([ord(c) for c in decoded]) % 256
    return checksum * 2  # Misleading value, not used later

def validate_frame(frame):
    # Unused validation logic (distractor)
    if len(frame) < 10:
        return False
    parity = 0
    for b in frame:
        parity ^= b
    return parity == frame[0]

def transform_sequence(seq):
    # Complex-looking but irrelevant sequence generator
    result = []
    for i, x in enumerate(seq):
        temp = (x ^ i) % 17
        if temp > 8:
            result.append(temp // 3)
    return result[::-1]  # Never actually used

def compute_entropy(signal):
    # Scientific-sounding but unused function
    total = sum(signal)
    probs = [s / total for s in signal if s > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 3)

def extract_fields(packet_str):
    # Real work starts here: parse meaningful data
    segments = packet_str.split('|')
    metadata = {}
    
    # Extract key-value pairs from first segment
    kv_pairs = segments[0].split(',')
    for pair in kv_pairs:
        k, v = pair.split(':')
        metadata[k] = int(v)
    
    # Second segment contains hex-encoded payload
    payload_hex = segments[1]
    payload_bytes = [int(payload_hex[i:i+2], 16) for i in range(0, len(payload_hex), 2)]
    
    # Third segment has control flags (partially relevant)
    flags = segments[2].split('.')
    mode_flag = int(flags[0])
    shift_param = int(flags[1]) if len(flags) > 1 else 3
    
    # Decoy operation on flags
    decoy_state = [(int(f) ** 2) % 19 for f in flags if f.isdigit()]
    decoy_state = sorted(decoy_state, reverse=True)[::2]
    
    return metadata, payload_bytes, mode_flag, shift_param

def apply_filter(buffer, strength=0.75):
    # Signal processing red herring
    filtered = []
    acc = 0
    for val in buffer:
        acc = acc * strength + val * (1 - strength)
        filtered.append(int(acc))
    return filtered[:len(buffer)//2]  # Truncated, never used

def generate_checksum(data):
    # Another decoy checksum
    chk = 0
    for i, d in enumerate(data):
        chk += d * (i + 1)
    return chk % 97

def process_payload(packet):
    # --- REAL LOGIC PATH ---
    meta, payload, mode, shift = extract_fields(packet)
    
    # Irrelevant preprocessing distractions
    padded_payload = [0] * 4 + payload + [0] * 4
    smoothed = [abs(padded_payload[i] - padded_payload[i-1]) for i in range(1, len(padded_payload))]
    filtered_outliers = [x for x in smoothed if x < 100]
    
    # Core calculation buried in noise
    base_value = meta['val']  # From metadata
    multiplier = meta['cfg'] + mode  # cfg from metadata, mode from flag
    
    # Key transformation: modular arithmetic on specific byte
    target_byte = payload[5]  # Critical index
    shifted = (target_byte << shift) & 0xFF  # Bit shift and mask
    
    # Combine with arithmetic expression
    intermediate = (base_value * multiplier) + shifted
    
    # Apply trigonometric weighting (actual use)
    angle = math.radians(intermediate % 90)
    weighted = intermediate * math.cos(angle)
    
    # String-based switch via dictionary mapping (relevant)
    type_key = 'T' + str(meta['typ'])
    type_map = {'T1': 1.5, 'T2': 2.0, 'T3': 0.8, 'T4': 1.1}
    scaling_factor = type_map.get(type_key, 1.0)
    
    scaled = weighted * scaling_factor
    
    # Final adjustment using slicing logic
    hex_repr = ''.join([f'{b:02x}' for b in payload])
    slice_sum = sum(int(hex_repr[i:i+2], 16) for i in range(0, len(hex_repr), 4))  # Every other byte pair
    
    final_output = int(scaled - (slice_sum % 19))  # Deterministic integer result
    
    # Dead code path below (never reached)
    if final_output < 0:
        recovery_log = {"error": "negative_output", "source": "phase3"}
        recovery_log["retry"] = transform_sequence([final_output])
    
    return final_output

# Simulated input data
data_packet = "val:17,cfg:12,typ:2|a32f1c8b4e|1.5"

# Trigger execution
final_output = process_payload(data_packet)
print(f"Result: {final_output}")