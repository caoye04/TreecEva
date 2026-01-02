import math

# Simulated sensor data processing with embedded logic chain
def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [val / max(filtered) for val in filtered]
    return normalized

# Irrelevant helper - distractor function
def smooth_data(data):
    smoothed = []
    for i in range(len(data)):
        neighbors = data[max(0, i-1):min(i+2, len(data))]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed  # Never used

# Data transformation with conditional logic
def transform_readings(signal):
    processed = []
    for val in signal:
        if val < 0:
            processed.append(abs(val) ** 0.5)
        else:
            processed.append(math.log(val + 1))
    # Misleading intermediate
    temp_sum = sum([x * 2 for x in processed if x > 1])
    adjustment = len(processed) % 7
    return [p + 0.1 for p in processed]  # Adds constant offset

# Pattern analyzer core logic
def count_peaks(series, sensitivity=0.3):
    if len(series) < 3:
        return 0
    peaks = 0
    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1] and series[i] > sensitivity:
            peaks += 1
    return peaks

# Decoy analysis function (never called)
def detect_outliers(data, limit=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val)**2 for x in data) / len(data)) ** 0.5
    return [i for i, x in enumerate(data) if abs(x - mean_val) > limit * std_dev]

# Main diagnostic engine
def analyze_pattern(data_stream, cutoff):
    # Step 1: Filter values above threshold
    significant = [x for x in data_stream if x >= cutoff]
    
    # Step 2: Compute rolling parity (bit manipulation red herring)
    parities = []
    for num in significant:
        bin_rep = bin(int(num * 100))[2:]
        parity = bin_rep.count('1') % 2
        parities.append(parity)
    
    # Step 3: Generate checksum (unused distraction)
    checksum = 0
    for i, p in enumerate(parities):
        checksum ^= (i + 1) * p
    
    # Step 4: Actual logic - count high-magnitude transitions
    transitions = 0
    for i in range(1, len(significant)):
        if abs(significant[i] - significant[i-1]) > 0.4:
            transitions += 1
    
    # Step 5: Apply nonlinear gain
    gain_factor = 3.7 if transitions > 2 else 2.1
    base_score = transitions * gain_factor
    
    # Step 6: Inject conditional offset using ternary
    offset = 10 if len(significant) >= 4 else 5
    
    # Step 7: Incorporate peak count from earlier logic
    peak_contribution = count_peaks(data_stream, sensitivity=0.25) * 1.8
    
    # Final computation
    result = base_score + offset + peak_contribution
    
    # Dead code branch - misleading final check
    if result > 20 and len(parities) % 2 == 0:
        result *= 0.9  # Not triggered in this case
        
    return result

# --- Execution Flow ---
raw_sensor_data = [0.05, -0.3, 0.7, 0.15, -0.8, 0.9, 0.2, 0.65]

# Preprocess the signal
filtered_signal = preprocess_signal(raw_sensor_data)

# Transform readings (core data modification)
transformed_data = transform_readings(filtered_signal)

# Unused alternate path - dead end
if len(transformed_data) > 10:
    transformed_data = smooth_data(transformed_data)

# Threshold for pattern analysis
threshold = 0.35

# Critical statement: compute final diagnostic score
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")