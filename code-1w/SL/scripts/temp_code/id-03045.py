def analyze_system_health(raw_logs):
    parsed_data = []
    for entry in raw_logs:
        if 'ERROR' in entry:
            severity = len(entry.split())
            timestamp = sum(ord(c) for c in entry[:10]) % 1000
            code = hash(entry) % 100
            parsed_data.append({'ts': timestamp, 'level': severity, 'code': code})
    
    # Irrelevant transformation (distractor)
    normalized = [d['level'] * 0.8 for d in parsed_data if d['code'] > 10]
    avg_norm = sum(normalized) / len(normalized) if normalized else 0

    # Another red herring: statistical anomaly detection (unused)
    deviations = [(x - avg_norm)**2 for x in normalized]
    variance = sum(deviations) / len(deviations) if deviations else 0

    return parsed_data

# Simulate log preprocessing (decoy function)
def filter_redundant(entries):
    seen = set()
    filtered = []
    for e in entries:
        key = (e['ts'], e['code'])
        if key not in seen:
            filtered.append(e)
            seen.add(key)
    return filtered

# Core metric processor (critical path)
def compute_stability_index(records):
    if not records:
        return 0
    
    total_weight = 0
    cumulative_score = 0
    
    for i, r in enumerate(records):
        weight = i + 1
        # Mix of arithmetic and modular logic
        trend = (r['ts'] + r['level']) % 7
        adjustment = 1 if r['code'] % 2 == 0 else -1
        cumulative_score += (trend * weight * adjustment)
        total_weight += weight
    
    return cumulative_score / total_weight if total_weight else 0

# String-based diagnostic tagger (partial distractor with subtle use)
def generate_diagnostics(flags):
    labels = []
    for f in flags:
        tag = ''
        if f % 15 == 0:
            tag = 'CRITICAL'
        elif f % 5 == 0:
            tag = 'WARNING'
        elif f % 3 == 0:
            tag = 'INFO'
        else:
            tag = 'UNKNOWN'
        labels.append(tag.lower())
    
    # Real usage: count uppercase letters across all tags
    char_count = sum(1 for l in labels for c in l if c.isupper())
    return char_count  # Only this matters indirectly

# Main processing pipeline
def process_metrics(logs, threshold):
    # Parse logs (reuses analysis)
    data = analyze_system_health(logs)
    
    # Dead branch: never taken due to prior filtering
    if any(d.get('invalid') for d in data):
        return -999
    
    # Filter duplicates (unused result)
    clean_data = filter_redundant(data)
    
    # Compute primary metric
    index = compute_stability_index(data)
    
    # Generate auxiliary diagnostics (distractor with side use)
    codes = [entry['code'] for entry in data]
    diag_sum = generate_diagnostics(codes)
    
    # Secondary metric: character pattern in timestamps
    ts_chars = ''.join(str(entry['ts']) for entry in data)
    digit_pairs = [int(ts_chars[i:i+2]) for i in range(0, len(ts_chars)-1, 2)]
    pair_score = sum(p % 11 for p in digit_pairs)  # Irrelevant
    
    # Control flow with conditional expression
    adjustment_factor = diag_sum if abs(index) > threshold else (diag_sum * 2)
    
    # Final computation: combines numeric and string-derived values
    intermediate = int(abs(index)) + adjustment_factor
    final_diagnostic = (intermediate ** 2) % 97  # Key deterministic result
    
    # Dead code path (never reached)
    if False:
        backup = sum(len(log) for log in logs) // 17
        final_diagnostic = backup

    return final_diagnostic

# Input data generation (deterministic seed via string content)
log_input = [
    'ERROR: Disk failure at node A',
    'CRITICAL: Memory overflow detected',
    'ERROR: Network timeout on port 80',
    'FATAL: System halt initiated',
    'ERROR: Failed to write to disk array'
]

system_threshold = 2.5
final_diagnostic = process_metrics(log_input, system_threshold)
print(f"Result: {final_diagnostic}")