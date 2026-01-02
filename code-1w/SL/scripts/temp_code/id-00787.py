def analyze_system_state(timestamp, load_str):
    # Parse system load from string input
    readings = [float(x) for x in load_str.split(',')]
    avg_read = sum(readings) / len(readings)
    peak_read = max(readings)
    
    # Distractor: historical anomaly detection (not used)
    anomaly_window = [x for x in readings if x < avg_read * 0.5]
    anomaly_count = len(anomaly_window)
    stability_score = 100 - (anomaly_count * 5) if anomaly_count > 0 else 100

    # Extract day type from timestamp (format: YYYY-MM-DD-HH)
    parts = timestamp.split('-')
    day_of_week = int(parts[2]) % 7
    hour = int(parts[3])
    
    # Determine base load based on time patterns
    if day_of_week < 5:  # Weekday
        base_load = avg_read * 1.3
    else:  # Weekend
        base_load = avg_read * 0.9
    
    # Simulate maintenance adjustment (semi-relevant but overridden later)
    maintenance_factor = 0.95
    if 'maintenance' in load_str:
        base_load *= maintenance_factor

    # Surge logic based on hour
    if 7 <= hour < 9 or 17 <= hour < 19:
        surge_factor = 1.8
    elif hour == 12:
        surge_factor = 1.4
    else:
        surge_factor = 1.0

    # Apply temperature-like effect from string length
    temp_effect = len(load_str) % 10 / 100.0
    base_load += temp_effect * 5

    # Core workload balancing function
    def balance_workload(load, surge):
        # Misleading intermediate calculation
        theoretical_max = 99.9
        headroom = theoretical_max - load
        adjusted = load * surge
        
        # Real limiting logic
        if adjusted > 85.0:
            adjusted = 85.0 + (adjusted - 85.0) * 0.3  # Diminishing returns
        
        # Use string method to check for overload markers
        marker_check = load_str.upper().replace(' ', '').strip()
        if 'HIGH' in marker_check and adjusted < 80:
            adjusted = 80.0
            
        # Final capping
        capped = min(adjusted, 90.0)
        return capped

    # Critical execution point
    final_load = balance_workload(base_load, surge_factor)
    
    # Dead code path - never reached due to return above
    if final_load < 0:
        final_load = 0
    
    # Irrelevant formatting
    status_label = f"Load:{final_load:.1f}"
    is_critical = status_label.find('90') != -1
    
    print(f"Result: {final_load}")
    return final_load

# Execute with realistic input
def main():
    ts = "2023-11-04-18"
    load_input = "62.1, 65.3, 63.7, HIGH, 64.2"
    result = analyze_system_state(ts, load_input)
    return result

main()