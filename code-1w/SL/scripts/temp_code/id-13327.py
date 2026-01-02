def preprocess_signal(raw_samples):
    # Irrelevant transformation (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    return [int(x * 100) for x in filtered]


def compress_data(sequence):
    # Real computation path uses this, but obscured by other functions
    base = sum(sequence) % 256
    shifted = [(x ^ base) % 100 for x in sequence]
    return [s for s in shifted if s % 2 == 0]  # Only even values retained


def validate_checksum(chunk):
    # Dead function – never called, distractor
    return sum(chunk) % 17 == 0


def auxiliary_diagnose(signal):
    # Misleading analysis – looks important but unused
    count = 0
    for val in signal:
        if val > 50:
            count += 1
    return count * 2


def analyze_signal(data, limit):
    # Core logic hidden among distractions
    temp = 0
    for i in range(len(data)):
        if i % 3 == 0:
            temp += data[i] * 2
        elif i % 4 == 0:  # Note: unreachable due to prior condition
            temp += data[i]
        else:
            temp -= data[i]
    
    # Secondary manipulation
    adjustment = len(data) // 2
    temp = abs(temp - adjustment)
    
    # Final nonlinear transformation
    if temp > limit:
        temp = (temp // limit) * 3
    else:
        temp = temp + (limit // temp) if temp != 0 else limit
    
    return temp

# Simulated sensor input (real source)
raw_sensor_input = [15, 23, 88, 17, 42, 91, 64, 12, 53]

# Irrelevant pre-processing chain
processed = preprocess_signal(raw_sensor_input)

# Key data used in actual computation
compressed_data = compress_data(processed)

# Red herring variables
checksum_valid = True  # Never actually computed
diagnostic_flag = auxiliary_diagnose(processed)
threshold = len(processed) * 2  # Used in final call

# Unused intermediate results
aggregated = sum(compressed_data) / len(compressed_data) if compressed_data else 0
weight_factor = round(aggregated, 2)

# Actual critical execution point
final_diagnostic = analyze_signal(compressed_data, threshold)

# Print required result
print(f"Result: {final_diagnostic}")