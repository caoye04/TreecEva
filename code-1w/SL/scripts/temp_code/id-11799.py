from collections import defaultdict, Counter
import math

# Simulated sensor network data with health metrics
def analyze_sensor_network():
    raw_readings = [23.4, 19.1, 25.6, 20.3, 21.8, 24.0, 18.7, 22.5]
    calibration_offsets = {'s1': 0.2, 's2': -0.1, 's3': 0.3, 's4': -0.2}
    
    # Irrelevant statistical analysis (distractor)
    mean_reading = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_reading)**2 for x in raw_readings) / len(raw_readings)
    std_deviation = math.sqrt(variance)
    z_scores = [(x - mean_reading) / std_deviation for x in raw_readings]
    
    # Health classification using defaultdict (relevant)
    health_status = defaultdict(str)
    for i, val in enumerate(raw_readings):
        if val < 19.0:
            health_status[f'sensor_{i+1}'] = 'critical'
        elif val < 22.0:
            health_status[f'sensor_{i+1}'] = 'warning'
        else:
            health_status[f'sensor_{i+1}'] = 'normal'
    
    # Misleading transformation chain (dead path)
    transformed_data = []
    for reading in raw_readings:
        adjusted = reading * 1.02 + 0.5
        normalized = (adjusted - 18.0) / (26.0 - 18.0)
        encoded = int(normalized * 100)
        transformed_data.append(encoded)
    
    # Unused recursive function (red herring)
    def calculate_entropy(data, depth=0):
        if depth >= 3 or len(data) <= 1:
            return 0.0
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        return 1 + calculate_entropy(left, depth+1) + calculate_entropy(right, depth+1)
    
    entropy_estimate = calculate_entropy(raw_readings)
    
    # Core logic hidden among distractions
    status_counts = Counter(health_status.values())
    critical_count = status_counts['critical']
    warning_count = status_counts['warning']
    normal_count = status_counts['normal']
    
    base_score = 100 - (critical_count * 15) - (warning_count * 5)
    stability_bonus = 10 if normal_count >= 5 else 0
    
    # Complex conditional offset (nested logic)
    system_age_years = 7
    maintenance_records = [True, False, True, True, False]
    recent_maintenance = any(maintenance_records[-2:])
    
    if system_age_years > 5:
        if recent_maintenance:
            system_offset = 8
        else:
            system_offset = -12
    else:
        system_offset = 5
    
    # Secondary distraction: matrix-like operations with no impact
    correlation_matrix = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if i != j:
                correlation_matrix[i][j] = abs(i - j) * 0.1
    
    # Key calculation buried in context
    aggregate_health_score = base_score + stability_bonus
    diagnostic_log = []
    diagnostic_log.append(f'Base: {base_score}, Bonus: {stability_bonus}')
    
    # Critical execution point
    final_diagnostic = aggregate_health_score + system_offset
    
    # Final red herring: unused optimization path
    def optimize_threshold(data, target='normal'):
        best_shift = 0
        best_count = 0
        for shift in range(-5, 6):
            temp_counts = Counter()
            for val in data:
                adj_val = val + shift * 0.1
                if adj_val < 19.0:
                    temp_counts['critical'] += 1
                elif adj_val < 22.0:
                    temp_counts['warning'] += 1
                else:
                    temp_counts['normal'] += 1
            if temp_counts[target] > best_count:
                best_count = temp_counts[target]
                best_shift = shift
        return best_shift
    
    optimal_shift = optimize_threshold(raw_readings)
    
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()