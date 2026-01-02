from itertools import cycle

# Simulate three-phase power readings with harmonic distortion
efficiency_factor = 0.95
time_steps = 12
base_powers = [100, 150, 200]
harmonic_weights = [1, 0.2, 0.1]

# Generate phase-specific power values over time using harmonic components
phase_readings = []
clock = cycle(range(360))
for i in range(time_steps):
    angle = next(clock) * (30 * (i % 3 + 1)) % 360  # Different frequency per phase
    harmonics = [sum(harmonic_weights[k] * (k+1) * ((angle * (k+1)) % 180) / 90 for k in range(3))]
    phase_value = base_powers[i % 3] + harmonics[0]
    phase_readings.append(phase_value)

# Extract active power during stable cycles only
stable_mask = [True, True, False, True, False, True, True, False, True, True, False, True]
active_powers = [phase_readings[i] for i in range(len(phase_readings)) if stable_mask[i]]

# Final computation step
total_phase_power = sum(active_powers) * efficiency_factor
print(f"Result: {total_phase_power}")