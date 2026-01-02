from collections import defaultdict

# Simulate system event logs with timestamps and load levels
event_log_data = [
    ('server_A', 1, 85), ('server_B', 2, 70), ('server_A', 3, 90), ('server_C', 1, 60),
    ('server_B', 4, 75), ('server_A', 5, 95), ('server_C', 6, 65), ('server_B', 7, 80),
    ('server_A', 8, 100), ('server_C', 9, 70), ('server_B', 10, 85), ('server_A', 11, 90)
]

# Irrelevant metadata about servers (distractor)
system_metadata = {
    'server_A': {'cores': 8, 'memory_gb': 32, 'location': 'us-east'},
    'server_B': {'cores': 6, 'memory_gb': 16, 'location': 'eu-west'},
    'server_C': {'cores': 4, 'memory_gb': 12, 'location': 'ap-south'}
}

# Track cumulative load per server (relevant)
load_tracker = defaultdict(int)
entry_count = defaultdict(int)

# Process raw logs to aggregate load (key step 1)
for server_id, timestamp, load in event_log_data:
    if load > 50:  # filter only significant loads
        load_tracker[server_id] += load
        entry_count[server_id] += 1

# Compute average load per server (key step 2)
avg_loads = {}
for server in load_tracker:
    avg_loads[server] = load_tracker[server] / entry_count[server]

# Misleading secondary analysis: peak detection (distractor)
peak_fluctuations = []
current_peak = 0
for _, _, load in event_log_data:
    if load > current_peak:
        current_peak = load
        peak_fluctuations.append(load)

# Helper function to compute capacity score (key step 3)
def calculate_capacity_score(avg_load, count):
    base_score = avg_load * 1.5
    adjustment = count * 0.8
    return base_score + adjustment  # simplified model

# Another distractor: simulate network jitter buffer
jitter_buffer = [0.1 * i for i in range(1, len(event_log_data) + 1)]
total_jitter = sum(jitter_buffer) // len(jitter_buffer) if jitter_buffer else 0

# Calculate individual server capacities (key step 4)
capacity_map = {}
for server in avg_loads:
    capacity_map[server] = calculate_capacity_score(avg_loads[server], entry_count[server])

# Apply threshold-based weighting (key step 5)
threshold = 85.0
weighted_scores = []
for server, score in capacity_map.items():
    load = avg_loads[server]
    if load >= threshold:
        weighted_scores.append(score * 1.2)
    else:
        weighted_scores.append(score * 0.9)

# Secondary irrelevant transformation: normalize fluctuation data
normalized_peaks = [p / max(peak_fluctuations) for p in peak_fluctuations] if peak_fluctuations else []
impact_factor = sum(normalized_peaks) * 0.5

# Core calculation: total system capacity (key step 6)
def calculate_system_capacity(log_entries, threshold):
    temp_total = 0
    temp_count = 0
    for record in log_entries:
        _, _, load = record
        if load > threshold - 10:
            temp_total += load
            temp_count += 1
    base_capacity = temp_total / temp_count if temp_count else 0
    
    # Add bonus for high-frequency high-load servers (key step 7)
    high_load_servers = [s for s in avg_loads if avg_loads[s] >= threshold]
    bonus_multiplier = 1 + (0.1 * len(high_load_servers))
    
    # Final capacity with bonus
    final = base_capacity * bonus_multiplier
    
    # Dead code path: never executed (distractor)
    if False:
        fallback = sum(capacity_map.values()) / len(capacity_map)
        final = fallback
        
    return final

# Execute main logic
final_capacity = calculate_system_capacity(event_log_data, threshold)

# Print result as required
print(f"Target result: {final_capacity}")