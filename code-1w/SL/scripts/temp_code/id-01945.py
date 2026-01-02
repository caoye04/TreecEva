from itertools import compress

def analyze_soil_quality(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return avg, variance

def calculate_harvest_efficiency(plots, thresholds):
    efficiency_list = []
    temp_debug_log = []
    total_plots = len(plots)
    valid_count = 0

    for idx, (plot_id, data) in enumerate(plots.items()):
        ph_levels = data['ph']
        nutrient_levels = data['nutrients']
        moisture = data['moisture']

        avg_ph, ph_var = analyze_soil_quality(ph_levels)
        avg_nutrients = sum(nutrient_levels) / len(nutrient_levels)

        # Irrelevant intermediate calculation (distractor)
        stability_score = (1.0 / (1.0 + ph_var)) if ph_var != 0 else 1.0
        temp_debug_log.append(f'Plot {plot_id} stability: {stability_score:.3f}')

        meets_ph = thresholds['ph_min'] <= avg_ph <= thresholds['ph_max']
        meets_nutrients = avg_nutrients >= thresholds['nutrients_min']
        meets_moisture = moisture >= thresholds['moisture_min']

        if not all([meets_ph, meets_nutrients, meets_moisture]):
            continue

        # Core logic: yield computation
        base_yield = avg_nutrients * 10
        moisture_factor = 0.5 + (moisture / 100) * 0.5
        ph_factor = 1.0 - abs(avg_ph - 6.5) * 0.1
        plot_yield = base_yield * moisture_factor * max(ph_factor, 0.3)

        efficiency_list.append(plot_yield)
        valid_count += 1

    # Dead code path (distractor)
    if valid_count == 0 and total_plots > 5:
        fallback_estimate = sum(thresholds.values()) / len(thresholds)
        final_avg = fallback_estimate * 0.7
    else:
        final_avg = sum(efficiency_list) / len(efficiency_list) if efficiency_list else 0

    # Key manipulation step
    adjustment_multiplier = 1.1 if valid_count >= 3 else 1.0
    final_yield = final_avg * adjustment_multiplier

    # String processing red herring (uses string methods)
    log_entry = f"Harvest batch {str(plot_id)[:3].upper()}-X processed."
    log_clean = log_entry.replace('-', '_').strip().lower()
    unused_tokens = log_clean.split('_')

    return final_yield

# Main execution block
plots_data = {
    'A1': {
        'ph': [6.2, 6.4, 6.3, 6.1],
        'nutrients': [8, 7, 9, 8],
        'moisture': 65
    },
    'B2': {
        'ph': [5.9, 6.0, 6.1, 6.2],
        'nutrients': [6, 7, 6, 5],
        'moisture': 70
    },
    'C3': {
        'ph': [6.6, 6.7, 6.5, 6.8],
        'nutrients': [10, 11, 10, 9],
        'moisture': 75
    },
    'D4': {
        'ph': [7.0, 7.2, 7.1, 6.9],
        'nutrients': [5, 4, 5, 6],
        'moisture': 50
    }
}

thresholds_config = {
    'ph_min': 6.0,
    'ph_max': 7.0,
    'nutrients_min': 6.5,
    'moisture_min': 60
}

# Intermediate variable (not directly used in answer but adds cognitive load)
diagnostic_mode = False
if diagnostic_mode:
    print("Running in debug mode")

final_yield = calculate_harvest_efficiency(plots_data, thresholds_config)

# Use of itertools (compress) as irrelevant filter
data_flags = [True, True, False, True]
filtered_plots = list(compress(plots_data.keys(), data_flags))

# Output result
print(f"Result: {final_yield}")