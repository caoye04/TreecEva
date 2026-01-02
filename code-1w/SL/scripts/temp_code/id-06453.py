from collections import defaultdict

# Simulate hourly resource utilization across multiple servers
def calculate_peak_utilization(log_entries):
    server_loads = defaultdict(list)
    temporal_weights = [1.0, 0.9, 0.8, 0.7, 0.6]  # Decay factors (irrelevant for peak)
    baseline_offset = 5  # Misleading constant

    # Parse logs and aggregate hourly loads
    for timestamp, server_id, usage in log_entries:
        hour = int(timestamp.split(':')[0])
        adjusted_usage = usage + (hour % 3) * 0.1  # Minor adjustment (not used in final logic)
        server_loads[server_id].append((hour, usage))

    # Track peak detection
    peak_capacity = 0
    historical_avgs = []
    total_hours_processed = 0

    for server_id, records in server_loads.items():
        sorted_records = sorted(records, key=lambda x: x[0])
        daily_totals = defaultdict(float)

        for hour, usage in sorted_records:
            daily_totals[hour // 8] += usage
            current_load = usage * 1.1  # Simulated scaled load
            
            # Core update point
            peak_capacity = max(peak_capacity, current_load)
            
            # Distractor: accumulate averages that are never used
            temp_avg = sum(daily_totals.values()) / len(daily_totals) if daily_totals else 0
            historical_avgs.append(temp_avg)

        total_hours_processed += len(records)

    # Dead code path: never executed due to data structure
    if False and historical_avgs:
        fallback = sum(historical_avgs) / len(historical_avgs)
        peak_capacity = max(peak_capacity, fallback)

    # Extra computation with no impact
    normalization_factor = 1 / (baseline_offset or 1)
    dummy_score = sum(temporal_weights) * normalization_factor

    print(f"Result: {peak_capacity}")

# Input data
logs = [
    ('02:15', 'svr-alpha', 45),
    ('02:30', 'svr-beta', 67),
    ('03:10', 'svr-alpha', 89),
    ('03:45', 'svr-gamma', 34),
    ('04:20', 'svr-beta', 78),
    ('04:50', 'svr-alpha', 91),
    ('05:10', 'svr-gamma', 45)
]

calculate_peak_utilization(logs)