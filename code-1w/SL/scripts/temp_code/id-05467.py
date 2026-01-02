import math

# Simulated sensor data processing with red herrings and complex transformations
def preprocess_sensor_array(raw_signal):
    filtered = [x for x in raw_signal if x > 0.1]
    normalized = [val / max(filtered) for val in filtered]
    return normalized

# Irrelevant audio-specific function (decoy)
def compute_spectral_entropy(signal):
    return sum([math.log(x + 1e-5) for x in signal])

# Data augmentation via window slicing (relevant)
def create_overlapping_windows(data, size=4, step=2):
    windows = []
    for i in range(0, len(data) - size + 1, step):
        windows.append(data[i:i+size])
    return windows

# Misleading compression function (dead code path)
def compress_via_huffman(seq):
    freq_map = {item: seq.count(item) for item in set(seq)}
    return sum(len(str(freq)) for freq in freq_map.values())

# Core transformation: bit manipulation meets sequence analysis
def apply_phase_shift(values):
    shifted = []
    for v in values:
        # Convert float to int representation for bitwise op
        as_int = int(v * 1000)
        rotated = ((as_int << 5) & 0xFF) | (as_int >> 3)  # 8-bit rotate
        shifted.append(rotated / 1000.0)
    return shifted

# Auxiliary checksum (irrelevant)
def calculate_adler32(chunk):
    a = b = 0
    for byte in ''.join(f'{c:.3f}' for c in chunk).encode():
        a = (a + byte) % 65521
        b = (b + a) % 65521
    return (b << 16) | a

# Real pattern analyzer (key function)
def analyze_pattern(dataset):
    total = 0
    for seq in dataset:
        if len(seq) >= 3:
            # Extract middle elements using slicing
            mid_section = seq[1:-1]
            for val in mid_section:
                # Apply non-linear transformation
                total += math.sin(val) ** 2
    return int(total * 1000)

# Fake entropy-based evaluator (distractor)
def evaluate_complexity(patterns):
    flat = [item for sublist in patterns for item in sublist]
    unique_vals = len(set(round(x, 3) for x in flat))
    return unique_vals > 15

# Main execution flow
if __name__ == '__main__':
    # Initial synthetic data
    base_readings = [0.12, 0.81, 0.45, 0.93, 0.11, 0.76, 0.63, 0.28]

    # Step 1: Filter and normalize (relevant)
    cleaned = preprocess_sensor_array(base_readings)

    # Step 2: Apply bit-level phase shift (relevant)
    perturbed = apply_phase_shift(cleaned)

    # Step 3: Create temporal windows using slicing (key step)
    windowed_data = create_overlapping_windows(perturbed, size=4, step=1)

    # Step 4: Compute useless metrics (distractors)
    spectral_score = compute_spectral_entropy(perturbed)
    adler_checksum = calculate_adler32(windowed_data[0])
    compression_metric = compress_via_huffman([int(x*100) for x in perturbed])

    # Step 5: Transform data structure again (relevant)
    flipped_axes = [row[::-1] for row in windowed_data]  # reverse each window

    # Step 6: Analyze original windows, not flipped ones (critical detail)
    final_diagnostic = analyze_pattern(windowed_data)

    # Print irrelevant info to distract
    debug_info = {
        'raw_count': len(base_readings),
        'windows_generated': len(windowed_data),
        'spectral': spectral_score,
        'adler': adler_checksum,
        'compression_idx': compression_metric
    }
    
    # Only this line matters
    print(f"Result: {final_diagnostic}")