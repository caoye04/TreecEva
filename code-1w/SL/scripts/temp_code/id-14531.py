import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    normalized = [(x - 10) / 90 for x in filtered]
    scaled = [int(x * 1000) for x in normalized]
    return scaled

# Irrelevant helper - dead path
def deprecated_filter(data):
    return [x for x in data if x % 2 == 0]

# Data transformation pipeline
def encode_sequence(values, base_shift):
    encoded = []
    for i, val in enumerate(values):
        shifted = (val + base_shift) % 256
        transformed = shifted ^ (i % 64)
        encoded.append(transformed)
    return encoded

# Core pattern analyzer
analyze_pattern = lambda seq, threshold: sum(
    1 for x in seq if (x & 3 == 0) and x > threshold
)

# Misleading auxiliary function (never called in critical path)
def compute_legacy_metric(seq):
    total = 0
    for x in seq:
        if x < 50:
            total += x ** 2
        else:
            total -= x
    return total / (len(seq) + 1)

# Decoy state tracker
class StateTracker:
    def __init__(self):
        self.history = []
        self.flag = False

    def update(self, val):
        self.history.append(val % 100)
        if val > 200:
            self.flag = True

# Unused recursive variant
def recursive_process(arr, depth):
    if depth == 0 or len(arr) == 0:
        return arr
    return recursive_process([x // 2 for x in arr if x > 10], depth - 1)

# Main execution flow
if __name__ == "__main__":
    # Initial sensor inputs (simulated)
    raw_sensor_data = [
        5, 15, 23, 34, 45, 56, 67, 78, 89, 95, 105, 44, 55, 66, 77
    ]

    # Irrelevant intermediate variables
    temp_buffer = [x * 2 + 1 for x in raw_sensor_data]
    outlier_count = sum(1 for x in raw_sensor_data if x < 10 or x > 100)
    avg_raw = sum(raw_sensor_data) / len(raw_sensor_data)
    
    # Signal conditioning
    processed = preprocess_readings(raw_sensor_data)
    
    # Dead code branch
    if len(processed) > 100:
        processed = deprecated_filter(processed)

    # Key transformation with distractor operations
    shift_key = 89
    encrypted_signal = encode_sequence(processed, shift_key)
    
    # More red herrings
    signal_entropy = 0.0
    non_zero_count = 0
    for val in encrypted_signal:
        if val != 0:
            signal_entropy += val * math.log(abs(val) + 1e-5)
            non_zero_count += 1
    if non_zero_count > 0:
        signal_entropy /= non_zero_count

    # Create dictionary-based mapping (partially relevant)
    index_map = {i: val for i, val in enumerate(encrypted_signal)}
    reverse_lookup = {v: k for k, v in index_map.items()}

    # Inject unused sorting
    sorted_values = sorted(encrypted_signal, reverse=True)
    median_estimate = sorted_values[len(sorted_values) // 2] if sorted_values else 0

    # Critical parameters
    calibration_offset = 33
    key_threshold = len(encrypted_signal) + calibration_offset  # 14 + 33 = 47

    # Apply meaningful transformation
    adjusted_signal = [x + calibration_offset for x in encrypted_signal]

    # Introduce bitwise decoy
    masked_values = [x & 0x7F for x in adjusted_signal]

    # Actual target computation uses original transformed data, not masked
    final_diagnostic = analyze_pattern(adjusted_signal, key_threshold)

    # Final irrelevant object
    tracker = StateTracker()
    for val in adjusted_signal:
        tracker.update(val)

    print(f"Result: {final_diagnostic}")