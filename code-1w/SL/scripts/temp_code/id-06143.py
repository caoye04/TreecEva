from collections import defaultdict, Counter

# Simulated system log analysis with red herrings and complex processing
def analyze_log_integrity(raw_logs):
    integrity_score = 0
    error_frequency = defaultdict(int)
    temporal_gaps = []
    for i, log in enumerate(raw_logs):
        parts = log.split('|')
        timestamp = int(parts[0])
        level = parts[1]
        message = parts[2]
        error_frequency[level] += 1
        if i > 0:
            gap = timestamp - prev_timestamp
            temporal_gaps.append(gap)
        prev_timestamp = timestamp
        if 'CRITICAL' in message and 'retry' not in message:
            integrity_score += 3
    avg_gap = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0
    return integrity_score, error_frequency, avg_gap

# Irrelevant helper - distractor function
def calculate_network_latency(packet_sizes, routing_table):
    weighted_sum = 0
    total_packets = len(packet_sizes)
    route_map = {k: v for k, v in zip(packet_sizes, range(len(packet_sizes)))}
    for size, route_id in route_map.items():
        weight = size * (route_id % 7)
        weighted_sum += weight
    return weighted_sum / total_packets if total_packets else 0

# Core diagnostic processor with mixed concerns
def extract_signatures(events):
    signatures = []
    code_map = defaultdict(list)
    for idx, event in enumerate(events):
        if 'ERROR' in event or 'FAIL' in event:
            code = hash(event) % 1000
            code_map[code].append(idx)
    for code, positions in code_map.items():
        if len(positions) > 1:
            signatures.append(code * len(positions))
    return signatures

# Main metric processor - critical path
def process_metrics(entries, thresholds):
    # Real computation begins
    severity_count = defaultdict(int)
    pattern_scores = []
    
    # Primary signal extraction
    for entry in entries:
        fields = entry.split('|')
        level = fields[1]
        msg = fields[2]
        if level in ['ERROR', 'CRITICAL'] and 'suppressed' not in msg:
            severity_count[level] += 1
    
    # Generate decoy metrics
    fake_aggregates = []
    for i in range(3):
        fake = sum([hash(str(v)) % 100 for v in severity_count.values()]) * (i + 1)
        fake_aggregates.append(fake)
    
    # Actual scoring logic
    base_score = 0
    for lvl, cnt in severity_count.items():
        if lvl == 'ERROR':
            base_score += cnt * 5
        elif lvl == 'CRITICAL':
            base_score += cnt * 12
    
    # Red herring: unused complex structure
    temp_analysis = {}
    for e in entries:
        key = e.split('|')[1]
        temp_analysis[key] = temp_analysis.get(key, 0) + 1
    sorted_keys = sorted(temp_analysis.keys(), key=lambda x: temp_analysis[x], reverse=True)
    
    # Signature extraction - actually used
    raw_signatures = extract_signatures([e.split('|')[2] for e in entries])
    signature_bonus = sum([s % 7 for s in raw_signatures]) if raw_signatures else 0
    
    # Threshold modulation
    threshold_modifier = 1
    for t_key, t_val in thresholds.items():
        if t_key == 'safety_margin' and t_val < 10:
            threshold_modifier *= 1.2
        elif t_key == 'buffer_limit' and t_val > 500:
            threshold_modifier *= 0.9
    
    # Final computation
    intermediate = base_score + signature_bonus
    final_diagnostic = int(intermediate * threshold_modifier)
    
    # Dead code branch - never executed due to data
    if final_diagnostic < 0:
        recovery_state = [0] * 5
        for i in range(len(recovery_state)):
            recovery_state[i] = (final_diagnostic * i) % 11
    
    return final_diagnostic

# Simulated input data
log_data = [
    "1001|INFO|System boot sequence initiated",
    "1005|ERROR|Disk I/O timeout detected",
    "1010|CRITICAL|Memory corruption in sector 7",
    "1015|WARNING|High CPU temperature",
    "1020|ERROR|Disk I/O timeout detected",
    "1025|INFO|User session established",
    "1030|CRITICAL|Memory corruption in sector 7",
    "1035|DEBUG|Garbage collector pass completed"
]

system_configs = {
    'timeout_window': 30,
    'safety_margin': 8,
    'buffer_limit': 640,
    'retry_attempts': 3
}

# Irrelevant network simulation data
dummy_packets = [64, 128, 256, 512]
routing_index = {'A': 1, 'B': 2, 'C': 3}
latency_metric = calculate_network_latency(dummy_packets, routing_index)

# Initial log analysis - partially relevant but not fully used
integrity_result = analyze_log_integrity(log_data)

# Key execution point
final_diagnostic = process_metrics(log_data, system_configs)

# Output result
print(f"Target result: {final_diagnostic}")