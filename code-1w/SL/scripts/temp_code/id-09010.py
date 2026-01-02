from collections import defaultdict, Counter
import math

# Simulated sensor network data with noise and redundancy
def fetch_sensor_data():
    raw_readings = [
        (101, 23.5, 'C'), (102, 45.0, 'C'), (103, -19.2, 'C'),
        (101, 24.1, 'C'), (104, 0.0, 'C'), (105, 100.0, 'C'),
        (106, 33.3, 'C'), (102, 44.8, 'C'), (107, -50.0, 'C'),
        (108, 78.9, 'C'), (109, 12.4, 'C'), (110, 67.1, 'C')
    ]
    return raw_readings

# Irrelevant auxiliary function - dead code path (distractor)
def compute_fusion_score(temps):
    weighted = sum(t * (i+1) for i, t in enumerate(temps)) / len(temps)
    return weighted * 0.85

# Misleading transformation: looks important but unused in final path
def calibrate_anomaly(readings):
    stats = defaultdict(list)
    for sid, temp, unit in readings:
        if temp < -273.15:
            continue
        stats['range_A' if temp < 0 else 'range_B'].append(temp)
    
    # Decoy calculations
    avg_neg = sum(stats['range_A']) / len(stats['range_A']) if stats['range_A'] else 0
    avg_pos = sum(stats['range_B']) / len(stats['range_B']) if stats['range_B'] else 0
    
    adjustment = abs(avg_neg) * 0.1 if avg_neg else 0.5
    return adjustment  # Never used

# Core processing pipeline
def filter_outliers(data, threshold=2.0):
    temperatures = [temp for _, temp, _ in data]
    mean_temp = sum(temperatures) / len(temperatures)
    variance = sum((x - mean_temp) ** 2 for x in temperatures) / len(temperatures)
    std_dev = math.sqrt(variance)
    
    filtered = [item for item in data if abs(item[1] - mean_temp) <= threshold * std_dev]
    return filtered

# Aggregation with meaningful structure
def aggregate_by_sensor(readings):
    grouped = defaultdict(list)
    for sensor_id, temp, unit in readings:
        grouped[sensor_id].append(temp)
    
    processed = {}
    for sid, temps in grouped.items():
        # Compute multiple metrics - some are distractors
        max_t = max(temps)
        min_t = min(temps)
        median_t = sorted(temps)[len(temps)//2]
        range_t = max_t - min_t
        
        # Only average is actually used later
        avg_t = sum(temps) / len(temps)
        processed[sid] = {'average': avg_t, 'stability': range_t}
    
    return processed

# Secondary analysis with red herring counters
def assess_stability_levels(aggregated):
    counter = Counter()
    for info in aggregated.values():
        stab = info['stability']
        if stab < 1.0:
            level = 'stable'
        elif stab < 5.0:
            level = 'fluctuating'
        else:
            level = 'unstable'
        counter[level] += 1
    
    # This counter is computed but not used in final logic
    total_unstable = counter['unstable']
    return total_unstable  # Unused return

# Critical diagnostic engine
def analyze_readings(aggregated_data):
    # Key logic: sum of averages from sensors with specific ID parity
    relevant_sensors = [v['average'] for k, v in aggregated_data.items() if k % 2 == 1]
    
    # Additional filtering: only those above freezing (0C)
    above_freezing = [avg for avg in relevant_sensors if avg > 0]
    
    # Final computation: harmonic mean scaled by count
    if not above_freezing:
        return 0.0
    
    inv_sum = sum(1 / x for x in above_freezing)
    harmonic_mean = len(above_freezing) / inv_sum
    
    # Scale by number of total sensors (including even IDs)
    scaling_factor = len(aggregated_data)
    result = harmonic_mean * scaling_factor
    
    # Red herring variables (computed but irrelevant)
    total_energy = sum(v['average']**2 for v in aggregated_data.values())
    entropy = -sum((p/len(aggregated_data)) * math.log(p/len(aggregated_data)) 
                   for p in [len(aggregated_data)]*len(aggregated_data)) if aggregated_data else 0
    
    return result

# Orchestration with decoy calls
def main_pipeline():
    raw_data = fetch_sensor_data()
    
    # Apply calibration (result ignored - distraction)
    _ = calibrate_anomaly(raw_data)
    
    cleaned = filter_outliers(raw_data, threshold=1.8)
    processed_data = aggregate_by_sensor(cleaned)
    
    # Assess stability (result ignored - misleading intermediate)
    _ = assess_stability_levels(processed_data)
    
    # Generate fusion score from isolated data (dead end)
    isolated_temps = [temp for _, temp, _ in cleaned if temp < 0]
    _ = compute_fusion_score(isolated_temps)
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_data)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# Execute
main_pipeline()