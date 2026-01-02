import math

# Irrelevant helper function (dead code path)
def calculate_entropy(data):
    return -sum(p * math.log2(p) for p in data if p > 0)

# Another decoy function with misleading intermediate results
def validate_checksum(buffer):
    checksum = 0
    for b in buffer:
        checksum ^= b * 31
    return checksum == 0xDEADBEEF

# Core transformation logic
def transform_signal(samples, gain=1.5, offset=0.25):
    amplified = [s * gain + offset for s in samples]
    filtered = [x for x in amplified if abs(x) > 0.5]
    normalized = [val / max(filtered) for val in filtered] if filtered else [0]
    return [round(n, 6) for n in normalized]

# Data processing with conditional logic and string-based routing
def route_packet(payload, mode='fast'):
    header = ''.join(chr(int(b)) for b in payload[:4])
    is_compressed = header.lower().startswith('cmp')
    priority = 1 if 'URG' in header else 0
    
    # Irrelevant string manipulation distractions
    metadata_tags = ['ENC:RSA', 'ZIP:LZ77', 'TTL:128']
    flags = {tag.split(':')[0]: tag.split(':')[1] for tag in metadata_tags}
    
    if mode == 'fast' and not is_compressed:
        return [int.from_bytes(str.encode(flags['ENC']), 'big')] + payload[4:]
    else:
        return payload

# Main chunk processor with bitwise operations and combinatorics
def compute_combinations(n, r):
    if r > n or r < 0:
        return 0
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result

def apply_mask(sequence, mask_bits):
    # Bitwise manipulation with red herring parameters
    active_bits = bin(mask_bits).count('1')
    shift_amount = mask_bits % 7
    masked = []
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            masked.append(val & (mask_bits | 0x0F))
        else:
            masked.append(val ^ ((mask_bits >> shift_amount) & 0xFF))
    return masked

def process_chunk(data_chunk, settings):
    # Distractor variables
    temp_buffer = [0] * 16
    debug_trace = []
    accumulator = 0
    
    # Real logic begins: extract configuration
    scale_factor = settings.get('scale', 1.0)
    enable_filter = settings.get('filter', True)
    mode_flag = settings.get('mode', 'A')
    
    # Conditional expression chain
    threshold = 0.3 if mode_flag == 'A' else (0.6 if mode_flag == 'B' else 0.9)
    exponent = 2 if enable_filter else 3
    
    # Apply non-linear transformation
    processed = [math.pow(abs(x * scale_factor), exponent) for x in data_chunk]
    
    # Filter based on dynamic threshold
    if enable_filter:
        processed = [p for p in processed if p > threshold]
    
    # Simulate data windowing
    window_size = len(processed) // 2
    window = processed[:window_size] if window_size > 0 else processed
    
    # Combinatorics distraction
    combo_score = compute_combinations(len(processed) + 3, 4)
    entropy_proxy = math.log(len(processed) + 1) if processed else 0
    
    # Final aggregation with misleading intermediates
    raw_sum = sum(window) * math.sqrt(scale_factor)
    adjustment = math.sin(math.pi * len(window) / 10)
    final_value = raw_sum + adjustment - entropy_proxy
    
    # Dead assignment - irrelevant to output
    temp_buffer[0] = int(entropy_proxy * 100)
    
    # Actual return
    return round(final_value, 6)

# Setup realistic data pipeline
if __name__ == '__main__':
    # Initial signal data
    raw_samples = [-0.8, -0.5, 0.1, 0.4, 0.7, 1.2, 0.9, -0.3]
    
    # Irrelevant packet data
    dummy_packet = [67, 77, 80, 0, 1, 2, 3, 4, 5]
    routed_data = route_packet(dummy_packet, mode='slow')
    
    # Transform main data
    transformed_data = transform_signal(raw_samples, gain=1.8, offset=-0.1)
    
    # Configuration with meaningful and distracting keys
    config = {
        'scale': 2.5,
        'filter': True,
        'mode': 'A',
        'debug_level': 9,
        'buffer_limit': 1024,
        'retries': 3,
        'timeout_ms': 500
    }
    
    # Critical execution point
    final_output = process_chunk(transformed_data, config)
    
    # Print result as required
    print(f"Target result: {final_output}")