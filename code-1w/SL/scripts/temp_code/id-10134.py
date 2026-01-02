from collections import defaultdict, Counter

# Simulated system log analysis with extensive distractions
def analyze_logs(raw_data):
    parsed_logs = []
    temp_buffer = []
    error_count = 0
    warning_tally = 0
    severity_map = {'ERR': 3, 'WRN': 2, 'INFO': 1, 'DBG': 0}
    
    for line in raw_data:
        if 'timestamp' in line and 'level' in line:
            entry = {}
            entry['ts'] = line.get('timestamp')
            entry['level'] = line.get('level')
            entry['module'] = line.get('module', 'unknown')
            entry['msg'] = line.get('msg', '')
            parsed_logs.append(entry)
            
            if entry['level'] == 'ERR':
                error_count += 1
            elif entry['level'] == 'WRN':
                warning_tally += 1

    # Irrelevant aggregation (red herring)
    module_stats = defaultdict(int)
    for log in parsed_logs:
        module_stats[log['module']] += 1

    priority_queue = []
    for item in parsed_logs:
        if item['level'] in severity_map:
            priority_queue.append((severity_map[item['level']], item['ts']))

    return parsed_logs

# Decoy function – looks important but unused in final computation
def compute_health_score(events, baseline=0.75):
    score = 100.0
    decay_factor = 0.9
    for e in events:
        if e['level'] == 'ERR':
            score *= decay_factor
        elif e['level'] == 'WRN':
            score -= 2.5
    return round(score, 2)

# Another decoy: complex bit manipulation with no impact
def generate_checksum(data_list):
    checksum = 0
    for i, item in enumerate(data_list):
        shifted = (i << 2) ^ len(str(item))
        checksum ^= shifted & 0xFF
    return checksum | 0xACE

# Core processing function buried among distractions
def extract_signals(entries):
    signals = []
    for i, e in enumerate(entries):
        # Signal based on message length and index parity
        signal_val = (len(e['msg']) + i) % 7
        signals.append(signal_val)
    return signals

# Misleading intermediate transformation
def filter_critical_sections(records, threshold=5):
    result_set = set()
    temp_dict = defaultdict(list)
    
    for idx, r in enumerate(records):
        temp_dict[r['module']].append(idx)
        
    for mod, indices in temp_dict.items():
        if len(indices) >= threshold:
            result_set.add(mod)
    
    # This return value is never used
    return result_set

# Real computation path hidden among noise
def aggregate_diagnostics(signals, flags):
    accum = 500
    mask = 0b1101
    
    for s in signals:
        if s > 3:
            accum += (s * 17) % 43
        else:
            accum -= (s ** 2) % 11
    
    # Apply flag-based adjustments
    if flags.get('overclock', False):
        accum += 23
    if flags.get('debug_mode', False):
        accum -= 19
    if flags.get('legacy_protocol', False):
        accum = accum * 2 // 3
    
    return accum

# Unused recursive distraction
def trace_dependency_chain(node, graph, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    total = 0
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
        total += trace_dependency_chain(neighbor, graph, visited)
    return total + len(node)

# Main integration function — only this matters at the end
def process_metrics(logs, config_flags):
    # Step 1: Extract signal values from logs
    signal_values = extract_signals(logs)
    
    # Step 2: Aggregate diagnostics using signals and flags
    diagnostic_score = aggregate_diagnostics(signal_values, config_flags)
    
    # Step 3: Apply final adjustment based on modular arithmetic
    adjustment = (diagnostic_score % 19) - (diagnostic_score % 7)
    final_value = diagnostic_score + adjustment
    
    # Red herring: irrelevant set operation
    unique_modules = {entry['module'] for entry in logs}
    module_counter = Counter([entry['module'] for entry in logs])
    _ = [module_counter[m] for m in sorted(unique_modules)]  # Dead computation
    
    # Final output
    return int(final_value)

# Simulated input data (real input for actual computation)
log_data = [
    {'timestamp': 1001, 'level': 'INFO', 'module': 'net_io', 'msg': 'Connection established'},
    {'timestamp': 1002, 'level': 'WRN', 'module': 'storage', 'msg': 'Disk usage high'},
    {'timestamp': 1003, 'level': 'ERR', 'module': 'auth', 'msg': 'Login failed'},
    {'timestamp': 1004, 'level': 'INFO', 'module': 'cache', 'msg': 'Cache refreshed'},
    {'timestamp': 1005, 'level': 'INFO', 'module': 'net_io', 'msg': 'Heartbeat OK'},
    {'timestamp': 1006, 'level': 'WRN', 'module': 'api', 'msg': 'Rate limit approaching'},
    {'timestamp': 1007, 'level': 'INFO', 'module': 'auth', 'msg': 'Session renewed'}
]

system_config = {
    'overclock': True,
    'debug_mode': False,
    'legacy_protocol': False,
    'redundancy_enabled': True,
    'encryption_level': 'high'
}

# Parse logs (this generates intermediate data)
parsed_log_entries = analyze_logs(log_data)

# Generate useless checksum (distraction)
_ = generate_checksum(parsed_log_entries)

# Compute health score (decoy call - not used)
_ = compute_health_score(parsed_log_entries)

# Trigger dead code path
_ = filter_critical_sections(parsed_log_entries, threshold=10)  # No module reaches 10

# Critical execution point — this produces the answer
final_diagnostic = process_metrics(parsed_log_entries, system_config)

# Output the target result
print(f"Target result: {final_diagnostic}")