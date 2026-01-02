from itertools import compress, cycle

# Simulated sensor readings with noise and calibration flags
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 18.7, 26.0, 20.5, 21.8, 24.0]
calibration_sequence = [True, False, True, True, False, True, False, True, True, False]
error_flags = [0, 1, 0, 0, 2, 0, 3, 1, 0, 0]
baseline_offset = 2.1
adjustment_factors = [0.9, 1.1, 0.95, 1.0, 1.05]

# Irrelevant transformation: phase shift emulation (dead path)
phase_shifted = list(map(lambda x: x * 0.5 + 10, temperature_readings))
dummy_aggregate = sum(phase_shifted) / len(phase_shifted)

# Misleading intermediate: normalized data using wrong baseline
wrong_normalized = [t + baseline_offset * 1.5 for t in temperature_readings]
spurious_total = sum(wrong_normalized)

# Real processing begins: apply dynamic adjustment using cycling factors
cyclic_adjusters = list(zip(temperature_readings, cycle(adjustment_factors[:len(temperature_readings)])))
adjusted_readings = [temp * adj for temp, adj in cyclic_adjusters]

# Apply calibration mask to exclude uncalibrated sensors
calibrated_readings = list(compress(adjusted_readings, calibration_sequence))

# Filter out readings with non-zero error flags (even if calibrated)
valid_readings_mask = [flag == 0 for flag in error_flags]
valid_calibrated_mask = [cal and valid for cal, valid in zip(calibration_sequence, valid_readings_mask)]
validated_readings = list(compress(temperature_readings, valid_calibrated_mask))

# Dual-path confusion: one path adjusts then filters, one filters then adjusts
path_a = [t * 1.05 for t in validated_readings]  # minor boost to valid only
path_b_intermediate = [t * adj for t, adj in zip(adjusted_readings, cycle([1.1, 0.9]))]
path_b = list(compress(path_b_intermediate, valid_calibrated_mask))

# Correct path: use calibrated AND valid readings from adjusted set
correct_source_data = list(compress(adjusted_readings, valid_calibrated_mask))

# Red herring: complex statistical decoy
mean_harmonic = len(correct_source_data) / sum(1/t for t in correct_source_data if t != 0)
median_fake = sorted(correct_source_data)[len(correct_source_data)//2]

# Actual logic: filter based on threshold derived from baseline
threshold = baseline_offset * 9.25  # magic factor from spec sheet (irrelevant but sounds legit)
above_threshold = [x for x in correct_source_data if x > threshold]

# Final filtering: only values that are above threshold AND have prime index in original
original_indices = [i for i, valid in enumerate(valid_calibrated_mask) if valid]
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_index_mask = [is_prime(idx) for idx in original_indices]
final_filtered = list(compress(correct_source_data, prime_index_mask))

# Key assignment point
filtered_result = sum(final_filtered)

print(f"Result: {filtered_result}")