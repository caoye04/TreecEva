import math

# Simulated sensor data processing with diagnostic logic
def collect_sensor_readings():
    raw_readings = [14.2, 18.7, 25.3, 9.1, 30.5, 22.8, 17.4, 28.9]
    offset = 5.8
    adjusted = [x + offset for x in raw_readings]
    return adjusted

def filter_outliers(data, limit=35.0):
    # Irrelevant filtering for values above 35 (none exist)
    return [x for x in data if x <= limit]

def rolling_window_average(series, window_size=3):
    averages = []
    for i in range(len(series) - window_size + 1):
        window_avg = sum(series[i:i+window_size]) / window_size
        averages.append(round(window_avg, 2))
    padding = [None] * (window_size - 1)
    return padding + averages  # Misleading: creates None values

def generate_checksum(sequence):
    # Distractor function: checksum not used in final result
    chk = 0
    for val in sequence:
        if isinstance(val, (int, float)):
            chk ^= int(val % 17)
    return chk

def transform_signal(x):
    # Nonlinear transformation applied to each element
    return math.sin(x / 10.0) * math.cos(x / 25.0)

def apply_envelope(signal_list):
    env = []
    for i, s in enumerate(signal_list):
        attenuation = 0.85 ** i
        env.append(s * attenuation if s > 0 else s * 0.75)
    return env

def count_transitions(data, delta_threshold=0.1):
    # Dead code path: counts sign transitions but unused
    if not data:
        return 0
    transitions = 0
    prev_positive = data[0] > 0
    for val in data[1:]:
        curr_positive = val > 0
        if curr_positive != prev_positive and abs(val) > delta_threshold:
            transitions += 1
        prev_positive = curr_positive
    return transitions

def build_lookup_table(start_val, steps):
    # Unused lookup table (red herring)
    table = {}
    for i in range(steps):
        key = round(start_val + i * 0.5, 2)
        table[key] = math.log(key) if key > 0 else -999
    return table

def shift_register_sequence(data, shifts=2):
    # Irrelevant bit manipulation on floats (converted to int codes)
    if not data:
        return []
    # Mapping float to truncated integer hash
    int_codes = [int(abs(d) * 10) % 256 for d in data]
    for _ in range(shifts):
        int_codes = [(code << 1 | (code >> 7)) & 255 for code in int_codes]  # Circular left shift
    return int_codes  # Never used

def analyze_pattern(dataset, threshold_fn):
    # Core analysis logic
    magnitude = sum(abs(x) for x in dataset if x is not None)
    count_valid = len([x for x in dataset if x is not None])
    avg_magnitude = magnitude / count_valid if count_valid else 0
    
    # Conditional expression used
    adjustment = 1.75 if threshold_fn(avg_magnitude) else 0.85
    
    # Apply recursive weighting
    def recursive_weight(n):
        if n <= 1:
            return 1
        return recursive_weight(n - 1) * 0.9 + 0.1
    
    base_score = avg_magnitude * adjustment
    final_weight = recursive_weight(count_valid)
    
    return int(base_score * final_weight * 100)  # Final diagnostic score

# Orchestration block
if __name__ == '__main__':
    # Step 1: Collect and adjust sensor data
    sensor_data = collect_sensor_readings()  # [20.0, 24.5, 31.1, 14.9, 36.3, 28.6, 23.2, 34.7]
    
    # Step 2: Filter outliers (no effect since all below 35)
    filtered_data = filter_outliers(sensor_data)
    
    # Step 3: Compute rolling average (creates Nones)
    moving_averages = rolling_window_average(filtered_data)
    
    # Step 4: Transform signal using trigonometric envelope
    transformed_signal = [transform_signal(x) for x in filtered_data]
    transformed_signal = apply_envelope(transformed_signal)
    
    # Step 5: Distractor operations (checksum, lookup, shift register)
    checksum = generate_checksum(transformed_signal)
    lookup_map = build_lookup_table(10.0, 20)
    shift_codes = shift_register_sequence(transformed_signal, 3)
    transition_count = count_transitions(transformed_signal)
    
    # Step 6: Prepare final dataset
    transformed_data = [round(x, 3) for x in transformed_signal if x is not None]
    
    # Step 7: Define threshold function as lambda (required feature)
    threshold_func = lambda x: x > 0.45
    
    # Step 8: Critical execution point
    final_diagnostic = analyze_pattern(transformed_data, threshold_func)
    
    # Output result
    print(f"Result: {final_diagnostic}")