from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
raw_readings = [127, 255, 64, 191, 32, 223, 159, 96, 175, 240]
error_flags = [False, True, False, False, True]

# Irrelevant auxiliary mappings (distractor)
status_map = {'OK': 0, 'WARN': 1, 'ERR': 2, 'CRIT': 3}
severity_weights = defaultdict(float, {'minor': 0.25, 'moderate': 0.5, 'severe': 0.75})

# Core diagnostic parameters
baseline_threshold = 128
critical_jump = 0
system_state = {'mode': 'ACTIVE', 'version': '2.1.7', 'uptime': 86400}

# Process raw readings into event categories (mixed logic and bit ops)
event_categories = []
for val in raw_readings:
    if val & 128:  # Check high bit
        category = 'HIGH'
    elif val & 64:
        category = 'MEDIUM'
    else:
        category = 'LOW'
    event_categories.append(category)

    # Dead computation path (red herring)
    if val > baseline_threshold:
        temp_adj = (val ^ 255) + 1
        critical_jump += temp_adj  # Accumulates but unused later

# Misleading accumulation structure (distraction)
diagnostic_trace = []
running_alerts = 0
for flag in error_flags:
    if flag:
        running_alerts += 1
    diagnostic_trace.append(running_alerts * 100)

# Unused recursive function (decoy)
def calculate_health_recursive(level, depth=0):
    if depth >= 3 or level <= 0:
        return 1
    return level * 0.9 + 0.1 * calculate_health_recursive(level - 10, depth + 1)

# Real processing begins: log entry construction
log_entries = []
for i, ts in enumerate(timestamps):
    entry = {
        'ts': ts,
        'reading': raw_readings[i % len(raw_readings)],
        'flag': error_flags[i % len(error_flags)],
        'category': event_categories[i % len(event_categories)]
    }
    log_entries.append(entry)

# Secondary irrelevant transformation (distractor)
flag_counter = Counter([entry['flag'] for entry in log_entries])
weighted_flags = sum(10 if f else 1 for f in flag_counter.keys())

# Actual aggregation logic hidden among noise
def analyze_stability(entries, state):
    stable_count = 0
    total_deviation = 0.0
    recent_spike = False

    for e in entries:
        reading = e['reading']
        # Stability defined by threshold crossing pattern
        if reading >= baseline_threshold and not recent_spike:
            stable_count += 1
            recent_spike = True
        elif reading < baseline_threshold:
            recent_spike = False

        # Deviation based on logarithmic scale
        if reading > 0:
            total_deviation += math.log(reading, 2)

    # Combine with version number quirk
    version_parts = list(map(int, state['version'].split('.')))
    version_factor = version_parts[0] * 100 + version_parts[1] * 10 + version_parts[2]

    return int((total_deviation * 10) + stable_count - (version_factor % 25))

# Another decoy function using defaultdict
def generate_diagnostics_report(data):
    report = defaultdict(lambda: 'N/A')
    report['status'] = 'COMPLETE'
    report['priority'] = 'NORMAL'
    return dict(report)

# Real final computation
final_diagnostic = 0
def aggregate_metrics(entries, sys_state):
    # Summation with conditional filtering
    valid_entries = [e for e in entries if e['category'] != 'LOW']
    high_priority = [e for e in valid_entries if e['flag']]

    base_score = 0
    for entry in valid_entries:
        base_score += entry['reading'] // 32
        if entry['flag']:
            base_score -= 5

    # Additional adjustment via dictionary lookup
    mode_bonus = {'ACTIVE': 12, 'STANDBY': 3, 'MAINT': -10}
    bonus = mode_bonus.get(sys_state['mode'], 0)

    # Critical calculation step
    reading_sum = sum(e['reading'] for e in high_priority)
    adjustment = len(valid_entries) * 3

    result = base_score + bonus + adjustment - (reading_sum % 17)

    # This is the actual answer
    return result

# Key execution point
final_diagnostic = aggregate_metrics(log_entries, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")