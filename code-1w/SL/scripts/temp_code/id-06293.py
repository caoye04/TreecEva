import itertools

# System telemetry simulation for a distributed sensor array
sensor_ids = [101, 102, 103, 104]
timestamps = [1623456000, 1623456060, 1623456120, 1623456180]
raw_readings = [18.3, -999.0, 19.1, 18.9, 17.8, 18.0, 19.5, -999.0, 18.4, 18.7]

def validate_checksum(data_chunk):
    # Simulated checksum validation (irrelevant to final result)
    weighted_sum = sum(d * (i + 1) for i, d in enumerate(data_chunk))
    return int(weighted_sum % 256)

def generate_combinations(elements):
    # Distractor: generates unused combinations
    combs = []
    for r in range(1, len(elements)+1):
        combs.extend(itertools.combinations(elements, r))
    return combs  # Never used

def filter_anomalies(readings):
    cleaned = []
    for val in readings:
        if val != -999.0:  # Placeholder for missing data
            cleaned.append(val)
    return cleaned

def compute_rolling_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        averages.append(round(avg, 2))
    return averages

def derive_phase_shift(ts_list):
    # Irrelevant time-delta transformation
    deltas = [ts_list[i+1] - ts_list[i] for i in range(len(ts_list)-1)]
    phase = sum(deltas) * 0.001
    return round(phase, 4)

def extract_signature(anomalies):
    # Create a numeric signature from anomaly indices
    sig = 0
    for i, val in enumerate(anomalies):
        sig += (i + 1) * int(val * 2)
    return sig

def reduce_signature(signature):
    # Apply modular arithmetic and bit manipulation
    temp = (signature ^ 0x1F) % 1000
    temp = (temp + 37) * 2
    temp = temp & 0xFFFF  # Keep within 16 bits
    return temp

def analyze_fault_pattern(reduced_sig):
    # Final computation using integer division and conditional logic
    a = reduced_sig // 7
    b = reduced_sig % 13
    c = (a ^ b) * 3
    d = (c + 987) // 5
    e = d - (reduced_sig // 20)
    return e

# Main execution flow
filtered_data = filter_anomalies(raw_readings)

# Dead code path — collected but unused
combinations = generate_combinations(sensor_ids)

# Compute rolling stats (distractor)
average_window = compute_rolling_average(filtered_data)

# Derive temporal phase (irrelevant)
time_phase = derive_phase_shift(timestamps)

# Checksum on raw subset (misleading intermediate)
subset_checksum = validate_checksum(raw_readings[:5])

# Build diagnostic signature
anomaly_indices = [i for i, x in enumerate(raw_readings) if x == -999.0]
signature = extract_signature([filtered_data[-1], filtered_data[0]])

# Transform signature
reduced_signature = reduce_signature(signature)

# Final analysis
final_diagnostic = analyze_fault_pattern(reduced_signature)

# Output target result
print(f"Result: {final_diagnostic}")