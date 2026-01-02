def analyze_data_stream(raw_bytes, threshold_multiplier=1.75):
    # Simulate sensor data validation and transformation pipeline
    if len(raw_bytes) < 5:
        return -1

    # Irrelevant statistical summaries (distractors)
    avg_val = sum(raw_bytes) / len(raw_bytes)
    variance_proxy = sum((x - avg_val) ** 2 for x in raw_bytes) / len(raw_bytes)
    outlier_flags = [i for i, x in enumerate(raw_bytes) if x > avg_val + variance_proxy * 0.5]

    # Data segmentation based on dynamic pivot (red herring)
    pivot = raw_bytes[len(raw_bytes) // 2]
    left_segment = raw_bytes[:len(raw_bytes)//2]
    right_segment = raw_bytes[len(raw_bytes)//2:]

    # Decoy processing path (never actually used in final result)
    transformed_right = []
    for val in right_segment:
        temp_x = (val ^ 0xA3) + 7
        if temp_x % 3 == 0:
            transformed_right.append(temp_x // 3)
        elif temp_x % 2 == 0:
            transformed_right.append(temp_x // 2)
        else:
            transformed_right.append(temp_x)

    # Real processing begins: filter and map relevant values
    filtered = [b for b in raw_bytes if b % 2 == 1 and b > 32]
    shifted_values = [v >> 2 for v in filtered]  # Bit manipulation

    # Character-based analysis (irrelevant but plausible)
    ascii_chars = ''.join(chr(b) for b in raw_bytes if 33 <= b <= 126)
    special_count = sum(1 for c in ascii_chars if c in "!@#$%^&*")

    # Core logic hidden among distractions
    base_key = 0
    for i, byte in enumerate(filtered):
        if i % 3 == 0:
            base_key += byte * (i + 1)

    # Secondary processing with slicing distraction
    windowed_sums = [sum(shifted_values[i:i+3]) for i in range(len(shifted_values)-2)]
    peak_window = max(windowed_sums) if windowed_sums else 0

    # Actual critical computation chain
    temp_stack = []
    for sv in shifted_values:
        if sv > 10:
            temp_stack.append(sv ^ 0x55)
        elif sv > 5:
            temp_stack.append(sv + 3)
    processed_count = len(temp_stack)

    # Nested conditional with misleading early exit (dead path)
    if processed_count > 100:
        result_hint = "overflow"
        magnitude = processed_count // 10
        # This branch will never execute due to input constraints
        return -999

    # Critical state variables
    status_map = {1: 'init', 2: 'active', 3: 'locked'}
    mode_flag = 3 if processed_count > 20 else (2 if processed_count > 5 else 1)

    # Final key derivation through multiple steps
    intermediate = base_key & 0xFFFF
    extended = (intermediate << 1) ^ 0x1337
    folded = (extended >> 8) | (extended & 0xFF)
    final_key = folded % 256

    # Checksum calculation - this is the target statement
    checksum = final_key ^ (processed_count & 0xFF)

    # Dead code path with decoy output (never reached in normal execution)
    if False:
        debug_dump = {
            'raw': raw_bytes,
            'filtered': filtered,
            'stack_trace': temp_stack[-5:]
        }
        print(f"Debug: {debug_dump}")

    print(f"Result: {checksum}")

# Hidden input encoding (avoiding hardcoded literals)
encoded_seed = [ord(c) for c in "sensor_v4"] + [202, 138, 177, 156, 199, 131, 188, 142]
scrambled = [(encoded_seed[i] ^ (i * 7)) % 256 for i in range(len(encoded_seed))]
rotated = scrambled[3:] + scrambled[:3]
input_stream = [b for b in rotated if b % 2 == 0] + [64, 36, 88]

# Execute main logic
analyze_data_stream(input_stream)