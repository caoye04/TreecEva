def main():
    # Sensor data calibration and ranking system
    raw_readings = [89, 93, 78, 96, 85]
    calibration_factor = 1.05
    offset = 2

    # Apply calibration using lambda
    calibrated = list(map(lambda x: (x * calibration_factor) + offset, raw_readings))

    # Normalize readings to 0-100 scale
    max_val = max(calibrated)
    normalized = [round(v * (100 / max_val), 2) for v in calibrated]

    # Compute metrics dictionary
    metrics = {f'sensor_{i}': normalized[i] for i in range(len(normalized))}

    # Scale metrics by performance tier
    def scale_by_tier(val):
        if val >= 90:
            return val * 1.2
        elif val >= 80:
            return val * 1.1
        else:
            return val * 0.95

    scaled_metrics = {k: scale_by_tier(v) for k, v in metrics.items()}

    # Calculate final composite ranking
    def calculate_ranking(data_dict):
        values = data_dict.values()
        return round(sum(values) / len(values), 3)

    final_score = calculate_ranking(scaled_metrics)

    # Irrelevant debug variable (minimal distraction - intervention level 4)
    debug_mode = False
    if debug_mode:
        print("Debug info:", scaled_metrics)

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()