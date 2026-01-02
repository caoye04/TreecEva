def parse_log_line(line):
    if 'ERROR' in line:
        return (1, 10)
    elif 'WARNING' in line:
        return (2, 5)
    elif 'INFO' in line:
        return (3, 1)
    else:
        return (0, 0)

# Simulated system log entries
temp_data_cache = ["temp_1=45", "temp_2=67", "status=active"]
config_settings = {"timeout": 30, "retries": 3, "mode": "diagnostic"}

log_entries = [
    "[TIMESTAMP=1] SYSTEM INIT OK",
    "[TIMESTAMP=2] SENSOR_READING value=23.5",
    "[TIMESTAMP=3] ERROR: disk full",
    "[TIMESTAMP=4] WARNING: high memory usage",
    "[TIMESTAMP=5] INFO: user login",
    "[TIMESTAMP=6] ERROR: failed connection",
    "[TIMESTAMP=7] WARNING: cpu spike",
    "[TIMESTAMP=8] INFO: backup completed"
]

# Irrelevant processing - red herring
buffer_overflow_sim = [x.upper() for x in temp_data_cache if "temp" in x]
metadata_index = {}
for i, item in enumerate(config_settings.items()):
    metadata_index[item[0]] = i * 2

# System flags with decoy values
debug_mode = True
system_flags = {
    "verbose": True,
    "maintenance": False,
    "audit_required": True,
    "simulated_failure": None  # unused
}

# Misleading intermediate calculation
baseline_score = 0
for entry in log_entries:
    if 'OK' in entry or 'INIT' in entry:
        baseline_score += 1

# Auxiliary function that is never called - dead code path
def compute_health_factor(metrics):
    total = 0
    for m in metrics:
        if m > 0:
            total += m ** 0.5
    return total / len(metrics) if metrics else 0

# Another decoy function
def analyze_temporal_pattern(logs):
    timestamps = []
    for log in logs:
        if "TIMESTAMP" in log:
            ts_part = log.split("=")[1].split("]")[0]
            if ts_part.isdigit():
                timestamps.append(int(ts_part))
    return max(timestamps) - min(timestamps) if timestamps else 0

# Core logic buried among distractions
classification_count = {1: 0, 2: 0, 3: 0}
severity_accumulator = {1: 0, 2: 0, 3: 0}

for line in log_entries:
    category, severity = parse_log_line(line)
    if category in classification_count:
        classification_count[category] += 1
        severity_accumulator[category] += severity

# Secondary irrelevant transformation
formatted_diagnostics = []
for line in log_entries:
    clean_line = line.replace('[', '').replace(']', '')
    formatted_diagnostics.append(clean_line.title())

# Complex conditional with partial relevance
if system_flags["verbose"] and len(log_entries) > 5:
    avg_severity = (
        (severity_accumulator[1] * 3) + 
        (severity_accumulator[2] * 2) + 
        (severity_accumulator[3] * 1)
    ) / len(log_entries)
else:
    avg_severity = 0

# Red herring: unused statistical calculation
median_value = sorted(severity_accumulator.values())[len(severity_accumulator)//2]

# Distractor list comprehension with string methods
processed_lines = [
    line.split(':')[-1].strip().lower() 
    for line in log_entries 
    if ':' in line and line.split(':')[0].strip() in ['ERROR', 'WARNING']
]

# Key aggregation logic hidden among noise
def aggregate_metrics(logs, flags):
    error_count = 0
    warning_count = 0
    info_count = 0
    total_priority = 0
    
    for log in logs:
        if 'ERROR' in log:
            error_count += 1
            total_priority += 10
        elif 'WARNING' in log:
            warning_count += 1
            total_priority += 5
        elif 'INFO' in log:
            info_count += 1
            total_priority += 1
    
    # Real computation
    base_metric = error_count * 100 + warning_count * 10 + info_count
    adjustment = 5 if flags["audit_required"] else -5
    final_score = base_metric + total_priority + adjustment
    
    # Decoy operations inside function
    temp_result = [base_metric, adjustment]
    temp_result.append(sum(temp_result))
    
    return final_score

# Unused variable - distraction
diagnostic_snapshot = {
    "entries_processed": len(log_entries),
    "error_tally": classification_count[1],
    "timestamp_range": analyze_temporal_pattern(log_entries)
}

# Critical execution point
final_diagnostic = aggregate_metrics(log_entries, system_flags)

# Output the target result
print(f"Target result: {final_diagnostic}")