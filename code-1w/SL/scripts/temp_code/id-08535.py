import itertools

def main():
    # Sensor input simulation (real data stream)
    raw_readings = [127, 255, 83, 191, 64]
    calibration_offset = 17
    sample_window = 3

    # Irrelevant signal smoothing (distractor)
    smoothed = [sum(raw_readings[i:i+3]) // 3 for i in range(len(raw_readings) - 2)]
    normalized = [x / max(raw_readings) for x in raw_readings]

    # Key data transformation chain
    adjusted = [(x + calibration_offset) % 256 for x in raw_readings]
    bit_inverted = [255 - x for x in adjusted]  # Invert all bits (8-bit complement)

    # Encoding phase with slicing and conditional logic
    encoded_data = []
    for val in bit_inverted:
        if val > 128:
            encoded_data.append(val // 2)
        else:
            encoded_data.append(val * 3 + 1)

    # Decoy pattern detection (dead path)
    patterns = []
    for i in range(len(encoded_data)):
        if encoded_data[i] % 4 == 0 and i % 2 == 1:
            patterns.append(i)

    # Flag generation with modular arithmetic and comparisons
    flags = []
    for i, v in enumerate(adjusted):
        flag = 0
        flag |= (v % 7 == 0) << 0
        flag |= (v > 200) << 1
        flag |= (bin(v).count('1') % 2 == 1) << 2  # Odd parity
        flags.append(flag)

    # Auxiliary checksum (irrelevant to final result)
    temp_checksum = sum(itertools.islice(encoded_data, 0, None, 2)) * len(flags)

    # Conditional expression based refinement (red herring)
    refined_flags = [f if f != 5 else 0 for f in flags]
    mask_sequence = [f & 0b101 for f in refined_flags]

    # Real processing function (depends only on original flags and encoded_data)
    def process_metrics(data, ctrl_flags):
        total = 0
        for i, val in enumerate(data):
            if i >= len(ctrl_flags):
                break
            f = ctrl_flags[i]
            if f & 1:  # Use modulo condition
                total += val % (i + 2)
            elif f & 2:  # Use division and rounding
                total += int(val / (i + 1))
            else:  # Default case: add digit sum
                digit_sum = sum(int(d) for d in str(val))
                total += digit_sum * (i + 1)
        return total + (len(data) % 5) * (len(ctrl_flags) % 3)

    # Critical statement
    final_diagnostic = process_metrics(encoded_data, flags)

    # Unused diagnostic dump (distractor)
    debug_dump = {"raw": raw_readings, "norm": normalized, "flags_raw": flags,
                  "inverted": bit_inverted, "temp_sum": temp_checksum}

    # Print target result
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main()