from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated system telemetry data
timestamps = [100, 101, 103, 106, 110, 115, 121]
raw_events = ['OK', 'ERROR', 'OK', 'WARNING', 'ERROR', 'OK', 'OK']

# Misleading auxiliary variables (distractors)
system_baseline = 42.5
baseline_checksum = sum([system_baseline * i for i in range(5)])
redundant_buffer = [0] * 20
for i in range(len(redundant_buffer)):
    redundant_buffer[i] = (i * 17) % 9

# Core data structure initialization
operational_log = defaultdict(list)
for t, event in zip(timestamps, raw_events):
    operational_log['timestamps'].append(t)
    operational_log['statuses'].append(event)

# Irrelevant transformation chain (dead path)
temp_analysis = []
for i in range(len(operational_log['statuses'])):
    if operational_log['statuses'][i] == 'ERROR':
        temp_analysis.append((i, timestamps[i]))
debug_snapshot = temp_analysis.copy()

# Decoy function that looks important but isn't used in critical path
def compute_health_score(log_data):
    score = 100
    for status in log_data.get('statuses', []):
        if status == 'ERROR':
            score -= 15
        elif status == 'WARNING':
            score -= 5
    return max(score, 0)

# Another decoy: complex but unused calculation
status_cycle = cycle(['OK', 'WARNING', 'ERROR'])
predicted_sequence = list(islice(status_cycle, len(raw_events)))
prediction_accuracy = sum(1 for a, p in zip(raw_events, predicted_sequence) if a == p) / len(raw_events)

# Real processing begins here — subtle because surrounded by noise
def extract_failure_patterns(status_list):
    pattern_count = 0
    for i in range(1, len(status_list)):
        if status_list[i-1] != 'ERROR' and status_list[i] == 'ERROR':
            pattern_count += 1
    return pattern_count

# Secondary metric with plausible but irrelevant logic
def calculate_stability_index(ts_list):
    intervals = [ts_list[i] - ts_list[i-1] for i in range(1, len(ts_list))]
    avg_interval = sum(intervals) / len(intervals)
    variance = sum((x - avg_interval) ** 2 for x in intervals) / len(intervals)
    return round(avg_interval - variance, 3)

# Key analysis function — only one actually contributing to final answer
def analyze_system_state(log):
    statuses = log['statuses']
    
    # Count transitions to ERROR from non-ERROR states
    error_transitions = extract_failure_patterns(statuses)
    
    # Compute frequency distribution (using Counter)
    freq = Counter(statuses)
    error_count = freq.get('ERROR', 0)
    warning_count = freq.get('WARNING', 0)
    
    # Real logic: diagnostic = (error_transitions * 100) + error_count - warning_count
    diagnostic_value = (error_transitions * 100) + error_count - warning_count
    
    # Red herring: modify a global-looking variable that's not used
    global baseline_checksum
    baseline_checksum += diagnostic_value  # Looks important, but irrelevant
    
    return diagnostic_value

# Critical execution point
final_diagnostic = analyze_system_state(operational_log)

# Output result as required
print(f"Result: {final_diagnostic}")