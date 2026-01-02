def calculate_engine_efficiency(rpm_values, load_profile):
    baseline = 75.0
    adjustments = []
    efficiencies = []
    temp_storage = []
    cumulative_drift = 0.0

    for i, (rpm, load) in enumerate(zip(rpm_values, load_profile)):
        # Real efficiency calculation
        base_rpm_factor = rpm / 1000.0
        load_factor = 1.0 + (load / 100.0)
        efficiency = baseline * base_rpm_factor * load_factor

        # Simulate sensor drift (not used in final result)
        drift = (i * 0.1) % 0.5
        cumulative_drift += drift
        adjusted_efficiency = efficiency - drift
        
        adjustments.append(adjusted_efficiency)
        efficiencies.append(round(efficiency, 4))

        # Dead code - stores data but never used
        if rpm > 3000:
            temp_storage.append((i, efficiency))

    # Secondary loop with irrelevant smoothing
    smoothed = []
    for j in range(len(efficiencies)):
        left = max(0, j-1)
        right = min(j+2, len(efficiencies))
        neighbor_avg = sum(efficiencies[left:right]) / (right - left)
        smoothed.append(neighbor_avg * 0.98)  # Not used

    # Key computation
    peak_efficiency = max(efficiencies)
    return peak_efficiency

# Input data
engine_rpms = [1200, 2400, 3600, 2800, 4000]
engine_loads = [60, 75, 80, 70, 85]

# Unused auxiliary data
sensor_temperatures = [88, 91, 94, 89, 95]
diagnostic_codes = ['OK', 'OK', 'WARN', 'OK', 'ERROR']

result = calculate_engine_efficiency(engine_rpms, engine_loads)
print(f"Target result: {result}")