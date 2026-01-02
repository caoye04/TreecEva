import math

# Simulated sensor array diagnostics with interference

def preprocess_signal(raw_readings):
    if not raw_readings:
        return [0]
    filtered = []
    for x in raw_readings:
        if x < -100 or x > 100:
            continue
        adjusted = x * 1.05 if x >= 0 else x * 0.95
        filtered.append(round(adjusted))
    return filtered

# Irrelevant signal smoothing (distractor)
def smooth_signal(signal):
    if len(signal) < 3:
        return signal
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return [round(x, 2) for x in smoothed]

# Unused feature extraction (dead path)
def extract_features(data):
    features = {}
    features['peak'] = max(data, default=0)
    features['variance'] = sum((x - sum(data)/len(data))**2 for x in data)/len(data) if data else 0
    features['zero_crossings'] = sum(1 for i in range(1, len(data)) if data[i-1]*data[i] < 0)
    return features

# Core transformation with red herring operations
def transform_readings(readings, mode='standard'):
    temp_buffer = []
    overflow_flags = []
    scaling_factor = 2.1  # unused in final logic
    
    for val in readings:
        # Distracting bit manipulation
        binary_shift = (val << 1) ^ 0b101
        if binary_shift < 0:
            overflow_flags.append(True)
            continue
        
        # Actual relevant transformation
        if val % 2 == 0:
            transformed = int(math.sqrt(abs(val)) * 10)
        else:
            transformed = abs(val) // 3
        
        # Conditional expression (required Python feature)
        temp_buffer.append(transformed if transformed > 5 else -transformed)
    
    # Dead code: never used later
    diagnostic_log = [
        f"Entry:{i}: {v}" for i, v in enumerate(temp_buffer[:3])
    ]
    
    return temp_buffer

# Misleading accumulation chain
def compute_aggregate_metrics(dataset):
    total_power = 0
    spike_count = 0
    history = set()
    
    for item in dataset:
        if item in history:
            total_power -= item  # misleading adjustment
        else:
            total_power += abs(item)
            history.add(item)
        if abs(item) > 50:
            spike_count += 1
    
    # Early break that rarely triggers (red herring)
    if spike_count > 100:
        return -1  
    
    # Unused derived metric
    normalized_score = total_power / (len(dataset) or 1)
    
    return total_power  # only this matters

# Main analysis with conditional control flow
def analyze_pattern(data_sequence, limit):
    if not data_sequence:
        return -999
    
    # Linear search for critical threshold breach
    critical_index = -1
    for idx, val in enumerate(data_sequence):
        if val >= limit:
            critical_index = idx
            break  # early break
    
    # Conditional expression determines processing path
    base_ref = data_sequence[critical_index] if critical_index != -1 else data_sequence[0]
    
    accumulator = 0
    multiplier = 3
    for i, x in enumerate(data_sequence):
        if i % 2 == 0:
            accumulator += x * multiplier
        else:
            accumulator -= x // (i + 1)
    
    # Final computation independent of many prior paths
    result = (accumulator ^ base_ref) + len(set(data_sequence))
    
    # Decoy complex operation (never accessed)
    deep_analysis = {
        'fft_peak': sum(math.sin(i * 0.1) * x for i, x in enumerate(data_sequence[:10])) if len(data_sequence) >= 10 else 0,
        'entropy': 0.0
    }
    
    return result

# --- Execution with heavy distractions ---

# Simulated input (real)
raw_sensor_data = [144, -87, 196, 50, 225, -33, 169, 88, 121, 75, 100]

# Irrelevant preprocessing chain
filtered_data = preprocess_signal(raw_sensor_data)
denoised_signal = smooth_signal(filtered_data)  # dead end
extracted_features = extract_features(denoised_signal)  # unused

# Key transformation path
transformed_data = transform_readings(filtered_data, mode='enhanced')

# Phantom metrics calculation
phantom_metric = compute_aggregate_metrics([x**2 for x in denoised_signal if x > 10])  # distractor

# Threshold logic with subtle dependency
threshold = 15

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f"Result: {final_diagnostic}")