def analyze_sequence(data_stream):
    # Simulate sensor data validation with embedded integrity check
    valid_packets = []
    temp_buffer = []
    byte_count = 0
    total_energy = 0.0
    entropy_accum = 0

    for i in range(len(data_stream)):
        if data_stream[i] % 17 == 0:  # rare condition for valid packet start
            temp_buffer.append(i)

        if len(temp_buffer) > 0 and i - temp_buffer[-1] > 10:
            valid_packets.extend(data_stream[temp_buffer[-1]:i])
            temp_buffer.pop()

    # Extract core payload using slicing based on first and last valid indices
    if len(valid_packets) < 10:
        valid_packets = [x for x in data_stream if x % 3 == 2]
    
    core_payload = valid_packets[::2]  # take every second element to reduce noise

    # Compute length-based sum (relevant)
    length_sum = len(core_payload) * 7

    # Misleading energy calculation (distractor)
    for val in core_payload:
        total_energy += (val ** 0.5) / 2.3
        byte_count += 1

    # Entropy-like metric using XOR (semi-relevant preprocessing)
    entropy_accum = 0
    for j, val in enumerate(core_payload):
        entropy_accum ^= (val + j) & 255

    # Secondary filtering creates another distractor buffer
    filtered_set = [x for x in core_payload if x & 1]  # odd values only
    sum_filtered = sum(filtered_set[:10])  # partial sum, not used later

    # Checksum components
    base_xor = 0
    for item in core_payload:
        base_xor ^= item

    final_xor = base_xor ^ entropy_accum

    # Key statement
    checksum = final_xor ^ (length_sum & 255)

    # Irrelevant debug logs
    debug_info = f'Debug: processed {byte_count} items, energy={total_energy:.3f}'
    log_entry = {'status': 'OK', 'checksum': checksum}

    # Output target result
    print(f"Result: {checksum}")

# Generate deterministic input
import hashlib
seed_input = "sensor_cal_2024"
hex_digest = hashlib.md5(seed_input.encode()).hexdigest()
data_stream = [int(hex_digest[i:i+2], 16) for i in range(0, len(hex_digest), 2)]

analyze_sequence(data_stream)