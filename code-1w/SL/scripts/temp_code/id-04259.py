import math

# Simulated sensor data aggregation and health diagnostic system
data_stream = [142, 89, 205, 76, 133, 91, 188, 65, 104, 121]
offset_key = 37
scaling_factor = 1.85
base_threshold = 100

# Irrelevant calibration constants (distractors)
ref_voltage = 3.3
sample_rate_hz = 44100
bit_depth = 16
frame_size = 1024

# Decoy transformation functions
def decoy_normalize(x):
    return (x - min(data_stream)) / (max(data_stream) - min(data_stream)) if max(data_stream) != min(data_stream) else 0

def decoy_encode(signal):
    return [int(s * 255 / max(signal)) for s in signal]

# Real preprocessing pipeline
def raw_adjust(val):
    return int((val + offset_key) * scaling_factor) % 256

def classify_severity(level):
    if level < 64:
        return 'LOW'
    elif level < 128:
        return 'MODERATE'
    elif level < 192:
        return 'HIGH'
    else:
        return 'CRITICAL'

# Bit manipulation for checksum (relevant)
def compute_checksum(chunk):
    result = 0
    for item in chunk:
        result ^= item  # byte-wise XOR
    return (result + len(chunk)) % 256

# Higher-order function filter (used later)
severity_filter = lambda mode: lambda val: val > (base_threshold + 20) if mode == 'strict' else val > (base_threshold - 10)

# Data transformation stage
temp_buffer = []
for x in data_stream:
    adjusted = raw_adjust(x)
    temp_buffer.append(adjusted)

transformed_data = temp_buffer.copy()

# Dead processing path (unused)
compressed_payload = []
for i in range(0, len(transformed_data), 2):
    if i + 1 < len(transformed_data):
        pair_sum = (transformed_data[i] + transformed_data[i + 1]) // 2
        compressed_payload.append(pair_sum)

# Unused recursive checksum verifier
def verify_chain(data, expected=120):
    if len(data) <= 1:
        return data[0] == expected if data else False
    new_layer = [(data[i] ^ data[i + 1]) for i in range(len(data) - 1)]
    return verify_chain(new_layer, expected)

# Configuration structure
config = {
    'mode': 'strict',
    'version': '2.1a',
    'checksum_req': True,
    'rounding_policy': 'floor',
    'case_format': 'uppercase'
}

# Core metric processor (critical section)
def process_metrics(data, cfg):
    filtered = [x for x in data if severity_filter(cfg['mode'])(x)]
    
    # Nested conditional with mixed arithmetic
    if cfg['checksum_req']:
        chk = compute_checksum(data)
        adjusted_len = len(filtered) + (chk % 10)
    else:
        adjusted_len = len(filtered)
    
    # Multiple mathematical operations including integer division and case logic
    raw_score = 0
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            raw_score += int(math.log(val + 1) ** 2)
        else:
            raw_score += (val // (i + 1))
    
    # Case conversion side effect (irrelevant but plausible)
    mode_case = cfg['mode'].upper() if cfg['case_format'] == 'uppercase' else cfg['mode'].lower()
    
    # Final computation with rounding
    if cfg['rounding_policy'] == 'floor':
        final_value = math.floor((raw_score * 0.75) / adjusted_len) if adjusted_len > 0 else 0
    else:
        final_value = round((raw_score * 0.75) / adjusted_len) if adjusted_len > 0 else 0
    
    return final_value

# Misleading intermediate call (does nothing to final result)
decoy_result = decoy_encode(data_stream)

# Critical execution point
final_diagnostic = process_metrics(transformed_data, config)

# Output the target result
print(f"Target result: {final_diagnostic}")