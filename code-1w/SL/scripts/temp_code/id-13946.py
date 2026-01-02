from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data for a distributed system health monitor
def generate_synthetic_load():
    return [i * 2 + (i % 3) for i in range(100) if i % 7 != 0]

# Irrelevant helper: formats timestamps (not used in computation)
def format_timestamp(ts):
    hours, rem = divmod(ts, 3600)
    mins, sec = divmod(rem, 60)
    return f'{int(hours):02}:{int(mins):02}:{sec:05.2f}'

# Misleading preprocessing step with decoy outputs
def analyze_outliers(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    outliers = [x for x in data if abs(x - mean_val) > 2 * std_dev]
    outlier_report = {'count': len(outliers), 'severity': 'high' if len(outliers) > 10 else 'low'}
    return outlier_report  # Not used later

# Core logic disguised among red herrings
def filter_critical_events(logs):
    critical = []
    for entry in logs:
        if entry % 10 == 0 and entry > 50:
            critical.append(entry)
    return critical

# Bit manipulation decoy (looks relevant but isn't)
def compute_checksum(value):
    chk = 0
    for b in f'{value:b}':
        chk ^= int(b)
    return chk + 1000  # Dead-end computation

# Real transformation chain (obfuscated by noise)
def aggregate_by_phase(data, phases=5):
    chunks = defaultdict(list)
    cyc = cycle(range(phases))
    for val in data:
        chunks[next(cyc)].append(val)
    
    # Only phase 0 is actually used later
    return {k: sum(v) for k, v in chunks.items()}

# Main processing with conditional logic and distractors
def evaluate_stability(metrics):
    status_flags = []
    temp_alert = False
    
    for k, v in metrics.items():
        if k == 0:
            if v > 1500:
                temp_alert = True
            checksummed = compute_checksum(v)  # Red herring call
            status_flags.append(temp_alert and (checksummed % 2 == 0))
        elif k == 3:
            status_flags.append(v < 800)
        else:
            status_flags.append(False)
    
    return any(status_flags)  # Distracting, not final output

# Actual answer derivation buried in logic
thresholds = [120, 240, 360]

health_data = generate_synthetic_load()

decoys = {'a': analyze_outliers(health_data), 'b': [compute_checksum(x) for x in range(5)]}

# Real signal extraction
phase_sums = aggregate_by_phase(health_data)

critical_events = filter_critical_events(health_data)
event_count_metric = len(critical_events) * 2  # Used in final calculation

# Fake branching path
if evaluate_stability(phase_sums):
    base_score = 100
else:
    base_score = 200  # This branch always taken due to logic above

# Hidden key computation
shifted_events = [e // 4 for e in critical_events if e > 100]

event_sum = sum(shifted_events)

# Final computation uses only specific elements
final_diagnostic = event_sum - event_count_metric + phase_sums[0]

# Decoy print statements (commented out)
# print(f'Debug: {decoys}')
# print(f'Status: {evaluate_stability(phase_sums)}')

Result: {final_diagnostic}