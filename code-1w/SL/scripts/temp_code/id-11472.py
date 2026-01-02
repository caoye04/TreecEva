from collections import defaultdict

# Simulate server load distribution across regions and time slots
def analyze_server_load(requests_log, maintenance_windows):
    usage_counts = defaultdict(int)
    temp_buffer = []
    total_processed = 0
    efficiency_factor = 0.85
    overhead_counter = 0  # Tracks irrelevant metadata

    for timestamp, region, req_count in requests_log:
        if any(start <= timestamp < end for start, end in maintenance_windows.get(region, [])):
            continue  # Skip during maintenance

        # Simulate request batching
        batch_size = 3 if req_count > 10 else 2
        batches = (req_count + batch_size - 1) // batch_size
        temp_buffer.append(batches)

        # Count effective usage per region
        usage_counts[region] += req_count
        total_processed += req_count

        # Distractor: track even vs odd timestamps
        if timestamp % 2 == 0:
            overhead_counter += 1

    # Dummy sorting with no impact
    sorted_buffer = sorted(temp_buffer, reverse=True)
    average_batch = sum(sorted_buffer) / len(sorted_buffer) if sorted_buffer else 0

    # Key computation with conditional expression
    base_peak = usage_counts['us-east'] if 'us-east' in usage_counts else sum(usage_counts.values())
    adjusted_peak = base_peak * (1.1 if average_batch > 2 else 1.0)

    # Critical assignment point
    peak_capacity = max(usage_counts.values()) * efficiency_factor

    # More red herring computations
    capacity_matrix = [[peak_capacity / (i+1) for i in range(3)] for _ in range(2)]
    flat_capacity = [item for row in capacity_matrix for item in row]
    final_diagnostic = sum(flat_capacity) / len(flat_capacity)

    print(f"Result: {peak_capacity}")
    return final_diagnostic

# Input data
requests = [
    (100, 'us-east', 15),
    (101, 'eu-west', 8),
    (102, 'us-east', 12),
    (103, 'ap-south', 20),
    (104, 'eu-west', 5),
    (105, 'us-east', 18)
]
maintenance = {
    'ap-south': [(103, 106)]
}

# Execute
analyze_server_load(requests, maintenance)