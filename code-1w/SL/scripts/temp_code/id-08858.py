from collections import defaultdict

# Simulate agricultural yield analysis across multiple plots

def main():
    # Field data: plot_id -> list of crop yield measurements (in tons)
    field_data = {
        'A1': [4.2, 3.8, 4.0, 4.4],
        'B2': [3.1, 3.3, 3.0, 2.9],
        'C3': [5.5, 5.7, 5.3, 5.6],
        'D4': [2.2, 2.0, 1.8, 2.1]
    }

    # Irrelevant auxiliary tracking (distractor)
    measurement_logs = defaultdict(int)
    for plot, readings in field_data.items():
        for val in readings:
            measurement_logs[round(val)] += 1

    # Threshold function to identify high-performing batches
    threshold_func = lambda x: x > 3.5

    # Secondary filter for low variance (not used in final calculation - distractor)
    stability_filter = lambda vals: max(vals) - min(vals) < 0.6

    # Simulated environmental factors (unused - adds distraction)
    env_factors = {'temp': 22.5, 'humidity': 68, 'soil_ph': 6.4}
    adjustment_score = 0.0
    if env_factors['temp'] > 20:
        adjustment_score += 0.1
    if env_factors['humidity'] > 65:
        adjustment_score += 0.05

    # Core computation: calculate average yield only for plots passing threshold in all readings
    valid_plots_count = 0
    total_aggregate = 0.0

    for plot_id, yields in field_data.items():
        # Check if all readings in a plot exceed threshold
        if all(threshold_func(yield_val) for yield_val in yields):
            valid_plots_count += 1
            total_aggregate += sum(yields)

    # Dead code branch - never executed due to logic, but looks plausible
    if valid_plots_count == 0:
        fallback_mode = True
        total_aggregate = 1.0  # This does not trigger

    # Compute efficiency metric
    base_efficiency = total_aggregate / (valid_plots_count or 1)

    # Additional unused transformation (misleading)
    transformed_yields = []
    for vals in field_data.values():
        transformed_yields.extend([y ** 0.5 for y in vals if y > 2.5])

    # Final yield calculation - depends only on threshold-filtered total and count
    final_yield = round(base_efficiency, 4)

    # Extraneous post-processing (no effect)
    outlier_count = 0
    for vals in field_data.values():
        for v in vals:
            if v < 2.0 or v > 5.8:
                outlier_count += 1

    print(f"Result: {final_yield}")

main()

def calculate_harvest_efficiency(data, threshold):
    # This function is referenced in description but not called in this version
    # Included to align with task description phrasing
    valid_total = 0.0
    valid_count = 0
    for readings in data.values():
        if all(threshold(r) for r in readings):
            valid_total += sum(readings)
            valid_count += 1
    return round(valid_total / (valid_count or 1), 4)
