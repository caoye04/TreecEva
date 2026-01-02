import itertools

# Simulated sensor data processing with error masking and validation
sensor_packets = [127, 83, 255, 191, 64]
error_flags = [False, True, False, True, False]
processing_keys = [3, 7, 5]
temp_buffer = []
redundant_sum = 0

# Irrelevant accumulator for distraction
aux_accumulator = 0
for i in range(len(sensor_packets)):
    aux_accumulator += sensor_packets[i] * (i + 1)

# Critical state variables
base_value = 100
running_xor = 0
modulus = 97
validation_tally = 0

# Simulate packet-by-packet processing with conditional logic and bit manipulation
for idx, packet in enumerate(sensor_packets):
    # Distractor: complex but unused transformation
    transformed = ((packet << 2) ^ 0xAA) & 0xFF
    if transformed > 100:
        redundant_sum += transformed % 13

    # Real processing path
    if not error_flags[idx]:
        masked = packet ^ processing_keys[idx % len(processing_keys)]
        running_xor ^= masked

        # Secondary distractor: dead logic branch (never executed due to flag pattern)
        if error_flags[idx] and packet < 200:
            temp_buffer.append(packet + 50)

    # Additional interference: spurious bit rotation
    rotated = (packet >> 3) | (packet << 5)
    rotated &= 0xFF

    # Validation tally accumulates only on odd indices (irrelevant to final result)
    if idx % 2 == 1:
        validation_tally += packet & 0x0F

# Unused helper function (dead code)
def compute_legacy_hash(data):
    result = 0
    for x in data:
        result = (result * 31 + x) % 256
    return result

# Use of itertools: generate key combinations (only first affects anything)
combined_keys = list(itertools.combinations(processing_keys, 2))
for k1, k2 in combined_keys:
    base_value = (base_value + (k1 * k2)) % 500  # Only last combination matters slightly

# Final checksum calculation — this is the critical point
checksum = (base_value ^ running_xor) % modulus

# Print required output
print(f"Result: {checksum}")