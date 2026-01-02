import math

# Simulated sensor data processing with red herrings and complex transformations
def fetch_calibration_sequence():
    return [0.1, 0.3, 0.5, 0.7, 0.9]

def compute_entropy(signal):
    entropy = 0.0
    for x in signal:
        if x > 0:
            entropy -= x * math.log(x)
    return round(entropy, 6)

def shift_phase(data, offset=1):
    # Irrelevant transformation - not used in final result
    return [data[(i + offset) % len(data)] for i in range(len(data))]

def generate_combinatorics_index(n):
    # Dead-end computation: calculates sum of combinations C(n,2) but unused
    return n * (n - 1) // 2

def encrypt_sequence(seq):
    # Distractor function: operates on strings, never called
    encoded = ''.join([chr(int(x * 100) + 65) for x in seq])
    return encoded.upper().replace('A', 'X')

def normalize_signal(raw):
    norm_factor = sum(x ** 2 for x in raw) ** 0.5
    return [round(x / norm_factor, 6) for x in raw]

def mirror_boundary(values):
    # Adds symmetric padding — looks important but unused
    return [values[0]] + values + [values[-1]]

def transform_case(text):
    # Uses string methods as required — irrelevant to numeric flow
    return text.lower().swapcase().title()

def apply_mask(signal, mask_type='binary'):
    if mask_type == 'binary':
        return [int(x >= 0.5) for x in signal]
    else:
        return [x for x in signal]

def filter_outliers(data, limit=0.8):
    # Another filtering path that isn't taken
    return [x for x in data if x <= limit]

def calculate_checksum(arr):
    # Bit manipulation distractor
    checksum = 0
    for val in arr:
        int_val = int(val * 100)
        checksum ^= int_val
        checksum = (checksum << 1) % 256
    return checksum

def rolling_derivative(series):
    # Unused advanced feature extraction
    return [round(series[i+1] - series[i], 6) for i in range(len(series)-1)]

def analyze_pattern(seq, limit):
    total = 0
    toggle = True
    for i, val in enumerate(seq):
        if toggle:
            total += val * (i + 1)
        else:
            total -= val * (i + 1)
        if val > limit:
            toggle = not toggle
    return int(total * 1000)  # Scale for integer output

# Main execution flow with distractions
raw_sensor_data = [0.25, 0.52, 0.33, 0.81, 0.42]
calibration = fetch_calibration_sequence()

# Normalization is critical
normalized_data = normalize_signal(raw_sensor_data)

# Apply transformations — only one matters
masked_data = apply_mask(normalized_data, 'binary')
filtered_data = filter_outliers(normalized_data, 0.75)  # Computed but not used

# Entropy calculation — looks diagnostic but unused
signal_entropy = compute_entropy(normalized_data)

# Generate derived arrays — some are dead ends
shifted_data = shift_phase(normalized_data, 2)
indexed_combinations = generate_combinatorics_index(5)
boundary_padded = mirror_boundary(normalized_data)

dynamic_threshold = 0.45
transformed_data = []
for i, val in enumerate(normalized_data):
    if i % 2 == 0:
        transformed_data.append(val + calibration[i] * 0.1)
    else:
        transformed_data.append(val - 0.05)

# String-based processing to satisfy language feature requirement
status_log = "SENSOR_OK"
processed_status = transform_case(status_log) + '_FINAL'

# Checksum computed but does not affect logic
diagnostic_checksum = calculate_checksum(transformed_data)

# Key statement
final_diagnostic = analyze_pattern(transformed_data, dynamic_threshold)

print(f"Result: {final_diagnostic}")