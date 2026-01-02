from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
raw_readings = [104.5, 98.2, 110.8, 95.1, 119.3, 108.7, 92.3, 125.6, 112.4, 88.9]
status_flags = [True, False, True, True, False, True, True, False, True, True]

# Irrelevant auxiliary data (distractor)
legacy_mapping = {'A': 1, 'B': 2, 'C': 3}
scaling_factors = [1.01, 0.99, 1.02, 1.00, 0.98]
offset_adjustment = sum(scaling_factors) * 0.5  # unused in logic

# System configuration (some values are red herrings)
system_thresholds = {
    'critical': 115.0,
    'warning': 100.0,
    'decay_rate': 0.85,
    'gain_factor': 2.1,
    'buffer_size': 512  # unused
}

# Log entry structure with multiple fields (only some are used)
class LogEntry:
    def __init__(self, ts, val, flag, source='sensor'):
        self.timestamp = ts
        self.value = val
        self.flag = flag
        self.source = source
        self.checksum = hash((ts, val)) % 1000  # irrelevant

log_entries = [
    LogEntry(t, v, f) for t, v, f in zip(
        timestamps * 2,  # duplicates to mislead
        raw_readings,
        status_flags
    )
]

# Decoy function that looks important but isn't called
def compute_legacy_score(data):
    weighted = [d * 0.9 for d in data if d > 90]
    return sum(weighted) / len(weighted)

# Another decoy using lambda and collections in a misleading way
decoy_aggregator = lambda logs: defaultdict(float, {
    'total_valid': sum(1 for log in logs if log.flag),
    'avg_time': sum(log.timestamp for log in logs) / len(logs)
})

# Real processing begins here
weighting_scheme = [0.7, 1.0, 1.3]  # low, normal, high weights based on thresholds

def classify_reading(val, thresholds):
    if val >= thresholds['critical']:
        return 2  # high priority
    elif val >= thresholds['warning']:
        return 1  # medium
    else:
        return 0  # low

def calculate_decay(value, iterations, rate):
    for _ in range(iterations):
        value *= rate
    return value

def process_metrics(entries, config):
    # Build frequency map of classifications
    classification_count = defaultdict(int)
    raw_values = []
    flagged_values = []

    for entry in entries:
        raw_values.append(entry.value)
        if entry.flag:
            flagged_values.append(entry.value)

    # Only flagged entries are processed further
    for val in flagged_values:
        cat = classify_reading(val, config)
        classification_count[cat] += 1

    # Compute base aggregate (mean of flagged)
    if not flagged_values:
        base_score = 0.0
    else:
        base_score = sum(flagged_values) / len(flagged_values)

    # Apply decay transformation three times (simulates signal filtering)
    adjusted_score = calculate_decay(base_score, 3, config['decay_rate'])

    # Boost score based on high-severity prevalence
    high_severity_ratio = classification_count[2] / len(flagged_values) if flagged_values else 0
    if high_severity_ratio > 0.4:
        adjusted_score *= config['gain_factor']
    elif high_severity_ratio > 0.2:
        adjusted_score *= 1.5
    else:
        adjusted_score *= 1.1

    # Secondary adjustment based on entropy-like measure
    counter = Counter(classification_count.keys())
    diversity_index = sum(counter.values()) / (max(counter.values()) or 1)

    # Diversity boost only if more than one category present
    if diversity_index > 1.0:
        adjusted_score *= (1.0 + diversity_index * 0.1)

    # Final non-linear transformation
    final_score = math.log(adjusted_score + 1) ** 2

    # Dead code branch (never reached due to logic above)
    if len(entries) < 5:
        fallback = sum(raw_values) % 100
        return fallback  # unreachable

    # Key result variable
    final_diagnostic = int(round(final_score * 100))

    # Spurious assignment to distract
    temp_result = {"score": final_diagnostic, "meta": "processed"}
    temp_result["checksum"] = sum(temp_result.values()) % 1000  # irrelevant

    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Output result as required
print(f"Target result: {final_diagnostic}")