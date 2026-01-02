from collections import defaultdict, Counter
import math

# Simulated system telemetry data over time
telemetry_streams = {
    'cpu_load': [0.78, 0.82, 0.91, 0.88, 0.76, 0.95, 0.99, 0.81],
    'mem_usage': [0.65, 0.71, 0.77, 0.83, 0.88, 0.92, 0.94, 0.87],
    'disk_io': [210, 195, 230, 255, 240, 265, 280, 270],
    'net_in': [180, 190, 175, 160, 170, 185, 195, 200],
    'net_out': [160, 170, 180, 175, 165, 150, 145, 140]
}

# Irrelevant historical baseline (distractor)
historical_avg = {
    'cpu_load': 0.62,
    'mem_usage': 0.58,
    'disk_io': 190,
    'net_in': 170,
    'net_out': 160
}

# System health thresholds for anomaly detection
system_thresholds = {
    'cpu_high': 0.90,
    'mem_high': 0.90,
    'disk_critical': 275,
    'spike_window': 3
}

# False alarm filter parameters (partially relevant but not used directly)
false_positive_filters = defaultdict(lambda: 0.1)
false_positive_filters.update({'cpu': 0.15, 'mem': 0.12})

# Decoy function: looks important but unused
def compute_anomaly_score(data, weights):
    return sum(d * w for d, w in zip(data, weights)) % 100

# Auxiliary transformation - normalizes disk and network to comparable scale
def normalize_stream(data, base=100):
    return [round(x / base, 3) for x in data]

# Misleading intermediate calculation (red herring)
disk_normal = normalize_stream(telemetry_streams['disk_io'], 100)
net_total = [inb + outb for inb, outb in zip(telemetry_streams['net_in'], telemetry_streams['net_out'])]
net_normal = normalize_stream(net_total, 200)

# Critical diagnostic accumulator
diagnostic_traces = defaultdict(int)
spike_count = {key: 0 for key in ['cpu', 'mem', 'disk']}

# Simulate multi-stage analysis pipeline
for i in range(len(telemetry_streams['cpu_load'])):
    # Stage 1: Check CPU spike
    if telemetry_streams['cpu_load'][i] > system_thresholds['cpu_high']:
        diagnostic_traces['cpu_spike'] += 1
        if i >= 2:
            recent_cpu_avg = sum(telemetry_streams['cpu_load'][i-2:i+1]) / 3
            if recent_cpu_avg > 0.92:
                spike_count['cpu'] += 1

    # Stage 2: Memory pressure check
    if telemetry_streams['mem_usage'][i] > system_thresholds['mem_high']:
        diagnostic_traces['mem_peak'] += 1
        # Accumulate sustained high memory
        j = i
        while j < len(telemetry_streams['mem_usage']) and telemetry_streams['mem_usage'][j] > 0.85:
            diagnostic_traces['mem_sustained'] += 1
            j += 1
        break  # Early break creates asymmetric evaluation

# Unused loop variant (dead code path - distractor)
# for i in range(len(telemetry_streams['disk_io'])):
#     if telemetry_streams['disk_io'][i] > 260:
#         diagnostic_traces['io_burst'] += 1

# Stage 3: Disk I/O burst detection with sliding window
window_size = system_thresholds['spike_window']
disk_rolling_avg = []
for i in range(len(telemetry_streams['disk_io']) - window_size + 1):
    window_avg = sum(telemetry_streams['disk_io'][i:i+window_size]) / window_size
    disk_rolling_avg.append(window_avg)

# Identify critical disk events
for avg in disk_rolling_avg:
    if avg > system_thresholds['disk_critical']:
        diagnostic_traces['disk_stress'] += 1

# Phantom correlation check (misleading logic)
cpu_mem_correlation = 0
for i in range(len(telemetry_streams['cpu_load'])):
    if telemetry_streams['cpu_load'][i] > 0.85 and telemetry_streams['mem_usage'][i] > 0.85:
        cpu_mem_correlation += 1

temp_registry = Counter()
temp_registry.update(['diagnostic_phase_1', 'diagnostic_phase_1', 'diagnostic_reset'])

# Core processing function combining multiple concepts
def process_metrics(log_data, thresholds):
    anomalies = 0
    
    # Bit manipulation for state encoding (obscure but valid)
    state_flag = 0b0
    
    # Arithmetic + boolean chain
    for i in range(len(log_data['cpu_load'])):
        load = log_data['cpu_load'][i]
        mem = log_data['mem_usage'][i]
        
        # Complex conditional with nested arithmetic
        if load > thresholds['cpu_high'] and mem > thresholds['mem_high']:
            score = (load * 100) ** 1.1
            penalty = int(math.log(score + 1) * 10)
            anomalies += max(1, penalty - 15)
            state_flag |= 0b1000
        
        # Secondary condition with hidden impact
        disk_val = log_data['disk_io'][i]
        if disk_val > 270 and i % 2 == 0:
            anomalies += 2
            state_flag ^= 0b0101
    
    # Data structure cross-reference
    io_counter = Counter(log_data['disk_io'])
    high_io_events = sum(1 for val in log_data['disk_io'] if val > 275)
    
    if high_io_events >= 2:
        anomalies += int(math.sqrt(high_io_events * 10))
    
    # Final integration with decoy variables
    decoy_contribution = len(temp_registry) * diagnostic_traces.get('mem_sustained', 0)
    control_adjustment = bin(state_flag).count('1')
    
    final_value = (anomalies * 100) + control_adjustment - decoy_contribution
    
    # Critical red herring: irrelevant print that looks diagnostic
    # print(f'[DEBUG] Anomaly score breakdown: {anomalies=}, {control_adjustment=}, {decoy_contribution=}')
    
    return final_value

# Execute main diagnostic
final_diagnostic = process_metrics(telemetry_streams, system_thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")