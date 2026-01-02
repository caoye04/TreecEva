def analyze_system_load(loads):
    return list(map(lambda x: (x * 1.5) + 2, filter(lambda x: x > 30, loads)))

# Simulated telemetry data
raw_signals = [12, 45, 67, 23, 89, 34, 76, 55]
signal_strength = sum([s ** 0.5 for s in raw_signals if s % 2 == 1])

# Irrelevant audio processing stub
audio_samples = [0.1, 0.4, 0.9]
def decode_audio(s): return s * 2
decoded = [decode_audio(x) for x in audio_samples]  # Dead path

# System event logs with mixed content
event_codes = ['ERR_404', 'OK_200', 'ERR_500', 'WARN_301']
error_count = len([c for c in event_codes if 'ERR' in c])
status_map = {code: idx for idx, code in enumerate(event_codes)}

# Core diagnostic pipeline
log_entries = [{'id': 1, 'load': 88, 'timestamp': 1623456789},
               {'id': 2, 'load': 92, 'timestamp': 1623456795},
               {'id': 3, 'load': 76, 'timestamp': 1623456801}]

system_flags = {
    'overload_threshold': 90,
    'grace_period_sec': 60,
    'debug_mode': False,
    'version': '2.1.8'
}

# Decoy transformation chain
temp_data = [{'val': x['load'] ** 0.5} for x in log_entries]
aggregated = sum(item['val'] for item in temp_data) / len(temp_data)

# Real metric processor
sorted_logs = sorted(log_entries, key=lambda x: x['timestamp'])
recent_loads = [entry['load'] for entry in sorted_logs if entry['load'] > system_flags['overload_threshold']]

# Secondary flag analysis (partially relevant)
criticality_score = 0
if len(recent_loads) >= 2:
    criticality_score += 40
if system_flags.get('debug_mode'):
    criticality_score += 10  # Never triggered

# Auxiliary checksum (distractor)
checksum = 0
for i, entry in enumerate(sorted_logs):
    checksum ^= entry['id'] * (i + 1)

# Actual core logic buried in context
def process_metrics(entries, flags):
    high_load = [e for e in entries if e['load'] > flags['overload_threshold']]
    time_spans = []
    for i in range(1, len(high_load)):
        delta = high_load[i]['timestamp'] - high_load[i-1]['timestamp']
        time_spans.append(delta)
    
    if not time_spans:
        base_score = 50
    else:
        avg_interval = sum(time_spans) / len(time_spans)
        base_score = 100 if avg_interval < 30 else 75
    
    # Additional condition from flag state
    if flags['version'].startswith('2'):
        base_score += 25
    
    # Final adjustment based on error count from earlier (cross-concept link)
    nonlocal error_count
    if error_count > 1:
        base_score -= 10
    
    return int(base_score)

# Misleading intermediate step
placeholder_result = analyze_system_load(raw_signals)
interim_value = signal_strength * 0.1  # Unused

# Key execution point
final_diagnostic = process_metrics(log_entries, system_flags)

# Output requirement
print(f"Result: {final_diagnostic}")