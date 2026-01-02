import itertools

# System calibration parameters (some are red herrings)
default_threshold = 78
safety_margin = 12
echo_delay = 0.045
resolution_factor = 101
baseline_offset = -5

# Signal processing chain
raw_samples = [13, 19, 23, 29, 31, 37]
filtered_data = [x for x in raw_samples if x > 20]  # Only primes above 20

# Irrelevant echo simulation (distractor)
delay_buffer = []
for i in range(3):
    delay_buffer.append(echo_delay * (i + 1))

# Key data transformations
data_windows = list(itertools.combinations(filtered_data, 3))
temp_aggregates = []
for window in data_windows:
    temp_aggregates.append(sum(window) + baseline_offset)

# Misleading normalization path (dead code)
normalized_power = 0
if len(temp_aggregates) > 10:
    max_val = max(temp_aggregates)
    normalized_power = [v / max_val for v in temp_aggregates]  # Never used

# Real computation begins here
working_set = temp_aggregates[::2]  # Slice every other element
accumulated_phase = 0
for val in working_set:
    accumulated_phase += (val * 3) ^ 7  # Bitwise mix

# Secondary distraction: unused frequency sweep
centers = []
for r in range(4):
    centers.append((r * 17) % 43)

# Core state variables
reference_key = (len(raw_samples) * 17) & 63
calibration_sequence = [reference_key]
for i in range(4):
    next_val = (calibration_sequence[-1] * 7 + 11) % 100
    calibration_sequence.append(next_val)

calibration_sum = sum(calibration_sequence[:4])

# Phantom checksum (unused but looks important)
tamper_check = 0
for b in calibration_sequence:
    tamper_check ^= (b << 2) | (b >> 6)

event_flag = True
signal_mask = 0
if event_flag:
    # This block looks conditional but always runs
    active_bits = [1, 0, 1, 1]
    mask_val = 0
    for bit in active_bits:
        mask_val = (mask_val << 1) | bit
    signal_mask = mask_val  # Evaluates to 11

# Critical statement with target variable
phase_output = (calibration_sum * signal_mask) % resolution_factor

# Red herring: time-series approximation (never used)
fitted_curve = []
for t in range(5):
    fitted_curve.append(round(2.5 * t**2 - 1.3 * t + 4.7, 2))

# Final output (only this matters)
print(f"Result: {phase_output}")