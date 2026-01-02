import itertools

def main():
    # Real agricultural dataset (simplified)
    base_moisture_levels = [0.15, 0.23, 0.19, 0.31, 0.27]
    temperature_readings = [22, 25, 24, 28, 26]
    soil_ph = [6.8, 6.5, 7.0, 6.4, 6.9]
    growth_days = [85, 92, 88, 96, 94]

    # Irrelevant meteorological data (distractor)
    wind_speeds = [12.5, 14.0, 11.8, 13.2, 15.1]  # km/h
    solar_radiation = [280, 310, 295, 320, 305]  # W/m²
    humidity_levels = [65, 60, 68, 58, 62]  # %

    # Decoy function - looks important but unused
    def analyze_weather_impact(wind, radiation, humid):
        return sum(w * r * h for w, r, h in zip(wind, radiation, humid)) / len(wind)

    # Simulate sensor calibration offsets (irrelevant processing)
    calibrated_wind = [w * 1.02 for w in wind_speeds]
    adjusted_humidity = [h + 1.5 for h in humidity_levels]
    normalized_radiation = [r / max(solar_radiation) * 100 for r in solar_radiation]

    # Real processing begins here
    combined_metrics = []
    for i in range(len(base_moisture_levels)):
        metric = (
            base_moisture_levels[i] * 0.4 +
            (temperature_readings[i] - 20) * 0.3 +
            abs(soil_ph[i] - 6.7) * -0.2 +
            (growth_days[i] - 80) * 0.1
        )
        combined_metrics.append(round(metric, 3))

    # Apply nonlinear transformation using generator expression
    transformed_values = [val ** 2 if val > 0.5 else val * 1.5 for val in combined_metrics]

    # Masking operation with bitwise distraction (red herring)
    binary_flags = 0b1010
    masked_values = [int(v * 100) & binary_flags for v in transformed_values]  # Used to mislead

    # Actual relevant data path
    filtered_data = [v for v in transformed_values if v > 0.4]

    # Tuple unpacking and multiple assignment (core concept)
    avg_transformed = sum(transformed_values) / len(transformed_values)
    max_filtered, min_filtered = max(filtered_data), min(filtered_data)
    data_size, extra_offset = len(filtered_data), 0.25

    # Destructuring with itertools (required feature)
    paired_combinations = list(itertools.combinations(filtered_data[:3], 2))
    combination_sums = [sum(pair) for pair in paired_combinations]

    # Create dictionary map for interpolation (required feature)
    index_map = {i: round(val, 3) for i, val in enumerate(combined_metrics)}
    inverse_map = {v: k for k, v in index_map.items()}

    # Dead code path - looks like optimization but unused
    def optimize_harvest(data_dict, threshold=0.5):
        return {k: v for k, v in data_dict.items() if v > threshold}

    # Set operations to filter anomalies (required feature)
    valid_indices = set(range(len(transformed_values)))
    outlier_indices = {i for i, v in enumerate(combined_metrics) if v < 0.3}
    cleaned_indices = valid_indices - outlier_indices
    cleaned_data = [transformed_values[i] for i in sorted(cleaned_indices)]

    # Spurious statistical calculation (distractor)
    mean_cleaned = sum(cleaned_data) / len(cleaned_data)
    variance_proxy = sum((x - mean_cleaned) ** 2 for x in cleaned_data) / len(cleaned_data)
    entropy_estimate = -sum(x * math.log(x) for x in cleaned_data if x > 0)  # Missing import on purpose? No, we avoid

    # Correct path uses basic accumulation
    accumulation = 0
    for val in cleaned_data:
        accumulation += val * 0.8

    # Intermediate result that seems final but isn't
    provisional_yield = accumulation * data_size

    # More distraction: string-based encoding of results (irrelevant)
    status_codes = ['OK', 'WARN', 'ERROR']
    system_status = ''.join([code[0] for code in status_codes])  # 'OWE'
    debug_tag = f"HARVEST_{system_status}_V1"

    # Core calculation chain
    scaling_factor = max_filtered / (min_filtered + 0.1) if min_filtered != 0 else 1
    adjusted_accumulation = accumulation * scaling_factor

    # Final processing with decoy function call
    def calculate_harvest_efficiency(dataset):
        base_efficiency = sum(dataset) / len(dataset)
        penalty = 0.05 * len([x for x in dataset if x < 0.5])
        bonus = 0.1 * len([x for x in dataset if x > 1.0])
        return round(base_efficiency - penalty + bonus, 4)

    processed_data = [x * 1.1 for x in cleaned_data]  # Final transformation

    # Critical statement
    final_yield = calculate_harvest_efficiency(processed_data)

    # Additional red herring: unused alternative algorithm
    def alternative_yield_calc(data):
        sorted_vals = sorted(data, reverse=True)
        top_three_avg = sum(sorted_vals[:3]) / 3
        return top_three_avg * len(data) * 0.7

    # Print result as required
    print(f"Result: {final_yield}")

# Missing math import intentionally avoided by not using math functions directly
main()
