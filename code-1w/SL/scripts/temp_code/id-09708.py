import math

def preprocess_data(raw):
    # Distractor: complex normalization with unused branches
    if len(raw) == 0:
        return [0]
    normalized = []
    max_val = max(raw)
    for x in raw:
        if x > 0:
            normalized.append(math.log(x + 1) / math.log(max_val + 1))
        else:
            normalized.append(0)
    return normalized

# Irrelevant utility function (dead code path)
def decrypt_hash(s):
    return ''.join(chr(ord(c) - 1) for c in s[::-1])

# Unused but plausible-looking data transformation
def shift_bits(n, direction='left'):
    if direction == 'left':
        return (n << 3) & 0xFF
    else:
        return (n >> 2) & 0xFF

# Decoy metric that looks important but isn't used
def calculate_entropy(values):
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    probs = [f / len(values) for f in freq.values()]
    return -sum(p * math.log2(p) for p in probs)

# Real logic begins here — subtle trigger in string pattern
def analyze_pattern(text):
    counts = {c: text.count(c) for c in set(text)}
    score = 0
    for k, v in counts.items():
        if k in 'aeiou':
            score += v * 1.5
        elif k.isalpha():
            score -= v * 0.5
    return score

# Core evaluation function with mixed concerns
def evaluate_performance(log_data, config):
    total = 0
    adjustments = []
    
    # Real processing branch
    for entry in log_data:
        if not isinstance(entry, dict) or 'event' not in entry:
            continue
            
        event_type = entry['event']
        timestamp = entry.get('ts', 0)
        
        # Real scoring logic hidden among distractions
        if event_type.startswith('TASK_'):
            base_points = len(event_type) * 2
            
            # String method distraction with actual impact
            modifier_key = event_type.lower().replace('task_', '')
            if 'critical' in modifier_key:
                base_points *= 3
            elif 'backup' in modifier_key:
                base_points //= 2
            
            # Dictionary lookup that matters
            if modifier_key in config['multipliers']:
                base_points *= config['multipliers'][modifier_key]
            
            total += base_points
            
            # Actual adjustment recorded
            adjustments.append(base_points)
        
        # Dead branch: looks relevant but never triggers due to data
        if event_type == 'DEBUG_TRACE':
            temp = shift_bits(len(event_type), 'right')
            total -= temp % 7

    # Final computation using real results
    avg_adjust = sum(adjustments) / len(adjustments) if adjustments else 0
    stability_penalty = abs(len(adjustments) - config['target_count']) * 1.2
    
    # The actual answer is computed here
    final_raw = total + avg_adjust - stability_penalty
    
    # Red herring: entropy-like calculation on irrelevant data
    dummy_seq = [len(str(x)) for x in range(1, 8) if x % 3 != 0]
    fake_entropy = sum(math.log(d + 1) for d in dummy_seq)
    
    # Only this line matters at the end
    return int(final_raw - fake_entropy + 5.7)  # Adjustment to land on deterministic integer

# Simulated input data with meaningful structure
raw_input = [10, 25, 30, 45, 60]
normalized_input = preprocess_data(raw_input)

# Plausible but partially unused configuration
decoy_string = "khoor#zruog"  # Encrypted 'hello world' — irrelevant
decoded = decrypt_hash(decoy_string)  # Computed but unused

metrics = {
    'multipliers': {
        'init': 1.2,
        'critical': 2.5,
        'cleanup': 0.8
    },
    'target_count': 4,
    'threshold': 15
}

data_log = [
    {'event': 'TASK_init', 'ts': 1001},
    {'event': 'TASK_critical', 'ts': 1002},
    {'event': 'TASK_cleanup', 'ts': 1003},
    {'event': 'TASK_critical', 'ts': 1004},
    {'event': 'DEBUG_TRACE', 'ts': 1005},  # Triggers dead code
    {'event': 'TASK_init', 'ts': 1006}
]

# Real execution point
final_score = evaluate_performance(data_log, metrics)

# Print result as required
print(f"Result: {final_score}")