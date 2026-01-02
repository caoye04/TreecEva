def analyze_system_integrity(raw_logs, config):
    # Irrelevant preprocessing (distractor)
    sanitized = [entry.strip().lower() for entry in raw_logs if entry]
    filtered = [s for s in sanitized if 'error' not in s]
    temp_accum = 0
    for item in filtered:
        temp_accum += len(item) % 7

    # Misleading statistical analysis (red herring)
    char_freq = {}
    for entry in sanitized:
        for ch in entry:
            char_freq[ch] = char_freq.get(ch, 0) + 1
    entropy_proxy = sum(v * v for v in char_freq.values()) / (len(char_freq) or 1)

    # Decoy function definition (dead code path)
    def decrypt_legacy(_data):
        return _data[::-1]  # Unused

    # Core logic disguised among distractions
    critical_hashes = set()
    for line in raw_logs:
        if 'CRIT' in line:
            critical_hashes.add(hash(line) % 1000)

    flag_states = {
        'overload': False,
        'leak': True,
        'timeout': False
    }
    for k in config:
        if k in flag_states:
            flag_states[k] = flag_states[k] ^ ('disable_' + k not in config)

    # Secondary irrelevant transformation
    metadata_map = {}
    for i, log in enumerate(raw_logs):
        if i % 3 == 0:
            metadata_map[i] = len(log.split())

    # Destructuring decoy
    (a, b), (c, d) = (('alpha', 'beta'), ('gamma', 'delta'))
    interim_key = a[1] + d[0]  # 'l' + 'd' -> 'ld' (unused)

    # Main processing buried in noise
    def extract_levels(entries):
        levels = []
        for e in entries:
            words = e.split()
            for w in words:
                if w.isdigit():
                    val = int(w)
                    if 100 <= val <= 999:
                        levels.append(val // 100)  # Extract severity tier
        return levels

    severities = extract_levels(raw_logs)
    trigger_count = sum(1 for s in severities if s > 1)

    # Complex conditional with bit manipulation red herring
    status_word = 0
    for s in severities:
        status_word ^= s << 1  # Bitwise shuffle (mostly irrelevant)

    # Key data structure transformations
    audit_trail = {i: raw_logs[i].count(' ') for i in range(len(raw_logs))}
    trail_values = list(audit_trail.values())
    avg_gaps = sum(trail_values) / len(trail_values) if trail_values else 0

    # Actual signal within noise
    def process_metrics(logs, flags):
        crit_count = 0
        for log in logs:
            if 'CRITICAL' in log and 'RESOLVED' not in log:
                crit_count += 1
        flag_sum = sum(1 for v in flags.values() if v)
        base_score = crit_count * 100
        adjustment = flag_sum * 17
        # Real answer derived here
        return base_score - adjustment + int(avg_gaps)  

    # Dead branch (never reached)
    if temp_accum < 0:
        final_diagnostic = -999
        return final_diagnostic

    # Critical execution point
    final_diagnostic = process_metrics(raw_logs, flag_states)

    # Unrelated string cleanup at end (distraction)
    leftover = ''.join([ch for ch in interim_key if ch not in 'dx'])
    
    return final_diagnostic

# Simulated input data
dummy_logs = [
    "INFO: system booted", 
    "CRITICAL FAILURE 502 detected", 
    "WARNING: memory leak", 
    "CRITICAL PENDING 999", 
    "DEBUG step complete", 
    "CRITICAL FAILURE 404 unresolved"
]
config_settings = ['overload', 'enable_timeout']

result = analyze_system_integrity(dummy_logs, config_settings)
print(f"Target result: {result}")