from itertools import compress, cycle

# Simulate sensor data from a manufacturing line
def generate_sensor_readings():
    base_values = [23, 45, 67, 89, 12, 34, 56, 78]
    adjustments = [0.1, -0.2, 0.3, -0.1, 0.2, -0.3, 0.1, -0.2]
    return [(base + adj) for base, adj in zip(base_values, adjustments)]

# Filter out readings below threshold using lambda
def filter_stable_readings(readings):
    threshold = 30.0
    is_stable = lambda x: x >= threshold
    return list(filter(is_stable, readings))

# Calculate process efficiency based on filtered metrics
def calculate_efficiency(metrics):
    total_output = sum(metrics['values'])
    downtime_events = metrics['downtime']
    calibration_offset = metrics['calibration']
    
    # Irrelevant computation - distractor
    peak_value = max(metrics['values'])
    avg_temp = sum(metrics['temperatures']) / len(metrics['temperatures'])
    temp_correction = avg_temp * 0.01 if avg_temp > 50 else 0
    
    # Core calculation
    base_efficiency = total_output * 0.87
    penalty = downtime_events * 1.5
    adjusted_efficiency = base_efficiency - penalty
    
    # Another red herring
    hypothetical_yield = peak_value * 10 if adjusted_efficiency > 100 else 0
    
    final_efficiency = adjusted_efficiency + calibration_offset
    return round(final_efficiency / (total_output * 0.1), 4)

# Main execution
if __name__ == "__main__":
    raw_readings = generate_sensor_readings()
    stable_readings = filter_stable_readings(raw_readings)
    
    # Simulate auxiliary temperature sensors (not fully used)
    temperature_logs = [22.1, 44.8, 66.9, 89.2, 11.9, 33.7, 56.1, 77.6]
    recent_temps = [t for t in temperature_logs if t > 30]
    
    # Construct process metrics with some redundant fields
    process_metrics = {
        'values': stable_readings,
        'downtime': 3,
        'calibration': 2.5,
        'temperatures': recent_temps,
        'version': '2.1a',
        'timestamp': '2023-11-05T10:30:00Z'
    }
    
    # Dead code path - misleading
    if process_metrics['version'].endswith('b'):
        process_metrics['calibration'] += 1.0
    
    # Key statement
    efficiency_ratio = calculate_efficiency(process_metrics)
    
    # Additional distraction
    status_flags = list(compress(['OK', 'FAIL', 'OK', 'WARN'], cycle([1, 0, 1])))
    summary_code = sum(ord(c) for c in status_flags[0]) // 100
    
    print(f"Result: {efficiency_ratio}")