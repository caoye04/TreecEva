def analyze_temperature(readings):
    temp_stats = {}
    average_temp = sum(readings) / len(readings)
    temp_stats['mean'] = average_temp
    temp_stats['variance'] = sum((x - average_temp) ** 2 for x in readings) / len(readings)
    
    # Distractor: unused computation
    normalized = [round((t - average_temp) / (max(readings) - min(readings) + 1e-5), 3) for t in readings]
    outlier_count = len([t for t in readings if abs(t - average_temp) > 2 * (temp_stats['variance'] ** 0.5)])

    return temp_stats['mean']


def process_moisture_levels(levels):
    moisture_set = set(levels)
    baseline = sum(levels) / len(levels)
    adjusted_levels = [lvl * 1.1 if lvl < baseline else lvl * 0.95 for lvl in levels]
    
    # Dead code path - never executed due to logic
    if False:
        extreme_dry = [m for m in moisture_set if m < 20]
        extreme_wet = {m for m in moisture_set if m > 80}

    filtered = [val for val in adjusted_levels if 25 <= val <= 75]
    return filtered


def compute_growth_index(temp_mean, moist_values):
    index = temp_mean * 0.3 + (sum(moist_values) / len(moist_values)) * 0.7
    fluctuation_penalty = 0.0
    
    for i in range(1, len(moist_values)):
        diff = abs(moist_values[i] - moist_values[i-1])
        if diff > 10:
            fluctuation_penalty += diff * 0.05
    
    # Intermediate irrelevant tracking
    stability_log = []
    for val in moist_values:
        stability_log.append('stable' if 40 <= val <= 60 else 'variable')
    
    return round(index - fluctuation_penalty, 4)


def harvest_results(data_package):
    growth_index = data_package['index']
    days_elapsed = data_package['days']
    pest_exposure = data_package.get('pests', 0)
    
    base_yield = growth_index * 12.5
    
    # Real yield calculation
    yield_reduction = (pest_exposure * 0.8) if pest_exposure > 5 else 0
    final_yield = base_yield - yield_reduction
    
    # Irrelevant string processing distraction
    status_msg = "Harvest successful" if final_yield > 50 else "Below threshold"
    tokens = status_msg.split(' ')
    reversed_tokens = [word[::-1] for word in tokens]
    debug_info = ' | '.join(reversed_tokens)
    
    print(f"Debug: {debug_info}")
    return int(round(final_yield))

# Main execution flow
if __name__ == "__main__":
    temperature_readings = [22, 25, 27, 24, 26, 28, 23]
    moisture_input = [30, 45, 50, 70, 60, 40, 35]

    mean_temp = analyze_temperature(temperature_readings)
    processed_moisture = process_moisture_levels(moisture_input)
    growth_score = compute_growth_index(mean_temp, processed_moisture)

    # Assemble data package
    crop_data = {
        'index': growth_score,
        'days': 90,
        'pests': 7
    }

    # Key execution point
    final_yield = harvest_results(crop_data)
    print(f"Result: {final_yield}")