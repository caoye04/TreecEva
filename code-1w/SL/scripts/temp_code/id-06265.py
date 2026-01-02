import itertools

# Simulated system telemetry and diagnostic module
def analyze_throughput(records):
    if not records:
        return 0
    total = sum(r[1] for r in records)
    count = len(records)
    return total / count if count else 0

# Irrelevant helper - distractor function
def deprecated_checksum(data):
    acc = 0
    for c in data:
        acc = (acc + ord(c)) % 257
    return acc

# Unused transformation path - dead code branch
def legacy_normalize(values):
    factor = max(values) if values else 1
    return [v / factor * 100 for v in values]

# Core signal filter - actually used indirectly
def extract_signals(raw_data, threshold=0.75):
    filtered = []
    for entry in raw_data:
        timestamp, val, active = entry[0], entry[1], entry[2]
        if active and val > threshold:
            filtered.append((timestamp, val))
    return filtered

# Misleading aggregation - looks important but unused
def compute_rolling_score(seq, window=3):
    if len(seq) < window:
        return 0
    scores = []
    for i in range(len(seq) - window + 1):
        window_avg = sum(seq[i:i+window]) / window
        penalty = abs(seq[i] - seq[i+window-1])
        scores.append(window_avg - penalty * 0.1)
    return max(scores) if scores else 0

# Key diagnostic aggregator - this is where final_diagnostic comes from
def aggregate_metrics(log_entries, flags):
    critical_level = flags.get('CRITICAL_OVERRIDE', 0)
    base_scores = [entry[1] * 1.5 for entry in log_entries if entry[1] > 0.5]
    
    # Apply conditional scaling based on flag combinations
    if flags.get('ENHANCED_MODE') and flags.get('STABILITY_PATCH'):
        base_scores = [s ** 1.2 for s in base_scores]
    
    # Real computation path
    temp_result = sum(base_scores)
    adjustment = len(list(itertools.groupby(base_scores, key=lambda x: x > 7.0))) * 2.5
    
    # Add side channel input from secondary analysis
    secondary_input = 0
    status_chain = ''.join(['1' if f else '0' for f in flags.values() if isinstance(f, bool)])
    if len(status_chain) >= 6:
        # Count alternating patterns
        alternations = sum(1 for i in range(1, len(status_chain)) if status_chain[i] != status_chain[i-1])
        secondary_input = alternations * 0.7
    
    # Final composition
    result = temp_result + adjustment + secondary_input
    return round(result * 10) / 10  # Normalize to one decimal

# --- Simulation Data Setup ---
data_stream = [
    ('T1', 0.3, False), ('T2', 0.8, True), ('T3', 0.9, True), ('T4', 0.4, True),
    ('T5', 0.7, True), ('T6', 0.95, True), ('T7', 0.6, False), ('T8', 0.85, True)
]

# Diagnostic metadata - contains red herrings
timing_log = extract_signals(data_stream, threshold=0.65)

# Extensive flag configuration with irrelevant entries
system_flags = {
    'ENHANCED_MODE': True,
    'STABILITY_PATCH': True,
    'DEBUG_TRACE': False,
    'VERBOSE_OUTPUT': True,
    'SECURITY_LOCK': False,
    'NETWORK_BOOST': True,
    'LEGACY_FALLBACK': False,
    'CRITICAL_OVERRIDE': 0  # Not active
}

# Dead computation branches - misleading usage
snapshot_values = [item[1] for item in data_stream]
normalized_snapshot = legacy_normalize(snapshot_values)  # Computed but unused
rolling_insight = compute_rolling_score(snapshot_values)  # Another unused metric

# Side-channel diagnostic using character logic
mode_signature = "EnhancedStability"
char_count = sum(1 for c in mode_signature if c.isupper())
weight_offset = char_count * 0.3

# Trigger actual target computation
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print final result as required
print(f"Target result: {final_diagnostic}")