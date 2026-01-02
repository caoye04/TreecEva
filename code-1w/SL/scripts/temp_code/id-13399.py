from collections import defaultdict
import math

# Simulated system metrics for performance analysis
telemetry_stream = [
    {"id": 101, "load": 85.3, "errors": 2, "timestamp": 1623456780},
    {"id": 102, "load": 92.1, "errors": 5, "timestamp": 1623456789},
    {"id": 103, "load": 76.4, "errors": 1, "timestamp": 1623456798},
    {"id": 104, "load": 95.7, "errors": 8, "timestamp": 1623456807},
    {"id": 105, "load": 68.9, "errors": 0, "timestamp": 1623456816}
]

# Irrelevant cache of historical user agents (distractor)
user_agent_cache = [
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Googlebot/2.1 (+http://www.google.com/bot.html)"
]

# Baseline thresholds for system health (used later)
baseline_thresholds = {
    'high_load': 90.0,
    'max_errors': 3,
    'grace_period': 60
}

# Decoy function - never called (dead code path)
def legacy_calibrate(x):
    return (x ** 2 + 3 * x + 1) % 100

# Misleading intermediate calculation (unused)
temp_aggregate = sum([t['load'] for t in telemetry_stream]) / len(telemetry_stream)

# Bit manipulation red herring (simulates encoding, but irrelevant)
encoded_flags = 0
for t in telemetry_stream:
    encoded_flags ^= int(t['load']) & 0xFF  # XOR with lower byte

# Another decoy structure: hashed credentials (never used)
hashed_secrets = defaultdict(lambda: 'unknown')
for i, agent in enumerate(user_agent_cache):
    hashed_secrets[agent] = hex(i * 1337 + 42)

# Real work begins: extract metric data
metric_data = []
for entry in telemetry_stream:
    score = 100.0
    if entry['load'] > baseline_thresholds['high_load']:
        score -= (entry['load'] - baseline_thresholds['high_load']) * 1.5
    if entry['errors'] > baseline_thresholds['max_errors']:
        score -= (entry['errors'] - baseline_thresholds['max_errors']) * 8.0
    # Apply time decay factor (not really used, but looks important)
    time_elapsed = 1623456900 - entry['timestamp']
    decay_factor = max(0.8, min(1.0, 1.0 - time_elapsed / 300))
    score *= decay_factor
    metric_data.append({'id': entry['id'], 'raw_score': round(score, 3)})

# Build baseline cache for reference (dictionary operation)
baseline_cache = {}
for i in range(100, 110):
    base_val = 95 - abs(i - 104) * 2.3
    baseline_cache[i] = {
        'expected_load': base_val,
        'recovery_window': 120,
        'priority': 'high' if base_val > 90 else 'normal'
    }

# Auxiliary string processing (distractor: parsing logs that aren't used)
raw_logs = "ERR_CRITICAL|WARN_TIMEOUT|INFO_READY|DEBUG_TRACE"
log_levels = raw_logs.split('|')
severity_map = {lvl: idx for idx, lvl in enumerate(log_levels)}

# Critical function: evaluates final performance score
def evaluate_performance(metrics, baseline):
    total_weight = 0.0
    cumulative = 0.0
    
    for m in metrics:
        raw = m['raw_score']
        item_id = m['id']
        
        # Extra distraction: check baseline priority (partially relevant)
        if item_id in baseline:
            if baseline[item_id]['priority'] == 'high':
                raw *= 1.1  # boost high-priority nodes
        
        # Weighting by ID oddness (bitwise red herring)
        weight = 1.0
        if item_id & 1:  # if odd
            weight += 0.05
        if item_id & 4:   # if bit 3 set
            weight += 0.03
        
        cumulative += raw * weight
        total_weight += weight
    
    # Final aggregation
    if total_weight == 0:
        return 0.0
    return round(cumulative / total_weight, 3)

# Unused recursive helper (dead code)
def recursively_refine(value, depth):
    if depth <= 0 or value < 10:
        return value
    return recursively_refine(value * 0.95, depth - 1)

# --- Key Statement ---
final_score = evaluate_performance(metric_data, baseline_cache)

# Print result as required
print(f"Target result: {final_score}")