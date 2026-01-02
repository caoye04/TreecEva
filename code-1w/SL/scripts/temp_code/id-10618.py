from collections import defaultdict, Counter
import math

# Simulate system telemetry processing with noise and irrelevant transformations
def analyze_throughput(data, window_size):
    if len(data) < window_size:
        return [0]
    averages = []
    for i in range(len(data) - window_size + 1):
        avg = sum(data[i:i+window_size]) / window_size
        averages.append(round(avg, 2))
    return averages

def validate_checksum(sequence):
    # Irrelevant validation function (dead-end)
    checksum = 0
    for val in sequence:
        checksum ^= val
    return checksum == 0

def transform_signal(raw_signal):
    # Distractor: signal processing not used in final result
    transformed = [int(x * math.sin(i)) for i, x in enumerate(raw_signal) if i % 2 == 0]
    normalized = [t / max(transformed) if max(transformed) != 0 else 0 for t in transformed]
    return [round(n, 3) for n in normalized]

def detect_anomalies(metrics, threshold=0.75):
    # Another red herring path
    anomalies = []
    sorted_vals = sorted(metrics)
    cutoff = sorted_vals[int(len(sorted_vals) * threshold)]
    for i, val in enumerate(metrics):
        if val > cutoff:
            anomalies.append((i, val))
    return anomalies

def compute_entropy(values):
    # Unused complex computation
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def filter_critical_events(logs):
    # Misleading filtering logic that isn't used
    critical = []
    for entry in logs:
        if 'ERR' in entry['type'] and entry['severity'] > 2:
            critical.append(entry)
    return critical

def aggregate_metrics(timing_log, flags):
    # Core relevant function buried among distractions
    base_score = 0
    for t in timing_log:
        if t > 50:
            base_score += t // 10
        else:
            base_score += t % 7
    
    # Bit manipulation relevant to final answer
    flag_state = 0
    for f in flags:
        flag_state ^= f  # Accumulate XOR of all flags
    
    # Key calculation step
    temp_result = (base_score * 3) ^ flag_state
    adjustment = len([x for x in timing_log if x % 4 == 0])  # Count multiples of 4
    final_value = (temp_result + adjustment) % 98765
    
    # Decoy operation (not assigned)
    [math.sqrt(x) for x in timing_log if x > 0]  # Unused list comprehension
    
    return final_value

# --- Simulated Data Inputs ---
sensor_readings = [127, 89, 214, 65, 193, 44, 110]
timing_log = [32, 67, 54, 88, 41, 73, 50, 94]
system_flags = [5, 12, 3, 8, 1]

# Irrelevant data structures to increase interference
event_queue = defaultdict(list)
event_queue['input'].extend([1, 1, 0, 1])
event_queue['output'].extend([0, 1, 1, 0])

usage_stats = {
    'cpu': [0.45, 0.67, 0.52, 0.71],
    'mem': [0.78, 0.82, 0.65, 0.91],
    'disk': [0.33, 0.41, 0.39, 0.55]
}

# Dead-end computations (distractors)
throughput_analysis = analyze_throughput(sensor_readings, 3)
validated = validate_checksum(sensor_readings)
signal_processed = transform_signal([1.2, 3.4, 2.1, 5.6, 4.3])
anomaly_list = detect_anomalies(timing_log)
entropy_value = compute_entropy([1, 1, 2, 2, 3, 3, 3])

# Unused log entries simulating real system noise
system_logs = [
    {'ts': 1001, 'type': 'INFO', 'severity': 1},
    {'ts': 1002, 'type': 'ERR', 'severity': 3},
    {'ts': 1003, 'type': 'WARN', 'severity': 2}
]
critical_events = filter_critical_events(system_logs)

# --- Key Execution Point ---
final_diagnostic = aggregate_metrics(timing_log, system_flags)
print(f"Result: {final_diagnostic}")