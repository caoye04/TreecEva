from collections import defaultdict, Counter
import math

def preprocess_logs(raw):
    # Irrelevant preprocessing step with decoy logic
    tokens = raw.split()
    freq = Counter(tokens)
    noise_floor = sum(freq.values()) / len(freq) if freq else 0
    return [token for token in tokens if freq[token] >= noise_floor]

def validate_checksum(data):
    # Dead code path - never actually used in correct execution
    checksum = 0
    for c in data:
        checksum ^= ord(c) * 3
    return checksum % 256 == 127

def generate_sequence(n):
    # Distractor function: generates Fibonacci-like sequence but unused
    seq = [1, 1]
    for i in range(2, n + 5):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def decode_signal(pattern):
    # Complex-looking but ultimately irrelevant bit manipulation
    acc = 0
    for i, p in enumerate(pattern):
        if p.isdigit():
            acc ^= int(p) << (i % 6)
    return acc & 0xFF

def filter_anomalies(entries):
    # Heavily nested filtering with red herring conditions
    result = []
    severity_map = defaultdict(int)
    for entry in entries:
        parts = entry.split('|')
        if len(parts) < 3:
            continue
        level_str, code, msg = parts[0], parts[1], parts[2]
        try:
            level = int(level_str)
            flag_code = int(code)
        except ValueError:
            continue
        
        # Real logic buried here among distractions
        if 'ERROR' in msg and 'retry' not in msg.lower():
            severity_map[flag_code] += 1
            if level > 3 and flag_code % 4 == 3:
                result.append(entry)
        elif 'CRITICAL' in msg:
            # Misleading branch that looks important
            temp_score = math.log(flag_code + 1) * level
            if temp_score > 10:
                severity_map[flag_code] += 5  # Decoy accumulation
    
    # Return filtered list – only some entries matter
    return result, dict(severity_map)

def evaluate_stability(flag_dict):
    # Unused stability metric – looks important but is a red herring
    total_weight = 0
    for k, v in flag_dict.items():
        if k % 2 == 0:
            total_weight += v * math.sqrt(k + 1)
        else:
            total_weight -= v
    return round(total_weight, 3)

def recursive_diagnose(state, depth):
    # Seemingly critical recursion, but only called with terminal case
    if depth <= 0 or state < 10:
        return state * 2
    if state % 2 == 0:
        return recursive_diagnose(state // 2, depth - 1)
    else:
        return recursive_diagnose(state - 1, depth - 1)

def analyze_pattern(logs, flags):
    # Core logic hidden within multiple layers of distraction
    base_value = 0
    error_count = 0
    
    for log in logs:
        components = log.split('|')
        if len(components) < 3:
            continue
        level, code_str, message = components[0], components[1], components[2]
        try:
            code = int(code_str)
        except ValueError:
            continue
        
        # Actual key condition: count high-level errors with specific code pattern
        if int(level) >= 4 and code % 5 == 2 and 'timeout' in message.lower():
            error_count += 1
            base_value ^= code  # Bitwise combination of qualifying codes
    
    # Secondary factor from flags – only one specific key matters
    special_factor = 0
    for k, v in flags.items():
        if k == 88 and v > 0:
            special_factor = v * 3
        elif k % 7 == 0:  # Looks systematic but irrelevant
            special_factor -= v

    # Final computation – combines real contributions only
    intermediate = (base_value * 17) + (error_count * 100)
    final_score = intermediate - special_factor
    
    # One last twist: if no qualifying logs, fallback to magic number
    if error_count == 0:
        final_score = 42 * 17  # Matches base_value scaling
    
    return final_score

# Simulated system log input – mixture of relevant and irrelevant entries
raw_log_input = '''
3|101|System reboot initiated
5|202|Network timeout detected in module A
4|303|Disk read error, retrying
5|407|Timeout occurred during handshake
4|112|Memory pressure warning
5|512|Critical failure: timeout on channel 3
6|613|Authentication expired
4|702|Connection timeout, retry disabled
'''

# Global configuration flags – many look meaningful
system_configuration = {
    11: 4,   # CPU priority
    22: 0,   # Disk buffer enable
    33: 2,   # Network retries
    44: 1,   # Logging verbosity
    55: 3,   # Timeout threshold
    66: 0,   # Cache invalidation
    77: 5,   # Retry backoff multiplier
    88: 9,   # <-- KEY FLAG: used in analysis
    99: 1,   # Watchdog interval
    100: 4,  # Max connections
}

# Step 1: Preprocess logs (distractor)
token_filtered = preprocess_logs(raw_log_input)

# Step 2: Extract actual structured logs
lines = raw_log_input.strip().split('\n')

# Step 3: Filter anomalies – produces side data but only list matters
filtered_entries, flag_severity = filter_anomalies(lines)

# Step 4: Evaluate stability (dead end)
stability_metric = evaluate_stability(flag_severity)

# Step 5: Generate unused sequence
dummy_sequence = generate_sequence(8)

# Step 6: Decode signal from decoy data
decoded_noise = decode_signal(token_filtered[::3] if len(token_filtered) > 3 else ['1','2'])

# Step 7: Recursive diagnosis with trivial input (red herring)
recursive_result = recursive_diagnose(decoded_noise, 0)

# Step 8: Main analysis – this is where answer is computed
final_diagnostic = analyze_pattern(filtered_entries, system_configuration)

# Output result as required
print(f"Result: {final_diagnostic}")