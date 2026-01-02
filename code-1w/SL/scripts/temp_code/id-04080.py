from itertools import cycle

# Simulated data stream processing with red herrings and distractions
def process_signal_stream():
    raw_samples = [173, 204, 95, 138, 241, 88, 67, 152]
    calibration_sequence = [3, 7, 2, 5]
    temporal_weights = [0.8, 1.2, 0.9, 1.1]
    
    # Irrelevant transformations (dead computations)
    weighted_avg = sum(raw_samples) / len(raw_samples) * 1.05
    peak_deviation = max(raw_samples) - min(raw_samples)
    entropy_approx = len(set(bin(x) for x in raw_samples))

    # Distractor: unused signal smoothing
    smoothed = []
    for i in range(len(raw_samples)):
        window = raw_samples[max(0, i-1):min(i+2, len(raw_samples))]
        smoothed.append(sum(window) / len(window))

    # Key initialization
    base_value = 0
    modulus = 9871  # Large prime for checksum
    shift_register = 5

    # Misleading block: complex but unused transformation chain
    def decoy_transform(data):
        acc = 0
        for d in data:
            acc = (acc * 31 + d) % 65537
            acc ^= (acc << 5) & 0xFFFF
        return acc
    
    unused_hash = decoy_transform(raw_samples)  # Dead end

    # Real logic begins: interweave two sequences with slicing
    paired = list(zip(raw_samples[::2], raw_samples[1::2]))  # Slice into pairs
    iterator = cycle(calibration_sequence)

    # Complex state evolution with distractors
    temp_buffer = []
    for idx, (a, b) in enumerate(paired):
        # Distractor computation
        magnitude = (a ** 2 + b ** 2) ** 0.5
        phase = abs(a - b) * next(iterator)
        
        # Red herring: intermediate diagnostic
        if magnitude > 200:
            diagnostic_flag = True
            # This path does nothing useful
            temp_buffer.extend([int(magnitude % 100), phase % 25])

        # Relevant transformation (obscured)
        combined = (a + b) * calibration_sequence[idx % 4]
        shifted = combined << 1
        masked = shifted & 0xFF  # Keep lower 8 bits

        # Another decoy operation
        _ = (masked * 7) % 1000  # Unused

        # Critical path hidden among noise
        if idx % 2 == 0:
            base_value += masked
        else:
            base_value -= (masked >> 2)

    # Introduce modular arithmetic and bit manipulation
    base_value = abs(base_value) % modulus

    # String-based distraction
    status_code = "ERR_0" if base_value < 100 else "OK_1"
    code_points = [ord(c) % 32 for c in status_code if c.isdigit()]

    # Bitwise obfuscation layer
    rotation_key = sum(code_points) or 1
    rotated = ((base_value << rotation_key) | (base_value >> (32 - rotation_key))) & 0xFFFFFFFF

    # Final transformation with key variables
    transformed = 0
    for i, w in enumerate(temporal_weights):
        # This loop appears meaningful but only last iteration matters
        scaled = int(w * (calibration_sequence[i] ** 2))
        transformed = (transformed ^ scaled) % 1000
    
    # CORE COMPUTATION — critical statement
    checksum = (base_value ^ transformed) % modulus

    # Dead output branch
    if checksum % 2 == 0:
        parity_status = "EVEN_SHADOW"
    else:
        parity_status = "ODD_GHOST"

    # Only this print matters
    print(f"Result: {checksum}")

process_signal_stream()