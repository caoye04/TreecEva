def analyze_data_stream(data_stream):
    base_offset = 17
    temp_buffer = []
    running_total = 0
    checksum = 0
    scaling_factor = 1.5
    dummy_accumulator = 0

    for index, (i, val) in enumerate(zip(range(len(data_stream)), data_stream)):
        shifted_index = i << 1
        inverted_val = ~val & 0xFFFF
        scaled_val = val * scaling_factor

        # Irrelevant transformation
        dummy_accumulator += scaled_val ** 0.5

        if val > 100:
            transformed = val // 4
        elif val < 50:
            transformed = val * 3 + base_offset
        else:
            transformed = val + (index % 7)

        temp_buffer.append(transformed)

        # Core logic with key statement
        processed_value = transformed % 256
        if processed_value > 0:
            checksum = (checksum << 1) ^ processed_value if processed_value % 2 else checksum + processed_value

        # Dead code branch (never reached due to structure)
        if False:
            running_total -= val

    final_adjustment = sum(1 for x in temp_buffer if x % 2 == 0)
    checksum = (checksum + final_adjustment) % 100000

    return checksum

# Input data
data_packets = [42, 150, 83, 200, 12, 99]
result = analyze_data_stream(data_packets)
print(f"Result: {result}")