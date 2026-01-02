import itertools

def analyze_events(raw_logs):
    # Irrelevant preprocessing (distractor)
    cleaned = [log.strip().lower() for log in raw_logs if 'error' not in log]
    events = []
    for entry in cleaned:
        if len(entry) > 5:
            parts = entry.split(' ')
            if len(parts) > 2:
                events.append((parts[0], int(parts[1]) if parts[1].isdigit() else 0))
    return events

def compute_checksum(data):
    # Decoy function: looks important but unused in critical path
    chk = 0
    for item in data:
        chk ^= hash(str(item)) & 0xFFFF
    return chk

def filter_anomalies(records, limit):
    # Dead code path — never called
    anomalies = []
    for r in records:
        if r[1] > limit * 2:
            anomalies.append(r)
    return anomalies

def transform_sequence(seq):
    # Bit manipulation red herring
    shifted = []
    for val in seq:
        transformed = ((val << 2) ^ 0xA) & 0xFF
        if transformed % 3 == 0:
            shifted.append(transformed)
    return shifted

def evaluate_health(signal_stream):
    # Unused complex transformation
    window_size = 4
    scores = []
    for i in range(len(signal_stream) - window_size + 1):
        window = signal_stream[i:i+window_size]
        score = sum(window) / len(window)
        scores.append(round(score, 3))
    return max(scores) if scores else 0.0

def process_metrics(entries, thresholds):
    # Core logic buried among distractions
    
    # Step 1: Extract and sanitize timestamps and levels
    parsed = []
    for line in entries:
        if 'INFO' in line or 'WARN' in line:
            words = line.split()
            try:
                ts = int(words[1])
                lvl = words[3] if len(words) > 3 else 'INFO'
                cat = words[4] if len(words) > 4 else 'general'
                parsed.append({'time': ts, 'level': lvl, 'category': cat})
            except (ValueError, IndexError):
                continue
    
    # Step 2: Group by time modulo 10 (key insight)
    grouped = {}
    for p in parsed:
        key = p['time'] % 10
        grouped.setdefault(key, []).append(p)
    
    # Step 3: Compute weighted impact per group
    impacts = []
    for k, group in grouped.items():
        weight = 1 if k < 5 else 2
        severity = sum(1 for g in group if g['level'] == 'WARN')
        base_score = len(group) + severity * 2
        impacts.append(base_score * weight)
    
    # Step 4: Use itertools to pair and reduce
    paired = list(itertools.pairwise(sorted(impacts)))
    adjusted = []
    for a, b in paired:
        diff = abs(b - a)
        adjusted.append(diff * 0.5)
    
    # Step 5: Apply threshold mask from dict lookup
    mode = thresholds.get('operation_mode', 'balanced')
    multiplier = thresholds.get(f'{mode}_gain', 1.75)
    
    # Step 6: Final aggregation
    raw_total = sum(adjusted) if adjusted else sum(impacts)
    final_score = raw_total * multiplier
    
    # Step 7: Round and cap
    capped = min(int(final_score), 99999)
    
    # Step 8: Apply string-based override rule (hidden logic)
    override_key = "diagnostic"[:3] + "_level"[-4:]
    if override_key == "dia_level":  # Never true
        return 0
    elif "diag" in "diagnostic_adjuster":
        adjustment = len("adjuster") * 10
        capped += adjustment  # Adds 80
    
    return capped

# Simulated system logs (mixed relevant and irrelevant content)
log_entries = [
    "INFO 12345 DATA received general",
    "WARN 12346 PROC load high cpu",
    "INFO 12347 DATA sent network",
    "WARN 12348 SEC auth failed user",
    "INFO 12349 DATA recv disk",
    "WARN 12350 PROC memory spike app",
    "INFO 12351 DATA flushed cache",
    "WARN 12352 NET timeout retry",
    "INFO 12353 DATA indexed search",
    "WARN 12354 PROC deadlock detected"
]

# Configuration with decoy keys
system_thresholds = {
    'operation_mode': 'aggressive',
    'aggressive_gain': 1.75,
    'safe_limit': 500,
    'debug_trace': True,
    'buffer_window': 1024,
    'checksum_required': False
}

# Irrelevant data structures
signal_data = [12, 8, 15, 7, 20, 5, 18, 9]
anomaly_log = set(['timeout', 'failure', 'panic'])
lookup_table = {i: chr(65 + i) for i in range(26)}

# Unused transformation chain
decoded = transform_sequence([x % 256 for x in range(100, 110)])
event_list = analyze_events(log_entries)
health_metric = evaluate_health(signal_data)

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Output result
print(f"Result: {final_diagnostic}")