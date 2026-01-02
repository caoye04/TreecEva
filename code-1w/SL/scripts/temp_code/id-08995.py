from collections import defaultdict, Counter
from itertools import cycle

# Simulated sensor network data processing with diagnostic analysis
def collect_sensor_readings():
    raw_streams = {
        'temp': [23.4, 24.1, 19.5, 25.0, 30.2, 28.7, 22.1, 26.8],
        'pressure': [101.3, 102.1, 99.7, 103.4, 100.1, 102.7, 98.9, 101.8],
        'humidity': [45, 47, 50, 44, 60, 65, 70, 72]
    }
    
    # Irrelevant transformation (distractor)
    normalized = {k: [round((v - min(vals)) / (max(vals) - min(vals)), 3) for v in vals] 
                   for k, vals in raw_streams.items()}
    
    readings = []
    for i in range(len(raw_streams['temp'])):
        reading = defaultdict(float)
        reading['id'] = i + 1000
        reading['temp'] = raw_streams['temp'][i]
        reading['pressure'] = raw_streams['pressure'][i]
        reading['humidity'] = raw_streams['humidity'][i]
        reading['status_flag'] = 1 if reading['temp'] > 25 else 0
        readings.append(reading)
    
    return readings

# Decoy function - looks important but unused in critical path
def analyze_trend_sequence(data):
    trends = []
    for i in range(1, len(data)):
        trend = {}
        for sensor in ['temp', 'pressure', 'humidity']:
            trend[sensor] = 'up' if data[i][sensor] > data[i-1][sensor] else 'down'
        trends.append(trend)
    return trends

# Auxiliary transformation with partial relevance
def classify_environment(temp, hum):
    if temp < 20:
        return 'cold'
    elif temp < 25:
        return 'moderate'
    else:
        return 'warm' if hum < 60 else 'humid'

# Red herring function - processes data but result discarded
def compute_stability_index(stream):
    diffs = [abs(stream[i+1] - stream[i]) for i in range(len(stream)-1)]
    return round(sum(diffs) / len(diffs), 4) if diffs else 0.0

# Core filtering logic (part of critical path)
def filter_anomalous_readings(readings):
    filtered = []
    pressure_sum = 0
    high_temp_count = 0
    
    for r in readings:
        pressure_sum += r['pressure']
        if r['temp'] > 25:
            high_temp_count += 1
            
        # Actual filtering condition
        if r['humidity'] <= 70 and r['pressure'] >= 99.0:
            filtered.append(r)
    
    # Dead computation - uses variables but not in return
    avg_pressure = pressure_sum / len(readings) if readings else 0
    spike_count = sum(1 for r in readings if r['status_flag'] == 1)
    
    return filtered

# Another irrelevant utility
def generate_shift_schedule(operators, days):
    schedule = {}
    rotator = cycle(operators)
    for day in range(1, days + 1):
        schedule[day] = next(rotator)
    return schedule

# Key processing function with distractors
def process_readings(data, thresholds):
    # Initialize various counters (some are decoys)
    diagnostic_score = 0
    complexity_weight = 0.0
    correlation_matrix = [[1.0 for _ in range(3)] for _ in range(3)]
    
    # Simulated weight adjustment (irrelevant)
    for i in range(3):
        for j in range(3):
            if i != j:
                correlation_matrix[i][j] = 0.5 + i * 0.1 - j * 0.05
    
    # Critical diagnostic computation
    temp_violations = 0
    pressure_deviation = 0.0
    humidity_categories = Counter()
    
    base_threshold = thresholds['temp']['critical']
    
    for reading in data:
        temp = reading['temp']
        pressure = reading['pressure']
        hum = reading['humidity']
        
        category = classify_environment(temp, hum)
        humidity_categories[category] += 1
        
        if temp > base_threshold:
            temp_violations += 1
        
        # Pressure deviation from standard atmosphere
        pressure_deviation += abs(pressure - 101.3)
    
    # Compute secondary metrics (some unused)
    avg_deviation = pressure_deviation / len(data) if data else 0
    entropy = 0.0
    total = sum(humidity_categories.values())
    for count in humidity_categories.values():
        if count > 0:
            p = count / total
            entropy -= p * __import__('math').log2(p)
    
    # Complexity weight based on pattern cycles (unused red herring)
    states = [(r['temp'] > 25, r['humidity'] > 50) for r in data]
    transitions = 0
    for i in range(1, len(states)):
        if states[i] != states[i-1]:
            transitions += 1
    
    # Final diagnostic calculation - only this matters
    diagnostic_score = (temp_violations * 100) + int(avg_deviation * 10)
    
    # Multiple distracting assignments below
    diagnostic_score += len(humidity_categories) * 10
    diagnostic_score -= int(entropy * 5)  # Minor but real factor
    complexity_weight = transitions / (len(data) - 1) if len(data) > 1 else 0
    
    final_diagnostic = diagnostic_score + int(complexity_weight * 20)
    
    # This print is NOT part of output requirement - just internal
    return final_diagnostic

# Orphaned data structure (dead code path)
legacy_config = {
    'version': '1.2',
    'calibration_needed': False,
    'last_updated': '2023-11-05'
}

# Main execution flow
if __name__ == '__main__':
    # Initial data collection
    all_readings = collect_sensor_readings()
    
    # Unused stability analysis (distractor)
    temp_stability = compute_stability_index([r['temp'] for r in all_readings])
    pressure_stability = compute_stability_index([r['pressure'] for r in all_readings])
    
    # Filtering step (critical)
    filtered_data = filter_anomalous_readings(all_readings)
    
    # Threshold configuration (critical)
    threshold_map = {
        'temp': {'warning': 25.0, 'critical': 27.0},
        'pressure': {'warning': 99.0, 'critical': 95.0},
        'humidity': {'warning': 60, 'critical': 75}
    }
    
    # Scheduling distraction
    operators = ['Alice', 'Bob', 'Charlie']
    shift_plan = generate_shift_schedule(operators, 7)
    
    # Trend analysis - computed but not used (red herring)
    trends = analyze_trend_sequence(all_readings)
    
    # Core diagnostic processing
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # REQUIRED OUTPUT FORMAT
    print(f"Result: {final_diagnostic}")