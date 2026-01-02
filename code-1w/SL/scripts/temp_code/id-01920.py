import math

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    trend = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend += 1
    return trend // 2

# Irrelevant helper function (dead code path)
def deprecated_checksum(data):
    checksum = 0
    for item in data:
        checksum ^= hash(str(item)) % 256
    return checksum

# Unused transformation function
def transform_legacy_format(record):
    return {"legacy_id": record.get('id'), "meta": record}

# Main diagnostic engine
log_entries = [
    {"id": 101, "level": "ERROR", "timestamp": 1623456780, "duration_ms": 120},
    {"id": 102, "level": "INFO", "timestamp": 1623456785, "duration_ms": 45},
    {"id": 103, "level": "ERROR", "timestamp": 1623456790, "duration_ms": 200},
    {"id": 104, "level": "DEBUG", "timestamp": 1623456795, "duration_ms": 10},
    {"id": 105, "level": "ERROR", "timestamp": 1623456800, "duration_ms": 80}
]

system_flags = {
    "overload_protection": True,
    "redundancy_active": False,
    "maintenance_mode": False,
    "cache_enabled": True,
    "replication_lag": 12
}

# Decoy variables with misleading names
aggregate_score = sum([entry["duration_ms"] for entry in log_entries]) * 0.1
baseline_threshold = 100 if system_flags["overload_protection"] else 50
intermediate_state = set()
for entry in log_entries:
    intermediate_state.add(entry["level"])

# Complex conditional logic with distractors
critical_count = 0
warning_duration = 0
error_durations = []
temporal_gaps = []

for i in range(len(log_entries)):
    entry = log_entries[i]
    if entry["level"] == "ERROR":
        critical_count += 1
        error_durations.append(entry["duration_ms"])
    if i > 0:
        gap = entry["timestamp"] - log_entries[i-1]["timestamp"]
        temporal_gaps.append(gap)

# Distractor: unused statistical computation
mean_gap = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0
std_deviation_proxy = math.sqrt(sum((x - mean_gap) ** 2 for x in temporal_gaps)) if temporal_gaps else 0

# Real processing begins here — deeply nested and obscured
status_codes = [500 if e["level"] == "ERROR" else 200 for e in log_entries]
unique_codes = set(status_codes)
code_distribution = {code: status_codes.count(code) for code in unique_codes}

# String-based filtering (using string methods)
valid_levels = [e for e in log_entries if e["level"].lower() in ['error', 'warning']]

# Core metric calculation buried among noise
raw_metric = 0
if critical_count >= 2:
    raw_metric += 400
if system_flags["redundancy_active"]:
    raw_metric += 150
else:
    raw_metric -= 75

if len(error_durations) > 0:
    avg_error = sum(error_durations) / len(error_durations)
    if avg_error > baseline_threshold:
        raw_metric += 200

# Simulated fault pattern detection
pattern_sequence = [len(str(e["id"])) for e in log_entries]
detected_trend = analyze_pattern(pattern_sequence)
if detected_trend > 1 and not system_flags["maintenance_mode"]:
    raw_metric += 50

# Misleading normalization attempt
normalization_factor = max(raw_metric, 100) / 100.0
adjusted_metric = raw_metric / normalization_factor if normalization_factor != 1 else raw_metric + 10

# Final decision logic obscured by tuple unpacking and boolean logic
flags_summary = (
    system_flags["overload_protection"],
    system_flags["cache_enabled"],
    len(intermediate_state) > 2
)

proceed_autoscale = all(flags_summary) or (not system_flags["redundancy_active"] and critical_count < 5)

# Key computation — answer derived here
if proceed_autoscale and raw_metric > 0:
    final_diagnostic = int(raw_metric * 0.85)
else:
    final_diagnostic = int(raw_metric * 0.3)

# Red herring: unrelated dictionary transformation
diagnostic_log = {}
for entry in log_entries:
    key = f"entry_{entry['id']}"
    diagnostic_log[key] = {"processed": True, "flagged": entry['level'] == "ERROR"}

# Output the target result
print(f"Result: {final_diagnostic}")