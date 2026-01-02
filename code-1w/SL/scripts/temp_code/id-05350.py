import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_readings(raw):    
    offset = 0.75
    scale = 2.1
    adjusted = [(x * scale + offset) for x in raw if x > 0]  # list comprehension
    normalized = [min(max(val, -1), 1) for val in adjusted]
    return normalized

# Irrelevant auxiliary function (decoy)
def compute_entropy(data):
    entropy = 0.0
    freq_map = {}
    total = len(data)
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

# Data transformation with filtering and masking
def transform_readings(signal):
    filtered = []
    for val in signal:
        if abs(val) < 0.95:  # threshold filter
            filtered.append(val ** 2)
        else:
            filtered.append(abs(val) * 0.5)
    inverted = [round(-x, 3) for x in filtered]
    return inverted

# Core analysis logic — only this affects final result
valid_codes = [101, 102, 103, 201, 205]
code_weights = {101: 1.1, 102: 1.3, 103: 1.7, 201: 1.9, 205: 2.3}

def generate_code_sequence(base):
    seq = []
    temp = base
    while temp > 1:
        if temp % 2 == 0:
            temp //= 2
            seq.append(101)
        else:
            temp = (temp * 3) + 1
            seq.append(102)
        if len(seq) > 15:
            break
    return seq[-5:]  # last five only

def analyze_pattern(data):
    baseline = sum(data) * 100
    adjustment_factor = 0
    
    # Conditional weighting based on pattern shape
    if len(data) >= 5 and data[2] < data[1] < data[0]:
        adjustment_factor += 2
    if data[-1] < 0:
        adjustment_factor += 1
    
    # Only portion that matters — rest are distractions
    raw_input = [3, 5, 7, 9, 11]
    code_seq = generate_code_sequence(len(raw_input))
    weight_sum = 0
    for code in code_seq:
        if code in code_weights:
            weight_sum += code_weights[code]
    
    # Final computation chain
    intermediate = baseline + (weight_sum * adjustment_factor * 10)
    validation_offset = len(code_seq) * 0.5
    result = int(intermediate - validation_offset)
    
    # Dead code path — never reached due to prior logic
    if result < 0:
        backup = compute_entropy(data)
        result = int(backup * 1000)
    
    return result

# Misleading initialization block
sensor_noise_floor = 0.023
calibration_matrix = [[0.1, 0.4], [0.8, 0.6]]
reference_checksum = 54321

# Main execution flow
raw_data = [-2, -1, 0, 1, 2, 3, 4, 5]
denoised_signal = preprocess_sensor_readings(raw_data)
transformed_data = transform_readings(denoised_signal)

# Unused variables — red herrings
aggregated_metric = sum([abs(x) for x in transformed_data]) / len(transformed_data)
anomaly_flags = [i for i, x in enumerate(transformed_data) if x > 0.5]

# Key statement
final_diagnostic = analyze_pattern(transformed_data)

# Output result as required
print(f"Result: {final_diagnostic}")