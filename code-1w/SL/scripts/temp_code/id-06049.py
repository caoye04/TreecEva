import math

# Simulated sensor data processing with red herrings and complex transformations
def preprocess_signal(raw_input, threshold=0.75):
    filtered = [x for x in raw_input if abs(x) > threshold]
    shifted = [(x * 1.05) % 4.0 for x in filtered]
    return shifted[::-1]  # Reverse after scaling

# Irrelevant auxiliary function (dead code path)
def deprecated_normalization(vec):
    norm = sum([abs(x) for x in vec])
    return [x / norm for x in vec] if norm else vec

# Core transformation with slicing and arithmetic distortion
def apply_envelope(signal, mode='quadratic'):
    length = len(signal)
    envelope = []
    for i in range(length):
        if mode == 'quadratic':
            factor = (i / length) ** 2
        elif mode == 'exponential':
            factor = math.exp(-i / length)
        else:
            factor = 1.0
        envelope.append(signal[i] * factor + 0.1 * i)
    return envelope[1::2]  # Return every second element starting from index 1

# Misleading intermediate analysis (decoy function)
def compute_entropy(data):
    total = sum([abs(x) for x in data])
    if total == 0:
        return 0.0
    probabilities = [abs(x) / total for x in data]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

# Data masking with bitwise obfuscation (partial use)
def mask_indices(indices, key=13):
    masked = []
    for idx in indices:
        masked.append((idx ^ key) & 15)  # XOR with key then truncate to 4 bits
    return masked

# Main pattern analyzer - this is where the answer originates
def analyze_pattern(seq):
    base_value = 0
    for i, val in enumerate(seq):
        temp = val * 100
        if i % 2 == 0:
            base_value += int(temp) // (i + 1)
        else:
            base_value -= int(temp) % (i + 5)
    
    # Critical branching with non-obvious resolution
    adjustment = 0
    if len(seq) > 3:
        slice_sum = sum(seq[1:4])
        if slice_sum > 5:
            adjustment = int(slice_sum * 10)
        else:
            adjustment = -int(slice_sum ** 2)
    else:
        adjustment = 100
        
    result = base_value + adjustment
    
    # Unused but misleading post-processing
    secondary_metric = result * 0.95 + 17
    outlier_flag = result > 200 and len(seq) % 2 == 1
    
    return result

# Orchestration with distractor variables
if __name__ == '__main__':
    # Initial synthetic signal
    primary_sensor_readings = [0.1, 2.3, 1.8, 3.2, 0.9, 4.1, 2.7]
    
    # Irrelevant secondary stream (distractor)
    auxiliary_stream = [8, 2, 5, 1, 9]
    processed_aux = mask_indices(auxiliary_stream, key=7)
    normalized_aux = deprecated_normalization(processed_aux)

    # Real processing chain
    cleaned = preprocess_signal(primary_sensor_readings, threshold=1.0)
    enhanced = apply_envelope(cleaned, mode='quadratic')
    
    # Decoy analysis
    entropy_score = compute_entropy(enhanced)
    
    # Key computation point
    final_diagnostic = analyze_pattern(enhanced)
    
    # Print required result
    print(f"Result: {final_diagnostic}")