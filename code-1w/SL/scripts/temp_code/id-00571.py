def analyze_system_performance(log_data):
    # Parse timestamp and status from log entries
    timestamps = [entry[:19] for entry in log_data if 'ERROR' not in entry]
    statuses = [entry[20:] for entry in log_data if 'ERROR' not in entry]

    # Extract hour from each timestamp for load analysis
    active_hours = [int(ts[11:13]) for ts in timestamps]
    peak_load = sum(1 for hour in active_hours if 9 <= hour <= 17)

    # Compute system uptime ratio (success vs total non-error entries)
    success_count = sum(1 for s in statuses if 'SUCCESS' in s)
    total_valid = len(statuses)
    uptime_ratio = success_count / total_valid if total_valid > 0 else 0

    # Irrelevant string transformation (distractor)
    formatted_logs = [ts.replace('-', '/').upper() for ts in timestamps]
    summary_tag = ''.join(formatted_logs[-1]).lower().strip('2023/04/01/') if formatted_logs else ''

    # Base metrics for efficiency calculation
    base_rating = len([s for s in statuses if 'WARNING' in s]) + uptime_ratio * 100

    # Simulate environmental factors (unused in final result)
    env_factors = []
    for i in range(3):
        env_factors.append((i * 0.1) ** 2)

    # Improvement factor based on off-peak efficiency
    off_peak_ops = sum(1 for hour in active_hours if hour < 9 or hour > 17)
    improvement_factor = off_peak_ops / total_valid if total_valid > 0 else 0

    # Key statement: compute final efficiency score
    efficiency_score = base_rating * (1 + improvement_factor)

    # Additional red herring computation
    synthetic_index = sum(env_factors) * len(summary_tag)

    # Output target result
    print(f"Result: {efficiency_score}")

# Simulated log input (deterministic)
log_entries = [
    "2023-04-01 08:15:22 SYSTEM INIT",
    "2023-04-01 08:20:10 STATUS UPDATE SUCCESS",
    "2023-04-01 09:05:33 TASK COMPLETE SUCCESS",
    "2023-04-01 10:11:44 WARNING MEMORY HIGH",
    "2023-04-01 12:30:01 DATA SYNC SUCCESS",
    "2023-04-01 14:45:19 WARNING IO TIMEOUT",
    "2023-04-01 18:22:05 CLEANUP COMPLETE SUCCESS",
    "2023-04-01 20:10:11 DIAGNOSTIC PASS"
]

analyze_system_performance(log_entries)