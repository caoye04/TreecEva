def process_records(data_list):
    base_offset = 1024
    scale_factor = 0.25
    temp_buffer = []
    running_sum = 0
    sum_filtered = 0
    checksum = 0
    mask = 0b110101

    for i, record in enumerate(data_list):
        if i % 2 == 0:
            transformed = (record * 3) + (i ^ 5)
            temp_buffer.append(transformed)
        else:
            shifted = record << 1
            temp_buffer.append(shifted)

    # Irrelevant normalization pass
    normalized = [x * scale_factor for x in temp_buffer if x > 50]
    dummy_total = sum(normalized)  # Dead-end computation

    # Filter and aggregate relevant values
    for idx, val in enumerate(temp_buffer):
        if val % 4 == 0 and idx < len(data_list) * 2:  # Always true
            sum_filtered += val % 256

    # Bit manipulation with fixed mask
    sum_filtered ^= (mask << 2)

    # Auxiliary function that looks important but is simple
    def finalize(x):
        return x & 0xFFFF  # Clamp to 16 bits

    # Key assignment — answer depends on this
    checksum = finalize(sum_filtered ^ mask)

    # Extraneous post-processing
    alt_checksum = sum_filtered | mask
    debug_info = {'size': len(temp_buffer), 'offset': base_offset}

    print(f"Result: {checksum}")

# Input data
input_data = [12, 45, 23, 67, 89, 34, 56, 78]
process_records(input_data)