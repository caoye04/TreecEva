def process_sensor_data(raw_readings, calibration_sequence):
    timing_log = []
    temp_buffer = []
    checksum = 0
    outlier_count = 0  # distractor: not used in final result

    for i, reading in enumerate(raw_readings):
        adjusted = reading * (1 + 0.01 * calibration_sequence[i % len(calibration_sequence)])
        if abs(adjusted) > 500:  # red herring: never triggers due to data range
            outlier_count += 1
        temp_buffer.append(adjusted)

    # Dead code path - no effect on output
    if len(temp_buffer) < 10:
        temp_buffer.extend([0] * (10 - len(temp_buffer)))

    # Real processing begins
    for j, val in enumerate(temp_buffer):
        transformed = abs(val) ** 0.5
        bucket_index = j % 4
        if bucket_index == 0:
            timing_log.append(int(transformed))
        elif bucket_index == 1:
            timing_log.append(int(transformed // 2))
        elif bucket_index == 2:
            timing_log.append(int(transformed * 0.75))
        else:
            timing_log.append(int(transformed + 10))

    # Irrelevant set operation with decoy logic
    unique_remainders = {x % 7 for x in timing_log if x > 10}
    dummy_aggregate = sum(unique_remainders) * 0.1  # unused

    return timing_log


def validate_timing_integrity(log_entries):
    # Complex but irrelevant validation chain
    if not log_entries:
        return False
    cumulative_xor = 0
    for idx, entry in enumerate(log_entries):
        cumulative_xor ^= (entry + idx) & 0xFF
    parity_check = bin(cumulative_xor).count('1') % 2
    return parity_check == 0  # Always true for this data, but looks important


def aggregate_metrics(log, factor):
    base_sum = sum(log)
    penalty = 0
    
    # Bit manipulation red herring
    for k, val in enumerate(log):
        if (k & 3) == 0 and val > 20:  # bitwise check that only affects some
            penalty += val >> 2

    # Real adjustment
    adjusted_total = base_sum - penalty
    correction_offset = factor * 1.75

    # Use of zip and enumerate together (required features)
    multipliers = [1.1, 0.9, 1.05, 0.95]
    indices = list(range(len(log)))
    for idx, (m, i) in enumerate(zip(multipliers, indices[::len(multipliers)])):
        if idx < len(log):
            adjusted_total += log[idx] * (m - 1)  # minor tweak

    # Final computation
    raw_average = adjusted_total / len(log)
    fluctuation_score = 0
    for x in log:
        fluctuation_score += (x - raw_average) ** 2
    stability_metric = fluctuation_score / len(log)

    # Actual answer derivation
    return int(raw_average - stability_metric + correction_offset)

# Main execution flow
if __name__ == '__main__':
    sensor_input = [144, 169, 196, 225, 256, 289, 324, 361]  # perfect squares
    calibration_curve = [2, -1, 3, 0, 1]
    timing_results = process_sensor_data(sensor_input, calibration_curve)
    
    # Decoy function call that does nothing
    is_valid = validate_timing_integrity(timing_results)
    
    # Unused data structures
    history_archive = {}
    history_archive['first_run'] = timing_results.copy()
    history_archive['checksum'] = sum(timing_results) ^ 0xFFFF

    # Critical statement
    correction_factor = 8
    final_diagnostic = aggregate_metrics(timing_log=timing_results, correction_factor=correction_factor)
    
    # Additional distraction: recursive sum that isn't used
    def recursive_sum(arr, n):
        if n <= 0:
            return 0
        return arr[n-1] + recursive_sum(arr, n-1)
    
    unused_total = recursive_sum(timing_results, len(timing_results))

    print(f"Result: {final_diagnostic}")