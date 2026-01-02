from itertools import compress, count

def analyze_growth_cycles(data, threshold=0.75):
    # Simulate sensor-based anomaly detection in agricultural plots
    indices = count(0)
    valid_cycles = []
    temp_buffer = []
    cumulative_noise = 0.0

    for i, readings in enumerate(data):
        cycle_avg = sum(readings) / len(readings)
        noise_level = abs(cycle_avg - 0.5) * 2
        cumulative_noise += noise_level

        if noise_level < threshold:
            valid_cycles.append(i)
            temp_buffer.append(cycle_avg)
        else:
            temp_buffer.append(None)  # Mark as invalid

    # Misleading computation: not used in final result
    avg_valid = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    decay_factor = max(0.1, 1 - (cumulative_noise / len(data)))

    return valid_cycles, decay_factor

def calculate_harvest_efficiency(plots, sensors):
    efficiency_log = []
    total_plots = len(plots)
    active_sensors = [s for s in sensors if s['status'] == 'active']
    coverage_ratio = len(active_sensors) / len(sensors) if sensors else 0

    # Simulate data alignment using zip and enumerate
    plot_data = []
    for p in plots:
        p_id = p['id']
        growth_data = [g + (p_id % 10) * 0.01 for g in p['growth_curve']]
        plot_data.append({'plot_id': p_id, 'data': growth_data})

    # Extract all growth curves for analysis
    all_curves = [p['data'] for p in plot_data]
    filtered_indices, _ = analyze_growth_cycles(all_curves, threshold=0.8)

    # Use compress to filter relevant plots based on cycle validity
    valid_plots = list(compress(plot_data, [i in filtered_indices for i in range(len(plot_data))]))

    # Core calculation: weighted efficiency score
    base_yield = 0
    adjustment_sum = 0
    debug_values = []  # Dead variable - distractor

    for idx, vp in enumerate(valid_plots):
        raw_yield = sum(vp['data']) / len(vp['data'])
        plot_weight = (vp['plot_id'] % 3) + 1
        local_adjustment = plot_weight * 0.15
        adjustment_sum += local_adjustment

        # Final contribution
        base_yield += raw_yield * plot_weight

    if valid_plots:
        normalized_yield = base_yield / len(valid_plots)
        final_adjustment = adjustment_sum / len(valid_plots)
        preliminary_score = normalized_yield * (1 + final_adjustment)
    else:
        preliminary_score = 0.5

    # Apply coverage correction (only if sufficient coverage)
    if coverage_ratio > 0.6:
        preliminary_score *= coverage_ratio

    # Irrelevant post-processing (distractor)
    smoothed_score = round(preliminary_score, 4)
    outlier_check = abs(smoothed_score - 0.66) > 0.1
    confidence_band = (0.95 if outlier_check else 0.99)

    # Actual answer computation
    final_yield = int(smoothed_score * 10000)  # Scale for integer output

    # Print required at end
    print(f"Result: {final_yield}")
    return final_yield

# Input data
plots_input = [
    {'id': 101, 'growth_curve': [0.62, 0.68, 0.71, 0.73]},
    {'id': 102, 'growth_curve': [0.45, 0.50, 0.53, 0.55]},
    {'id': 103, 'growth_curve': [0.80, 0.82, 0.79, 0.81]},
    {'id': 104, 'growth_curve': [0.30, 0.33, 0.35, 0.31]},
    {'id': 105, 'growth_curve': [0.67, 0.69, 0.72, 0.70]}
]

sensor_array = [
    {'name': 'S1', 'status': 'active'},
    {'name': 'S2', 'status': 'inactive'},
    {'name': 'S3', 'status': 'active'},
    {'name': 'S4', 'status': 'active'},
    {'name': 'S5', 'status': 'faulty'}
]

# Key execution point
final_yield = calculate_harvest_efficiency(plots_input, sensor_array)