def analyze_system_load(usage_data, threshold):
    # Irrelevant helper: computes entropy (not used in final result)
    def compute_entropy(data):
        from math import log
        freq = {}
        for x in data:
            freq[x] = freq.get(x, 0) + 1
        total = len(data)
        entropy = 0
        for count in freq.values():
            p = count / total
            entropy -= p * log(p)
        return entropy

    # Distractor: unused transformation
    normalized = [x / max(usage_data) for x in usage_data if x > 0]

    # Real logic begins: find first critical spike above threshold
    spike_indices = []
    for i in range(1, len(usage_data)):
        if usage_data[i] > threshold and usage_data[i-1] <= threshold:
            spike_indices.append(i)

    # Dead path: never taken due to condition
    if len(spike_indices) > 100:
        fallback = sum(normalized) // len(normalized)
        return fallback * 2

    return spike_indices[0] if spike_indices else -1


def generate_sequence(seed, length):
    # Unused PRNG-like sequence (red herring)
    seq = [seed]
    for i in range(1, length):
        seq.append((seq[-1] * 1103515245 + 12345) % (1<<31))
    return seq[:length]

# Simulate sensor log entries with timestamps and readings
def process_metrics(entries, limit):
    timestamps = [entry[0] for entry in entries]
    values = [entry[1] for entry in entries]

    # Use enumerate and zip (required Python features)
    anomalies = []
    for idx, (ts, val) in enumerate(zip(timestamps, values)):
        if val > limit:
            anomalies.append((idx, ts, val))

    # Complex but irrelevant aggregation
    cumulative = [0]
    for v in values:
        cumulative.append((cumulative[-1] + v) % 97)  # Modular arithmetic (suggested paradigm)

    # Linear search for first anomaly after warm-up period
    first_anomaly_index = -1
    for i in range(len(anomalies)):
        if anomalies[i][0] > 2:  # Skip early anomalies
            first_anomaly_index = anomalies[i][0]
            break

    # Destructuring assignment (Variable Assignment concept)
    if first_anomaly_index != -1:
        _, peak_time, peak_value = anomalies[0]  # Note: using first, not searched one
    else:
        peak_time, peak_value = timestamps[0], values[0]

    # Bit manipulation red herring
    magic = 0
    temp = peak_time
    while temp:
        magic ^= temp & 1
        temp >>= 1

    # Core calculation: weighted diagnostic score
    base_score = 0
    for i, v in enumerate(values):
        if i % 3 == 0:  # Every third reading contributes
            base_score += v * (i + 1)

    # Final computation - only this matters
    adjustment = len(anomalies) * 17
    raw_diagnostic = base_score - adjustment

    # Multiple assignments (distractor)
    temp_a, temp_b = raw_diagnostic, adjustment
    temp_a, temp_b = temp_b, temp_a  # Swap, irrelevant

    # Final answer derived here
    final_diagnostic = (raw_diagnostic + magic) % 100000

    return final_diagnostic

# Setup: synthetic system log data
timestamp_log = list(range(100, 200, 3))  # Artificial timestamps
readings_log = []
for t in timestamp_log:
    val = (t * 2 + 13) % 89
    if t == 118:
        val = 88  # Inject high value
    readings_log.append(val)

log_entries = list(zip(timestamp_log, readings_log))
system_threshold = 85

# Key execution point
final_diagnostic = process_metrics(log_entries, system_threshold)
print(f"Target result: {final_diagnostic}")