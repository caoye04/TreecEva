def process_sensor_array():
    # Real sensor data from environmental monitoring array
    raw_readings = [14.2, 18.5, 13.1, 22.8, 17.3, 19.0, 15.7, 21.4, 16.9, 18.1]
    calibration_offsets = [0.3, -0.2, 0.5, -0.4, 0.1, -0.3, 0.2, -0.1, 0.4, -0.5]
    location_tags = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2']
    
    # Irrelevant auxiliary data (distractor)
    maintenance_logs = {tag: {'last_cleaned': '2023-01-01', 'status': 'active'} for tag in location_tags}
    deployment_metadata = {'version': '2.1.0', 'firmware': 'v3.4', 'nodes': 10}
    
    # Apply calibration (relevant)
    calibrated_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]
    
    # Simulate noise filtering with windowing (partially relevant)
    filtered_readings = []
    for i in range(1, len(calibrated_readings) - 1):
        avg_window = (calibrated_readings[i-1] + calibrated_readings[i] + calibrated_readings[i+1]) / 3
        if avg_window > 15.0:
            filtered_readings.append(avg_window)
    
    # Additional irrelevant transformation (red herring)
    normalized_readings = [round((x - min(calibrated_readings)) / (max(calibrated_readings) - min(calibrated_readings)), 4) for x in calibrated_readings]
    statistical_moments = {
        'mean': sum(calibrated_readings) / len(calibrated_readings),
        'variance': sum((x - sum(calibrated_readings)/len(calibrated_readings))**2 for x in calibrated_readings) / len(calibrated_readings),
        'skew_hint': 'not_used'
    }
    
    # Map readings to locations (relevant)
    labeled_readings = list(zip(location_tags, calibrated_readings))
    
    # Extract only readings above base threshold (relevant)
    thresholded_readings = [(loc, val) for loc, val in labeled_readings if val > 17.5]
    
    # Create control checksum (decoy - looks important but unused)
    control_checksum = sum([hash(loc) % 1000 for loc, _ in labeled_readings]) + 12345
    temp_aggregates = {tag: round(val**1.05, 3) for tag, val in labeled_readings}  # Dead computation path
    
    # Define dynamic thresholds based on position (relevant)
    threshold_map = {}
    for idx, (loc, val) in enumerate(labeled_readings):
        if idx % 3 == 0:
            threshold_map[loc] = 18.0
        elif idx % 3 == 1:
            threshold_map[loc] = 17.0
        else:
            threshold_map[loc] = 19.0

    # Filter final dataset using sliding logic (relevant)
    filtered_data = []
    for i, val in enumerate(filtered_readings):
        if i < len(threshold_map):
            loc_key = location_tags[i]
            if loc_key in threshold_map and val > threshold_map[loc_key]:
                filtered_data.append((loc_key, val))
    
    # Decoy machine learning prep (heavy distraction)
    feature_matrix = [[val, val**2, val*0.1] for val in calibrated_readings if val > 16.0]
    correlation_approx = sum(feature_matrix[0]) * sum(feature_matrix[-1]) / 100.0
    model_weights = [0.2, 0.5, 0.3]
    predicted_anomaly = sum(w * feature_matrix[0][i] for i, w in enumerate(model_weights)) > 25
    
    # Core analysis function (critical)
    def analyze_readings(data, thresholds):
        total_score = 0
        adjustment_factor = 0.85
        
        # Irrelevant preprocessing (distraction)
        sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
        rank_map = {item[0]: rank for rank, item in enumerate(sorted_data)}
        
        # Actual scoring logic (nested conditions)
        for loc, reading in data:
            base_threshold = thresholds.get(loc, 17.5)
            deviation = reading - base_threshold
            
            # Multi-step conditional scoring
            if deviation > 3.0:
                contribution = 8
            elif deviation > 1.5:
                contribution = 5
            elif deviation > 0:
                contribution = 2
            else:
                contribution = 0
            
            # Apply positional bonus (only every second valid entry)
            loc_index = location_tags.index(loc)
            if loc_index % 2 == 0 and reading > 18.0:
                contribution += 1
            
            total_score += contribution
        
        # Extra obfuscation layer (looks complex but deterministic)
        if len(data) > 0:
            average_contribution = total_score / len(data)
            final_adjustment = int(round(average_contribution * adjustment_factor * 10))
        else:
            final_adjustment = 0
        
        return total_score + final_adjustment

    # Unused diagnostic functions (dead code paths)
    def simulate_failure_modes():
        return [abs(hash('fail')) % 100 for _ in range(5)]
    
    def generate_synthetic_baseline(n):
        return [15.0 + 2.0 * (i % 4) for i in range(n)]
    
    # Key execution point
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Return nothing - just ensure side effect prints
    return None

# Execute the function
def main():
    process_sensor_array()

main()