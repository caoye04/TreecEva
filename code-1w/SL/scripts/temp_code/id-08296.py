import itertools

# Simulated system telemetry data from distributed sensors
telemetry_streams = [
    [14, 17, 23, 19, 15, 22, 25, 18],
    [31, 33, 30, 32, 29, 34, 35, 33],
    [8, 11, 10, 9, 12, 13, 11, 10]
]

# Irrelevant auxiliary transformation - dead path
transformed_cache = []
for series in telemetry_streams:
    temp = []
    for val in series:
        if val > 20:
            temp.append(val ** 0.5)
        else:
            temp.append(val // 2)
    transformed_cache.append(temp)

# Misleading intermediate diagnostic (decoy)
current_health_score = sum(len(stream) for stream in telemetry_streams) * 1.5

# Actual relevant data: log-derived event counts
raw_log_entries = [
    'ERROR:disk', 'WARN:net', 'INFO:mem', 'ERROR:io',
    'ERROR:disk', 'WARN:cpu', 'ERROR:disk', 'INFO:gpu'
]

# Mapping events to counters using dictionary operations
log_counter = {}
for entry in raw_log_entries:
    category = entry.split(':')[0]
    log_counter[category] = log_counter.get(category, 0) + 1

# Set-based anomaly filtering (irrelevant but plausible)
known_stable_components = {'mem', 'gpu', 'net'}
detected_issues = set()
for entry in raw_log_entries:
    comp = entry.split(':')[1]
    if comp not in known_stable_components:
        detected_issues.add(comp)

# Spurious bit manipulation - looks important but unused later
anomaly_signature = 0
for issue in detected_issues:
    anomaly_signature ^= hash(issue) & 0xFFFF

# Real signal extraction: count critical errors
critical_errors = log_counter.get('ERROR', 0)
warning_count = log_counter.get('WARN', 0)

# System thresholds with fallback defaults
system_thresholds = {
    'critical_floor': 3,
    'warning_ceiling': 10,
    'decay_rate': 0.85
}

# Complex data restructuring using itertools (actual usage)
flattened_telemetry = list(itertools.chain.from_iterable(telemetry_streams))
spike_events = [x for x in flattened_telemetry if x > 30]

# Decoy statistical summary
mean_spikes = sum(spike_events) / len(spike_events) if spike_events else 0

# Core logic hidden among distractors
steady_low_signals = [x for x in flattened_telemetry if 8 <= x <= 15]
baseline_reference = len(steady_low_signals)

# Conditional override based on error dominance
if critical_errors >= system_thresholds['critical_floor'] and baseline_reference > 5:
    adjustment_factor = 2.5
else:
    adjustment_factor = 0.9

# Multi-step metric fusion
raw_metric = (critical_errors * 17) + (warning_count * 5)
decayed_metric = raw_metric * (system_thresholds['decay_rate'] ** 2)
adjusted_metric = decayed_metric * adjustment_factor

# Final transformation involving set difference (legitimate use)
active_components = {entry.split(':')[1] for entry in raw_log_entries}
redundant_components = active_components - known_stable_components
complexity_bonus = len(redundant_components) * 3

# Key assignment statement
final_diagnostic = int(adjusted_metric + complexity_bonus)

# Distractor: unused function
def analyze_fault_chains(data):
    return sorted(set(itertools.permutations(data, 2)), key=sum)

# Distractor: irrelevant list comprehension
snapshot_moment = [x * 2 + 1 for x in range(8) if x % 3 == 0]

# Print required result
print(f"Result: {final_diagnostic}")