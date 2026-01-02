def process_phase_data(raw_readings):
    normalized = [round(x * 0.87 + 12.5, 2) for x in raw_readings]
    offset = sum(normalized) / len(normalized) - 50
    adjusted = [val + offset for val in normalized]
    return [adj * 1.03 for adj in adjusted]


def validate_stability_index(seq):
    if len(seq) < 3:
        return False
    for i in range(2, len(seq)):
        if seq[i] < seq[i-1] and seq[i-1] < seq[i-2]:
            return False
    return True

raw_sensor_data = [45, 67, 58, 72, 81]
processed_data = process_phase_data(raw_sensor_data)

stability = validate_stability_index(processed_data)
baseline_reference = sum(processed_data) / len(processed_data)

# Extraneous calculation: atmospheric variance (not used in final result)
atmospheric_variance = sum([(x - baseline_reference)**2 for x in processed_data]) / len(processed_data)
signal_damping = 0.91
filtered_output = [sig * signal_damping for sig in processed_data]

# Efficiency model based on peak-to-average ratio
peak_reading = max(processed_data)
average_reading = sum(processed_data) / len(processed_data)
efficiency_ratio = (average_reading / peak_reading) if peak_reading != 0 else 0

# Phase weight distribution (simulated multi-phase system)
phase_weights = []
for i, val in enumerate(processed_data):
    weight = val / average_reading
    if i % 2 == 0:
        weight *= 1.1
    else:
        weight *= 0.95
    phase_weights.append(round(weight, 3))

# Dead code path - simulates fault detection but unused
if efficiency_ratio < 0.85:
    fault_codes = ["F1", "F9"]
    recovery_attempt = True
else:
    recovery_attempt = False

# Key computational function combining arithmetic and logic
def calculate_thermal_output(efficiency, weights):
    base_energy = 1000 * efficiency
    adjustment_factor = 1.0
    for w in weights:
        if w > 1.0:
            adjustment_factor += w * 0.05
        elif w < 0.95:
            adjustment_factor -= 0.02
    # Apply non-linear scaling
    thermal_output = base_energy * (adjustment_factor ** 1.5)
    return round(thermal_output, 4)

# Critical execution point
thermal_capacity = calculate_thermal_output(efficiency_ratio, phase_weights)

# Additional irrelevant tracking
status_log = {"timestamp": "2024-05-20", "mode": "diagnostic"}
status_log["last_entry"] = "System nominal"

# Print final target result
print(f"Result: {thermal_capacity}")