import itertools

# Simulated sensor data processing with diagnostic flags
def parse_sensor_sequence(raw_stream, threshold):
    parsed = []
    for val in raw_stream:
        if val > threshold:
            parsed.append(int(bin(val ^ 0b1010)[2:], 2) + 1)
        else:
            parsed.append(val // 2)
    return parsed

# Legacy checksum (unused but looks important)
def compute_legacy_checksum(data):
    checksum = 0
    for i, x in enumerate(data):
        checksum += x * (i + 1) % 7
    return checksum % 15

# Main transformation pipeline
def transform_signal(signal_chunk, mode):
    if mode == 'A':
        return [x * 3 + 2 for x in signal_chunk]
    elif mode == 'B':
        return [x * 2 - 1 for x in signal_chunk]
    else:
        return [x for x in signal_chunk]

# Complex filtering with red herring logic
def filter_anomalies(dataset, window_size=3):
    filtered = []
    decoy_sum = 0
    temp_flag = False
    
    for i in range(len(dataset)):
        segment = dataset[max(0, i - window_size + 1):i + 1]
        avg = sum(segment) / len(segment)
        if abs(dataset[i] - avg) > 2:
            temp_flag = True
        decoy_sum += avg * 0.1  # Irrelevant accumulation
        filtered.append(dataset[i] if not temp_flag else avg)
    
    # Unused but misleading intermediate
    final_decoy_state = ''.join(str(int(temp_flag)) for _ in range(3))
    
    return filtered

# Core aggregation function used in final step
def aggregate_metrics(log_data, offset):
    total = 0
    multipliers = [2, 1, 3]
    
    for i, val in enumerate(log_data):
        index_key = (i + offset) % 3
        total += val * multipliers[index_key]
        
        # Simulated bit manipulation side effect
        shifted = (val << 1) ^ 5
        total -= (shifted & 3)  # Small correction based on bit pattern
    
    return int(total)

# === Distractor Functions Below ===

def generate_synthetic_trace(n):
    trace = []
    a, b = 1, 1
    for _ in range(n):
        trace.append(a)
        a, b = b, a + b
    return trace[:n]

def validate_integrity(arr):
    return all(x % 2 == 0 for x in arr[::2]) and sum(arr) < 10000

# === Main Execution with High Interference ===
if __name__ == "__main__":
    # Real input data
    raw_input_stream = [24, 18, 31, 12, 29, 8, 21]
    base_threshold = 20
    base_offset = 4

    # Step 1: Parse sensor data
    processed_signal = parse_sensor_sequence(raw_input_stream, base_threshold)
    
    # Step 2: Transform signal using mode 'A'
    transformed_data = transform_signal(processed_signal, 'A')
    
    # Step 3: Apply anomaly filter (has internal distractors)
    cleaned_sequence = filter_anomalies(transformed_data, window_size=3)
    
    # === Red Herring Section: Looks important but unused ===
    synthetic_trace = generate_synthetic_trace(7)
    legacy_checksum = compute_legacy_checksum(synthetic_trace)
    is_valid = validate_integrity(synthetic_trace)
    decoy_analysis = list(itertools.accumulate(synthetic_trace, lambda x, y: (x + y) % 10))
    sliced_view = decoy_analysis[2:5:2]
    
    # String distraction - appears meaningful
    status_tag = "DIAG_ACTIVE"
    flag_bits = ''.join([c for c in status_tag if c.isalpha()])[:6]
    pivot_index = len(flag_bits) % 4
    
    # Real work continues: Prepare log for aggregation
    temp_log = []
    for idx, item in enumerate(cleaned_sequence):
        if idx % 2 == 0:
            temp_log.append(item + pivot_index)
        else:
            temp_log.append(item - 1)
    
    # Key statement: this determines the answer
    final_diagnostic = aggregate_metrics(temp_log, base_offset)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")