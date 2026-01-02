def calculate_engine_efficiency(rpm, load):
    base_efficiency = 0.85
    rpm_factor = 1 - abs(rpm - 3000) / 6000
    load_factor = 1 - abs(load - 0.75) / 1.5
    return int((base_efficiency * rpm_factor * load_factor) * 100)

rpms = [2000, 2500, 3000, 3500, 4000]
loads = [0.5, 0.6, 0.7, 0.8, 0.9]

# Irrelevant auxiliary variable (mild distraction)
temperature_warning = False

# Compute efficiencies using list comprehension and zip
efficiencies = [calculate_engine_efficiency(r, l) for r, l in zip(rpms, loads)]

# Determine peak efficiency
peak_efficiency = max(efficiencies)

# Additional unrelated check (minimal interference)
if any(e < 60 for e in efficiencies):
    temperature_warning = True

print(f"Result: {peak_efficiency}")