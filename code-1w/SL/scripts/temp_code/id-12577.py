from collections import defaultdict

# Simulate a data integrity verification process with noise filtering
def compute_integrity_score(data_stream):
    histogram = defaultdict(int)
    running_sum = 0
    temp_factor = 0
    control_flag = True
    
    # Irrelevant tracking variables (distractors)
    peak_magnitude = 0
    noise_events = 0
    baseline_offset = sum([i % 3 for i in range(len(data_stream))])  # Unused computation

    for i, val in enumerate(data_stream):
        if val < 0:
            noise_events += 1
            continue
            
        # Core logic steps
        histogram[val] += 1
        running_sum += val * (i + 1)
        
        if i % 4 == 0:
            temp_factor += (val ^ i) % 7
        elif i % 3 == 0 and control_flag:
            temp_factor -= (val + i) // 5
            control_flag = False

        # Red herring block: modifies unused variable
        if val > peak_magnitude:
            peak_magnitude = val
            adjustment = (peak_magnitude // 2) * (i % 2)
            _ = adjustment  # Dead computation

    # Secondary loop with partial overlap
    aggregated_shift = 0
    for count in histogram.values():
        aggregated_shift ^= count << 1

    # Final computation chain
    modulus = 977
    temp_factor = (temp_factor + aggregated_shift) % 100
    correction_term = len(histogram) * 3
    running_sum -= correction_term

    final_checksum = (running_sum ^ temp_factor) % modulus

    # Print required to expose result
    print(f"Result: {final_checksum}")

    return final_checksum

# Input data
stream_data = [12, -5, 24, 18, 12, 33, -8, 15, 24, 9, 18]
compute_integrity_score(stream_data)