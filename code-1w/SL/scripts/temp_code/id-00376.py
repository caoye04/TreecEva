import itertools

# Simulated sensor data packet with metadata
data_packet = [102, 205, 193, 44, 150, 78, 241, 93]
metadata = {'version': 2, 'length': len(data_packet), 'mode': 'encrypted'}

# Protocol configuration constants
FRAME_HEADER = 0xAB
FRAME_FOOTER = 0xCD
KEY_SEGMENT = 255
MASK_OFFSET = 170

# Initialize state variables for decoding process
frame_valid = False
running_sum = 0
temp_value = 0
diagnostic_log = []
redundant_buffer = [0] * 8
bit_flip_counter = 0
epoch_timestamp = 1712345678
sync_trail = []

# Precompute auxiliary values (some irrelevant)
expansion_table = [i ** 2 % 256 for i in range(16)]
lookup_seed = sum(expansion_table) // 16
twist_factor = (lookup_seed ^ KEY_SEGMENT) % 100

# Begin frame validation and checksum computation
if data_packet[0] + data_packet[-1] == FRAME_HEADER ^ FRAME_FOOTER:
    frame_valid = True

if frame_valid:
    # Primary processing loop with distractions
    for i, byte in enumerate(data_packet):
        shifted = byte >> (i % 4)
        wrapped = (byte + i * 3) % 256
        
        # Update running sum with bit-manipulated value
        running_sum += (shifted ^ MASK_OFFSET) & 0xFF
        
        # Compute intermediate temp value using cyclic lookup
        cycle_index = i % len(expansion_table)
        temp_value = expansion_table[cycle_index] ^ byte
        
        # Update redundant buffer (not used in final result)
        redundant_buffer[i] = (wrapped << 1) % 256
        
        # Conditional red herring: affects diagnostic only
        if byte > 150:
            bit_flip_counter += 1
            sync_trail.append(i)
        
        # Key statement — compute masked XOR checksum fragment
        mask = 0xFF if (i + 1) % 4 == 0 else 0x00
        checksum = (running_sum ^ temp_value) & mask
        
        # Log diagnostics (irrelevant to checksum)
        diagnostic_log.append({
            'index': i,
            'shifted_val': shifted,
            'temp_debug': temp_value,
            'valid_frame': frame_valid
        })
        
        # Early exit red herring (never triggers under current data)
        if i > 10:
            break

    # Post-processing: distraction using itertools
    pairs = list(itertools.combinations(data_packet[:4], 2))
    pair_sums = [a + b for a, b in pairs]
    aggregate_score = sum(pair_sums) // len(pair_sums)

    # Secondary checksum (unused distractor)
    validation_token = (aggregate_score ^ twist_factor) & 0xFFFF

# Final output for inspection
Result: {checksum}