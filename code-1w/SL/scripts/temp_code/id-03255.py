def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature in Celsius)
    raw_readings = [23.5, 19.0, 25.3, 20.1, 30.2, 18.7, 27.8, 22.4, 24.6]
    
    # Irrelevant auxiliary data - red herring
    device_ids = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9']
    deployment_zones = ['North', 'South', 'East', 'West', 'Central', 'Roof', 'Basement', 'Lab', 'Field']
    zone_temps = {zone: temp for zone, temp in zip(deployment_zones, raw_readings)}
    avg_zone_temp = sum(zone_temps.values()) / len(zone_temps)  # Distractor computation

    # Calibration parameters
    base_offset = 1.2
    sensor_drift = [0.1, -0.05, 0.2, 0.0, 0.15, -0.1, 0.08, 0.03, -0.07]
    adjusted_drift = [(d + base_offset) % 0.5 for d in sensor_drift]  # Misleading transformation

    # Filter logic: only sensors above median temperature
    sorted_readings = sorted(raw_readings)
    median_temp = sorted_readings[len(sorted_readings) // 2]
    high_temp_sensors = [i for i, temp in enumerate(raw_readings) if temp > median_temp]
    
    # Extract corresponding devices and zones (irrelevant but plausible)
    active_devices = [device_ids[i] for i in high_temp_sensors]
    active_zones = [deployment_zones[i] for i in high_temp_sensors]
    
    # Actual filtered data based on index parity - subtle relevant condition
    filtered_indices = [i for i in high_temp_sensors if i % 2 == 1]
    filtered_data = [raw_readings[i] for i in filtered_indices]
    
    # Decoy statistical analysis
    outlier_count = 0
    for val in raw_readings:
        if abs(val - sum(raw_readings)/len(raw_readings)) > 5:
            outlier_count += 1
    normalized_scores = [round((x - 18.7) / (30.2 - 18.7), 3) for x in raw_readings]  # Unused path

    # Key calibration factor derived from modular arithmetic on lengths
    n_filtered = len(filtered_data)
    n_active = len(active_devices)
    calibration_factor = (n_filtered * 7 + n_active * 3) % 4 + 1.5  # Evaluates to 3.5

    # Real processing function (appears complex due to nesting)
    def process_readings(data, factor):
        if not data:
            return 0.0
        
        transformed = []
        for idx, val in enumerate(data):
            # Apply non-linear transformation with integer division
            step1 = (val + factor) ** 1.5
            step2 = int(step1) // (idx + 1) if idx > 0 else int(step1)
            step3 = round(step2 * 0.87, 2)
            transformed.append(step3)
            
            # Nested conditional decoy
            if step3 > 100:
                alert_code = hash('HIGH_READING') % 1000  # Dead code branch
                break
        
        # Aggregate using weighted sum based on position
        total_weight = 0
        weighted_sum = 0
        for i, v in enumerate(transformed):
            weight = 2 ** (len(transformed) - i)  # Higher weight for earlier elements
            weighted_sum += v * weight
            total_weight += weight
            
            # Spurious entropy calculation
            if i > 0:
                delta = abs(v - transformed[i-1])
                normalized_delta = delta / (max(transformed) - min(transformed) + 1e-8)
                shannon_index = -sum(p * p for p in [normalized_delta, 1-normalized_delta])

        return int(weighted_sum / total_weight) if total_weight != 0 else 0

    # Secondary irrelevant transform chain
    inverted_data = [30.2 - x for x in raw_readings]
    compression_ratio = len(raw_readings) / (len(inverted_data) + 1)  # Always < 1

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Unused diagnostic dump
    debug_snapshot = {
        'raw_count': len(raw_readings),
        'filtered': filtered_data,
        'calibration': calibration_factor,
        'entropy_shadow': sum([x*x for x in adjusted_drift])
    }
    
    return final_diagnostic

# Execute and capture result
def main():
    result = analyze_sensor_network()
    return result

main()