from collections import defaultdict
import itertools

# Simulate hourly resource usage across multiple servers
def calculate_peak_resource_usage(server_logs):
    usage_tracker = defaultdict(int)
    temp_aggregates = []
    auxiliary_sum = 0
    debug_flag = False

    # Process each log entry
    for timestamp, server_id, load in server_logs:
        hour = timestamp // 100  # Extract hour from timestamp (e.g., 1345 -> 13)
        key = f'{server_id}_{hour}'
        
        # Real logic: accumulate load per server-hour
        usage_tracker[key] += load
        
        # Distractor: collect temporary stats (not used in final result)
        temp_aggregates.append(load * 0.95 + 2)  
        auxiliary_sum += load ** 0.5

        # Nested conditional with side computation
        if load > 50:
            spike_marker = hour * 1000 + server_id
            for i in range(2):
                # Simulate secondary tracking (irrelevant)
                adjusted = (spike_marker >> i) & 255
                if adjusted > 100:
                    debug_flag = True

    # Secondary loop: post-process to smooth values (unused)
    smoothed = []
    for val in temp_aggregates:
        smoothed.append(round(val * 1.05, 2))

    # Core result: find peak capacity across all server-hour bins
    if not usage_tracker:
        peak_capacity = 0
    else:
        peak_capacity = max(usage_tracker.values())

    # Extra distraction: compute unused combinatorics
    pairs = list(itertools.combinations([1, 2, 3, 4], 2))
    pair_sums = sum(a + b for a, b in pairs)

    # Output the required result
    print(f"Result: {peak_capacity}")
    return peak_capacity

# Input data: (timestamp, server_id, cpu_load)
sample_logs = [
    (1300, 'SVC_A', 30),
    (1345, 'SVC_A', 45),
    (1350, 'SVC_B', 60),
    (1405, 'SVC_A', 20),
    (1420, 'SVC_C', 80),
    (1430, 'SVC_B', 10),
    (1500, 'SVC_A', 70),
    (1515, 'SVC_C', 55)
]

result = calculate_peak_resource_usage(sample_logs)