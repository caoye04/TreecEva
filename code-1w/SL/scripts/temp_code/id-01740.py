import math

# Simulated sensor data processing with embedded logic chain
def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 6) for x in filtered]
    return normalized

# Irrelevant helper: computes statistical dispersion (not used in final path)
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Data transformation core function
def apply_window(signal, window_size=5):
    padded = [0] * (window_size // 2) + signal + [0] * (window_size // 2)
    smoothed = []
    for i in range(len(signal)):
        window = padded[i:i + window_size]
        avg = sum(window) / window_size
        smoothed.append(round(avg, 6))
    return smoothed

# Bit manipulation layer for checksum simulation
def generate_checksum(sequence):
    checksum = 0
    for val in sequence:
        scaled = int(abs(val) * 1000) % 256
        checksum ^= scaled  # Use XOR to accumulate
    return checksum & 0xFF

# Main pattern analyzer with conditional branching and slicing
def analyze_pattern(seq, reference):
    # Slice middle portion for analysis
    mid_start = len(seq) // 4
    mid_end = 3 * len(seq) // 4
    segment = seq[mid_start:mid_end]
    
    # Compute moving product of pairs (relevant for result)
    product_chain = 1
    for i in range(0, len(segment) - 1, 2):
        paired_mul = segment[i] * segment[i + 1]
        product_chain *= int(abs(paired_mul * 100)) + 1
    
    # Logical gate array simulation (distractor)
    gates = [True, False, True]
    for _ in range(3):
        gates = [gates[i] ^ gates[(i+1)%3] for i in range(3)]  # XOR cascade
    
    # Red herring computation: harmonic mean (unused)
    if len(segment) >= 2:
        harmonic_mean = len(segment) / sum(1/(x + 1e-6) for x in segment)
    else:
        harmonic_mean = 0
    
    # Control flow with nested conditions (partially dead code)
    threshold = 0.5
    activation = 0
    if len(reference) > 4:
        if sum(reference) % 2 == 0:
            activation += 100
        else:
            temp_ref = reference[1:-1]  # Slicing
            activation += sum(temp_ref) // len(temp_ref)
    else:
        activation += 50  # Dead branch due to input size
    
    # Key dependency: combine product chain and checksum
    magic_offset = generate_checksum(seq)
    result = (product_chain % 97) + magic_offset + activation
    
    # Decoy list operations
    decoy_list = [result, result ^ 255, ~result, result << 2]
    decoy_aggregate = sum(decoy_list[:2]) - decoy_list[3]
    
    # Final diagnostic depends on non-obvious combination
    final_diagnostic = result  # This is the actual output
    return final_diagnostic

# Orchestration function
def main_pipeline():
    # Raw sensor readings (simulated)
    raw_data = [0.12, -0.45, 0.67, 0.89, -0.23, 0.33, 0.71, -0.64, 0.52, 0.83]
    
    # Unused alternate dataset (distraction)
    alt_stream = [0.91, 0.11, 0.76, 0.29, 0.44]
    
    # Preprocess and transform
    cleaned = preprocess_signal(raw_data)
    processed = apply_window(cleaned, window_size=3)
    
    # Generate key sequence using slice and transform
    key_sequence = [int(x * 10) for x in processed[::2]]  # Every other element
    
    # Transform for analysis
    transformed_data = [math.sin(x * math.pi) for x in processed]
    
    # Misleading intermediate check (prints but doesn't affect result)
    validity_check = all(-1 <= x <= 1 for x in transformed_data)
    debug_status = f"Signal valid: {validity_check}, Length: {len(transformed_data)}"
    print(debug_status)  # Distractor output
    
    # Critical execution point
    final_diagnostic = analyze_pattern(transformed_data, key_sequence)
    
    # Output required for evaluation
    print(f"Result: {final_diagnostic}")

# Execute
main_pipeline()