def analyze_crop_health(sensor_data):
    healthy_count = 0
    total_samples = len(sensor_data)
    temp_sum = 0
    for i, reading in enumerate(sensor_data):
        if reading > 75:
            healthy_count += 1
        temp_sum += reading * 0.1  # Irrelevant accumulation
    return healthy_count


def calculate_harvest_efficiency(plots, thresholds):
    efficiency_scores = []
    debug_log = []
    total_yield = 0
    base_multiplier = 1.5
    
    for idx, (plot, threshold) in enumerate(zip(plots, thresholds)):
        raw_yield = 0
        penalty = 0
        
        # Real logic: count characters in plot ID as proxy for complexity
        complexity_factor = len(plot['id'])
        
        for measurement in plot['readings']:
            if measurement > threshold:
                raw_yield += measurement * base_multiplier
            else:
                penalty += 5
        
        # Actual yield calculation
        adjusted_yield = raw_yield - penalty
        efficiency_scores.append(adjusted_yield)
        
        # Distractor: dead code path (never used)
        if adjusted_yield < 0:
            debug_log.append(f'Negative yield in plot {plot["id"]}')

    # Summing up relevant yields
    total_yield = sum(efficiency_scores)
    
    # Red herring variables
    avg_baseline = sum(thresholds) / len(thresholds) if thresholds else 0
    fake_correction = avg_baseline * 0.3  # Not used
    
    final_yield = int(total_yield + complexity_factor)  # Uses last-seen complexity_factor
    return final_yield

# Sensor data (irrelevant but present)
sensor_readings = [80, 92, 65, 77, 88, 90, 60, 72]
analyze_crop_health(sensor_readings)  # Called but result ignored

# Main data
plots = [
    {'id': 'A1', 'readings': [85, 90, 88]},
    {'id': 'B2', 'readings': [70, 75, 80]},
    {'id': 'C3', 'readings': [95, 87, 92]}
]
thresholds = [80, 72, 85]

# Key computation
final_yield = calculate_harvest_efficiency(plots, thresholds)
print(f'Result: {final_yield}')