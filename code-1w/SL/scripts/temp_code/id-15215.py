def analyze_signal_packet(raw_payload):
    # Irrelevant decoding attempt of signal header
    header = raw_payload[:4]
    magic_number = int.from_bytes(header, 'big')
    if magic_number < 1000:
        return -1  # Early exit red herring

    # Distractor: Parse unused metadata
    metadata = raw_payload[4:12]
    timestamp = int.from_bytes(metadata[:8], 'little')
    channel_id = metadata[8] | 0x20

    # Real data processing starts here
    data_segment = raw_payload[12:28]
    data_values = [data_segment[i] for i in range(0, len(data_segment), 2)]

    # Decoy accumulation with misleading sum
    decoy_sum = 0
    for x in data_segment:
        decoy_sum += x * 0x10
    decoy_sum = decoy_sum % 997

    # Actual relevant computation chain
    data_sum = sum(d for d in data_values if d % 2 == 1)  # Only odd bytes contribute

    # Bit manipulation red herring
    shifted_entropy = 0
    for i, val in enumerate(data_values):
        shifted_entropy ^= val << (i % 4)
    shifted_entropy &= 0xFFFFFFFF

    # Conditional adjustment based on string inspection (using string method)
    payload_str = raw_payload.hex()
    flag_marker = 'aabbccdd'
    if payload_str.endswith(flag_marker) or payload_str.count('dead') > 1:
        adjustment = 0xABC
    else:
        adjustment = 0xDEF

    # Key execution point — target variable assignment
    checksum = (data_sum ^ adjustment) & 0xFFFF

    # Dead code path: unreachable due to logic
    if len(data_values) < 0:  # Impossible condition
        backup = sum(data_values)
        checksum = (backup + 555) & 0xFFFF

    # Additional distractor: unused tuple unpacking
    stats = (decoy_sum, shifted_entropy, channel_id, timestamp)
    _, _, _, _ = stats  # Unpack and ignore

    # Final output
    print(f"Result: {checksum}")

# Simulated payload with deterministic content
payload = bytes.fromhex(
    '1a2b3c4d'           # header (magic=0x1a2b3c4d > 1000, so continue)
    '0102030405060708'   # metadata (timestamp = 0x0807060504030201, little-endian)
    '04'                 # channel_id = 0x04 | 0x20 => 0x24
    'f0f1f2f3f4f5f6f7'   # data_segment (every 2nd byte starting at 0: f0,f2,f4,f6)
)
analyze_signal_packet(payload)
