import itertools

# Simulate sensor readings from a thermal regulation system
def generate_thermal_profile(base_temp, cycles):
    profile = []
    for i in range(cycles):
        fluctuation = (i % 7) ** 2 if i % 3 == 0 else -(i % 5)
        adjusted = base_temp + fluctuation
        profile.append(round(adjusted, 2))
    return profile

# System calibration parameters
calibration_offsets = [0.5, -0.3, 0.8, -0.6]
base_temperature = 22.0
cycle_count = 12

# Generate raw thermal data
raw_readings = generate_thermal_profile(base_temperature, cycle_count)

# Apply calibration using offset cycling
calibrated_readings = [
    round(raw + offset, 2) 
    for raw, offset in zip(raw_readings, itertools.cycle(calibration_offsets))
]

# Filter out sub-threshold values (< 20.0) to focus on active zones
active_zones = [temp for temp in calibrated_readings if temp >= 20.0]

# Compute derived metrics
thermal_spikes = list(filter(lambda x: x > 25.0, active_zones))
spike_count = len(thermal_spikes)

# Background diagnostic check (distractor)
diagnostic_log = []
for val in raw_readings:
    status = "OK" if 18 <= val <= 26 else "CHECK"
    diagnostic_log.append(f"{val}:{status}")

# Simulate packet loss in transmission (irrelevant)
transmission_packets = [f"PKT{i}" for i in range(len(raw_readings))]
lost_indices = [i for i in range(len(transmission_packets)) if i % 5 == 0]
sent_packets = [p for i, p in enumerate(transmission_packets) if i not in lost_indices]

# Core computation: derive thermal loads from active, calibrated data
thermal_loads = []
for zone in active_zones:
    load = (zone - 20.0) ** 1.5  # non-linear stress factor
    thermal_loads.append(round(load, 3))

# Efficiency degrades with higher usage
if len(active_zones) > 8:
    efficiency_factor = 0.88
else:
    efficiency_factor = 0.94

# Key assignment point
peak_capacity = max(thermal_loads) * efficiency_factor

# Additional unused metric (distractor)
avg_diagnostic_temp = sum(raw_readings) / len(raw_readings)

# Final output
Result: peak_capacity