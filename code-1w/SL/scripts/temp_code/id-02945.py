def analyze_component_health(reading, threshold_map):
    status_flags = {}
    for key, value in reading.items():
        if key == 'voltage':
            status_flags['voltage'] = 'OK' if value > threshold_map['voltage_low'] else 'LOW'
        elif key == 'temperature':
            status_flags['temp'] = 'CRITICAL' if value > threshold_map['overheat'] else ('WARNING' if value > threshold_map['high_temp'] else 'NORMAL')
        elif key == 'load':
            status_flags['load'] = 'HIGH' if value > 85 else 'ACCEPTABLE'
    return status_flags


def calculate_performance(results, limits):
    scores = []
    penalties = 0
    temp_warning_count = 0
    
    # Irrelevant pre-processing: simulate calibration offset (not used in final logic)
    calibration_offset = sum([len(str(x)) for x in limits.values()]) % 7
    baseline_adjustment = (calibration_offset * 1.5) if calibration_offset > 3 else 0
    
    for idx, entry in enumerate(results):
        raw_score = 0
        health_status = analyze_component_health(entry, limits)
        
        # Core scoring logic
        if entry['voltage'] > limits['voltage_low']:
            raw_score += 25
        if health_status['temp'] == 'NORMAL':
            raw_score += 30
        elif health_status['temp'] == 'WARNING':
            raw_score += 15
        # CRITICAL gives 0
        
        if health_status['load'] == 'ACCEPTABLE':
            raw_score += 20
            
        # Bonus for balanced operation
        if abs(entry['voltage'] - 120) < 10 and entry['load'] < 75:
            raw_score += 10
        
        # Accumulate temp warnings for later distraction
        if health_status['temp'] in ['WARNING', 'CRITICAL']:
            temp_warning_count += 1
            
        scores.append(raw_score)
    
    # Distraction: unused aggregation
    avg_score = sum(scores) / len(scores) if scores else 0
    max_penalty = min(temp_warning_count * 2, 10)
    adjusted_avg = avg_score - max_penalty + baseline_adjustment  # Not used
    
    # Final computation with conditional expression
    total_base = sum(scores)
    bonus_granted = len([s for s in scores if s >= 70])
    final_score = total_base + (bonus_granted * 5) if bonus_granted >= 2 else total_base - 10
    
    # Unused set operations for interference
    unique_scores = set(scores)
    potential_bonuses = {5, 10, 15}
    eligible_bonuses = unique_scores & potential_bonuses  # Computed but not used
    
    return final_score

# Simulated benchmark data
benchmark_results = [
    {'voltage': 118, 'temperature': 67, 'load': 70},
    {'voltage': 122, 'temperature': 73, 'load': 88},
    {'voltage': 115, 'temperature': 59, 'load': 65},
    {'voltage': 125, 'temperature': 85, 'load': 72}
]

thresholds = {
    'voltage_low': 110,
    'overheat': 80,
    'high_temp': 65
}

# Key execution point
final_score = calculate_performance(benchmark_results, thresholds)
print(f"Target result: {final_score}")