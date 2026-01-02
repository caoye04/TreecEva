import itertools

def preprocess_sensor_data(data_chunk):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in data_chunk if x > 0]

def validate_calibration(sequence):
    # Misleading validation logic
    total = sum(sequence)
    threshold = 256
    return total < threshold

def decode_frequency_pattern(signal):
    # Unused signal decoding (distractor)
    decoded = []
    for i, val in enumerate(signal):
        if i % 3 == 0:
            decoded.append(val ** 0.5)
    return decoded

def calculate_thermal_rating(log_entries):
    base_rating = 0
    adjustment_factor = 1.75
    
    # Real logic starts here — nested and interdependent
    for index, entry in enumerate(log_entries):
        if index % 2 == 0:
            base_rating += entry * (index + 1)
        else:
            base_rating -= entry // (index + 1)
    
    # Apply transformation using slicing and zip
    shifted = log_entries[1:] + [log_entries[0]]
    paired = list(zip(log_entries, shifted))
    
    secondary_correction = 0
    for a, b in paired:
        secondary_correction += (a - b) * 0.5
    
    # Tertiary influence from itertools-generated sequence
    counter_sequence = list(itertools.islice(itertools.count(1, 3), len(log_entries)))
    tertiary_weight = 0
    for val, step in zip(log_entries, counter_sequence):
        if step % 5 != 0:  # Conditional red herring
            tertiary_weight += val / step

    final_rating = base_rating + secondary_correction + (tertiary_weight * adjustment_factor)
    
    # Decoy operations below
    dummy_var = [x ** 2 for x in counter_sequence if x < 10]  # Dead computation
    overflow_check = sum(dummy_var) > 1000  # Irrelevant check
    metadata_buffer = {'status': 'cleared', 'version': 3.1}  # Useless struct
    
    return final_rating

def main():
    # Simulated telemetry stream (real input)
    sensor_readings = [12, 8, 15, 23, 7, 19]
    
    # Distractor variables
    calibration_matrix = [[1, 0], [0, 1]]  # Unused
    spectral_weights = {k: v**2 for k, v in enumerate([2.1, 1.3, 0.9])}  # Irrelevant
    temporal_offset = 0.0076  # Nowhere used
    
    # Real data flow begins
    normalized_input = [int(x * 0.8) for x in sensor_readings]  # Transform
    efficiency_log = []
    
    for val in normalized_input:
        if val > 10:
            efficiency_log.append(val + 2)
        elif val > 5:
            efficiency_log.append(val + 1)
        else:
            efficiency_log.append(val)
    
    # Key statement: what is thermal_capacity after this?
    thermal_capacity = calculate_thermal_rating(efficiency_log)
    
    # More distractions
    debug_trace = []
    for idx, num in enumerate(efficiency_log):
        debug_trace.append(f"Step {idx}: {num}")
    
    anomaly_detector = any([x > 20 for x in debug_trace])  # String comparison side effect
    
    # Output must follow format
    print(f"Result: {thermal_capacity}")

if __name__ == "__main__":
    main()