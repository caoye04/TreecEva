def preprocess_signal(data):
    return [x ^ 255 for x in data if x % 3 != 0]

system_log = {
    'errors': [101, 205, 304, 404],
    'warnings': [100, 102],
    'timestamp': 1735689240,
    'active': True
}

# Irrelevant signal transformation chain (red herring)
def transform_sequence(seq):
    if len(seq) > 3:
        seq = seq[::-1]
    return [s << 2 for s in seq]

def evaluate_health(signal):
    base_score = sum(signal) // len(signal)
    penalty = 0
    if base_score > 200:
        penalty += 50
    return base_score - penalty

# Unused recursive function (dead code path)
def recursive_compress(data, depth=0):
    if depth >= 3 or len(data) == 1:
        return data
    return recursive_compress([data[i] + data[i+1] for i in range(0, len(data)-1, 2)], depth + 1)

# Core diagnostic logic (obscured by noise)
def decode_pattern(seq):
    filtered = [x for x in seq if x & 1 == 1]  # Keep only odd values
    if not filtered:
        return 0
    return sum(filtered) >> 1

def analyze_system_state(buffer, log):
    temp_state = []
    for byte in buffer:
        if byte in log['errors']:
            temp_state.append(byte * 2)
        elif byte > 200:
            temp_state.append(byte + 50)
        else:
            temp_state.append(byte)
    
    # Apply slicing and dictionary lookup distraction
    segment = temp_state[1:6:2]
    adjustment = len(log['warnings']) * 15
    
    # Actual critical computation path
    raw_diagnostic = decode_pattern(temp_state)
    secondary_score = evaluate_health(segment)
    
    # Misleading combination with irrelevant components
    decoy_value = sum(transform_sequence([1, 2, 3])) // 3
    final_diagnostic = raw_diagnostic - adjustment + (secondary_score % 25)
    
    # This print is required but uses correct variable
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Initialization with mixed relevance
quantum_buffer = [101, 202, 195, 304, 210, 88, 111]

# Spurious data structures to increase interference
network_queue = [{'id': 501, 'type': 'retry'}, {'id': 502, 'type': 'timeout'}]
temp_cache = set()
for item in network_queue:
    temp_cache.add(item['id'] * 2)

# Additional red herring: unused bit manipulation
flag_mask = 0b11001010
calibration_key = flag_mask ^ 0xFF

# Trigger main analysis
final_diagnostic = analyze_system_state(quantum_buffer, system_log)