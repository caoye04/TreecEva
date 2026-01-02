def analyze_system_performance(log_entries):
    temperatures = [float(entry.split()[1]) for entry in log_entries if 'TEMP' in entry]
    pressures = [float(entry.split()[1]) for entry in log_entries if 'PRES' in entry]
    
    adjusted_temps = []
    for t in temperatures:
        if t > 100:
            adjusted_temps.append(t * 0.92)
        elif t < 0:
            adjusted_temps.append(t * 1.05)
        else:
            adjusted_temps.append(t)
    
    # Misleading computation: this is not used later
    avg_pressure = sum(pressures) / len(pressures) if pressures else 0
    pressure_variance = sum((p - avg_pressure) ** 2 for p in pressures) / len(pressures) if pressures else 0

    base_efficiency = 85.0
    efficiency_modifiers = []
    for i, temp in enumerate(adjusted_temps):
        modifier = 1.0
        if temp > 90:
            modifier *= 0.88
        elif temp < 10:
            modifier *= 1.03
        if i % 3 == 0:
            modifier *= 1.02  # periodic calibration boost
        efficiency_modifiers.append(modifier)

    # Compute actual efficiencies
    efficiencies = []
    for temp, mod in zip(adjusted_temps, efficiency_modifiers):
        raw_eff = base_efficiency * mod
        # Simulate sensor dampening
        if raw_eff > 95:
            raw_eff = 95 + (raw_eff - 95) * 0.3
        efficiencies.append(round(raw_eff, 3))

    # Dead code path - never executed due to data constraints
    if False and len(efficiencies) > 100:
        efficiencies = efficiencies[:100]

    total_diagnostics = len(log_entries)
    diagnostic_codes = [entry.split()[0] for entry in log_entries]
    code_frequency = {}
    for code in diagnostic_codes:
        code_frequency[code] = code_frequency.get(code, 0) + 1

    # Key statement
    peak_efficiency = max(efficiencies)
    return peak_efficiency

log_data = [
    "TEMP 105.0", "PRES 98.2", "TEMP -5.0", "PRES 102.1", "TEMP 45.5",
    "TEMP 115.3", "PRES 95.0", "TEMP 8.0", "TEMP 92.7", "PRES 100.3"
]

result = analyze_system_performance(log_data)
print(f"Result: {result}")