from collections import defaultdict

# Simulate server load analysis across multiple regions and time windows
def analyze_server_load(log_entries):
    region_load = defaultdict(lambda: 0)
    hourly_requests = [0] * 24
    temp_aggregator = {}
    phantom_counter = 0  # Distractor: not used in final result

    for entry in log_entries:
        timestamp, region, req_count_str = entry.split('|')
        hour = int(timestamp.split(':')[0])
        req_count = int(req_count_str)

        # Track hourly request volume (relevant for pattern detection)
        hourly_requests[hour] += req_count

        # Accumulate regional load (critical path)
        region_load[region] += req_count

        # Distractor computation: tracking string length patterns (irrelevant)
        phantom_counter += len(region) % 3

        # Semi-relevant: track peak per-region usage in temp structure
        if region not in temp_aggregator or temp_aggregator[region] < region_load[region]:
            temp_aggregator[region] = region_load[region]

    # Use list comprehension to filter high-traffic hours (> average)
    avg_hourly = sum(hourly_requests) / len(hourly_requests)
    high_traffic_hours = [h for h, v in enumerate(hourly_requests) if v > avg_hourly]

    # Build usage tracker from temp_aggregator with additional transformation
    usage_tracker = defaultdict(float)
    scaling_factor = 1.25
    for reg, load in temp_aggregator.items():
        # Apply non-linear scaling (simulates capacity planning adjustment)
        usage_tracker[reg] = (load ** 0.95) * scaling_factor

    # Key execution point
    peak_capacity = max(usage_tracker.values())

    # Dead code path - never executed but adds cognitive load
    if False:
        fallback = sum(phantom_counter for _ in range(5))
        peak_capacity -= fallback

    return peak_capacity

# Simulated log data (format: HH:MM|region|request_count)
logs = [
    "08:15|us-west|120",
    "08:22|us-east|150",
    "08:30|eu-central|90",
    "09:10|us-west|200",
    "09:15|us-east|175",
    "09:20|eu-central|110",
    "10:05|us-west|250",
    "10:10|us-east|160",
    "10:18|eu-central|95",
    "11:00|us-west|300",
    "11:05|us-east|180",
    "11:10|eu-central|105"
]

result = analyze_server_load(logs)
print(f"Target result: {result}")