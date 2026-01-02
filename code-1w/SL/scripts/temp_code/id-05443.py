from collections import defaultdict, Counter
import math

# Simulated system log processing with diagnostic computation

def analyze_frequency(data):
    # Irrelevant helper: computes symbol frequencies (not used in final result)
    freq = defaultdict(int)
    for item in data:
        freq[item] += 1
    return freq

def validate_checksum(entry):
    # Dead code path: never called
    return sum(ord(c) for c in entry) % 7 == 0

def extract_timestamp(record):
    # Distractor function: used in unused branch
    return int(record.split('-')[1]) if '-' in record else 0

def legacy_filter(items):
    # Obsolete filtering logic (never invoked)
    return [x for x in items if len(x) > 3 and 'X' not in x]

def compute_entropy(values):
    # Red herring: looks important but unused
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)

def accumulate_signals(logs):
    # Partially relevant: builds intermediate structure but only one field matters
    signal_map = defaultdict(list)
    temp_values = []
    for log in logs:
        parts = log.split(':')
        key = parts[0]
        val = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
        signal_map[key].append(val)
        if key == 'DBG':
            temp_values.append(val * 2)
    
    # Derived metric not used in final answer
    avg_dbg = sum(temp_values) / len(temp_values) if temp_values else 0
    
    # But we do extract this one value (used later)
    critical_peak = max(temp_values) if temp_values else 0
    
    return signal_map, critical_peak

def evaluate_thresholds(peaks, flags):
    # Complex conditional logic with misleading branches
    level = 0
    emergency_count = 0
    for p in peaks:
        if p > 100:
            emergency_count += 1
            level += 3
        elif p > 50:
            level += 2
        else:
            level += 1
    
    # Flags introduce side logic that seems important
    flag_analysis = Counter(flags)
    if flag_analysis['ERR'] > 2:
        level += 5
    if flag_analysis['WRN'] > 4:
        level *= 1.1
    
    # Decoy return component
    diagnostics = {
        'level': int(level),
        'alerts': emergency_count,
        'raw_flags': flag_analysis
    }
    
    return int(level), diagnostics

def process_metrics(entries, config_flags):
    # Main data flow with hidden simplicity amid complexity
    raw_signals, primary_spike = accumulate_signals(entries)
    
    # Extract sequences for certain keys (some irrelevant)
    sequence_A = raw_signals.get('SYS', [])
    sequence_B = raw_signals.get('DBG', [])
    sequence_C = raw_signals.get('IO', [])
    
    # Compute multiple aggregates (only one matters)
    base_score = sum(sequence_B) * 3
    adjustment = len(sequence_A) - len(sequence_C)
    volatility = sum(abs(a - b) for a, b in zip(sequence_C, sequence_C[1:]))
    
    # Hidden core logic: find first even number in DBG sequence doubled
    target_value = None
    for x in sequence_B:
        if x % 2 == 0:
            target_value = x * 2
            break
    
    if target_value is None:
        target_value = primary_spike
    
    # Multi-step transformation chain
    stage_1 = (target_value + base_score) // 2
    stage_2 = stage_1 ^ 257  # Bit manipulation red herring
    stage_3 = stage_2 + adjustment
    
    # Conditional bypass based on length
    if len(entries) % 2 == 1:
        stage_3 -= 17
    
    # Final threshold evaluation (uses config_flags)
    peaks_of_interest = [primary_spike, stage_3 % 100]
    threat_level, _ = evaluate_thresholds(peaks_of_interest, config_flags)
    
    # The real answer is embedded here
    final_diagnostic = stage_3 * threat_level
    
    # Unused derived values (distractors)
    entropy_measure = compute_entropy([stage_1, stage_2, stage_3])
    frequency_map = analyze_frequency([f"{x}" for x in entries])
    
    return final_diagnostic

# Simulated input data
log_entries = [
    "SYS:45", "DBG:13", "IO:88", "DBG:19", "SYS:67",
    "DBG:22", "IO:89", "IO:92", "SYS:44", "DBG:11",
    "IO:95", "DBG:24", "SYS:68", "IO:91"
]

system_flags = ['OK', 'OK', 'ERR', 'WRN', 'OK', 'ERR', 'WRN', 'WRN', 'ERR', 'WRN', 'OK', 'WRN']

# Key execution point
final_diagnostic = process_metrics(log_entries, system_flags)

print(f"Result: {final_diagnostic}")