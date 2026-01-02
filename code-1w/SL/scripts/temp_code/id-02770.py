import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_value, count):
    return [base_value * (i + 1) % 97 for i in range(count)]

def apply_filter(raw_samples):
    filtered = []
    for x in raw_samples:
        if x % 3 == 0:
            filtered.append(x + 5)
        elif x % 7 == 0:
            filtered.append(x * 2)
        else:
            filtered.append(x)
    return filtered

def compute_entropy(values):
    # Irrelevant entropy calculation (dead-end)
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

def generate_checksum(sequence):
    # Distractor: checksum not used in final result
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= (val + i) & 0xFF
    return chk

def transform_signal(data_stream):
    # Real transformation path
    shifted = [(x >> 1) ^ 17 for x in data_stream]
    reversed_data = shifted[::-1]
    processed = [x for x in reversed_data if x % 4 != 0]  # List comprehension
    return [x + 10 for x in processed[:50]]

def build_lookup(keys):
    # Unused function — red herring
    return {k: math.sqrt(k) for k in keys if k > 10}  # Dictionary operation

def decode_sequence(signal):
    # Misleading decoding logic that isn't part of main flow
    decoded = []
    for s in signal:
        if s > 50:
            decoded.append(s - 23)
    return decoded

def analyze_pattern(dataset, settings):
    temp_state = 0
    threshold = settings['limit']
    factor = settings['scale']
    
    for i in range(len(dataset)):
        if i % settings['stride'] == 0:
            temp_state += dataset[i] * factor
        elif i % 5 == 0:
            temp_state -= settings.get('offset', 3)
        
        # Bitwise manipulation with conditional update
        if temp_state & 1:
            temp_state = (temp_state ^ 15) + 2
        else:
            temp_state = (temp_state >> 1) + 1
    
    # Final adjustment based on length and modulo condition
    if len(dataset) % 7 == 0:
        temp_state *= 2
    return int(abs(temp_state)) % 1000000

# --- Main Execution with Heavy Interference ---
if __name__ == "__main__":
    # Initialization block with multiple variables (many irrelevant)
    base_input = 13
    sample_size = 84
    debug_mode = True
    max_iterations = 12
    timeout_flag = False
    
    # Step 1: Collect raw samples
    raw_sensor_data = collect_samples(base_input, sample_size)
    
    # Step 2: Apply filter (partially relevant)
    cleaned_readings = apply_filter(raw_sensor_data)
    
    # Distractor: Compute unused metrics
    signal_entropy = compute_entropy(cleaned_readings)
    validation_key = generate_checksum(cleaned_readings)
    lookup_table = build_lookup(cleaned_readings)
    tentative_decoding = decode_sequence(cleaned_readings)
    
    # Step 3: Transform signal – critical path begins
    transformed_data = transform_signal(cleaned_readings)
    
    # Configuration dictionary with decoy keys
    config = {
        'limit': 42,
        'scale': 3,
        'stride': 4,
        'offset': 7,
        'debug_path': '/tmp/log',  # unused
        'version': '2.1a'          # unused
    }
    
    # Step 4: Analyze pattern – key statement
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")