def compute_system_efficiency(log_entries):
    total_output = 0
    idle_count = 0
    peak_threshold = 85
    fluctuation_sum = 0
    previous_load = None

    for idx, (timestamp, load, status) in enumerate(log_entries):
        if status == 'active':
            total_output += load
            if previous_load is not None:
                fluctuation_sum += abs(load - previous_load)
            previous_load = load
        elif status == 'idle':
            idle_count += 1

    # Misleading computation: fluctuation average not used later
    avg_fluctuation = fluctuation_sum / (len(log_entries) - 1) if len(log_entries) > 1 else 0

    # Distractor: secondary analysis with dead-end logic
    high_load_periods = [load for _, load, _ in log_entries if load > peak_threshold]
    spike_count = len(high_load_periods)
    spike_ratio = spike_count / len(log_entries) if log_entries else 0

    # Core logic hidden among distractions
    active_periods = sum(1 for _, _, status in log_entries if status == 'active')
    baseline_estimate = sum(load for _, load, _ in log_entries) * 0.1  # unused but plausible

    efficiency_score = total_output // active_periods if active_periods else 0

    # Red herring: adjustment based on unused metrics
    if avg_fluctuation > 10 and spike_ratio < 0.2:
        efficiency_score -= 5  # never reached in this case due to data

    return efficiency_score

# Simulated system log: (timestamp, CPU_load_percent, status)
system_log = [
    (1672531200, 70, 'active'),
    (1672531260, 80, 'active'),
    (1672531320, 0,  'idle'),
    (1672531380, 90, 'active'),
    (1672531440, 85, 'active'),
    (1672531500, 0,  'idle'),
    (1672531560, 75, 'active')
]

result = compute_system_efficiency(system_log)
print(f"Result: {result}")