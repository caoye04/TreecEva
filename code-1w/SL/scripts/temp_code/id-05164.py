from collections import defaultdict

# System diagnostics for thermal regulation unit
unit_status = ['active', 'standby', 'active', 'maintenance', 'active']
efficiency_readings = [0.88, 0.91, 0.85, None, 0.93]

# Initialize data structures
event_count = defaultdict(int)
efficiency_log = []

for status in unit_status:
    event_count[status] += 1

# Filter and normalize efficiency values
for i, reading in enumerate(efficiency_readings):
    if reading is not None and unit_status[i] == 'active':
        efficiency_log.append(reading * 100)
    elif reading is None:
        # Compensate missing reading with moving average placeholder
        placeholder = sum(efficiency_log) / len(efficiency_log) if efficiency_log else 90
        efficiency_log.append(placeholder)

# Misleading diagnostic: power fluctuations (not used in final calculation)
power_fluctuations = []
baseline_power = 450
for i in range(len(unit_status)):
    fluctuation = (i % 2) * 15 - 7
    adjusted_power = baseline_power + fluctuation + (1 if unit_status[i] == 'maintenance' else 0)
    power_fluctuations.append(adjusted_power)

# Auxiliary function to assess system stress (unused red herring)
def compute_stress_factor(events):
    stress = 0
    for event in events:
        if event == 'standby':
            stress += 5
        elif event == 'maintenance':
            stress += 20
    return stress

# Core thermal rating logic
def calculate_thermal_rating(log_values):
    base_rating = sum(log_values)
    adjustment = len(log_values) * 0.5
    
    # Apply conditional multiplier based on stability
    stable = all(abs(log_values[i] - log_values[i-1]) < 3 for i in range(1, len(log_values)))
    multiplier = 1.2 if stable else 0.8
    
    # Final rating with artificial precision trim
    rating = (base_rating + adjustment) * multiplier
    return round(rating, 2)

# Critical computation step
thermal_capacity = calculate_thermal_rating(efficiency_log)

# Peripheral debug trace (irrelevant to result)
diagnostic_trace = []
for key, count in event_count.items():
    diagnostic_trace.append(f"{key}:{count}")

# Output result as required
print(f"Result: {thermal_capacity}")