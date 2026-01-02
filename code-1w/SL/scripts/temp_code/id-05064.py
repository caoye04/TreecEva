def preprocess_signal(raw):    
    # Irrelevant scaling (distractor)
    scaled = [x * 0.98 for x in raw if x > 0]
    offset = sum(scaled) / len(scaled) if scaled else 0
    
    # Core transformation (relevant path)
    processed = [(x + offset) % 127 for x in raw]
    return processed


def generate_checksum(sequence):
    # Misleading checksum function (dead code path)
    total = 0
    for val in sequence:
        total = (total + val) * 3 % 97
    return total

def transform_sequence(data, key=3):
    # Bit manipulation red herring
    masked = [d ^ key for d in data]
    shifted = [(d << 1) % 256 for d in masked]  # Unused
    
    # Actual relevant transformation
    modded = [d % 17 for d in data if d % 2 == 1]  # Only odd values mod 17
    extended = modded + [len(modded), sum(modded) % 100]
    return extended

def filter_anomalies(dataset):
    # Complex filtering with decoy logic
    anomalies = []
    for i, val in enumerate(dataset):
        if val == 0 or (val > 10 and val % 5 == 0):
            anomalies.append(i)
    # Return something irrelevant to main logic
    return [x * 2 for x in anomalies]  # Dead end

def analyze_pattern(seq):
    # Core analysis buried in distractions
    
    # Distractor: character counting analogy (misleading)
    ascii_vals = [ord(c) for c in 'diagnostic']
    base_shift = sum(ascii_vals) % 13
    
    # Real computation begins
    if len(seq) < 5:
        return -1
    
    # Extract key components
    length_marker = seq[-2]
    sum_remainder = seq[-1]
    body = seq[:-2]
    
    # Conditional data flow
    if length_marker > 10:
        core_sum = sum(body)
    else:
        core_sum = sum(b * (i+1) for i, b in enumerate(body))  # Weighted sum
    
    # Final computation
    result = (core_sum + sum_remainder * 100) - (length_marker ** 2)
    return result

# Main execution with multiple diversions
raw_input = [42, 15, 28, 17, 89, 34, 53]

# Irrelevant preprocessing chain
processed_signal = preprocess_signal(raw_input)
dummy_checksum = generate_checksum(processed_signal)
anomaly_indices = filter_anomalies(processed_signal)

# Key data transformation (buried)
transformed_data = transform_sequence(raw_input, key=5)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data)

# Output the target result
print(f"Result: {final_diagnostic}")