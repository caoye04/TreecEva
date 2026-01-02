from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456801, 1623456810, 1623456815]
raw_events = ['read', 'write', 'read', 'read', 'write', 'read']
error_codes = [0, 0, 1, 0, 2, 0]
sensor_readings = [23.4, 24.1, 25.3, 25.3, 26.0, 25.8]

# Irrelevant auxiliary computation (distractor)
def calculate_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

entropy_value = calculate_entropy(raw_events)  # Red herring

# Misleading diagnostic flag (dead code path)
legacy_mode_active = False
device_compatibility_score = 0.87

# Core data transformation
log_entries = []
for i in range(len(timestamps)):
    entry = {
        'time': timestamps[i],
        'event': raw_events[i],
        'err': error_codes[i],
        'temp': sensor_readings[i],
        'priority': 1 if error_codes[i] > 0 else 0
    }
    log_entries.append(entry)

# System flags with multiple decoys
system_flags = {
    'overload': False,
    'legacy_sync': True,
    'buffer_full': False,
    'secure_mode': None,
    'retry_count': 3
}

# Unused complex structure (distractor)
class DiagnosticBuffer:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
    
    def push(self, val):
        self.data = [val] + self.data[:-1]

buffer = DiagnosticBuffer(10)

# Phantom checksum calculation (irrelevant)
temp_checksum = 0
for reading in sensor_readings:
    temp_checksum += int(reading * 10) % 7
temp_checksum = (temp_checksum * 13) % 101  # No effect on final result

# Key pattern analyzer with nested logic
def analyze_pattern(entries, flags):
    # Build frequency map using defaultdict (relevant)
    event_count = defaultdict(int)
    error_severity = 0
    recent_errors = []
    
    for entry in entries:
        event_count[entry['event']] += 1
        if entry['err'] > 0:
            error_severity += entry['err'] ** 2
            recent_errors.append(entry['time'])
    
    # Compute time gaps (distraction with partial relevance)
    time_gaps = []
    for i in range(1, len(entries)):
        gap = entries[i]['time'] - entries[i-1]['time']
        time_gaps.append(gap)
    
    avg_gap = sum(time_gaps) / len(time_gaps) if time_gaps else 0
    
    # Complex conditional with red herrings
    base_score = 0
    if event_count['read'] > event_count['write']:
        base_score += 15
    
    if error_severity > 0 and flags['overload']:
        base_score -= 20
    elif error_severity == 5:  # 1^2 + 2^2 = 5
        base_score += 8
    
    # Bit manipulation decoy
    encoded_flag = 0
    for i, gap in enumerate(time_gaps[:4]):
        encoded_flag ^= (gap << 1) | (i & 1)
    
    # Tuple unpacking with filtering (relevant)
    filtered_temps = [e['temp'] for e in entries if e['err'] == 0]
    temp_avg = sum(filtered_temps) / len(filtered_temps)
    
    # Destructuring assignment (relevant to language feature)
    first_temp, *middle_temps, last_temp = filtered_temps
    
    # Final composite calculation
    stability_index = (last_temp - first_temp) ** 2
    
    # Primary answer computation (non-obvious due to distractions)
    final_diagnostic = int(base_score + temp_avg - stability_index + error_severity)
    
    # Dead code branch (misleading)
    if flags['legacy_sync'] and not flags['secure_mode']:
        final_diagnostic = final_diagnostic // 2  # Never executed
    
    return final_diagnostic

# Critical execution point
final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Result: {final_diagnostic}")