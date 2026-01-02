import math

# Simulated sensor data processing with noise filtering and signal analysis
def collect_sensor_data():
    raw_data = [i * 0.5 + (i % 7) for i in range(30)]
    noise_mask = [math.sin(i * 0.3) for i in range(30)]
    return [raw_data[i] + noise_mask[i] for i in range(30)]

# Irrelevant helper: computes statistical dispersion (not used in final logic)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Misleading transformation: looks important but unused
def transform_frequency_domain(signal):
    transformed = []
    for i, val in enumerate(signal):
        phase = math.cos(i * 0.2)
        transformed.append(val * phase)
    return transformed

# Decoy function: simulates calibration but not invoked
def auto_calibrate(sensors):
    baseline = sum(sensors[:5]) / 5
    adjusted = [val - baseline + 0.1 for val in sensors]
    return adjusted

# Real signal filter based on dynamic threshold
def filter_anomalies(data, limit):
    cleaned = []
    temp_buffer = []
    for idx, value in enumerate(data):
        if abs(value) > limit:
            temp_buffer.append(value * 0.9)  # dampened store
        else:
            temp_buffer.append(value)
    # Only values below threshold are kept
    for val in temp_buffer:
        if abs(val) <= limit * 1.1:
            cleaned.append(val)
    return cleaned

# Signal classification (distractor)
def classify_signal_strength(data):
    categories = []
    for x in data:
        if x > 5: categories.append('strong')
        elif x > 2: categories.append('moderate')
        elif x > -1: categories.append('weak')
        else: categories.append('critical')
    return categories

# Core processing: integrates multiple concepts
def process_signals(signals, thresh):
    result_stack = []
    magnitude_sum = 0
    
    # Use enumerate and zip: align indices with shifted version
    shifted = [signals[i-2] for i in range(len(signals))]
    for i, (idx_val, sig, shift) in enumerate(zip(enumerate(signals), signals, shifted)):
        index = idx_val[0]
        primary = sig
        offset = shift
        
        # Conditional logic with modular arithmetic
        if index % 4 == 0:
            adjusted = (primary + offset) * 0.5
        elif index % 3 == 0:
            adjusted = primary ** 2 / (offset + 1)
        else:
            adjusted = primary - offset
        
        # Accumulate only every 3rd valid adjusted value
        if i % 3 == 0:
            magnitude_sum += abs(adjusted)
    
    # Composite calculation
    avg_magnitude = magnitude_sum / (len(signals) // 3 + 1)
    
    # Final transformation using modular reduction and rounding
    code_key = int(avg_magnitude * 100) % 89
    normalized = round(avg_magnitude - (code_key * 0.01), 4)
    
    # Critical assignment
    final_value = int((normalized * 10000) % 100000)
    
    # Dead code path: never executed due to structure
    if False:
        fallback = sum(math.tan(x * 0.1) for x in signals)
        final_value = int(fallback) % 1000
    
    return final_value

# Main execution flow
sensor_readings = collect_sensor_data()
dispersion = calculate_variance(sensor_readings)  # Unused but plausible
threshold = 6.5

# Apply actual filter
filtered_data = filter_anomalies(sensor_readings, threshold)

# Unused frequency analysis
# freq_data = transform_frequency_domain(filtered_data)

# Signal classification ignored
# classifications = classify_signal_strength(filtered_data)

# Key statement
final_output = process_signals(filtered_data, threshold)

print(f"Result: {final_output}")