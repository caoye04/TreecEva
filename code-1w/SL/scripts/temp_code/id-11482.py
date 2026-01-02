def process_segment(data, key_offset):
    temp = 0
    for i in range(len(data)):
        if i % 2 == 0:
            temp ^= (data[i] + key_offset) << 1
        else:
            temp += (data[i] ^ key_offset) >> 1
    return temp & 0xFFFF

def validate_sequence(seq):
    return sum(seq) % 256 == seq[-1]

def decode_frame(payload):
    segment_a = payload[1:5]
    segment_b = payload[7:11]
    decoy_sum = sum(payload) * 2  # Irrelevant computation
    offset_x = payload[0] | 17
    offset_y = payload[5] & 7
    result_a = process_segment(segment_a, offset_x)
    result_b = process_segment(segment_b, offset_y)
    mixed = ((result_a << 4) | (result_b >> 4)) & 0xFFFFFF
    flag_check = mixed % 3 == 0
    unused_flag = flag_check and (len(payload) > 10)
    return mixed

def finalize(buffer, mode):
    if mode == 'fast':
        return buffer ^ 0xAAAA
    elif mode == 'secure':
        acc = 0
        for b in buffer:
            acc = (acc * 31 + b) % 1000003
        return acc
    else:
        base = buffer & 0xFFFF
        shift = (buffer >> 16) & 0xFF
        return (base ^ (shift * 13)) % 50000

def main():
    raw_stream = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 22]
    valid = validate_sequence(raw_stream)
    
    # Dead code path — never executed due to condition
    debug_mode = False
    if debug_mode:
        print("Debug:", raw_stream)
        extra_analysis = [x ** 2 for x in raw_stream]

    frame_data = decode_frame(raw_stream)
    mode_flag = 'normal'
    if frame_data > 100000:
        mode_flag = 'secure'
    elif frame_data < 50000:
        mode_flag = 'fast'
    
    temp_buffer = frame_data + 12345
    
    # Multiple irrelevant transformations
    shadow_copy = temp_buffer ^ 0xFF
    inverted = ~temp_buffer & 0xFFFFFFFF
    scaled_test = temp_buffer * 1.5  # Unused float
    
    checksum = finalize(temp_buffer, mode_flag)
    
    # Final red herring: complex-looking but unused bitwise chain
    decoy_final = ((temp_buffer + checksum) ^ 0xDEADBEEF) % 987654
    
    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()