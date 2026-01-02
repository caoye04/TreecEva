def preprocess_logs(raw_data):
    # Irrelevant preprocessing that doesn't affect final result
    cleaned = []
    for item in raw_data:
        if 'error' in item[1]:
            continue
        timestamp, msg = item
        if len(msg) > 5:
            cleaned.append((timestamp % 1000, msg.upper()))
    return cleaned

# Decoy function – never called
def calculate_latency(events):
    total = 0
    for i in range(len(events) - 1):
        total += events[i+1][0] - events[i][0]
    return total / len(events) if events else 0

# Another decoy – looks important but unused
system_config = {
    'version': '2.1.5',
    'mode': 'diagnostic',
    'debug_level': 9,
    'timeout': 300,
    'buffer_size': 4096
}

# Misleading auxiliary computation
baseline_metrics = [i**2 for i in range(15) if i % 3 != 0]
aggregate_offset = sum(baseline_metrics) // 100  # Distractor value

# Unused recursive red herring
def trace_dependency(graph, node):
    if node <= 1:
        return 1
    return trace_dependency(node - 1) + trace_dependency(node - 2)

# Simulated log data with mixed content
raw_log_data = [
    (100, "boot"),
    (150, "init"),
    (220, "poll"),
    (305, "poll"),
    (400, "sync"),
    (475, "poll"),
    (600, "halt")
]

# Additional noise: fake filters
exclusion_tags = {"debug", "trace", "verbose"}
filtered_tags = [tag for tag in exclusion_tags if len(tag) > 5]

# Real processing begins here
log_entries = [(ts, msg) for ts, msg in raw_log_data if msg != "boot"]

system_threshold = 100

# Core logic hidden among distractions
def analyze_performance(entries, threshold):
    count = 0
    gaps = []
    last_time = entries[0][0]
    
    for idx, (timestamp, message) in enumerate(entries):
        if idx == 0:
            continue
        delta = timestamp - last_time
        gaps.append(delta)
        last_time = timestamp
    
    # Use of enumerate and zip – required Python features
    weighted_sum = 0
    for i, gap in enumerate(gaps):
        adjustment = 1 if i % 2 == 0 else 0.5
        weighted_sum += gap * adjustment
    
    # Secondary analysis with zip
    paired = list(zip(gaps, gaps[1:]))
    surge_count = 0
    for curr, next_val in paired:
        if next_val > curr and curr < threshold:
            surge_count += 1
    
    # Actual answer derivation buried here
    base_score = len([g for g in gaps if g > threshold])
    penalty = surge_count * 2
    efficiency_score = base_score * 17 - penalty + aggregate_offset  # Uses distractor
    
    # Dead code branch – misleading
    if efficiency_score < 0:
        efficiency_score = abs(efficiency_score)
    
    return efficiency_score

# Key execution point
interim_result = preprocess_logs(raw_log_data)
critical_flag = False
if len(interim_result) > 5:
    critical_flag = True

# This is the actual target statement
efficiency_score = analyze_performance(log_entries, system_threshold)

# Print final result as required
print(f"Result: {efficiency_score}")