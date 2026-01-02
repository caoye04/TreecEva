from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780 + i*30 for i in range(100)]
raw_sensor_data = [((i * 17) % 101) + ((i * 3) % 15) for i in range(100)]

# Irrelevant auxiliary data (distractor)
user_sessions = defaultdict(lambda: {'start': 0, 'active': False})
for i in range(15):
    user_sessions[f'user_{i}'] = {'start': 1623456780 + i*100, 'active': i % 3 == 0}

# System health indicators (mixed relevant and irrelevant)
cpu_load_history = [(t % 90) / 100.0 for t in range(100)]
disk_io_ops = [abs((t * 7) % 100 - 50) for t in range(100)]
memory_usage = [((t * 13) % 85) for t in range(100)]

# Core diagnostic thresholds (only some are actually used later)
system_thresholds = {
    'critical_load': 0.85,
    'elevated_temp': 75,
    'io_bottleneck': 40,
    'safe_memory': 80,
    'decay_factor': 0.92
}

# Log entry structure with red herring fields
log_entries = []
for i in range(len(timestamps)):
    entry = {
        'ts': timestamps[i],
        'sensor_val': raw_sensor_data[i],
        'temp_c': 45 + ((i * 5) % 40),
        'load': cpu_load_history[i],
        'mem_pct': memory_usage[i],
        'disk_op': disk_io_ops[i],
        'checksum': (raw_sensor_data[i] ^ timestamps[i]) & 0xFF,
        'status_flag': 'OK' if i % 4 != 3 else 'WARN'
    }
    log_entries.append(entry)

# Decoy analysis function (never called - dead code path)
def analyze_user_patterns(sessions):
    active_count = sum(1 for s in sessions.values() if s['active'])
    avg_start = sum(s['start'] for s in sessions.values()) / len(sessions)
    return {'concurrent_users': active_count, 'baseline_time': avg_start}

# Auxiliary transformation (used indirectly)
def smooth_series(series, factor=0.85):
    if not series:
        return []
    smoothed = [series[0]]
    for i in range(1, len(series)):
        smoothed.append(factor * smoothed[-1] + (1 - factor) * series[i])
    return smoothed

# Real-time anomaly detection using lambda with closures (relevant)
def create_detector(threshold):
    count = 0
    return lambda x: (x > threshold, (count + 1) if x > threshold else count)

# Complex preprocessing with distractors
event_categories = defaultdict(list)
for entry in log_entries:
    category = 'thermal' if entry['temp_c'] > 60 else 'standard'
    category = 'io_intensive' if entry['disk_op'] > 45 else category
    category = 'load_spike' if entry['load'] > 0.7 else category  # rarely triggered
    event_categories[category].append(entry)

# Misleading metric computation (partially unused)
aggregated_stats = {}
for cat, events in event_categories.items():
    values = [e['sensor_val'] for e in events]
    if values:
        mean_val = sum(values) / len(values)
        variance = sum((v - mean_val)**2 for v in values) / len(values)
        aggregated_stats[cat] = {
            'count': len(events),
            'avg': mean_val,
            'var': variance,
            'peak': max(values)
        }

# Sensor recalibration matrix (red herring - looks important but unused)
recalibration_matrix = [
    [1.02, -0.01, 0.005],
    [0.00,  0.98, 0.015],
    [0.01,  0.00, 1.00]
]

# Core processing function with multiple concepts
def process_metrics(entries, thresholds):
    # Extract temporal sensor readings
    sensor_readings = [e['sensor_val'] for e in entries]
    
    # Smooth the signal (relevant)
    filtered_signal = smooth_series(sensor_readings, thresholds['decay_factor'])
    
    # Detect sustained deviations using stateful logic
    deviation_counter = 0
    for val, filt in zip(sensor_readings, filtered_signal):
        if abs(val - filt) > 15:  # heuristic threshold
            deviation_counter += 1
    
    # Analyze periodicity via modular patterns (key insight)
    periodic_outliers = 0
    for i, entry in enumerate(entries):
        if (entry['ts'] % 100 < 10) and (entry['sensor_val'] % 13 == 0):
            periodic_outliers += 1
    
    # Memory pressure analysis (irrelevant branch)
    high_mem_events = [e for e in entries if e['mem_pct'] > thresholds['safe_memory']]
    suspected_leaks = 0
    for event in high_mem_events:
        if event['load'] < 0.5:  # low CPU but high memory - suspicious
            suspected_leaks += 1
    
    # Final diagnostic calculation - only this matters
    base_score = deviation_counter * 17
    adjustment = periodic_outliers * 3
    
    # Critical formula using bitwise and arithmetic ops
    final_value = (base_score << 2) - (adjustment * 5)
    
    # Masking operation that cancels out decoy influence
    mask = 0xFFFF
    masked_result = final_value & mask
    
    # Normalize to positive diagnostic code
    normalized_diagnostic = (masked_result + 1000) % 9000
    
    # This is the actual answer variable
    final_diagnostic = int(math.sqrt(normalized_diagnostic ** 2)) // 10
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")