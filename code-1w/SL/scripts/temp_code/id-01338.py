import math

def analyze_sensor(x, y):
    if x < 0:
        return (y ** 2) % 100
    else:
        return (x + y) & 63

# Irrelevant helper function (dead code path)
def deprecated_calibrate(val):
    scale = 3.7
    offset = -2
    return int((val * scale) + offset) if val > 10 else val

# Unused constant (distractor)
MAX_BUFFER_SIZE = 512

# Simulated telemetry packet (with decoy fields)
telemetry_stream = [
    {'id': 1, 'raw': 45, 'flag': True, 'meta': 'A'},
    {'id': 2, 'raw': 23, 'flag': False, 'meta': 'B'},
    {'id': 3, 'raw': 67, 'flag': True, 'meta': 'C'}
]

# Lambda for dynamic threshold (actually used)
dynamic_threshold = lambda base, adj: round(base * 1.05 + adj, 2)

# Misleading transformation chain (partially unused)
transform_chain = [
    lambda x: x << 2,
    lambda x: x ^ 255,
    lambda x: x + (x // 10)
]

# Core data structure
system_state = {
    'status': 'ACTIVE',
    'readings': [18, 24, 42, 15, 9],
    'checksum': 0,
    'version': 'v2.1'
}

# Decoy checksum calculation (never called)
def compute_legacy_checksum(data):
    chk = 0
    for d in data:
        chk = (chk * 31 + d) % 65536
    return chk

# Real processing begins here
def preprocess_readings(raw_list):
    processed = []
    for val in raw_list:
        if val % 3 == 0:
            # Apply bit rotation left by 1
            rotated = ((val << 1) | (val >> 7)) & 255
            processed.append(rotated % 50)
        elif val % 5 == 0:
            processed.append(abs(val - 10))
        else:
            processed.append(val)
    return processed

def evaluate_health(score):
    if score < 20:
        return 'CRITICAL'
    elif score < 40:
        return 'WARNING'
    else:
        return 'NORMAL'

# Complex conditional with red herring variables
counterfeit_mask = 0b11001100
activation_key = 0xABCD

# Actual calibration logic
def process_metrics(data_packet):
    temp_series = []
    for item in data_packet:
        a = item
        b = (a * 2) + 7
        c = analyze_sensor(a, b)
        temp_series.append(c)
    
    # Aggregate through bitwise and arithmetic mixing
    aggregate = 0
    for idx, val in enumerate(temp_series):
        if idx % 2 == 0:
            aggregate += val ^ (idx + 1)
        else:
            aggregate += val & (idx * 3)
    
    # Introduce floating point via dynamic threshold
    reference = 85.0
    adjusted_ref = dynamic_threshold(reference, -5)
    
    # Final computation
    intermediate = (aggregate * 3) + int(adjusted_ref)
    final_score = intermediate // 2
    
    # Dead branch (misleading control flow)
    if final_score > 1000:
        fallback = 0
        for i in range(5):
            fallback += (i * final_score) % 7
        final_score = fallback  # Never executed
    
    # Key result assignment
    final_diagnostic = final_score + len(temp_series)
    
    # More irrelevant state
    debug_trace = [math.sin(x / 10) for x in temp_series if x % 4 == 0]
    
    return final_diagnostic

# Generate input from system readings
calibration_data = preprocess_readings(system_state['readings'])

# Execute main logic
final_diagnostic = process_metrics(calibration_data)

print(f"Result: {final_diagnostic}")