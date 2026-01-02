from itertools import cycle

# Simulate three-phase power readings with harmonic pattern
phase_a = [100 + i * 2 for i in range(5)]
phase_b = [95 + i * 3 for i in range(5)]
phase_c = [105 + i * 1 for i in range(5)]

# Combine phase powers at each time step using zip
time_step_powers = [a + b + c for a, b, c in zip(phase_a, phase_b, phase_c)]

# Apply load imbalance correction using enumerate
corrected_powers = []
for i, power in enumerate(time_step_powers):
    correction = 0.98 if i % 2 == 0 else 1.02
    corrected_powers.append(power * correction)

# Extract active power components above base threshold (modular arithmetic used)
active_powers = [p for p in corrected_powers if int(p) % 10 != 0]

# Final computation step: aggregate and apply system efficiency
efficiency_factor = 0.94
total_phase_power = sum(active_powers) * efficiency_factor

# Irrelevant auxiliary variable (minimal distraction)
baseline_avg = sum([100, 95, 105]) / 3

print(f"Result: {total_phase_power}")