from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456000 + i * 300 for i in range(20)]
raw_signals = [2.3, 1.8, 4.5, 3.2, 5.1, 4.9, 6.2, 5.8, 7.3, 6.9, 8.1, 7.7, 9.0, 8.6, 9.4, 9.2, 9.8, 9.6, 10.0, 9.9]

# Irrelevant auxiliary data (distractor)
user_sessions = defaultdict(lambda: {'start': 0, 'active': False, 'data_volume': 0})
for i in range(15):
    user_sessions[f'user_{i}']['data_volume'] = (i ** 3) % 1024

# Signal normalization and noise filtering (partially relevant)
normalized = [(x - min(raw_signals)) / (max(raw_signals) - min(raw_signals)) * 10 for x in raw_signals]
filtered = [x for x in normalized if x > 1.5]  # Remove near-zero noise

# System flag simulation with decoy logic
system_flags = {}
for t in timestamps:
    flag_code = (t % 17) ^ 3
    system_flags[t] = {
        'error': flag_code % 3 == 0,
        'warning': flag_code % 5 == 0,
        'debug': flag_code % 7 == 0,
        'legacy_mode': False  # Dead constant (distractor)
    }

# Decoy function - never called (dead code path)
def legacy_calibrate(data):
    return sum(x ** 0.5 for x in data if x > 0) // len(data)

# Auxiliary statistic (misleading intermediate)
avg_normalized = sum(normalized) / len(normalized)
stdeviation = (sum((x - avg_normalized) ** 2 for x in normalized) / len(normalized)) ** 0.5

# Log entry construction with metadata bloat
log_entries = []
for i, ts in enumerate(timestamps):
    entry = {
        'timestamp': ts,
        'value': round(filtered[i] if i < len(filtered) else 0.0, 2),
        'category': 'CRITICAL' if i % 4 == 0 else 'INFO',
        'checksum': (ts * 3 + i) % 10007,
        'retries': 0,
        'meta': {'source': 'sensor_A', 'version': '2.1'}  # Extra nesting (distractor)
    }
    if i % 5 == 0:
        entry['retries'] = (i * 2) % 4
    log_entries.append(entry)

# Real processing begins here — complex analysis with cross-references
def extract_cycles(entries, flags):
    cycles = []
    temp_cycle = []
    for e in entries:
        ts = e['timestamp']
        if flags[ts]['error'] or len(temp_cycle) > 5:
            if temp_cycle:
                cycles.append(temp_cycle)
            temp_cycle = []
        else:
            temp_cycle.append(e['value'])
    if temp_cycle:
        cycles.append(temp_cycle)
    return cycles

# Secondary transformation with combinatorics flavor
def compute_entropy(values):
    if not values:
        return 0.0
    counter = Counter([int(x * 2) for x in values])  # Discretize
    total = sum(counter.values())
    return -sum((count / total) * math.log(count / total) for count in counter.values() if count > 0)

# Main analysis pipeline
flag_summary = defaultdict(int)
for flag_set in system_flags.values():
    for k, v in flag_set.items():
        if v:
            flag_summary[k] += 1

# Bit manipulation red herring
obfuscated_key = 0
for i in range(8):
    obfuscated_key ^= (i * 257) % 65536
    obfuscated_key = (obfuscated_key << 1) | (obfuscated_key >> 15)
obfuscated_key &= 0xFFFF  # Result unused (distractor)

# Real dependency chain starts here
cycle_groups = extract_cycles(log_entries, system_flags)
entropies = [compute_entropy(group) for group in cycle_groups]

# Modulo arithmetic with conditional accumulation
accum = 0
for i, e in enumerate(entropies):
    if flag_summary['warning'] > 3:
        accum += int(e * 100) % (i + 5)
    else:
        accum += int(e * 80) % (i + 7)

# Final diagnostic computed from controlled logic chain
def analyze_pattern(entries, flags):
    total_weight = 0.0
    critical_count = 0
    for e in entries:
        if e['category'] == 'CRITICAL':
            ts = e['timestamp']
            if flags[ts]['error']:
                total_weight += e['value'] * 1.5
            elif not flags[ts]['debug']:
                total_weight += e['value'] * 0.8
            critical_count += 1
    if critical_count == 0:
        critical_count = 1
    base_score = total_weight / critical_count
    
    # Incorporate entropy-derived component
    cycle_data = extract_cycles(entries, flags)
    entropy_val = compute_entropy([v for c in cycle_data for v in c])
    adjusted = base_score * (1 + entropy_val / 10)
    
    # Final nonlinear transformation
    result = int((adjusted ** 2) / 1.5) + (flag_summary['error'] * 10)
    return result

# Key execution point
final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Result: {final_diagnostic}")