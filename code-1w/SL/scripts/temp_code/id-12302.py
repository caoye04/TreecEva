import math

# Simulated sensor array data with noise and metadata
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 47, 50, 52, 48, 55, 60, 53]
raw_signal = [0.88, 0.91, 0.77, 0.95, 0.82, 0.69, 0.93, 0.85]

def apply_calibration(data, factor=1.02, offset=0.5):
    # Irrelevant calibration function for temperature
    return [round((x + offset) * factor, 2) for x in data]

def compute_entropy(signal):
    # Distractor: computes entropy but not used in final path
    total = sum(signal)
    probabilities = [s / total for s in signal]
    return round(-sum(p * math.log(p) for p in probabilities if p > 0), 4)

def filter_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

def generate_checksum(text_key):
    # String method distractor
    checksum = 0
    for char in text_key.upper().replace('-', '').strip():
        checksum += ord(char) % 10
    return checksum

def preprocess_signal(signal, mode='strict'):
    # Apply smoothing with irrelevant branching
    smoothed = []
    for i in range(len(signal)):
        if i == 0:
            smoothed.append(signal[i])
        elif i == len(signal) - 1:
            smoothed.append((signal[i-1] + signal[i]) / 2)
        else:
            val = (signal[i-1] + signal[i] + signal[i+1]) / 3
            smoothed.append(round(val, 3))
    if mode == 'strict':
        # This branch is taken, but contains red herring operations
        temp_flag = ''.join([str(int(s > 0.8)) for s in smoothed[:4]])
        flag_value = int(temp_flag, 2)
        adjusted = [s * (1 + flag_value * 0.01) for s in smoothed]
        return [round(x, 3) for x in adjusted]
    return smoothed

def accumulate_with_decay(values, decay=0.9):
    # Another distractor accumulation pattern
    acc = 0
    series = []
    for v in values:
        acc = acc * decay + v
        series.append(round(acc, 3))
    return series

def extract_diagnostic_code(label: str) -> int:
    # Uses string methods meaningfully but not on critical path
    parts = label.split('_')
    code_str = ''.join(filter(str.isdigit, parts[-1])) if parts else ''
    return int(code_str) if code_str else 777

def analyze_signal(cleaned):
    # Core logic hidden among multiple layers
    n = len(cleaned)
    if n == 0:
        return 0
    
    # Compute rolling max deviation
    max_dev = 0
    for i in range(1, n):
        dev = abs(cleaned[i] - cleaned[i-1])
        if dev > max_dev:
            max_dev = dev
    
    # Determine stability band using modular arithmetic
    band = int((max_dev * 100) % 7) + 1
    
    # Summation with conditional rounding
    base_score = sum(math.sin(x) for x in cleaned)
    rounded_score = round(base_score * 10) / 10
    
    # Final transformation using multiple concepts
    intermediate = (rounded_score ** 2) * 1000
    bit_shifted = int(intermediate) ^ (band << 3)  # XOR with left-shifted band
    final_value = bit_shifted + (bit_shifted & 255)  # Add bitwise AND tail
    
    # Dead code path - never executed due to structure
    if False:
        fallback = generate_checksum('DIAG-TEMP-ERR')
        return fallback
        
    return final_value

# Irrelevant preprocessing chain
calibrated_temps = apply_calibration(temperature_readings)
entropy_metric = compute_entropy(raw_signal)  # Computed but unused
filtered_humidity = filter_outliers(humidity_readings, threshold=1.5)

# Key processing steps
processed_signal = preprocess_signal(raw_signal, mode='strict')
accumulated_series = accumulate_with_decay(processed_signal)  # Distractor assignment

# Critical execution point
final_diagnostic = analyze_signal(processed_signal)

# Print required result
print(f"Result: {final_diagnostic}")