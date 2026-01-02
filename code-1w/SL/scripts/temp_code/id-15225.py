import math

# System calibration and signal processing simulation
def generate_reference_grid(size):
    return [[(i + j) % 7 for j in range(size)] for i in range(size)]

# Irrelevant helper function (dead code path)
def calculate_efficiency(ratio):
    if ratio > 1.0:
        return math.log(ratio) * 100
    else:
        return 0

# Unused transformation matrix
decoymatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Signal encoding with bitwise manipulation
def encode_payload(data_stream, mask_sequence):
    encoded = []
    for i, val in enumerate(data_stream):
        masked = val ^ mask_sequence[i % len(mask_sequence)]  # XOR masking
        shifted = (masked << 1) | (masked >> 7)  # Rotate left by 1 bit
        encoded.append((shifted + i) % 256)
    return encoded

# Decoy function that is never called
def decrypt_layer(signal, key):
    return [s ^ key for s in signal][::-1]

# Real processing logic hidden among distractions
def transform_kernel(matrix, factor):
    size = len(matrix)
    return [
        [(matrix[i][j] * factor + i * j) % 15 for j in range(size)]
        for i in range(size)
    ]

# Another irrelevant utility
def validate_checksum(stream):
    total = sum(stream)
    return total % 256 == stream[-1]

# Main transformation function
# Combines slicing, enumeration, zip, bitwise ops, list comprehensions
def process_transmission(chunks, calib):
    # Step 1: Extract and slice relevant segments
    primary_chunk = chunks[::2]  # Take every other element
    secondary_chunk = chunks[1::2]  # Remaining elements

    # Step 2: Apply calibration using matrix
    adjustment = 0
    for i, row in enumerate(calib):
        for j, _ in enumerate(row):
            if i % 2 == 0:
                adjustment += calib[i][j] ^ (i + j)  # Bitwise red herring

    # Step 3: Pair indices using enumerate and zip
    indexed_primary = list(enumerate(primary_chunk))
    indexed_secondary = list(enumerate(secondary_chunk[::-1]))  # Reverse one

    combined_values = []
    for (i, p), (j, s) in zip(indexed_primary, indexed_secondary):
        # Complex but deterministic computation
        temp = (p * s) + (i ** 2) - (j * adjustment)
        if temp > 0:
            temp = temp ^ 255  # Bit flip mask
        combined_values.append(abs(temp) % 1000)

    # Step 4: Final reduction with distractor logic
    accumulator = 0
    weights = [0.1, 0.3, 0.4, 0.2]
    for idx, val in enumerate(combined_values):
        noise = math.sin(idx + 0.5) * 10
        adjusted_val = (val + noise) * weights[idx % len(weights)]
        accumulator += adjusted_val

    # Distractor: unused conditional branch
    if accumulator < 0:
        backup = sum(combined_values) // 2
        accumulator = backup  # Never reached due to abs() above

    return int(accumulator)

# --- Simulation Setup ---

data_input = [12, 45, 67, 89, 23, 56, 78, 91, 14, 37]
mask_pattern = [255, 170, 85, 0]  # Alternating XOR pattern (AA, 55 in hex)

calibration_matrix = generate_reference_grid(5)

# Transform calibration matrix through multiple steps
for _ in range(2):
    calibration_matrix = transform_kernel(calibration_matrix, 3)

# Encode the data
encoded_chunks = encode_payload(data_input, mask_pattern)

# Add decoy variables
baseline_offset = 42
scaling_factor = 1.618
ignored_buffer = [0] * 10

# Critical statement
final_signal = process_transmission(encoded_chunks, calibration_matrix)

# Print result as required
print(f"Target result: {final_signal}")