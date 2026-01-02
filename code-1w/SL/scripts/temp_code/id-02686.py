from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
raw_readings = [127, 193, 255, 64, 128]
status_flags = [True, False, True, True, False]

# Irrelevant preprocessing - red herring
shifted_values = [x << 2 for x in raw_readings]
normalized = [x / 255.0 for x in raw_readings]
sine_weighted = [math.sin(x) for x in normalized]

# Distractor: unused function
def decrypt_signal(data):
    return [d ^ 0xFF for d in data]

# Distractor: dead code path
temporary_buffer = []
for val in raw_readings:
    if val > 128:
        temporary_buffer.append(val >> 1)

# Real processing begins: construct log entries
log_entries = []
for i in range(len(timestamps)):
    entry = {
        'ts': timestamps[i],
        'val': raw_readings[i],
        'flag': status_flags[i],
        'meta': f"log_{i}" # unused field
    }
    log_entries.append(entry)

# System state with multiple fields, some irrelevant
system_state = {
    'mode': 'ACTIVE',
    'threshold': 128,
    'version': 2.1,
    'debug': False,
    'mask': 0x7F,
    'calibration': [0.98, 1.02, 1.0] # unused
}

# Misleading intermediate calculation
candidate_scores = []
for entry in log_entries:
    score = 0
    if entry['flag']:
        score += entry['val'] // 16
    else:
        score += entry['val'] % 16
    candidate_scores.append(score)

# Decoy aggregation using irrelevant logic
decoy_counter = Counter()
for entry in log_entries:
    key = 'high' if entry['val'] > system_state['threshold'] else 'low'
    decoy_counter[key] += 1

# Real metric computation
bit_analysis = defaultdict(int)
for entry in log_entries:
    masked_val = entry['val'] & system_state['mask']  # Apply mask 0x7F (127)
    parity = bin(masked_val).count('1') % 2
    bit_analysis[parity] += 1

# Secondary real computation: time gaps
time_gaps = []
for i in range(1, len(timestamps)):
    time_gaps.append(timestamps[i] - timestamps[i-1])
avg_gap = sum(time_gaps) / len(time_gaps)

event_count = len([e for e in log_entries if e['flag']])

# Core logic: conditional bit count weighted by event frequency
base_metric = bit_analysis[1] * 100  # Count of odd-parity masked values
if event_count > 2:
    base_metric += int(avg_gap)
else:
    base_metric -= int(avg_gap)

# Final transformation via complex function
def aggregate_metrics(entries, state):
    # Extract relevant features
    threshold = state['threshold']
    active_count = sum(1 for e in entries if e['val'] > threshold)
    
    # Irrelevant local transformation
    inverted_map = {e['ts']: e['val'] ^ 0xFF for e in entries}
    
    # More distractions
    summary_stats = {
        'max': max(e['val'] for e in entries),
        'min': min(e['val'] for e in entries),
        'range': max(e['val'] for e in entries) - min(e['val'] for e in entries)
    }
    
    # Actual dependency on prior base_metric (computed outside)
    global base_metric
    adjustment = active_count * 17
    
    # Critical operation: combines external metric and internal logic
    if state['mode'] == 'ACTIVE' and summary_stats['range'] > 100:
        result = base_metric + adjustment
    else:
        result = base_metric - adjustment
    
    # Final nonlinear transformation
    result = int((result ** 0.5) * 10) if result > 0 else result
    
    return result

# Execute final statement
final_diagnostic = aggregate_metrics(log_entries, system_state)
print(f"Target result: {final_diagnostic}")