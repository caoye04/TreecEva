from collections import Counter, defaultdict
import math

# Simulated system log processor with diagnostic analysis

def preprocess_logs(raw):    
    processed = []
    noise_filter = {'DEBUG', 'TRACE', 'VERBOSE'}
    for entry in raw:
        if entry['level'] not in noise_filter and len(entry['message']) > 3:
            processed.append(entry)
    return processed

# Irrelevant helper - distractor
def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Dead function - never called, red herring
def legacy_checksum(seq):
    chk = 0
    for i, c in enumerate(seq):
        chk ^= (ord(c) + i) % 256
    return chk

# Auxiliary transformation - looks important but only partially used
def extract_tokens(logs):
    tokens = []
    token_freq = defaultdict(int)
    for log in logs:
        words = log['message'].upper().split()
        for word in words:
            clean = ''.join(filter(str.isalpha, word))
            if clean:
                tokens.append(clean)
                token_freq[clean] += 1
    return tokens, dict(token_freq)

# Core analysis logic
def evaluate_threshold(value, base=100):
    if value < base * 0.25:
        return 'LOW'
    elif value < base * 0.75:
        return 'MEDIUM'
    else:
        return 'HIGH'

# Misleading aggregation - appears central but is unused in final result
def aggregate_severity(logs):
    severity_map = {'ERROR': 3, 'WARNING': 2, 'INFO': 1}
    total = 0
    for log in logs:
        total += severity_map.get(log['level'], 0)
    return total

# Key pattern analyzer - actually contributes to answer
def analyze_pattern(entries, flags):
    # Step 1: Count specific error types
    error_count = 0
    for e in entries:
        if 'ERROR' in e['level'] and 'timeout' in e['message'].lower():
            error_count += 1

    # Step 2: Extract all numeric codes from messages
    codes = []
    for e in entries:
        parts = e['message'].split()
        for part in parts:
            if part.isdigit() and 100 <= int(part) <= 999:
                codes.append(int(part))
    
    # Step 3: Compute weighted sum using position and flag state
    weighted_sum = 0
    for i, code in enumerate(codes):
        weight = 1.5 if flags['priority_mode'] else 0.8
        adjustment = 2 if code % 2 == 0 else -1
        weighted_sum += code * weight + adjustment * (i + 1)
    
    # Step 4: Apply conditional correction based on count
    if error_count >= 2:
        weighted_sum = int(weighted_sum * 0.85)
    
    # Step 5: Use string method to filter correction factor
    correction_key = ''.join([f.lower() for f in flags])[:3]
    if correction_key == 'pri':
        weighted_sum -= 17
    
    # Step 6: Final threshold evaluation feeds into output
    baseline = 42
    if evaluate_threshold(weighted_sum, baseline * 10) == 'HIGH':
        multiplier = 3
    else:
        multiplier = 2
    
    # Final computation
    intermediate = weighted_sum + error_count * 11
    final_score = intermediate * multiplier
    
    # This is the actual answer variable
    final_diagnostic = final_score - 84
    
    return final_diagnostic

# --- Simulation Setup ---
if __name__ == '__main__':
    # Realistic input data
    raw_log_data = [
        {'timestamp': 1641024000, 'level': 'ERROR', 'message': 'Connection timeout detected at node 502'},
        {'timestamp': 1641024001, 'level': 'WARNING', 'message': 'High latency observed in cluster B'},
        {'timestamp': 1641024002, 'level': 'ERROR', 'message': 'Timeout occurred with code 704'},
        {'timestamp': 1641024003, 'level': 'INFO', 'message': 'System reboot initiated'},
        {'timestamp': 1641024004, 'level': 'ERROR', 'message': 'Critical failure 208 timeout'}
    ]

    # System configuration flags
    system_flags = {
        'priority_mode': True,
        'debug_trace': False,
        'retry_enabled': True
    }

    # Irrelevant preprocessing chain - distractor
    cleaned_logs = preprocess_logs(raw_log_data)
    all_tokens, frequency_map = extract_tokens(cleaned_logs)
    entropy_value = compute_entropy(all_tokens)  # Computed but unused

    # Another unused aggregation
    total_severity = aggregate_severity(cleaned_logs)

    # Critical execution point
    final_diagnostic = analyze_pattern(cleaned_logs, system_flags)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")