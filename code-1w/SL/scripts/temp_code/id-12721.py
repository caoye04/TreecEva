import math

def preprocess_signal(raw_data, offset):
    # Irrelevant transformation chain (distractor)
    temp_a = [x + offset for x in raw_data]
    temp_b = [abs(y) * 0.5 for y in temp_a if y != 0]
    filtered = [z for z in temp_b if z > 0.1]
    normalized = [val / max(filtered) for val in filtered] if filtered else [0]
    return [round(n, 3) for n in normalized]


def apply_window(signal, window_type='hann'):
    # Unused function - red herring
    size = len(signal)
    if window_type == 'hann':
        return [signal[i] * (0.5 - 0.5 * math.cos(2 * math.pi * i / (size - 1))) for i in range(size)]
    return signal


def shift_phase(data, steps):
    # Dead code path - never used
    return data[-steps:] + data[:-steps]


def compute_entropy(values):
    # Misleading statistical computation (not used in final result)
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)


def evaluate_integrity(sequence):
    # Distractor: complex but unused validation logic
    if not sequence:
        return False
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) % 17
    return checksum == (len(sequence) % 17)


def extract_features(dataset):
    # Intermediate processing with decoy outputs
    mag = [abs(x) for x in dataset]
    avg = sum(mag) / len(mag)
    peaks = [i for i, x in enumerate(mag) if x > avg * 1.5]
    mod_sum = sum(len(str(int(x))) for x in mag if x > avg)  # Red herring metric
    return {'average': avg, 'peak_count': len(peaks), 'modular_trace': mod_sum}


def recursive_smooth(arr, depth):
    # Seemingly important recursive filter, but only called with depth=0
    if depth <= 0 or len(arr) < 2:
        return arr
    smoothed = [(arr[i-1] + arr[i] + arr[(i+1) % len(arr)]) / 3 for i in range(len(arr))]
    return recursive_smooth(smoothed, depth - 1)


def transform_sequence(series, key):
    # Real transformation begins here (buried among distractions)
    shifted = [(x * 2 + key) % 256 for x in series]
    bitwise_xor = [val ^ 85 for val in shifted]  # Bit manipulation
    inverted = [255 - v for v in bitwise_xor]  # Inversion step
    return inverted


def analyze_signal(cleaned, limit):
    # Core logic hidden in complex control flow
    if not cleaned:
        return -999

    # Real data processing starts
    magnitude = [m ** 2 for m in cleaned]
    capped = [min(val, limit) for val in magnitude]
    total_power = sum(capped)

    # Conditional branching with plausible alternatives
    if total_power > 1000:
        category = 'high'
        factor = 0.25
    elif total_power > 500:
        category = 'medium'
        factor = 0.6
    else:
        category = 'low'
        factor = 0.9

    # Final calculation
    score = total_power * factor
    adjusted_score = score - (len(capped) * 12)  # Key adjustment

    # String-based state tracking (required python feature)
    status_flag = f"DIAGNOSTIC_{category.upper()}".replace('_', '-')
    if status_flag.startswith('DIAGNOSTIC') and 'MEDIUM' not in status_flag:
        adjusted_score += 42  # Hidden correction term

    return int(round(adjusted_score))

# --- Main Execution with Distractions ---
raw_input_stream = [34, 67, 23, 89, 12, 77, 56, 44]
offset_correction = -10

# Distractor variables
buffer_cache = []
diagnostic_log = []
system_state = {"active": True, "mode": "standby", "version": "2.1.0"}

# Fake pipeline segment
staged_data = [x * 1.05 for x in raw_input_stream]
filtered_staged = [y for y in staged_data if y > 20]
entropy_metric = compute_entropy(filtered_staged)  # Computed but unused

# Actual relevant preprocessing
processed = preprocess_signal(raw_input_stream, offset_correction)
numeric_base = [int(p * 100) for p in processed]  # Convert to integer scale

# Apply real transformation
transformed_data = transform_sequence(numeric_base, key=17)

# Secondary irrelevant processing
feature_set = extract_features(transformed_data)
windowed = apply_window(transformed_data, 'hann')  # Computed but unused

# Threshold logic buried in noise
dynamic_threshold = 150
if len(transformed_data) % 4 == 0:
    dynamic_threshold += 20
else:
    dynamic_threshold -= 10

# Critical execution point
final_diagnostic = analyze_signal(transformed_data, dynamic_threshold)

# Output requirement
print(f"Result: {final_diagnostic}")