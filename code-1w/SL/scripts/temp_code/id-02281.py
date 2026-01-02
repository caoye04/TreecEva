from collections import defaultdict, Counter
import math

# Simulated sensor network log with diagnostic tags
timestamped_reads = [
    (1001, 'T:45.2,H:80,A:3'),
    (1003, 'T:46.1,H:78,A:3'),
    (1005, 'T:32.0,H:60,A:1'),
    (1008, 'T:47.3,H:85,A:4'),
    (1010, 'T:45.8,H:79,A:3'),
    (1015, 'T:33.1,H:62,A:1'),
    (1018, 'T:46.9,H:82,A:4'),
    (1020, 'T:45.4,H:77,A:3')
]

# Irrelevant mapping - decoy for attention
mode_labels = {1: 'STANDBY', 2: 'ACTIVE', 3: 'MONITOR', 4: 'CALIBRATE'}
status_counter = Counter()

# Dead function - never called but looks important
def analyze_trend(data):
    trends = []
    for i in range(1, len(data)):
        prev_temp = float(data[i-1][1].split(',')[0].split(':')[1])
        curr_temp = float(data[i][1].split(',')[0].split(':')[1])
        trends.append('UP' if curr_temp > prev_temp else 'DOWN')
    return trends

# Unused helper - distractor computation
def calculate_variance(samples):
    mean = sum(samples) / len(samples)
    return sum((x - mean) ** 2 for x in samples) / len(samples)

# Misleading aggregation path
temp_history = []
for ts, entry in timestamped_reads:
    temp = float(entry.split(',')[0].split(':')[1])
    temp_history.append(temp)

# Real processing begins here — hidden among noise
system_log = []
def parse_entry(log_str):
    parts = log_str.split(',')
    temp = float(parts[0].split(':')[1])
    humidity = float(parts[1].split(':')[1])
    mode = int(parts[2].split(':')[1])
    return (temp, humidity, mode)

for ts, data_str in timestamped_reads:
    t, h, m = parse_entry(data_str)
    status_counter[mode] += 1
    system_log.append((t, h, m, ts))  # Reordered fields

# Filter out non-monitoring modes (A:3 only)
def filter_stable(log_entries):
    filtered = []
    for t, h, m, ts in log_entries:
        if m == 3:  # Only monitoring mode
            filtered.append((t, h, ts))
    return filtered

# Process temperature stability within monitoring window
def process_readings(readings):
    if not readings:
        return -1
    temps = [entry[0] for entry in readings]
    base = temps[0]
    deviations = [abs(t - base) for t in temps]
    avg_dev = sum(deviations) / len(deviations)
    max_dev = max(deviations)
    
    # Secondary check on timing gaps
    timestamps = [r[2] for r in readings]
    intervals = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    avg_interval = sum(intervals) / len(intervals)
    
    # Critical decision logic
    if avg_dev < 1.0 and max_dev < 2.0 and avg_interval > 5:
        score_factor = 100
    else:
        score_factor = 50
    
    # Decoy calculation using humidity (irrelevant to final result)
    humidities = [entry[1] for entry in readings]
    hum_ratio = sum(1 for h in humidities if h > 75) / len(humidities)
    adjustment = math.floor(hum_ratio * 10)
    
    # Final diagnostic is based solely on temperature stability scoring
    return int(score_factor + base)  # base temp added to fixed score

# Key execution point
final_diagnostic = process_readings(filter_stable(system_log))

# Output required format
print(f"Target result: {final_diagnostic}")