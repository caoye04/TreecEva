def analyze_growth_cycle(temperature_data, moisture_levels):
    peak_stress = 0
    cumulative_thermal_units = 0
    stress_factors = []
    temp_baseline = 25
    moisture_threshold = 40

    for i in range(len(temperature_data)):
        heat_stress = abs(temperature_data[i] - temp_baseline) ** 1.1
        moisture_stress = 100 - moisture_levels[i] if moisture_levels[i] < moisture_threshold else 0
        total_crop_stress = heat_stress + moisture_stress

        if total_crop_stress > peak_stress:
            peak_stress = total_crop_stress

        cumulative_thermal_units += max(0, temperature_data[i] - 10)

        if i % 3 == 0:
            stress_factors.append(round(total_crop_stress * 0.85, 2))
        else:
            stress_factors.append(round(total_crop_stress * 0.9, 2))

    adjustment_factor = 0.95 if cumulative_thermal_units > 800 else 1.05
    return stress_factors, adjustment_factor, peak_stress


def normalize_string_inputs(raw_labels):
    cleaned = [label.strip().lower().replace('_', '-') for label in raw_labels]
    encoded_values = [sum(ord(c) for c in s) % 50 for s in cleaned]
    return encoded_values


def calculate_harvest_efficiency(base_output, stress_factors):
    efficiency = base_output
    decay_rate = 0.03
    boost_credit = 0

    for idx, stress in enumerate(stress_factors):
        if stress == 0:
            continue
        efficiency -= stress * decay_rate

        if idx % 4 == 0 and stress < 15:
            boost_credit += 2.5

        # Simulate sensor fluctuation noise (irrelevant to final result)
        noise_offset = (idx ** 2) % 7 * 0.01
        efficiency += noise_offset - noise_offset

    efficiency += boost_credit
    return round(efficiency * 1.1, 2)

# Main simulation
if __name__ == '__main__':
    # Environmental input data
    daily_temps = [22, 26, 34, 39, 28, 24, 23, 31, 36, 33, 27, 25, 24, 30]
    soil_moisture = [55, 48, 38, 32, 45, 60, 58, 40, 35, 33, 47, 52, 50, 49]

    # Irrelevant metadata processing
    sensor_ids = ['SNSR_01', 'SNSR_02', 'SNSR_03', 'SNSR_04']
    normalized_ids = normalize_string_inputs(sensor_ids)
    avg_id_encoding = sum(normalized_ids) / len(normalized_ids)

    # Key computation path
    stress_metrics, factor, max_stress = analyze_growth_cycle(daily_temps, soil_moisture)
    baseline_productivity = 87

    # Apply adjustment (mostly neutral in this case)
    adjusted_base = baseline_productivity * factor

    # Critical statement
    final_yield = calculate_harvest_efficiency(adjusted_base, stress_metrics)

    # Distraction block: simulate secondary system readout
    predicted_demand = 92.5
    surplus = final_yield - predicted_demand
    compliance_status = 'OK' if surplus >= 0 else 'ALERT'
    status_code = hash(compliance_status) % 100

    print(f"Result: {final_yield}")