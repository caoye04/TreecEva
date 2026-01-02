from collections import defaultdict, Counter
import math

# Simulated system log processing with diagnostic analysis

def preprocess_logs(raw_logs):
    processed = []
    for log in raw_logs:
        parts = log.split(' ')
        timestamp = int(parts[0])
        level = parts[1]
        component = parts[2]
        code = int(parts[3])
        processed.append((timestamp, level, component, code))
    return processed

# Irrelevant helper - decoy function (dead path)
def decrypt_signal(x):
    return (x * 17) ^ 255

# Another red herring: signal harmonics calculation (unused)
def compute_harmonics(data):
    total = 0
    for i in range(len(data)):
        if i % 3 == 0:
            total += int(math.sin(i) * 100)
    return total

# Misleading aggregation: looks important but not used in final result
tamper_score = 0
def check_integrity(seq):
    global tamper_score
    score = 0
    for i, val in enumerate(seq):
        if val % 7 == 0 and i % 2 == 1:
            score += 1
    tamper_score = score * 2
    return score > 5

# Core logic buried among distractions
def detect_anomalies(entries):
    anomaly_count = 0
    last_time = -1
    gap_sum = 0
    
    for ts, lvl, comp, code in entries:
        if comp == "SEC" and lvl == "WARN":
            anomaly_count += 1
        if last_time != -1:
            gap = ts - last_time
            gap_sum += gap
        last_time = ts
    
    avg_gap = gap_sum / len(entries) if entries else 0
    # Key threshold logic
    if anomaly_count >= 3 and avg_gap < 500:
        return True, anomaly_count
    return False, anomaly_count

# Distractor: complex bit analysis (not actually used)
def analyze_bits(x):
    ones = bin(x).count('1')
    zeros = 32 - ones
    return ones ^ zeros

# Main pattern analyzer - this one matters
def analyze_pattern(logs, flags):
    # Real work starts here
    event_counter = defaultdict(int)
    severity_map = {'ERR': 3, 'WARN': 2, 'INFO': 1}
    total_severity = 0
    component_load = Counter()
    
    for ts, lvl, comp, code in logs:
        event_counter[comp] += 1
        component_load[comp] += severity_map.get(lvl, 0)
        total_severity += severity_map.get(lvl, 0)
    
    # Critical condition chain
    sec_events = event_counter['SEC']
    net_events = event_counter['NET']
    high_load = sum(1 for x in component_load.values() if x > 4)
    
    flag_state = flags & 0b1101  # Extract relevant bits
    trigger_condition = (sec_events > 2) and (net_events % 2 == 1) and (flag_state == 0b1101)
    
    intermediate = total_severity * 100 + high_load
    
    # This branch contains the actual answer path
    if trigger_condition:
        adjustment = 0
        if component_load['DB'] > 0:
            adjustment = 5
        elif component_load['API'] > 2:
            adjustment = -3
        final_value = intermediate + adjustment  # Final computation
    else:
        # Dead end with misleading large numbers
        backup = 0
        for i in range(100):
            backup += (i * i) % 97
        final_value = 999999  # Decoy result
    
    return final_value

# --- Simulation setup ---
raw_log_data = [
    "100 INFO API 200",
    "150 WARN SEC 401",
    "200 ERR DB 500",
    "250 WARN SEC 403",
    "300 INFO NET 200",
    "350 WARN SEC 401",
    "400 ERR API 500",
    "450 INFO NET 200",
    "500 WARN SEC 403"
]

# Unused data structure - distractor
correlation_matrix = [
    [1, 0.5, 0.3],
    [0.5, 1, 0.7],
    [0.3, 0.7, 1]
]

# Prepare inputs
log_entries = preprocess_logs(raw_log_data)
system_flags = 0b1101  # Meets condition

# Red herring call - looks important
check_integrity([14, 21, 28, 35])

# Actual key computation
final_diagnostic = analyze_pattern(log_entries, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")