def analyze_system_load(base_load, peak_factor):
    load_multiplier = 1.75 if base_load < 50 else 2.25
    adjusted_load = base_load * load_multiplier
    return adjusted_load * peak_factor

# System telemetry data
current_load = 48
peak_usage = 1.6
threshold = 85.0

# Compute dynamic energy level
energy_level = analyze_system_load(current_load, peak_usage)

# Determine operational statuses
system_status = 1 if energy_level >= threshold else 0
backup_status = int(energy_level < threshold)

# Apply conditional logic with lambda-based fallback
status_resolver = lambda x, y, cond: x + 10 if cond else y - 5
final_diagnostic = system_status if energy_level > threshold else backup_status

# Secondary unused diagnostic (distractor)
nominal_ratio = current_load / peak_usage
reference_margin = nominal_ratio * 0.85

# Final adjustment based on safety protocol
energy_threshold = energy_level + 5.0 if final_diagnostic == 1 else energy_level - 3.0

print(f"Result: {energy_threshold}")