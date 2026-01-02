from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    'CPU:80|MEM:45|DISK:70',
    'CPU:40|MEM:60|DISK:30',
    'CPU:90|MEM:80|DISK:90',
    'CPU:30|MEM:20|DISK:10'
]

# Misleading auxiliary data (distractor)
signal_data = [0.1, 0.4, 0.7, 0.9, 1.2]
fft_bins = [abs(math.sin(x)) for x in signal_data]
noise_floor = sum(fft_bins) / len(fft_bins)

# Parse function with red herring logic
def parse_telemetry(stream):
    records = []
    for entry in stream:
        parts = entry.split('|')
        record = {}
        for part in parts:
            k, v = part.split(':')
            record[k] = int(v)
        records.append(record)
    
    # Distractor: unused transformation
    normalized = []
    for r in records:
        norm_r = {k: v/100.0 for k, v in r.items()}
        normalized.append(norm_r)
    
    return records  # actual return; normalized is dead code path

# Heuristic weights (some are misleading)
weights = defaultdict(float)
weights['CPU'] = 0.4
weights['MEM'] = 0.3
weights['DISK'] = 0.3
weights['GPU'] = 0.5  # irrelevant weight (no GPU in data)

# Legacy threshold map (partially obsolete)
thresh_map = {'low': 30, 'med': 60, 'high': 80}

# Flag configuration influencing processing
flags = {
    'include_volatility': False,
    'use_exp_decay': True,
    'strict_mode': True
}

# Secondary helper with distractor computation
def calculate_volatility(seq):
    if len(seq) < 2:
        return 0.0
    diffs = [abs(a - b) for a, b in zip(seq, seq[1:])]
    volatility = sum(diffs) / len(diffs)
    # Complex but irrelevant transform
    transformed = list(map(lambda x: math.log(1 + x), diffs))
    smoothed = sum(transformed) / len(transformed) if transformed else 0
    return volatility  # 'smoothed' is distraction

# Main processing function
def process_metrics(data, config):
    cpu_vals = [d['CPU'] for d in data]
    mem_vals = [d['MEM'] for d in data]
    disk_vals = [d['DISK'] for d in data]
    
    # Real-time averages
    avg_cpu = sum(cpu_vals) / len(cpu_vals)
    avg_mem = sum(mem_vals) / len(mem_vals)
    avg_disk = sum(disk_vals) / len(disk_vals)
    
    # Distractor: peak detection (unused)
    peaks = []
    for i in range(1, len(cpu_vals)-1):
        if cpu_vals[i] > cpu_vals[i-1] and cpu_vals[i] > cpu_vals[i+1]:
            peaks.append(cpu_vals[i])
    
    # Volatility metric (not used when flag is False)
    vol_cpu = calculate_volatility(cpu_vals)
    vol_mem = calculate_volatility(mem_vals)
    
    # Scoring logic
    base_score = 0.0
    base_score += avg_cpu * weights['CPU']
    base_score += avg_mem * weights['MEM']
    base_score += avg_disk * weights['DISK']
    
    # Conditional penalty
    penalty = 0.0
    if flags['strict_mode']:
        if avg_cpu > thresh_map['high'] or avg_mem > thresh_map['high']:
            penalty += 15.0

    # Exponential decay adjustment (only active if enabled)
    adjusted_score = base_score
    if config['use_exp_decay']:
        decay_factor = math.exp(-0.1 * (vol_cpu + vol_mem))
        adjusted_score = base_score * decay_factor
    
    # Final heuristic boost (irrelevant if not in legacy mode)
    legacy_boost = 0
    if 'legacy_compat' in config and config['legacy_compat']:
        legacy_boost = 10
    
    final_score = int(round(adjusted_score - penalty + legacy_boost))
    
    # Dead code branch (never reached due to structure)
    if False:
        fallback = sum(cpu_vals) % 100
        final_score = max(final_score, fallback)
    
    return final_score

# Data extraction
raw_data = parse_telemetry(telemetry_stream)

# Extraneous string processing (distractor)
log_headers = "Time|Event|Status"
tokens = log_headers.lower().replace('|', ' ').split()
header_count = Counter(tokens)

# Critical execution point
final_score = process_metrics(raw_data, flags)

# Output result
print(f"Result: {final_score}")