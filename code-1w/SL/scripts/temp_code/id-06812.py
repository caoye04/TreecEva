import itertools

# Simulated sensor array data processing with calibration and noise filtering
def main():
    raw_readings = [14, 7, 23, 11, 5, 19, 13, 3, 17, 21]
    calibration_factor = 0.85
    noise_threshold = 10
    baseline_offset = 2

    # Irrelevant auxiliary variables (distractors)
    temp_buffer = [0] * len(raw_readings)
    cumulative_checksum = 0
    spike_count = 0
    normalized_power = 0.0

    # Misleading preprocessing path - not actually used in final result
    for i in range(len(raw_readings)):
        if raw_readings[i] > noise_threshold:
            temp_buffer[i] = raw_readings[i] + baseline_offset
        else:
            temp_buffer[i] = raw_readings[i] - baseline_offset
        cumulative_checksum ^= temp_buffer[i]

    # Dead code path: simulates frequency analysis but unused
    def analyze_frequency_pattern(seq):
        freq_map = {}
        for val in seq:
            freq_map[val] = freq_map.get(val, 0) + 1
        return sorted(freq_map.items())

    # Unused recursive smoothing function (decoy)
    def smooth_recursive(data, depth):
        if depth == 0 or len(data) < 2:
            return data
        smoothed = [(data[i] + data[i+1]) / 2 for i in range(len(data)-1)]
        return smooth_recursive(smoothed, depth - 1)

    # Actual signal extraction: only this branch contributes to answer
    filtered_signal = [x for x in raw_readings if x % 2 == 1]  # Keep only odd readings
    
    # Transform via bit manipulation and scaling
    processed_levels = []
    for val in filtered_signal:
        shifted = (val << 1) ^ 3  # Left shift and XOR mask
        scaled = int(shifted * calibration_factor)
        processed_levels.append(scaled)
    
    # Introduce slicing distraction
    slice_preview = processed_levels[::2]  # Every other element - unused
    reverse_view = processed_levels[::-1]   # Reversed - unused

    # Core aggregation logic
    def aggregate_transform(sequence, factor):
        # Use itertools to generate sliding window pairs
        windows = list(itertools.pairwise(sequence))
        products = [a * b for a, b in windows]
        if not products:
            return sum(sequence)
        avg_product = sum(products) / len(products)
        total = sum(sequence) + avg_product
        return int(total * factor)  # Final transformation

    # Secondary irrelevant calculation chain
    outlier_flags = []
    for val in processed_levels:
        if val > 30 or val < 5:
            outlier_flags.append(True)
        else:
            outlier_flags.append(False)
    flagged_count = sum(1 for f in outlier_flags if f)

    # Key computation
    flux_sequence = processed_levels[1:6]  # Critical slicing
    final_flux = aggregate_transform(flux_sequence, calibration_factor)

    # Unrelated telemetry summary (dead code)
    def generate_telemetry_report():
        report = {
            'readings': len(raw_readings),
            'spikes': spike_count,
            'calibration': calibration_factor,
            'status': 'nominal'
        }
        return report

    print(f"Result: {final_flux}")

if __name__ == '__main__':
    main()