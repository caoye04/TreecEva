from collections import defaultdict

# System efficiency factors for different energy sources
efficiencies = [0.85, 0.90, 0.75, 0.95]

# Power generation values in megawatts
generation = [200, 150, 300, 100]

# Calculate effective power output after losses
power_outputs = []
for gen, eff in zip(generation, efficiencies):
    power_outputs.append(gen * eff)

# Adjust negative fluctuations due to grid instability
adjusted_powers = [p - 5 if p > 150 else p for p in power_outputs]

# Simulate emergency backup activation for low-output sources
backup_activation = 0
for power in adjusted_powers:
    if power < 100:
        backup_activation += 1

# Primary load calculation
powers = [p + 10 for p in adjusted_powers]

# Redundant system check (irrelevant to final result)
diagnostic_log = defaultdict(int)
for i, p in enumerate(powers):
    diagnostic_log[f'zone_{i}'] = p

# Final total load computation
total_load = sum(powers)
print(f"Result: {total_load}")