from collections import defaultdict, Counter
import math

# Simulated system log analyzer with performance metrics (distraction: detailed logging)
def parse_log_line(line):
    parts = line.split()
    return {
        'timestamp': int(parts[0]),
        'level': parts[1],
        'module': parts[2],
        'event': ' '.join(parts[3:])
    }

def collect_events_by_module(log_lines):
    # Irrelevant aggregation function (dead path)
    module_events = defaultdict(list)
    for line in log_lines:
        parsed = parse_log_line(line)
        module_events[parsed['module']].append(parsed['event'])
    return module_events

def filter_errors(log_lines):
    # Misleading filtering - looks important but unused later
    return [line for line in log_lines if 'ERROR' in line]

def compute_event_frequency(log_lines):
    # Another red herring: computes frequency but not used in final result
    events = [parse_log_line(line)['event'] for line in log_lines]
    return Counter(events)

def calculate_response_time(timestamps):
    # Distraction: time analysis that isn't directly used
    if len(timestamps) < 2:
        return 0
    return sum(abs(timestamps[i] - timestamps[i-1]) for i in range(1, len(timestamps))) / (len(timestamps) - 1)

def extract_timestamps(log_lines):
    # Unused helper - distracts from real data flow
    return [int(line.split()[0]) for line in log_lines]

def generate_weight_map(modules):
    # Decoy weight generation (never called)
    return {module: (hash(module) % 10 + 1) for module in modules}

def validate_log_integrity(log_lines):
    # Looks critical but actually irrelevant
    total_chars = sum(len(line) for line in log_lines)
    checksum = total_chars % 1000
    return checksum == 42  # Always false in this case

def normalize_scores(raw_scores, base=1.5):
    # Used only partially; creates misleading intermediate values
    normalized = {}
    max_score = max(raw_scores.values()) if raw_scores else 1
    for k, v in raw_scores.items():
        norm_value = (v / max_score) ** 0.5 * base
        if norm_value > 0.1:
            normalized[k] = round(norm_value, 3)
    return normalized

def compute_module_stability(log_entries):
    # Real but obfuscated component: computes module consistency score
    stability = defaultdict(int)
    prev = {}
    for entry in log_entries:
        mod = entry['module']
        evt_hash = hash(entry['event']) % 100
        if mod in prev:
            stability[mod] += 1 if abs(evt_hash - prev[mod]) < 50 else -1
        prev[mod] = evt_hash
    return stability

def compute_efficiency_metric(stability, event_count):
    # Intermediate transformation - part of real logic chain
    efficiency = {}
    for mod in stability:
        if mod in event_count:
            efficiency[mod] = stability[mod] / (event_count[mod] ** 0.5)
    return efficiency

def aggregate_performance(log_entries, weights):
    # Core calculation buried in distractions
    event_count = Counter(entry['module'] for entry in log_entries)
    stability = compute_module_stability(log_entries)
    efficiency = compute_efficiency_metric(stability, event_count)
    
    # Critical logic hidden among noise
    weighted_sum = 0.0
    total_weight = 0.0
    for i, entry in enumerate(log_entries):
        mod = entry['module']
        if mod in weights and i % 3 == 0:  # Every third entry only
            raw_score = abs(math.sin(hash(entry['event']) % 3.14))
            normalized_score = (raw_score + stability[mod] * 0.1) * weights[mod]
            weighted_sum += normalized_score
            total_weight += weights[mod]
    
    # Final answer computation
    if total_weight == 0:
        return 0.0
    base_performance = weighted_sum / total_weight
    penalty = len([e for e in log_entries if 'CRITICAL' in e['event']]) * 0.25
    final_value = max(0, base_performance - penalty) * 1000
    return int(final_value)

# --- Real input data ---
log_data = [
    "1001 INFO auth User login successful",
    "1003 WARN auth Weak password detected",
    "1007 ERROR storage Disk write failure",
    "1012 INFO auth Session refresh",
    "1018 CRITICAL security SQL injection attempt blocked",
    "1023 INFO network Connection established",
    "1029 WARN storage Low disk space",
    "1035 INFO auth Logout confirmed",
    "1040 ERROR security Failed login threshold exceeded",
    "1046 INFO network Keep-alive signal",
    "1051 CRITICAL security Brute force attack detected",
    "1057 INFO auth MFA verification passed"
]

# Parse logs - actual entry point to relevant logic
parsed_logs = [parse_log_line(line) for line in log_data]

# Real weights used in calculation (not generated)
weights_config = {
    'auth': 1.8,
    'security': 2.5,
    'network': 1.2,
    'storage': 1.0
}

# Extracted event counts (used in core logic)
event_counter = Counter(log['module'] for log in parsed_logs)

# Secondary metric - looks important but only used once
average_gap = calculate_response_time([log['timestamp'] for log in parsed_logs])

# Normalize some scores (partial usage)
frequency_stats = compute_event_frequency(log_data)
pseudo_reliability = normalize_scores(frequency_stats, base=2.0)

# Perform integrity check (unused result)
is_valid = validate_log_integrity(log_data)

# Finally: compute the target value
final_score = aggregate_performance(parsed_logs, weights_config)

# Output result
print(f"Target result: {final_score}")