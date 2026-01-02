from itertools import groupby

def analyze_workload(data):
    return [sum(1 for _ in group) for _, group in groupby(data)]

def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings]

def calculate_thermal_output(load, eff):
    base = sum(load)
    adjusted = base * (eff + 0.1)
    penalty = 0
    for val in load:
        if val > 50:
            penalty += val * 0.02
    return adjusted - penalty

def monitor_system_health(sensor_data):
    stats = {}
    filtered = [x for x in sensor_data if x > 0]
    smoothed = normalize_readings(filtered)
    stats['peak'] = max(smoothed)
    stats['avg'] = sum(smoothed) / len(smoothed)
    return stats

def main():
    # Simulated cluster workload readings over time
    raw_load_profile = [45, 67, 52, 33, 78, 89, 44, 51, 60, 72, 68, 55]
    
    # Irrelevant preprocessing step (distractor)
    workload_segments = analyze_workload([x // 10 for x in raw_load_profile])
    
    # Actual relevant data extraction
    cluster_load = [x for x in raw_load_profile if x >= 45]
    
    # Misleading normalization chain (semi-relevant but not used in final calc)
    processed_sensors = [x * 1.05 for x in raw_load_profile]
    health_metrics = monitor_system_health(processed_sensors)
    
    # Efficiency factor derived from system state
    efficiency_factor = 0.85
    if health_metrics['avg'] > 0.5:
        efficiency_factor *= 1.05
    
    # Key computational step
    thermal_capacity = calculate_thermal_output(cluster_load, efficiency_factor)
    
    # Dead code path (distractor)
    if False:
        backup = sum(processed_sensors)
        thermal_capacity += backup * 0.01
    
    # Final result output
    print(f"Result: {thermal_capacity}")

if __name__ == "__main__":
    main()