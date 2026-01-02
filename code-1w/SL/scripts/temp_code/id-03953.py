import itertools

# Simulated sensor data stream with metadata headers and noise
def generate_signal_packets():
    base_data = [23, 45, 67, 89, 12, 34, 56, 78]
    noise_floor = 5
    packets = []
    for i, val in enumerate(base_data):
        header = (i << 10) | 0x1F  # Metadata: packet ID + type flag
        corrupted_val = val + ((i * 17) % noise_floor)  # Add minor noise
        parity = bin(corrupted_val).count('1') % 2
        packets.append({'hdr': header, 'val': corrupted_val, 'par': parity})
    return packets

# Legacy validation function (not used in current logic)
def validate_with_crc(data_list):
    crc = 0
    for x in data_list:
        crc ^= x << 1
        crc = crc % 65536
    return crc

# Unused helper for alternate encoding
def encode_twos_complement(n, bits=16):
    return (1 << bits) + n if n < 0 else n

# Main signal decoder with embedded checksum algorithm
signal_packets = generate_signal_packets()
raw_values = []
sequence_log = []

# Irrelevant pre-processing: extract headers for unused analysis
header_analysis = [p['hdr'] & 0x3FF for p in signal_packets if p['hdr'] > 0]
header_sum = sum(header_analysis) // len(header_analysis) if header_analysis else 0

# Simulate buffer alignment (distractor)
buffer_offset = 0
for _ in range(3):
    buffer_offset = (buffer_offset + 11) % 7

# Primary data extraction with decoy operations
for packet in signal_packets:
    raw_val = packet['val']
    
    # Apply gain correction (neutral factor - red herring)
    adjusted_val = raw_val * 1.0
    
    # Normalize parity (unused intermediate)
    normalized_parity = float(packet['par']) * 0.5
    
    # Accumulate raw values
    raw_values.append(int(adjusted_val))
    sequence_log.append((len(sequence_log), raw_val))

# Secondary transformation: apply windowing function (partially irrelevant)
windowed_values = []
hanning_window = [0.5 - 0.5 * (1 - (i / (len(raw_values)-1)))**2 for i in range(len(raw_values))] if len(raw_values) > 1 else [1.0]

for i, val in enumerate(raw_values):
    windowed_values.append(int(val * hanning_window[i]))

# Checksum calculation using bit manipulation (TARGET LOGIC)
checksum = 0xACE1  # Initial seed
processing_mask = 0xFF

# Key loop containing target statement
for idx, wv in enumerate(windowed_values):
    # Complex condition with short-circuit (distractor)
    if idx % 2 == 0 and (wv >> 3) > 10:
        wv = wv ^ 0xAA
    elif wv < 20:
        wv = wv + 17
    else:
        pass  # Dead code branch

    # Decoy transformation chain
    temp_shift = (wv >> 2) | (wv << 6)
    temp_shift &= 0xFF
    inverted = (~temp_shift) & 0xFF
    processed_value = (inverted ^ idx) & 0xFF

    # Critical statement - answer depends on final iteration's execution
    checksum = (checksum << 1) ^ processed_value & 0xFFFF

    # Update with unused rolling statistic
    avg_so_far = sum(windowed_values[:idx+1]) // (idx + 1)

# Spurious post-processing (irrelevant to answer)
final_payload = list(itertools.chain(
    [checksum >> 8, checksum & 0xFF],
    [0]*2,
    windowed_values[::2]
))

# Additional dead-end computation
reconstructed = 0
for b in final_payload[:2]:
    reconstructed = (reconstructed << 8) | b

# Output the required result
Result: checksum