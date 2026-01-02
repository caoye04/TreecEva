def normalize_signal(raw_values):
    normalized = []
    base_offset = sum(raw_values) / len(raw_values)
    for val in raw_values:
        normalized.append((val - base_offset) * 0.85)
    return normalized

# Irrelevant signal processing function (decoy)
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append(sum(data[i-1:i+2]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Unused transformation (dead code path)
def frequency_shift(signal, factor=1.2):
    return [s * factor for s in signal]

# Distractor: complex but unused filter
class NoiseFilter:
    def __init__(self, threshold):
        self.threshold = threshold
        self.history = []

    def apply(self, values):
        return [v for v in values if abs(v) > self.threshold]

# Real processing chain
def encode_timestamps(time_list):
    encoded = []
    for i, t in enumerate(time_list):
        encoded.append(t ^ (i + 1))  # XOR with index
    return encoded

# Misleading intermediate aggregation
def compute_moment(readings):
    moment_sum = 0
    for i, r in enumerate(readings):
        moment_sum += r * (i ** 2)
    return moment_sum / len(readings) if readings else 0

# Core data processing
def process_readings(raw_readings, timestamps):
    temp_storage = {}
    filtered_pairs = []

    # Use of zip and enumerate (required features)
    for idx, (reading, ts) in enumerate(zip(raw_readings, timestamps)):
        if reading < -50 or reading > 50:
            continue  # Filter outliers
        adjusted = reading * 1.1 + (ts % 10)
        filtered_pairs.append((adjusted, ts))
        temp_storage[f'entry_{idx}'] = {'value': adjusted, 'flag': idx % 3 == 0}
    
    processed = [pair[0] for pair in filtered_pairs]
    
    # Apply normalization
    processed = normalize_signal(processed)
    
    # Sorting as part of transformation (suggested paradigm)
    processed.sort(reverse=True)
    
    # Add decoy statistics
    avg = sum(processed) / len(processed)
    variance = sum((x - avg) ** 2 for x in processed) / len(processed)
    _ = round(variance * 100, 3)  # Unused metric
    
    return processed

# Recursive analysis (simple recursion - suggested paradigm)
def analyze_readings(data, depth=0):
    if depth >= 3 or len(data) <= 1:
        return abs(data[0]) if data else 0
    
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]
    
    left_val = analyze_readings(left_half, depth + 1)
    right_val = analyze_readings(right_half, depth + 1)
    
    # Combine results with bit manipulation
    combined = int(left_val * 1.5) ^ int(right_val * 1.5)
    return combined + depth

# Simulate sensor input
def generate_test_data():
    # Fixed seed equivalent for deterministic output
    base_readings = [x * 2.5 for x in range(-20, 25, 3)]
    time_stamps = [t * 7 + 2 for t in range(len(base_readings))]
    return base_readings, time_stamps

# Main execution flow
if __name__ == '__main__':
    # Generate real data
    raw_sensor_data, timing_signals = generate_test_data()
    
    # Process the readings
    processed_data = process_readings(raw_sensor_data, timing_signals)
    
    # Perform diagnostic analysis
    final_diagnostic = analyze_readings(processed_data)
    
    # Irrelevant string operation (distractor using required feature)
    log_entry = "SensorDiagnostic_" + "_".join(["OK" if x > 0 else "ERR" for x in processed_data[:5]])
    status_flag = len(log_entry.replace("_", "")) % 7
    
    # Another decoy computation with set (suggested paradigm)
    unique_magnitudes = set(round(abs(x), 1) for x in processed_data)
    _ = len(unique_magnitudes.intersection({x + 0.1 for x in unique_magnitudes}))  # No effect
    
    # Print target result
    print(f"Result: {final_diagnostic}")