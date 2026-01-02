from itertools import permutations

# Simulate sensor data processing with noise filtering and integrity check
raw_readings = [18, 27, 93, 41, 56]
filtered_data = []
noise_floor = 20
saturation_limit = 90

# Apply filtering: exclude values below noise floor or above saturation
temp_sum = 0
drop_count = 0
for reading in raw_readings:
    if reading < noise_floor:
        drop_count += 1
        continue
    if reading > saturation_limit:
        drop_count += 1
        continue
    filtered_data.append(reading)
    temp_sum += reading

# Compute rolling average for stability assessment
window_size = 2
rolling_averages = []
for i in range(len(filtered_data) - window_size + 1):
    window_avg = sum(filtered_data[i:i+window_size]) / window_size
    rolling_averages.append(window_avg)

# Misleading statistic: peak-to-peak variation (not used later)
if filtered_data:
    ptp_variation = max(filtered_data) - min(filtered_data)
    normalized_ptp = ptp_variation / len(filtered_data)

# Characterize data pattern using string representation of digits
digit_chars = ''.join(set(str(d) for d in filtered_data))
sorted_digits = ''.join(sorted(digit_chars))
offset_value = len(sorted_digits) * 7  # Heuristic offset

# Generate synthetic control sequence to simulate system state
control_sequence = []
for i in range(3):
    control_sequence.append((i * offset_value) % 25)

# Compute base checksum using modular arithmetic and permutation entropy
perm_count = 0
for _ in permutations(filtered_data, 3):
    perm_count += 1
    if perm_count > 100:  # Early break for efficiency
        break

entropy_estimate = perm_count % 100
base_value = (temp_sum * len(rolling_averages)) + entropy_estimate

# Adjustment logic based on digit uniqueness
unique_digits = set()
for val in filtered_data:
    unique_digits.update(set(str(val)))
digit_score = sum(int(d) for d in unique_digits if d in '13579')
adjustment = digit_score * len(control_sequence)

# Final integrity checksum (key statement)
modulus = 97
final_checksum = (base_value + adjustment) % modulus

# Distractor: secondary validation using sorted digits
validation_key = int(sorted_digits) % 13 if sorted_digits else 0

# Output target result
print(f"Result: {final_checksum}")