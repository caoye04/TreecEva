from itertools import compress, count

def main():
    # Simulate sensor readings with noise
    raw_readings = [104, 95, 112, 87, 99, 118, 93, 108]
    baseline = 100
    tolerance = 5

    # Irrelevant transformation: normalize around baseline (not used in final result)
    normalized = [(x - baseline) for x in raw_readings]

    # Identify valid readings within tolerance (boolean logic)
    within_tolerance = [abs(x - baseline) <= tolerance for x in raw_readings]

    # Extract valid readings using itertools.compress
    filtered_readings = list(compress(raw_readings, within_tolerance))

    # Tracking state with enumerate for alignment analysis (semi-relevant)
    alignment_score = 0
    for i, val in enumerate(filtered_readings):
        alignment_score += abs(val - (baseline + (-1)**i * 2))

    # Secondary processing: amplify every second element (distractor)
    amplified = []
    for j, val in enumerate(filtered_readings):
        if j % 2 == 0:
            amplified.append(val * 1.1)
        else:
            amplified.append(val)

    # Key data for checksum: use original filtered values only
    processed_data = [x ^ 7 for x in filtered_readings]  # Bitwise XOR obfuscation

    # Red herring: complex sorting that isn't used
    sorted_desc = sorted(processed_data, reverse=True)
    sorted_asc = sorted(processed_data)

    # Final aggregation function
    def finalize_sum(data):
        total = 0
        idx_gen = count(1)
        for val in data:
            weight = next(idx_gen)
            total += weight * val  # Weighted sum based on position
        return int(total)

    checksum = finalize_sum(processed_data)
    
    # Debug prints (not affecting logic)
    debug_mode = False
    if debug_mode:
        print(f"Filtered: {filtered_readings}")
        print(f"Processed: {processed_data}")
    
    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()