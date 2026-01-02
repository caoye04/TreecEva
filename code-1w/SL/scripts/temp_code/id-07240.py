import math

def preprocess_data(raw_input):
    tokens = raw_input.strip().split(',')
    numeric_values = [float(x) for x in tokens if x.replace('.', '').lstrip('-').isdigit()]
    return [x for x in numeric_values if x > 0]


def generate_calibration(size):
    base = [1]
    for i in range(1, size):
        base.append((base[-1] * (i + 1)) % 97)
    return base


def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = math.sqrt(sum((x - mean_val) ** 2 for x in data) / len(data))
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev], mean_val, std_dev


def transform_signal(signal):
    # Irrelevant transformation path (dead code for final result)
    transformed = []
    for val in signal:
        transformed.append(int(val * 17) & 255)
    return transformed


def dummy_analysis(seq):
    # Decoy function with misleading intermediate computations
    temp_result = 0
    for i in range(len(seq)):
        temp_result ^= int(seq[i] * 100) % 19
    temp_result = (temp_result * 13) % 101
    return temp_result


def validate_sequence(seq):
    # Irrelevant validation logic (not used in main path)
    if len(seq) < 5:
        return False
    checksum = 0
    for i, val in enumerate(seq):
        checksum += val * (i + 1)
    return checksum % 7 == 0


def decode_pattern(buffer):
    # Unused decoding logic - red herring
    pattern = []
    for b in buffer:
        shifted = (b >> 2) ^ (b << 1) & 255
        pattern.append(shifted % 10)
    return pattern


def analyze_signal(buffer, calibration):
    # Core relevant computation
    weighted_sum = 0.0
    for i in range(min(len(buffer), len(calibration))):
        weight = calibration[i] / (i + 1)
        contribution = buffer[i] * weight
        weighted_sum += contribution
    
    # Key distraction: multiple intermediate variables
    adjustment_factor = 1.0
    if len(buffer) > 10:
        adjustment_factor *= 0.9
    elif len(buffer) % 3 == 0:
        adjustment_factor *= 1.1
    else:
        adjustment_factor *= 1.05
    
    # Real manipulation
    weighted_sum = (weighted_sum * 1.23) % 10000
    
    # Fake normalization path
    normalized = weighted_sum / (max(buffer) if buffer else 1)
    normalized = round(normalized, 4)
    
    # Final computation uses only weighted_sum
    entropy_marker = 0
    for val in calibration[:8]:
        entropy_marker += (val * 7) % 5
    
    final_score = int(weighted_sum) + (entropy_marker * 2)
    
    # Actual answer variable
    final_diagnostic = final_score - 500
    
    return final_diagnostic

# Main execution block
raw_data = "3.1, 4.5, -2.0, 7.8, abc, 9.2, 0.5, 6.3, 8.1, 2.7, 5.4, 1.9, 10.0"
processed_data = preprocess_data(raw_data)

# Irrelevant filtered copy
clean_data, avg, spread = filter_outliers(processed_data)

# Buffer built from clean subset
pattern_buffer = [x * 1.5 for x in clean_data]

# Signal transformation (unused)
encoded_signal = transform_signal(pattern_buffer)

# Calibration sequence generation
calibration_sequence = generate_calibration(len(pattern_buffer) + 5)

# Dummy analysis (red herring)
diagnostic_hint = dummy_analysis(calibration_sequence)

# Validate (but not used)
is_valid = validate_sequence(pattern_buffer)

# Decode attempt (unused)
pattern_codes = decode_pattern(encoded_signal)

# Critical statement
final_diagnostic = analyze_signal(pattern_buffer, calibration_sequence)

print(f"Result: {final_diagnostic}")