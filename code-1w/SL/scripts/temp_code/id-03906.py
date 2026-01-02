def calculate_engine_efficiency(rpm, load):
    base_efficiency = rpm * 0.01
    adjustment = load * 0.05 if rpm >= 3000 else -load * 0.02
    return round(base_efficiency + adjustment, 3)

rpms = [2500, 3000, 3500, 4000]
loads = [60, 70, 80, 90]
efficiencies = []

for i, (rpm, load) in enumerate(zip(rpms, loads)):
    efficiency = calculate_engine_efficiency(rpm, load)
    efficiencies.append(efficiency)

peak_efficiency = max(efficiencies)
print(f'Result: {peak_efficiency}')