import itertools

# Simulated sensor array diagnostics with interference
sensor_ids = ['S1', 'S2', 'S3', 'S4']
raw_readings = [104, 97, 110, 99]
status_flags = [True, False, True, True]
dummy_offsets = [3, -1, 0, 2, 5, -3]  # Irrelevant offsets

# Distractor: unused calibration matrix
calibration_matrix = [[0.98, 1.02], [1.01, 0.99]]
baseline_shift = sum(dummy_offsets) * 0.01  # Misleading computation

# Real processing begins
paired_data = list(zip(sensor_ids, raw_readings, status_flags))

# Filter active sensors (status True) and transform names to ASCII sums
active_sensors = [s for s in paired_data if s[2]]
ascii_sum = sum(ord(c) for c in ''.join(itertools.chain.from_iterable((s[0] for s in active_sensors))))

# Compute checksum from readings above threshold
thresholded_values = [val for val in raw_readings if val > 100]
checksum = sum(v ** 2 for v in thresholded_values) // 10

# Phantom calculation using string methods (distractor)
phantom_tag = 'SYS_DIAG_42'.lower().replace('_', '').upper()
phantom_value = len(phantom_tag) * 17  # Dead-end computation

# Temperature simulation (irrelevant loop)
current_temp = 22.5
for i in range(5):
    current_temp *= 1.05
    if i % 2 == 0:
        current_temp -= 0.3

# Key intermediate values
aggregate_score = ascii_sum + checksum  # Core value

# Decoy function that's defined but not used
def apply_noise_correction(data, factor=0.95):
    return [x * factor for x in data if x > 100]

# Another red herring: unused bitwise analysis
shift_register = 0b1101
mask_pattern = 0b1011
masked = shift_register & mask_pattern
inverted = ~masked & 0b1111

# Environmental factors
temperature_factor = abs(current_temp - 25) if current_temp > 20 else 0.5

# Correction term based on logical conditions
all_active = len(active_sensors) == len(raw_readings)
any_critical = any(r < 95 for r in raw_readings)
correction_term = (-10 if any_critical else (5 if all_active else 2))

# Final diagnostic calculation (target execution point)
final_diagnostic = aggregate_score + temperature_factor * correction_term

# Output result
print(f"Result: {final_diagnostic}")