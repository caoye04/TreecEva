import itertools

def analyze_events(events):
    # Irrelevant function – dead code path
    return sum(hash(e) for e in events) % 1000

def compute_signal_strength(data, threshold=5.0):
    # Distractor computation with misleading intermediate result
    magnitude = sum(x ** 2 for x in data) ** 0.5
    normalized = magnitude / (len(data) + 1e-8)
    return normalized > threshold

def extract_timestamps(entries):
    # Unused utility – decoy function
    return [entry['ts'] for entry in entries if 'ts' in entry]

def validate_checksum(record):
    # Red herring: looks important but unused
    return sum(ord(c) for c in record) % 256

def process_metrics(entries, status):
    # Core logic begins
    critical_count = 0
    warning_codes = []
    
    for entry in entries:
        if 'level' in entry:
            if entry['level'] == 'CRITICAL':
                critical_count += 1
                if 'code' in entry:
                    warning_codes.append(entry['code'])
    
    # Bit manipulation red herring
    masked_flags = 0
    for code in warning_codes:
        if isinstance(code, int):
            masked_flags ^= (code << 1) & 0xFF
    
    # Real dependency: count of CRITICAL entries
    base_score = critical_count * 17
    
    # Conditional expression with distractor variables
    adjustment = len(status['active_modules']) if status.get('health_override') else len(status['failed_subsystems'])
    
    # Modular arithmetic used meaningfully
    adjusted_score = (base_score + (adjustment * 3)) % 89
    
    # Dictionary operation that filters out noise
    tag_freq = {}
    for entry in entries:
        tag = entry.get('tag', 'unknown')
        if tag != 'diagnostic':  # Exclude self-referential logs
            tag_freq[tag] = tag_freq.get(tag, 0) + 1
    
    # Use of itertools to create non-trivial transformation
    pairs = list(itertools.combinations(tag_freq.keys(), 2))
    pair_count = len([p for p in pairs if abs(tag_freq[p[0]] - tag_freq[p[1]]) <= 1])
    
    # Final computation combining multiple concepts
    consistency_bonus = 4 if pair_count > 2 else 0
    final_diagnostic = adjusted_score + consistency_bonus + (masked_flags % 10)  # masked_flags usage looks relevant but contribution capped
    
    # Dead code: this branch is never reached due to hard-coded flag
    if False and 'debug' in status:
        final_diagnostic *= 2  # Misleading multiplication
    
    return final_diagnostic

# Simulated log data with mixed relevance
log_entries = [
    {'level': 'INFO', 'tag': 'startup'},
    {'level': 'WARNING', 'tag': 'io', 'code': 42},
    {'level': 'CRITICAL', 'tag': 'memory', 'code': 15},
    {'level': 'CRITICAL', 'tag': 'network', 'code': 23},
    {'level': 'ERROR', 'tag': 'io'},
    {'level': 'CRITICAL', 'tag': 'memory', 'code': 15},  # duplicate tag
    {'level': 'INFO', 'tag': 'diagnostic'},  # excluded from tag count
    {'level': 'CRITICAL', 'tag': 'power', 'code': 30}
]

system_status = {
    'active_modules': ['sensor', 'comms', 'control', 'power_ctrl', 'monitor'],
    'failed_subsystems': ['thermal', 'backup'],
    'health_override': False,
    'version': '2.1.9'
}

# Trigger key computation
final_diagnostic = process_metrics(log_entries, system_status)

# Print result as required
print(f"Result: {final_diagnostic}")