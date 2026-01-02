import math

def analyze_signal(values, threshold=5.0):
    """Irrelevant function analyzing signal strength (distractor)"""
    anomalies = []
    for i, v in enumerate(values):
        if abs(v) > threshold:
            anomalies.append((i, v))
    return anomalies

def generate_checksum(sequence):
    """Dead code path: generates checksum but never used"""
    chk = 0
    for byte in sequence:
        chk ^= byte % 256
        chk = (chk << 1) | (chk >> 7)
        chk &= 0xFF
    return chk

def transform_coordinates(coords):
    """Unused transformation logic (red herring)"""
    transformed = []
    for idx, (x, y) in enumerate(coords):
        angle = math.atan2(y, x)
        r = math.sqrt(x**2 + y**2)
        new_x = r * math.cos(angle + 0.1)
        new_y = r * math.sin(angle + 0.1)
        transformed.append((new_x + idx, new_y - idx))
    return transformed

def evaluate_stability(readings):
    """Misleading computation with early returns (distraction)"""
    if len(readings) < 3:
        return 0.0
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    if variance < 1e-4:
        return round(math.exp(-variance), 4)
    trend = all(readings[i] <= readings[i+1] for i in range(len(readings)-1))
    return 0.5 if trend else 0.25

def process_metrics(log_data, config_weights):
    """Core function that computes the final result"""
    cumulative = 0
    base_shift = 17
    temp_buffer = []

    # Real logic embedded within distractions
    for index, (entry, weight) in enumerate(zip(log_data, config_weights)):
        raw_value = entry['magnitude'] * weight
        offset = entry.get('offset', 0) or 1  # Avoid zero division

        # Key calculation step
        adjusted = (raw_value + base_shift) / offset
        if index % 2 == 0:
            adjusted = math.floor(adjusted)
        else:
            adjusted = math.ceil(adjusted)

        # Destructuring assignment (tuple unpacking)
        flags = entry['flags']
        critical, debug_mode = flags['critical'], flags['debug']

        # Conditional interference
        if critical:
            adjusted *= 1.5
        if debug_mode:
            temp_buffer.append(adjusted * 0.1)  # Unused buffer

        # Accumulate only non-critical path values
        if not debug_mode:
            cumulative += int(adjusted)

        # Early termination red herring (never triggers due to data)
        if cumulative > 10000:
            return -999  # Dead path

    # Secondary processing with dictionary lookup
    modifiers = {0: 0.95, 1: 1.05, 2: 1.1, 3: 0.85}
    modifier_key = len(log_data) % 4
    cumulative = int(cumulative * modifiers.get(modifier_key, 1.0))

    # Final adjustment using bitwise (irrelevant in practice)
    decoy_flag = 0b101010
    mask = 0b111100
    masked = decoy_flag & mask
    if masked > 40:
        cumulative += 100  # Never executed

    return cumulative

# Irrelevant dataset (signal data)
signal_readings = [5.1, 4.9, 5.0, 5.2, 4.8, 5.3]
analyze_signal(signal_readings)

# Unused coordinate list
coords = [(1.0, 2.0), (3.5, 4.1), (0.5, 6.0)]
transform_coordinates(coords)

# Checksum dummy data
byte_sequence = [65, 66, 67, 68, 69]
generate_checksum(byte_sequence)

evaluate_stability([1.0, 1.1, 1.2, 1.3])

evaluate_stability([2.0, 2.0, 2.0])

# Core input data driving actual computation
data_log = [
    {'magnitude': 42.0, 'offset': 3, 'flags': {'critical': True, 'debug': False}},
    {'magnitude': 38.5, 'offset': 2, 'flags': {'critical': False, 'debug': True}},
    {'magnitude': 55.0, 'offset': 5, 'flags': {'critical': True, 'debug': False}},
    {'magnitude': 29.3, 'offset': 1, 'flags': {'critical': False, 'debug': False}},
    {'magnitude': 61.7, 'offset': 4, 'flags': {'critical': True, 'debug': False}}
]

weights = [1.2, 0.8, 1.5, 0.9, 1.1]

# Execution point of interest
final_score = process_metrics(data_log, weights)

# Print result as required
print(f"Target result: {final_score}")