import math

# System configuration constants (distractors)
CALIBRATION_FACTOR = 0.87
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 256
TEMP_OFFSET = -273.15

# Simulated sensor input stream (real and fake data mixed)
sensor_readings = [127, 134, 129, 131, 142, 145, 138, 136, 151, 158, 155, 153]
noise_floor = [random_value % 10 for random_value in range(12)]
adjusted_readings = [r + (n * 0.1) for r, n in zip(sensor_readings, noise_floor)]

# Derived metrics (some irrelevant)
power_states = {i: (reading > 140) for i, reading in enumerate(sensor_readings)}
efficiency_index = sum([r / 100 for r in sensor_readings if r > 130])
baseline_avg = sum(sensor_readings[2:8]) / 6
peak_magnitude = max(sensor_readings) - min(sensor_readings)

# Historical efficiency tracking with decoy computations
efficiency_log = []
for idx, val in enumerate(adjusted_readings):
    raw = sensor_readings[idx]
    norm = (val - baseline_avg) / baseline_avg
    if raw > 135:
        score = math.log(raw) * (norm + 1)
        # Dead code path - never executed due to logic
        if score < 0:
            score *= -1
        efficiency_log.append(round(score, 3))

# Irrelevant bit manipulation (red herring)
bitmask = 0b10101010
masked_values = [raw & bitmask for raw in sensor_readings]
decoy_shift = (bitmask << 3) | 0b111
parity_check = sum(1 for v in masked_values if bin(v).count('1') % 2 == 0)

# Control flow with misleading conditionals
system_active = len(efficiency_log) > 5 and peak_magnitude >= 20
status_flags = [system_active, efficiency_index > 5.0, parity_check > 3]
activation_key = all(status_flags)

# Unused recursive function (decoy)
def compute_depth_factor(n):
    if n <= 1:
        return 1
    return n * compute_depth_factor(n - 2)  # Skips many values

# Fake data transformation chain
corrupted_snapshot = adjusted_readings[::-1][:len(adjusted_readings)//2]
reconstructed = [corrupted_snapshot[i] * (i+1) for i in range(len(corrupted_snapshot))]
avg_reconstructed = sum(reconstructed) / len(reconstructed) if reconstructed else 0

# Core calculation hidden among distractions
def calculate_thermal_properties(last_efficiency):
    base_temp = TEMP_OFFSET + sum(sensor_readings[:5]) / 5
    adjustment = math.sin(math.pi * last_efficiency / 10)
    capacity = (base_temp - TEMP_OFFSET) * last_efficiency * (1 + adjustment)
    return round(capacity, 4)

# Critical assignment with conditional logic
thermal_capacity = calculate_thermal_properties(efficiency_log[-1]) if system_active else 0

# Redundant sorting (no effect on result)
sorted_diagnostics = sorted([efficiency_index, avg_reconstructed, thermal_capacity], reverse=True)
final_report = [f"Metric_{i}: {val}" for i, val in enumerate(sorted_diagnostics)]

# Output only the target variable
print(f"Result: {thermal_capacity}")