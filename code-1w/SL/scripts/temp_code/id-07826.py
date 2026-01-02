from collections import defaultdict, Counter

# Simulate sensor data with some noise and metadata
data = [
    {'sensor': 'A', 'value': 12, 'status': 'active', 'timestamp': 100},
    {'sensor': 'B', 'value': 8,  'status': 'active', 'timestamp': 101},
    {'sensor': 'A', 'value': 15, 'status': 'active', 'timestamp': 102},
    {'sensor': 'C', 'value': 5,  'status': 'idle',   'timestamp': 103},
    {'sensor': 'B', 'value': 7,  'status': 'active', 'timestamp': 104},
    {'sensor': 'A', 'value': 10, 'status': 'active', 'timestamp': 105},
]

weights = {'A': 1.5, 'B': 2.0, 'C': 0.5}

def preprocess_data(records):
    # Filter only active sensors
    active_records = [r for r in records if r['status'] == 'active']
    
    # Track first and last occurrence per sensor
    first_occurrence = {}
    last_occurrence = {}
    for r in active_records:
        sid = r['sensor']
        if sid not in first_occurrence:
            first_occurrence[sid] = r
        last_occurrence[sid] = r
    
    # Extract values from last occurrence only
    latest_values = {r['sensor']: r['value'] for r in last_occurrence.values()}
    
    # Compute rolling average for each sensor (for distraction)
    rolling_avg = defaultdict(list)
    for r in active_records:
        rolling_avg[r['sensor']].append(r['value'])
    avg_vals = {k: sum(v) / len(v) for k, v in rolling_avg.items()}
    
    # Return both latest and average (only latest used later)
    return latest_values, avg_vals, first_occurrence

def calculate_adjustment_factor(timestamps):
    # Dummy function to add interference
    if len(timestamps) > 10:
        return 0.9
    elif len(timestamps) > 5:
        return 1.05
    else:
        return 1.0

def calculate_final_score(data, weights):
    # Preprocess to get relevant values
    latest, averages, firsts = preprocess_data(data)
    
    # Extract timestamps for adjustment (but use constant instead)
    all_timestamps = [r['timestamp'] for r in data]
    adjustment = calculate_adjustment_factor(all_timestamps)  # Not actually used
    
    # Introduce distractor logic with Counter
    status_counter = Counter(r['status'] for r in data)
    idle_count = status_counter['idle']
    active_count = status_counter['active']
    
    # Spurious normalization factor (unused)
    total_count = idle_count + active_count
    norm_factor = total_count / (total_count + 1) if total_count > 0 else 1
    
    # Core scoring logic: weighted sum of latest values
    score = 0
    for sensor_id, value in latest.items():
        weight = weights.get(sensor_id, 1.0)
        contribution = value * weight
        score += contribution
    
    # Apply fixed adjustment (bypassing calculated one)
    final_adjustment = 0.8 if idle_count > 0 else 1.0
    final_score = score * final_adjustment
    
    # Additional red herring: conditional expression with no effect
    _ = 100 if final_score > 50 else -100
    
    return final_score

# Main execution
latest_vals, avg_vals, firsts = preprocess_data(data)
timestamps = [r['timestamp'] for r in data]
baseline = sum(avg_vals.values())

# Key statement
final_score = calculate_final_score(data, weights)

print(f"Result: {final_score}")