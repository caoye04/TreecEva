import itertools

# Simulate packet data segmentation and validation with noise filtering
def main():
    raw_signal = [0.8, 1.2, -0.5, 3.1, 2.9, -1.1, 4.4, 0.2, 1.9, 3.3]
    thresholds = {'low': 0.75, 'high': 3.0, 'gain': 1.5}
    stats_log = []
    filtered_peaks = []
    temp_accumulator = 0

    # Irrelevant pre-processing: smooth signal (not used in final path)
    smoothed = [x * thresholds['gain'] for x in raw_signal]
    for val in smoothed:
        if val > thresholds['high']:
            temp_accumulator += val * 0.1

    # Real processing: identify segments above threshold
    data_segments = []
    segment_buffer = []

    for x in raw_signal:
        if x > thresholds['low']:
            segment_buffer.append(x)
        else:
            if len(segment_buffer) > 1:
                data_segments.append(segment_buffer[:])
            segment_buffer.clear()

    if len(segment_buffer) > 1:
        data_segments.append(segment_buffer)

    # Debugging stats (semi-relevant)
    for seg in data_segments:
        avg = sum(seg) / len(seg)
        stats_log.append({'length': len(seg), 'mean': avg})

    # Configuration with red herring fields
    config = {
        'mode': 'checksum',
        'debug': True,
        'padding': 999,  # unused
        'scaling_factor': 2.0  # unused in this context
    }

    # Misleading transformation chain
    transformed = list(itertools.chain.from_iterable(data_segments))
    squared_norm = sum(x ** 2 for x in transformed)  # looks important but not used

    # Core logic: compute weighted checksum using only segments of length >= 3
    def process_segments(segments, cfg):
        total_weight = 0.0
        running_xor = 0
        magnitude_sum = 0

        for i, seg in enumerate(segments):
            if len(seg) >= 3:
                weight = len(seg) * 2
                segment_sum = sum(seg)
                total_weight += weight
                magnitude_sum += segment_sum

                # Integer conversion for bitwise stage
                int_repr = int(abs(segment_sum) * 1.5) % 256
                running_xor ^= int_repr  # contributes to final answer

        # Combine components: uses magnitude, weight, and XOR
        preliminary = (magnitude_sum * 100) + running_xor
        scaling_offset = 42  # constant offset

        # Final computation
        result = (preliminary + total_weight) - scaling_offset

        # Dead code branch (never executed due to data)
        if config['debug'] and False:
            print("Debug mode active - not reached")

        return int(result)

    final_checksum = process_segments(data_segments, config)
    
    # Additional distraction: unused entropy calculation
    unique_vals = set(round(x, 1) for x in raw_signal)
    entropy_approx = sum(1 for _ in itertools.combinations(unique_vals, 2))

    print(f"Result: {final_checksum}")

if __name__ == "__main__":
    main()