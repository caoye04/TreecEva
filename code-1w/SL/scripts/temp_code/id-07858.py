import math

# Irrelevant helper function (decoy)
def validate_checksum(data):
    return sum(data) % 256 == 0

# Misleading transformation chain
def transform_signal(x):
    if x < 0:
        return abs(x) ** 0.5
    return (x * 1.5) % 7

# Unused but plausible data pipeline stage
def filter_anomalies(seq):
    threshold = 3.5
    return [s for s in seq if abs(s - 4.2) < threshold]

# Core processing logic hidden among distractors
def encode_frame(payload):
    temp = 0
    for item in payload[:4]:
        temp += (item ^ 5) * 2
    return temp // 3

# Decoy constant table (red herring)
CALIBRATION_TABLE = {
    'A': 100, 'B': 205, 'C': 312,
    'X': 999, 'Y': 888, 'Z': 777  # Distracting high values
}

# Real but obfuscated computation path
def decode_sequence(seq):
    a, b, c = seq[0], seq[2], seq[4]
    intermediate = (a + c) * b
    # Conditional expression with string method distraction
    mode_flag = 'shift' if str(intermediate).endswith('5') else 'normal'
    adjustment = 7 if mode_flag == 'shift' else 3
    return intermediate - adjustment

# Higher-order function red herring
data_mapper = lambda f, x: [f(val) for val in x]

# Main processing function buried in complexity
def process_data(buffer):
    # Extract relevant segment
    segment = [buffer[i] for i in (0, 3, 5, 6, 8, 9)]
    
    # Dead code path - never taken due to fixed input
    if len(buffer) > 20:
        return sum(buffer) // 10
    
    # Actual critical computation
    x = decode_sequence(segment)
    y = encode_frame(buffer[1:7])
    
    # Bit manipulation decoy (irrelevant)
    masked_value = buffer[0] & 15 | 48
    
    # String-based distraction using conditional expression
    status_tag = "DEBUG".lower() if x > y else "ERROR".upper()
    
    # Real answer derivation
    raw_result = x * 2 - y
    final_output = int(math.floor(raw_result + 1.5))
    
    # Never-used debugging print
    # print(f'Debug: {masked_value=}, {status_tag=}')
    
    return final_output

# Simulated sensor data stream (real input)
stream_buffer = [7, 2, 1, 8, 4, 3, 6, 1, 5, 9]

# Spurious independent calculations (distractors)
baseline_offset = sum([i**2 for i in range(5)])  # 30
reference_key = ''.join([chr(97 + i) for i in range(3)])  # 'abc'
echo_pulse = (stream_buffer[1] + stream_buffer[8]) << 2  # (2+5)<<2 = 28

# Key execution point
final_output = process_data(stream_buffer)

# Target result output
print(f"Target result: {final_output}")