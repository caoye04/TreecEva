def main():
    # Agricultural yield simulation with noise filtering and efficiency calculation
    sensor_readings = [104, 95, 110, 88, 92, 108, 98, 100, 103, 87]
    calibration_offset = 5
    base_threshold = 90
    adjustment_factor = 0.85

    # Irrelevant signal processing (distractor)
    filtered_noise = list(map(lambda x: (x + calibration_offset) * 0.95, sensor_readings))
    smoothed_values = [val for val in filtered_noise if val > 90]

    # Core data transformation
    adjusted_readings = [r + calibration_offset for r in sensor_readings]
    
    # Define dynamic threshold function (relevant)
    threshold_func = lambda x: x > base_threshold + (x * 0.1)

    # Simulate soil quality bands (semi-relevant, not used directly)
    soil_bands = {"low": 0, "medium": 1, "high": 2}
    quality_flags = [soil_bands["medium"] if x > 100 else soil_bands["low"] for x in adjusted_readings]

    # Field data preparation
    field_data = []
    for i, val in enumerate(adjusted_readings):
        status = "optimal" if threshold_func(val) else "suboptimal"
        field_data.append({"index": i, "reading": val, "status": status})

    # Dead code path (distractor)
    if len(smoothed_values) > 10:
        adjustment_factor *= 1.1

    # Helper function for efficiency calculation
    def calculate_harvest_efficiency(data, condition):
        valid_count = 0
        total_value = 0.0
        for entry in data:
            if condition(entry["reading"]):
                valid_count += 1
                total_value += entry["reading"]
        return (total_value / valid_count) if valid_count > 0 else 0.0

    # Key computation step
    final_yield = calculate_harvest_efficiency(field_data, threshold_func)

    # Unused aggregation (distractor)
    outlier_count = sum(1 for v in adjusted_readings if v < 90 or v > 110)
    avg_outlier_ratio = outlier_count / len(adjusted_readings)

    print(f"Result: {final_yield}")

if __name__ == "__main__":
    main()