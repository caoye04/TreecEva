import math

# Irrelevant helper function (decoy)
def compute_entropy(values):
    return -sum(p * math.log2(p) for p in values if p > 0)

# Unused transformation (dead code path)
def transform_legacy(x):
    return (x << 3) ^ 0xFF

# Core processing components
def validate_checksum(sequence):
    return sum(sequence) % 256 == sequence[-1]

def extract_payload(packet):
    if len(packet) < 5 or not validate_checksum(packet):
        return None
    return packet[1:-1]  # Exclude header and checksum

def decode_signal(signal_bytes):
    decoded = []
    for b in signal_bytes:
        flipped = ((b >> 4) | (b << 4)) & 0xFF  # Bit reversal
        adjusted = (flipped - 37) % 256
        decoded.append(adjusted)
    return decoded

def map_to_physical(reading):
    # Simulate sensor calibration curve
    base = reading * 0.7854
    if base > 127:
        base -= 256
    return round(base * 1.22, 3)

def filter_outliers(stream, threshold=1.5):
    if len(stream) < 3:
        return stream
    median_val = sorted(stream)[len(stream)//2]
    return [v for v in stream if abs(v - median_val) / (median_val + 1e-5) < threshold]

def aggregate_readings(readings):
    total = 0.0
    weight_sum = 0
    weights = [0.8 ** i for i in range(len(readings))]
    for i, val in enumerate(readings):
        total += val * weights[i]
        weight_sum += weights[i]
    return total / weight_sum if weight_sum != 0 else 0.0

def finalize_result(value, mode='standard'):
    # Conditional expression usage
    offset = 42 if mode == 'enhanced' else 0
    normalized = (value + offset) % 1000
    return round(normalized, 4)

def process_pipeline(raw_data):
    # Step 1: Extract valid payload
    payload = extract_payload(raw_data)
    if not payload:
        return -1
    
    # Step 2: Decode bit-reversed signal
    decoded_values = decode_signal(payload)
    
    # Step 3: Map to physical units with calibration
    physical_mapped = [map_to_physical(x) for x in decoded_values]
    
    # Step 4: Filter spurious readings
    cleaned = filter_outliers(physical_mapped)
    
    # Step 5: Aggregate using exponential weighting
    aggregated = aggregate_readings(cleaned)
    
    # Step 6: Final normalization
    result = finalize_result(aggregated, mode='enhanced' if len(cleaned) > 4 else 'standard')
    
    return result

# === Distractor Section: Misleading computations ===

def analyze_frequency_pattern(seq):
    freq_map = {}
    for item in seq:
        freq_map[item] = freq_map.get(item, 0) + 1
    return {k: v for k, v in freq_map.items() if v > 1}

def generate_synthetic_data(seed=123):
    data = [(seed * i + 47) % 251 for i in range(8)]
    checksum = sum(data) % 256
    return [0xAA] + data + [checksum]

def debug_print_structure(obj):
    print(f"[DEBUG] Object type: {type(obj)}")
    if hasattr(obj, '__len__'):
        print(f"[DEBUG] Length: {len(obj)}")

# Unused global constants (red herring)
MAX_BUFFER_SIZE = 1024
PROTOCOL_VERSION = "2.1"
ENCRYPTION_KEY = 0xDEADBEEF
DEFAULT_TIMEOUT = 30.5

# Simulated incoming data stream (real input)
data_stream = [0xAA, 0x1C, 0x3A, 0x5F, 0x1B, 0x2D, 0x4E, 0x0A, 0x93]

# Irrelevant pre-processing (distractor)
sorted_bytes = sorted(data_stream[1:-1])
reversed_pairs = [(sorted_bytes[i], sorted_bytes[-i-1]) for i in range(len(sorted_bytes)//2)]
bit_stats = {i: sum((b >> i) & 1 for b in data_stream) for i in range(8)}

# Real processing path
debug_print_structure(data_stream)  # Side effect only
interim_check = analyze_frequency_pattern(data_stream)

# Critical execution point
final_output = process_pipeline(data_stream)

# Output result as required
print(f"Result: {final_output}")