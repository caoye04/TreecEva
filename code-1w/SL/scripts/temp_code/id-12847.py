from itertools import cycle

# Simulate environmental sensor data for temperature fluctuations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.7]

# Device operational parameters
base_power = 17
runtime_cycles = 4
voltage_stability = 0.93

# Initialize derived metrics
efficiency_factor = 0.0
cumulative_drift = 0.0
redundant_accumulator = 0  # unused tracking variable (distractor)
phase_offset = 1.0

# Pattern generator for signal modulation (semi-relevant)
signal_pattern = cycle([1, -1, 0])

# Simulate calibration sequence over multiple cycles
for i in range(runtime_cycles):
    temp_deviation = abs(temperature_readings[i % len(temperature_readings)] - 24.0)
    phase_mod = next(signal_pattern)
    
    # Update efficiency with thermal and phase effects
    if temp_deviation > 1.0:
        efficiency_factor += 0.05 * voltage_stability
    else:
        efficiency_factor += 0.08 * voltage_stability

    # Apply phase-based adjustment (minor effect)
    efficiency_factor += 0.01 * phase_mod * 0.5

    # Irrelevant computation - simulates logging but doesn't affect result
    log_entry = f"Cycle {i}: Drift={cumulative_drift:.2f}, Offset={phase_offset:.1f}"
    cumulative_drift += temp_deviation * 0.02

# Critical assignment: compute final thermal capacity
thermal_capacity = base_power * efficiency_factor

# Additional unrelated transformation (dead code path - distractor)
if __debug__:
    adjusted_capacity = thermal_capacity * (1 + 0.1 * (efficiency_factor % 0.1))

# Output the target result
print(f"Result: {thermal_capacity}")