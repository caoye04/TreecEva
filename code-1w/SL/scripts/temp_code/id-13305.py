import math

def preprocess_logs(raw):
    # Irrelevant preprocessing (dead code path)
    cleaned = []
    for entry in raw:
        if 'ERROR' in entry:
            cleaned.append(entry.strip().lower())
    return [len(x) for x in cleaned]  # Unused result

def compute_entropy(data):
    # Distractor function: computes character frequency entropy but not used in main logic
    freq = {}
    total = 0
    for s in data:
        for c in s:
            freq[c] = freq.get(c, 0) + 1
            total += 1
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def decode_signal(sequence):
    # Bit manipulation red herring
    masked = 0
    for val in sequence:
        masked ^= (val << 2) & 0xFF
    return bin(masked).count('1')

def analyze_pattern(entries, flags):
    # Core logic embedded in distractions
    
    # Decoy variables and structures
    temp_cache = {'a': [], 'b': set(), 'c': {}}
    diagnostic_map = {i: 0 for i in range(25)}
    anomaly_threshold = len(entries) > 5
    
    # Real signal extraction
    critical_values = []
    for idx, entry in enumerate(entries):
        stripped = entry.strip()
        if not stripped:
            continue
        
        # Extract numeric payload from log line
        parts = stripped.split('|')
        if len(parts) < 3:
            continue
        
        # Actual relevant computation begins here
        try:
            # Parse third segment as number
            raw_value = parts[2].strip()
            num = float(raw_value)
            
            # Trigger condition based on string pattern
            tag = parts[0].split(':')[0]
            if tag.startswith('SYS') and 'DEBUG' not in stripped:
                if num.is_integer():
                    critical_values.append(int(num))
        except (ValueError, IndexError):
            pass
    
    # Distractor: unused transformation
    shifted_pairs = [(x >> 1, x << 1) for x in critical_values if x > 0]
    
    # Real aggregation
    base_score = 0
    for v in critical_values:
        if v % 3 == 0 and v % 5 != 0:
            base_score += v * 2
        elif v % 5 == 0:
            base_score -= v // 4
    
    # Control flow with early termination red herring
    if flags.get('safe_mode', False):
        return base_score % 100  # Dead end due to flag state
    
    # Actual key operation
    adjustment_factor = len([e for e in entries if 'WARN' in e])
    intermediate = abs(base_score) + (adjustment_factor * 7)
    
    # Final computation using dictionary state
    status_lookup = {0: 5, 1: 3, 2: 7, 3: 2, 4: 8}
    hash_key = intermediate % 5
    if hash_key in status_lookup:
        final_modifier = status_lookup[hash_key]
        final_diagnostic = (intermediate + final_modifier) * (1 if intermediate % 2 == 1 else -1)
    else:
        final_diagnostic = intermediate
    
    return final_diagnostic

# Main execution with heavy interference
if __name__ == '__main__':
    # Simulated system log entries (mix of relevant and irrelevant)
    log_entries = [
        'SYS1|TIMEOUT|42',
        'NET|DEBUG|abc123|payload',
        'SYS2|CRITICAL|15',
        '',
        'SYS3|||',  # Invalid
        'USR|INFO|value|777',
        'SYS1|WARN|9.0',
        'SYS4|FATAL|30',
        'SYS5|WARN|invalid',
        'SYS6|INFO|6',
        'SYS7|WARN|45'
    ]

    # System configuration with decoy fields
    system_flags = {
        'safe_mode': False,
        'debug_trace': True,
        'buffer_limit': 1024,
        'retry_count': 3,
        'use_ssl': None
    }

    # Call distractor functions to increase interference
    _ = compute_entropy(log_entries)
    _ = decode_signal([len(entry) for entry in log_entries if entry])
    _ = preprocess_logs(log_entries)

    # Key assignment statement
    final_diagnostic = analyze_pattern(log_entries, system_flags)

    # Output result
    print(f"Result: {final_diagnostic}")