from collections import defaultdict, Counter
from itertools import zip_longest

def analyze_events(event_stream, filters):
    # Irrelevant preprocessing (distractor)
    sanitized = [e.lower().strip() for e in event_stream if e]
    frequency_map = Counter(sanitized)
    filtered_results = []
    for key, count in frequency_map.items():
        if any(f in key for f in filters):
            filtered_results.append((key, count * 2))
    return filtered_results

def compute_health_score(metrics, weights):
    # Misleading health computation (dead path)
    score = 0
    for m, w in zip(metrics, weights):
        score += (m % 7) * w
    return round(score / sum(weights), 3)

def generate_report(snapshot, config):
    # Unused report generator (red herring)
    lines = []
    for k, v in snapshot.items():
        status = 'CRITICAL' if v > config.get(k, 100) else 'OK'
        lines.append(f'{k}: {v} [{status}]')
    return '\n'.join(lines)

def extract_signals(raw_logs):
    # Signal extraction with decoy transformations
    signals = []
    buffer = []
    for log in raw_logs:
        parts = log.split('|')
        if len(parts) < 3:
            continue
        timestamp, level, msg = parts[0], parts[1], parts[2]
        try:
            priority = len(msg) % 5 + ord(level[0]) % 10
            buffer.append(priority)
        except:
            pass
    # Real signal: average of transformed priorities
    if buffer:
        avg_priority = sum(buffer) / len(buffer)
        signals.append(int(avg_priority * 100))
    return signals

def validate_checksum(data):
    # Complex but irrelevant checksum logic
    chk = 0
    for i, val in enumerate(data):
        chk ^= (val * (i + 1)) % 256
    return chk == 128  # Rare condition (almost never true)

def process_metrics(log_entries, thresholds):
    # Core logic buried in distractions
    temp_readings = []
    error_flags = []
    diagnostic_log = defaultdict(int)
    
    # Real data processing starts here
    for entry in log_entries:
        if not entry or '|' not in entry:
            continue
        
        # Parse log structure
        segments = entry.strip().split('|')
        code = segments[0].strip()
        value_str = segments[1].strip()
        category = segments[2].strip()
        
        if not value_str.isdigit():
            continue
            
        value = int(value_str)
        
        # Only entries with category 'SYS_TEMP' are relevant
        if category == 'SYS_TEMP':
            temp_readings.append(value)
            diagnostic_log['temp_count'] += 1
            
        # Distraction: collect error codes anyway
        if code.startswith('ERR'):
            error_flags.append(code)

    # Key computation: median filtering and threshold adjustment
    if not temp_readings:
        return -999
    
    sorted_temps = sorted(temp_readings)
    mid = len(sorted_temps) // 2
    median_temp = (sorted_temps[mid] + sorted_temps[-(mid + 1)]) / 2
    
    # Apply dynamic threshold from input
    base_threshold = thresholds.get('thermal', 75)
    adjusted_limit = base_threshold * (1.0 + 0.1 * diagnostic_log['temp_count'] / (len(temp_readings) + 1))
    
    # Final diagnostic: difference scaled by count
    deviation = abs(median_temp - adjusted_limit) * len(temp_readings)
    final_value = int(deviation)
    
    # Dead branch: never reached due to logic above
    if validate_checksum([final_value]):
        final_value *= 2
    
    return final_value

# Simulated sensor log data (mixed content)
log_data = [
    'SYS|120|ERROR_CRITICAL|...',
    'ERR_502|45|NET_LATENCY',
    'TMP|68|SYS_TEMP',
    'TMP|72|SYS_TEMP',
    'TMP|70|SYS_TEMP',
    'LOG|NA|HEARTBEAT',
    'TMP|76|SYS_TEMP',
    'TMP|74|SYS_TEMP',
    'DIAG|1024|SYS_SELFTEST',
    '',
    'TMP|71|SYS_TEMP',
    'SEC|0|AUTH_SUCCESS'
]

# System thresholds configuration (misleading extra keys)
system_thresholds = {
    'thermal': 73,
    'pressure': 85,
    'humidity': 60,
    'vibration': 12
}

# Extract auxiliary signals (irrelevant to final result)
signal_burst = extract_signals(log_data)
analysis_outcome = analyze_events(
    [entry for entry in log_data if entry], 
    ['ERR', 'CRIT']
)

# Compute phantom health score (distraction)
health_diagnosis = compute_health_score(
    [len(log_data), signal_burst[0] if signal_burst else 0, 5], 
    [0.5, 0.3, 0.2]
)

# Generate unused report
report_text = generate_report(
    {'entries': len(log_data), 'signals': len(signal_burst)}, 
    {'entries': 50, 'signals': 3}
)

# Critical execution point
final_diagnostic = process_metrics(log_data, system_thresholds)

# Output result
print(f"Result: {final_diagnostic}")