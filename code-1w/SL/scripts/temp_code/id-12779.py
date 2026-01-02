from collections import defaultdict, Counter
from itertools import cycle

# Simulated system telemetry stream
def generate_telemetry():
    return [
        {'node': 'A', 'temp': 68, 'load': 0.45, 'errors': 2},
        {'node': 'B', 'temp': 75, 'load': 0.68, 'errors': 1},
        {'node': 'C', 'temp': 83, 'load': 0.89, 'errors': 5},
        {'node': 'A', 'temp': 71, 'load': 0.52, 'errors': 1},
        {'node': 'B', 'temp': 73, 'load': 0.61, 'errors': 0},
        {'node': 'C', 'temp': 85, 'load': 0.93, 'errors': 7}
    ]

# Irrelevant helper - looks useful but unused in critical path
def rolling_average(data, window=3):
    result = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        result.append(sum(data[start:i+1]) / (i - start + 1))
    return result

# Decoy function - never called
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return entropy

# Real processing chain
def extract_errors(logs):
    error_map = defaultdict(list)
    temp_cache = {}  # Red herring: partially used, distracts from flow
    for entry in logs:
        node = entry['node']
        error_map[node].append(entry['errors'])
        temp_cache[node] = entry['temp']  # Written but not used later
    return error_map

# Another irrelevant transformation
def shift_cipher(text, key=3):
    return ''.join(chr((ord(c) - ord('a') + key) % 26 + ord('a')) if c.isalpha() else c for c in text)

# Core logic buried among distractions
def analyze_stability(error_lists):
    instability_score = 0
    for node, errors in error_lists.items():
        consecutive_bursts = 0
        for i in range(1, len(errors)):
            if errors[i] > errors[i-1] and errors[i] >= 3:
                consecutive_bursts += 1
        # Bit manipulation red herring
        masked = consecutive_bursts & 0xFF
        instability_score += masked << 1
    return instability_score

# Misleading normalization function
def normalize_readings(readings):
    max_val = max(readings) if readings else 1
    return [round(x / max_val, 3) for x in readings]

# Critical threshold engine with hidden logic
def apply_thresholds(scores, base_limit=10):
    adjusted = 0
    for score in scores:
        if score > base_limit:
            adjusted += score * 1.5
        elif score == base_limit:
            adjusted += score
        else:
            adjusted += score * 0.8
    return int(adjusted)

# Main data processor
def process_metrics(log_entries, limits):
    # Step 1: Extract error sequences
    error_history = extract_errors(log_entries)
    
    # Dead code branch: looks important but unused
    if len(log_entries) > 100:
        fallback = sum(limits.values()) // len(limits)
        return fallback
    
    # Step 2: Compute raw stability metrics
    raw_scores = {}
    for node, errors in error_history.items():
        peak = max(errors)
        freq = sum(1 for e in errors if e >= 3)
        raw_scores[node] = (peak * 2) + freq  # Composite metric
    
    # Step 3: Analyze pattern-based instability
    instability_base = analyze_stability(error_history)
    
    # Distractor: complex but irrelevant bit arithmetic
    magic_key = 0xABC
    salted = (instability_base ^ magic_key) & 0xFFFF
    blended = (salted >> 4) | ((salted & 0xF) << 12)
    
    # Step 4: Apply business rules (only this matters)
    rule_adjusted = apply_thresholds(raw_scores.values(), limits['error_base'])
    
    # Final computation buried in noise
    multiplier = len([e for e in log_entries if e['load'] > 0.85])
    penalty = 0
    for entry in log_entries:
        if entry['temp'] > 80 and entry['errors'] > 3:
            penalty += 2
    
    # Actual answer determination
    final_value = rule_adjusted - penalty
    
    # Irrelevant string transformation (dead end)
    status_flag = shift_cipher('diagnostic', final_value % 26)
    
    return final_value

# Global configuration (some values are decoys)
thresholds = {
    'temp_ceiling': 90,
    'load_warning': 0.75,
    'error_base': 10,
    'heartbeat_interval': 5
}

# Generate input data
log_data = generate_telemetry()

# Execute main logic
temp_summary = {item['node']: item['temp'] for item in log_data}  # Unused
load_series = [entry['load'] for entry in log_data]  # Partially irrelevant
final_diagnostic = process_metrics(log_data, thresholds)
print(f"Target result: {final_diagnostic}")