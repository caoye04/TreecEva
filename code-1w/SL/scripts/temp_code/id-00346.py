def analyze_status(flags, log):
    # Core diagnostic logic
    severity_map = {'red': 3, 'amber': 2, 'green': 1}
    status_weights = [severity_map.get(entry, 0) for entry in log if entry in severity_map]

    # Irrelevant helper: counts vowels in flag names (distractor)
    vowel_count = lambda text: sum(1 for c in text.lower() if c in 'aeiou')
    entropy_score = sum(vowel_count(flag) for flag in flags) * 0.7  # Red herring

    # Real processing: count critical flags and recent log trends
    critical_count = sum(1 for f in flags if 'critical' in f)
    recent_events = log[-5:]  # Slice to get most recent entries
    active_alerts = [e for e in recent_events if e == 'red']

    # Misleading intermediate: computes unused correlation index
    correlation_index = 0
    for i in range(1, len(log)):
        if log[i] == 'red' and log[i-1] == 'amber':
            correlation_index += 1
    adjusted_correlation = correlation_index * 2.5  # Dead computation

    # State tracking with dictionary (relevant)
    state_summary = {}
    for event in log:
        state_summary[event] = state_summary.get(event, 0) + 1

    # Compute baseline risk from log frequency
    baseline_risk = sum(state_summary.values()) / (len(state_summary) or 1)

    # Destructuring assignment (irrelevant but plausible)
    system_uptime, last_reboot_code = 1420, 'RST9'
    calibration_offset = system_uptime % 7 if last_reboot_code.startswith('R') else 0

    # Key logic: compute diagnostic score
    trend_weight = sum(severity_map[e] for e in recent_events) / 5
    flag_penalty = critical_count * 10

    # Final diagnostic calculation (only this matters)
    final_diagnostic = int(baseline_risk + trend_weight - flag_penalty + 50)

    return final_diagnostic


# Simulation data
operational_flags = [
    'core_critical_fault',
    'temp_stable',
    'io_normal',
    'memory_critical_warning',
    'network_standby'
]

system_log = [
    'green', 'green', 'amber', 'green', 'red',
    'amber', 'amber', 'red', 'red', 'green',
    'green', 'amber', 'red', 'amber', 'green'
]

# Dead code path: unused function
def compute_resilience_metric(log_data):
    return len([x for x in log_data if x != 'green']) * 0.8

# Unused variable (distractor)
baseline_efficiency = 98.6
reference_pattern = ['green', 'amber', 'red']
system_age_years = 6

# Execution point of interest
final_diagnostic = analyze_status(operational_flags, system_log)
print(f"Result: {final_diagnostic}")