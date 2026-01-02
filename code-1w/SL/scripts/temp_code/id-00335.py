def analyze_system_state(log_entries):
    # Core analysis variables
    error_count = 0
    warning_threshold = 3
    system_health = 100
    cumulative_load = 0
    temporal_weights = [0.1, 0.3, 0.6]

    # Irrelevant statistical tracker (distractor)
    mean_response_time = 0.0
    peak_utilization = -1
    debug_snapshot = {}

    # Simulated log processing with mixed relevance
    for entry in log_entries:
        level = entry.get('level', 'info')
        load = entry.get('load', 0)
        duration = entry.get('duration', 0.0)

        # Relevant health deduction logic
        if level == 'error':
            error_count += 1
            system_health -= 8
        elif level == 'warning':
            system_health -= 3
            
        # Cumulative load calculation (partially relevant)
        cumulative_load += load

        # Dead code path - never executed due to fixed keys (distractor)
        if 'deprecated_flag' in entry:
            debug_snapshot['legacy'] = True  # Unreachable

        # Misleading complex computation (irrelevant)
        if duration > 0:
            inverse_efficiency = 1 / (duration + 1e-9)
            mean_response_time += inverse_efficiency * 0.05

    # Secondary irrelevant function nested inside (distractor)
    def calculate_entropy(seq):
        from math import log
        freq = {}
        total = len(seq)
        for item in seq:
            freq[item] = freq.get(item, 0) + 1
        entropy = 0
        for count in freq.values():
            p = count / total
            entropy -= p * log(p)
        return entropy

    # Unused entropy call (dead code)
    event_types = [e.get('type', 'unknown') for e in log_entries]
    signal_entropy = calculate_entropy(event_types)  # Computed but unused

    # Bitwise obfuscation of health (red herring)
    encoded_health = system_health ^ 0xFF
    decoded_health = encoded_health ^ 0xFF  # Identity transform

    # Key conditional with short-circuit evaluation
    if error_count >= warning_threshold and cumulative_load > 0:
        initial_diagnosis = -1
    else:
        initial_diagnosis = system_health // 2

    # Dictionary-based state mapping (core concept)
    diagnosis_map = {
        -1: 42,
        50: 76,
        40: 88,
        30: 94
    }

    # Complex default resolution with get() and fallback arithmetic
    base_diagnostic = diagnosis_map.get(initial_diagnosis, system_health - 10)

    # Final adjustment using conditional expression
    final_diagnostic = base_diagnostic if system_health > 20 else base_diagnostic * 0.5

    # Spurious list comprehension (distractor)
    normalized_logs = [
        {k: v for k, v in e.items() if k != 'timestamp'} 
        for e in log_entries if 'mask' not in e
    ]

    # Unused aggregation (irrelevant)
    total_entries = len(log_entries)
    if total_entries > 0:
        avg_load = cumulative_load / total_entries
        peak_utilization = max(avg_load * 2, 90)  # Never used

    return final_diagnostic

# Simulated operational log (realistic input)
operational_log = [
    {'level': 'info', 'load': 10, 'duration': 0.15},
    {'level': 'warning', 'load': 20, 'duration': 0.25},
    {'level': 'warning', 'load': 25, 'duration': 0.10},
    {'level': 'info', 'load': 15, 'duration': 0.20}
]

# Execution point of interest
final_diagnostic = analyze_system_state(operational_log)
print(f"Result: {final_diagnostic}")