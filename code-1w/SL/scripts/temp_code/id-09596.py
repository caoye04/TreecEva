import math

def preprocess_signals(data_stream):
    # Irrelevant signal processing (dead path)
    filtered = [x for x in data_stream if x > 0]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return sorted(normalized, reverse=True)


def decode_transmission(transmission):
    # Distractor: complex string decoding with no impact on result
    segments = transmission.split('-')
    decoded = []
    for seg in segments:
        if seg.isalpha():
            decoded.append(ord(seg[-1]) - ord('a'))
        else:
            decoded.append(int(seg[:2]))
    return set(decoded)  # Unused return


def calculate_checksum(frame):
    # Bit manipulation red herring
    checksum = 0
    for b in frame:
        checksum ^= b
        checksum = (checksum << 1) & 0xFF
    return checksum + 55  # Never actually used


def evaluate_stability(readings):
    # Complex but irrelevant stability metric
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance) < 1.5


def calculate_thermal_buffer(state, log_entry):
    # Core logic hidden among distractions
    base = len(state) * 2
    modifier = 0
    
    # Real logic begins here
    for item in log_entry:
        if 'eff' in item:
            try:
                val = float(item.split('_')[1])
                modifier += val
            except:
                continue
    
    # Actual computation path
    temp_grid = [[i + j for j in range(3)] for i in range(3)]
    sum_grid = sum(sum(row) for row in temp_grid)
    
    # Key calculation
    if sum_grid > 10:
        modifier *= 1.5
    else:
        modifier *= 0.8
    
    # Final result
    return int(base + modifier)

# Simulated sensor inputs (distractions)
data_stream = [-2, -1, 0, 1, 4, 9, 16]
network_state = [1, 1, 0, 1, 1]
efficiency_log = ['eff_2.4', 'std_3.1', 'eff_1.8', 'log_9.0', 'eff_3.0']
transmission_code = "ab-12-xr-78"
sensor_frame = [0x1A, 0x2B, 0x3C, 0x4D]
performance_readings = [2.1, 1.9, 2.3, 2.0, 1.8]

# Dead code paths that look important
signal_profile = preprocess_signals(data_stream)
transmission_set = decode_transmission(transmission_code)
stability_flag = evaluate_stability(performance_readings)
frame_checksum = calculate_checksum(sensor_frame)

# Unused complex expressions
auxiliary_metric = (len(transmission_code.replace('-', '')) ** 2) >> 2
redundant_flag = any(stability_flag for _ in range(5))

# Key execution point
thermal_capacity = calculate_thermal_buffer(network_state, efficiency_log)

# Final output
print(f"Result: {thermal_capacity}")