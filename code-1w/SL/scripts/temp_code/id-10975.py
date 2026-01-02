from itertools import cycle, islice

def main():
    # Sensor simulation data: temperature readings in microvolts
    raw_readings = [2345, 6789, 1234, 5678, 9876, 4321, 8765, 3456]
    
    # Irrelevant transformation: normalize to arbitrary scale (distractor)
    normalized = [x / 1000.0 for x in raw_readings]
    avg_normalized = sum(normalized) / len(normalized)

    # Relevant path begins: filter anomalies using threshold logic
    threshold = 5000
    filtered = [x for x in raw_readings if x > threshold]

    # Apply phase shift based on index parity (conditional branching)
    phased = []
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            phased.append(val << 1)  # Left shift even indices
        else:
            phased.append(val >> 2)  # Right shift odd indices

    # Decoy checksum using string hashing (irrelevant)
    decoy_input = "sensor_data_v1"
    decoy_checksum = sum(ord(c) * (i + 1) for i, c in enumerate(decoy_input)) % 9999

    # Generate rotating mask sequence using itertools
    mask_cycle = cycle([15, 255, 167, 31])
    masks = list(islice(mask_cycle, len(phased)))

    # Apply bitwise interference (XOR with cycling mask)
    masked_values = [v ^ m for v, m in zip(phased, masks)]

    # Conditional inversion based on population count (bit manipulation)
    def invert_if_sparse(n):
        return n if bin(n).count('1') >= 4 else ~n & 0xFFFF
    
    densified = [invert_if_sparse(v) for v in masked_values]

    # Simulate redundant validation chain (dead path)
    validation_score = 0
    for v in densified:
        if v > 30000:
            validation_score += 1
    # Unused result

    # Core aggregation: sum only values passing secondary threshold
    phase_sequence = [x for x in densified if x & 0xFF != 0]

    # Secondary red herring: complex but unused formula
    aux_data = [(x * 3 + 7) % 65537 for x in raw_readings]
    weighted_sum = sum(x * (len(aux_data) - i) for i, x in enumerate(aux_data)) // 1000

    # Finalization step: sum and truncate to 16-bit unsigned
    def finalize(total):
        return total & 0xFFFF

    checksum = finalize(sum(phase_sequence))

    # Irrelevant print statements (distraction)
    debug_state = {"count": len(densified), "max": max(densified)}
    metadata_log = f"Processed {debug_state['count']} entries, peak {debug_state['max']}"

    # Critical output - DO NOT MODIFY
    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()