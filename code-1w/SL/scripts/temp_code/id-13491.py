import itertools

def main():
    # Real sensor data (simulated)
    raw_readings = [234, 567, 891, 123, 456]
    calibration_offset = 42
    sampling_rate = 1000

    # Irrelevant signal processing chain (distractor)
    filtered_data = [x for x in raw_readings if x > 300]
    normalized = list(map(lambda y: (y - min(filtered_data)) / (max(filtered_data) - min(filtered_data)), filtered_data))
    smoothed = [normalized[i] + 0.01 * i for i in range(len(normalized))]

    # Unused transformation path (dead code)
    def transform_legacy(arr):
        return [a ^ 255 for a in arr]

    legacy_output = transform_legacy(raw_readings)  # Never used

    # Core logic disguised among distractions
    base_sequence = [x ^ calibration_offset for x in raw_readings]
    summation = sum(base_sequence)  # Key intermediate value

    # Decoy checksum using floating point (misleading)
    fake_checksum = sum(smoothed) * 1000
    temp_buffer = [int(s * 100) for s in smoothed]

    # Encoding key derived from bit manipulation and permutations
    bits = [(summation >> i) & 1 for i in range(8)]
    flipped = [1 - b for b in bits[:4]] + bits[4:]
    encoding_key = 0
    for i, bit in enumerate(flipped):
        encoding_key += bit * (2 ** i)

    # Red herring: complex unused permutation tree
    permutations_list = list(itertools.permutations([calibration_offset, sampling_rate, len(raw_readings)], 2))
    unused_tree = []
    for p in permutations_list:
        unused_tree.append((p[0] * p[1]) ^ 123)

    # Finalize function buried in logic
    def finalize(total, key):
        return (total ^ key) + 100

    checksum = finalize(summation, encoding_key)

    # Print required result
    print(f"Result: {checksum}")

main()