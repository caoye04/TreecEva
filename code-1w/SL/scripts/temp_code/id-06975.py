def analyze_efficiency(logs):
    total_entries = len(logs)
    critical_events = {entry for entry in logs if 'ERROR' in entry}
    warning_count = sum(1 for entry in logs if 'WARN' in entry)
    
    # Irrelevant calculation (distractor)
    avg_length = sum(len(entry) for entry in logs) / max(total_entries, 1)
    size_factor = int(avg_length // 10)

    high_priority = [e for e in critical_events if 'CRITICAL' in e]
    severity = len(high_priority) * 2 + len(critical_events)

    return total_entries, severity, warning_count


def evaluate_performance(items_produced, defects):
    base_rate = items_produced / max(defects, 1)
    bonus = 10 if items_produced > 50 else 0
    penalty = defects * 2
    
    # Semi-relevant transformation (not used directly)
    efficiency_ratio = (items_produced - defects) / max(items_produced, 1)
    
    # Actual result computation
    raw_score = base_rate * 5 + bonus - penalty
    return int(raw_score)

# Simulated dataset
log_data = [
    'INFO: system boot',
    'ERROR: disk failure',
    'WARN: high memory usage',
    'ERROR: CRITICAL: database timeout',
    'INFO: user login',
    'WARN: retry attempt',
    'ERROR: CRITICAL: auth expired',
    'INFO: backup complete'
]

# Extract metrics from logs
total_ops, error_severity, warnings = analyze_efficiency(log_data)

# Simulate productivity and quality
tasks_completed = total_ops - warnings
bugs_found = error_severity

# Distractor variables
duplicate_check = {len(item) for item in log_data}
size_distribution = sorted(duplicate_check)
median_size = size_distribution[len(size_distribution)//2] if size_distribution else 0

# Core state tracking
cycle_effort = (tasks_completed + median_size) // 3  # unused but plausible
productivity = tasks_completed + 5
errors = bugs_found - 1 if bugs_found > 1 else 1

# Key statement
final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")