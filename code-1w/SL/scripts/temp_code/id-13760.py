from itertools import compress, count

# Sensor data processing simulation with noise filtering and integrity checks
def main():
    raw_signals = [240, 17, 58, 221, 93, 142, 77, 195, 64, 111]
    signal_flags = [True, False, True, True, False, True, True, False, True, False]
    
    # Irrelevant transformation: amplitude normalization (unused path)
    normalized = [round(x / 255.0, 3) for x in raw_signals]
    threshold_ref = sum([n for n in normalized if n > 0.5])

    # Decoy function: looks important but unused
    def analyze_pattern(seq):
        return sum((s << (i % 4)) ^ 17 for i, s in enumerate(seq))

    # Real processing begins
    base_offset = 37
    mask = 0xFF  # 8-bit truncation mask
    filtered = list(compress(raw_signals, signal_flags))  # Apply valid signal mask

    # Secondary filter: only signals with high nibble symmetry
    refined = []
    decoy_sum = 0
    for val in filtered:
        hi_nibble = (val >> 4) & 0xF
        lo_nibble = val & 0xF
        if hi_nibble ^ lo_nibble == 0x7:  # XOR balance condition
            refined.append(val)
        else:
            # Dead branch: accumulates but unused
            temp_adj = (val + base_offset) ^ 0x55
            decoy_sum += temp_adj % 19

    # Checksum seed derived from control sequence
    control_stream = count(100, 7)
    seed_vals = [next(control_stream) for _ in range(len(raw_signals))]
    entropy = sum(v % k for v, k in zip(seed_vals, [3,5,7,11,13,17,19,23,29,31]))

    # Core logic: sum refined signals with offset
    sum_filtered = sum(refined) + (base_offset & 0x1F)

    # Bit manipulation chain: obfuscate intent
    temp_state = ((sum_filtered << 3) & 0xFFFF) ^ 0xAA55
    temp_state = ((temp_state >> 4) | (temp_state << 12)) & 0xFFFF  # Rotate right 4

    # Finalization function with red herring parameters
    def finalize(value):
        # Unused complexity
        prime_weights = [11, 13, 17, 19, 23]
        weighted = sum((value * p) % 101 for p in prime_weights)
        # Actual computation
        return (value ^ 0x5A) & mask
    
    checksum = finalize(sum_filtered & mask)
    
    # Multiple print statements to distract
    debug_mode = False
    if debug_mode:
        print(f'Debug: {decoy_sum=}, {entropy=}, {temp_state=}')
    
    # Critical output
    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()