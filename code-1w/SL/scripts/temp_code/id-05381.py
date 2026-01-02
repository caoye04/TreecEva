import itertools

def main():
    # System initialization parameters (many are distractions)
    calibration_sequence = [0.1, 0.3, 0.5, 0.7, 0.9]
    system_mode = 'diagnostic'
    debug_flag = False
    max_iterations = 500
    tolerance = 1e-6

    # Irrelevant sensor arrays (distractors)
    temp_readings = [22.1, 22.3, 21.9, 22.5, 23.0, 22.8]
    pressure_log = [(101.3, 'kPa'), (102.1, 'kPa'), (99.7, 'kPa')]
    unused_cache = {i: i**3 for i in range(15)}

    # Core signal data (relevant)
    raw_samples = [
        [1, 0, 1, 1],
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 1]
    ]

    # Signal preprocessing with red herrings
    processed = []
    shift_offset = 0
    for idx, sample in enumerate(raw_samples):
        shifted = [(bit << 1) & 2 for bit in sample]  # Distraction: not used later
        inverted = [1 - bit for bit in sample]
        combined = [a & b for a, b in zip(sample, inverted)]  # Always zero
        if idx % 2 == 0:
            processed.append([b * 2 for b in sample])  # Double even-indexed rows
        else:
            processed.append(sample[:])  # Keep odd as-is

    # Build signal buffer using enumerate and transformation (relevant path)
    signal_buffer = []
    for i, row in enumerate(processed):
        val = 0
        for j, bit in enumerate(row):
            val += bit * (2 ** (3 - j))
        signal_buffer.append(val)

    # Threshold map setup (relevant)
    levels = ['low', 'medium', 'high', 'critical']
    base_thresholds = [5, 10, 15]
    threshold_map = {level: thr for level, thr in zip(levels, base_thresholds + [float('inf')])}

    # Decoy statistical analysis (dead code path)
    if system_mode == 'production':
        avg_temp = sum(temp_readings) / len(temp_readings)
        variance = sum((t - avg_temp) ** 2 for t in temp_readings)
    elif debug_flag:
        print("Debug mode active - skipping calibration")

    # Unused recursive function (decoy)
    def calculate_entropy(data, depth=0):
        if depth > 5 or len(data) == 0:
            return 0.0
        split = len(data) // 2
        left = data[:split]
        right = data[split:]
        return 0.5 * calculate_entropy(left, depth + 1) + 0.1 * len(right)

    entropy_score = calculate_entropy(calibration_sequence)  # Computed but unused

    # Real computation begins: pattern analyzer
    def analyze_pattern(signal, thresholds):
        count_high = 0
        cumulative_xor = 0
        segment_peaks = []

        # Complex nested logic with distractors
        for i, val in enumerate(signal):
            # Distractor: parity check with no effect
            parity = bin(val).count('1') % 2
            temp_flag = (val & 6) == 4

            # Actual logic: count values above medium threshold
            if val > thresholds['medium']:
                count_high += 1
                segment_peaks.append(val)

            # Critical XOR accumulation across all values
            cumulative_xor ^= val

            # Dead branch: never executed due to fixed condition
            if i > len(signal) * 10:
                reset_counter = True
                break

        # Secondary transformation on peaks
        adjusted_peaks = []
        for p in segment_peaks:
            bits = [int(b) for b in bin(p)[2:].zfill(4)]
            flipped = [1 - b for b in bits]
            new_val = sum(flipped[j] * (2 ** (3 - j)) for j in range(4))
            adjusted_peaks.append(new_val)

        # Final diagnostic computed from multiple sources
        peak_sum = sum(adjusted_peaks)
        base_metric = count_high * 100
        xor_contribution = cumulative_xor * 5
        peak_contribution = peak_sum * 2

        # One more decoy calculation
        combinatorial_weight = 0
        for r in range(1, 4):
            combinatorial_weight += len(list(itertools.combinations([1,2,3,4], r)))

        final_score = base_metric + xor_contribution + peak_contribution
        return final_score  # This is the real answer

    # Execute critical statement
    final_diagnostic = analyze_pattern(signal_buffer, threshold_map)

    # Print result for evaluation
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()