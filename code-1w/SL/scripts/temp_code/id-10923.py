from collections import Counter, defaultdict
import math

# Simulated system log analysis with diagnostic reasoning

def preprocess_logs(raw):
    # Irrelevant transformation: reverses and pads logs (distraction)
    padded = [entry[::-1] + '_X' for entry in raw]
    return [p[2:-2] for p in padded if len(p) > 4]

def count_transitions(seq):
    # Misleading frequency counter (not used in final result)
    transitions = defaultdict(int)
    for i in range(len(seq) - 1):
        key = (seq[i], seq[i+1])
        transitions[key] += 1
    return dict(transitions)

def generate_checksum(data):
    # Decoy function: looks important but unused
    chk = 0
    for item in data:
        chk ^= hash(item) % 100
    return chk + 55

def filter_anomalies(entries, threshold=3):
    # Counts character frequency per entry - partially relevant
    freq_map = []
    for entry in entries:
        char_count = Counter(entry)
        anomalies = sum(1 for c in char_count.values() if c > threshold)
        freq_map.append(anomalies)
    return freq_map

def compute_entropy(signal):
    # Advanced distraction: computes entropy but not used directly
    counts = Counter(signal)
    total = len(signal)
    probs = [n/total for n in counts.values()]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

def extract_features(logs):
    # Extract length patterns and vowel density (some irrelevant)
    features = {}
    vowels = set('aeiou')
    for i, log in enumerate(logs):
        features[i] = {
            'length': len(log),
            'vowel_ratio': round(sum(1 for c in log if c in vowels) / len(log), 3),
            'is_symmetric': log == log[::-1]
        }
    return features

def analyze_pattern(logs, flags):
    # Core logic hidden among distractions
    processed = [log.strip().lower() for log in logs if log.strip()]
    
    # Red herring: complex structure that isn't fully used
    feature_set = extract_features(processed)
    transition_stats = count_transitions([len(x) for x in processed])
    
    # Actual critical path begins here
    flag_values = [f for f in flags if f % 2 == 1]  # Only odd flags matter
    base_score = sum(flag_values) * 10
    
    # Real signal: count logs with repeated characters
    repeat_count = 0
    for log in processed:
        has_repeat = False
        for i in range(len(log) - 1):
            if log[i] == log[i+1]:  # Consecutive duplicate
                has_repeat = True
                break
        if has_repeat:
            repeat_count += 1
    
    # Secondary factor: logs longer than average
    lengths = [len(log) for log in processed]
    avg_len = sum(lengths) / len(lengths)
    long_logs = sum(1 for l in lengths if l > avg_len)
    
    # Final computation (non-obvious from code flow)
    adjustment = (repeat_count * 17) + (long_logs * 3)
    intermediate = base_score + adjustment
    
    # Apply modulo pattern based on system flag sum
    mod_key = sum(flags) % 9 or 1
    final_value = (intermediate * 7) % (mod_key * 13)
    
    # Normalize with fake "diagnostic smoothing"
    smooth_factor = 2 if len(processed) % 2 == 0 else 1
    final_diagnostic = int((final_value * smooth_factor) / 2.0)
    
    # Dead code branch (never executed due to above condition)
    if len(processed) % 7 == 0:
        backup = compute_checksum(processed)
        final_diagnostic = (final_diagnostic + backup) // 3
    
    return final_diagnostic

# Simulated input data
log_entries = [
    'sys@init', 'boot_OK', 'svc_ready', 'svc_ready', 'data_flow',
    'flow_sync', 'sync_init', 'init_done', 'done_reset', 'reset_svc'
]

system_flags = [8, 15, 3, 12, 7, 20, 1, 4, 9, 6, 11]

# Preprocessing calls (distractors)
decoy_checksum = generate_checksum(log_entries)
entropy_metric = compute_entropy([chr(f % 26 + 97) for f in system_flags])

# Actual execution point of interest
final_diagnostic = analyze_pattern(log_entries, system_flags)

# Output result
print(f"Result: {final_diagnostic}")