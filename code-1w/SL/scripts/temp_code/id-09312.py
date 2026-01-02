from itertools import combinations

def main():
    # Sensor data blocks with noise and metadata
    raw_blocks = [12, 8, 15, 7, 3, 10]
    noise_profile = {2, 5, 7, 11, 13}
    scaling_factor = 1.0
    temp_offset = 0

    # Irrelevant pre-processing: simulate calibration (not used in final result)
    calibrated = [x * scaling_factor + temp_offset for x in raw_blocks]
    calibrated = [x for x in calibrated if x > 5]  # Filter step (distractor)

    # Real processing begins: identify anomalous pairs using set logic
    anomaly_flags = []
    for a, b in combinations(raw_blocks, 2):
        if (a ^ b) in noise_profile:  # XOR to detect irregularities
            anomaly_flags.append(a | b)  # OR combination as flag

    # Aggregate anomalies through bitwise reduction (semi-relevant)
    anomaly_sum = 0
    for flag in anomaly_flags:
        anomaly_sum ^= flag  # Cumulative XOR (distraction from main path)

    # Core transformation: process every third block with tuple unpacking
    processed_blocks = []
    for i, val in enumerate(raw_blocks):
        if (i + 1) % 3 == 0:  # Every third element
            temp_val = val ^ 5  # Apply fixed XOR key
            processed_blocks.append(temp_val)

    # Secondary distraction: zip with offset list
    offsets = [1, 2, 3]
    paired = list(zip(processed_blocks, offsets))
    adjusted = [p[0] + p[1] for p in paired]  # Computation not used later

    # Critical function call
    final_checksum = compute_checksum(processed_blocks)
    
    # Output required format
    print(f"Target result: {final_checksum}")


def compute_checksum(data_list):
    # Checksum calculation using enumerate and cumulative product
    total = 0
    for idx, value in enumerate(data_list):
        contribution = (idx + 1) * value  # Weight by position
        total += contribution
    
    # Additional distraction: sort and reverse (no effect on total)
    sorted_data = sorted(data_list)
    reversed_pairs = list(zip(sorted_data, reversed(sorted_data)))
    
    # Final transformation
    return total ^ 17  # XOR final sum with prime

if __name__ == "__main__":
    main()