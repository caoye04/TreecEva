def main():
    # Sensor data processing simulation with noise filtering and thresholding
    raw_readings = [127, 255, 93, 188, 64, 210, 45, 150, 77, 200]
    calibration_offsets = [8, -5, 12, -3, 7, -10, 5, -8, 0, 3]
    
    # Apply calibration (relevant)
    calibrated_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]
    
    # Noise detection (distractor: computed but not used later)
    high_noise_candidates = []
    for val in raw_readings:
        if val > 200:
            high_noise_candidates.append(val * 0.1)
    
    # Normalize readings to 0-1 scale (relevant)
    normalized_readings = [round((x - 50) / 205, 4) for x in calibrated_readings if x > 40]
    
    # Simulate environmental factor adjustment (semi-relevant)
    environment_factor = 1.08
    adjusted_readings = [val * environment_factor for val in normalized_readings]
    
    # Segment into groups (distractor list construction)
    grouped = []
    for i in range(0, len(adjusted_readings), 3):
        grouped.append(adjusted_readings[i:i+3])
    
    # Compute rolling average over last 5 values (partially relevant)
    recent_trend = []
    for i in range(1, min(6, len(adjusted_readings)+1)):
        recent_trend.append(adjusted_readings[-i] * 0.8 ** i)
    
    # Scale values using exponential weighting (relevant)
    scaled_values = [val * (1.1 ** i) for i, val in enumerate(adjusted_readings)]
    
    # Define dynamic thresholds based on median (relevant)
    sorted_vals = sorted(scaled_values)
    mid = len(sorted_vals) // 2
    median_val = (sorted_vals[mid] + sorted_vals[~mid]) / 2
    thresholds = [median_val * 0.9, median_val * 1.1]
    
    # Auxiliary debug logging (dead code path)
    debug_logs = []
    for idx, v in enumerate(scaled_values):
        status = "LOW" if v < thresholds[0] else "HIGH" if v > thresholds[1] else "NORMAL"
        debug_logs.append(f"[{idx}] {v:.3f}: {status}")
    
    # Core aggregation logic (depends on scaled_values and thresholds)
    def compute_aggregate(data, limits):
        low_lim, high_lim = limits
        count_in_range = 0
        sum_enhanced = 0.0
        
        for x in data:
            enhanced = x ** 1.05  # slight non-linear boost
            sum_enhanced += enhanced
            if low_lim <= x <= high_lim:
                count_in_range += 1
        
        balance_factor = (count_in_range / len(data)) * 100
        return int(sum_enhanced / balance_factor) if balance_factor > 0 else 0
    
    final_score = compute_aggregate(scaled_values, thresholds)
    print(f"Result: {final_score}")

main()