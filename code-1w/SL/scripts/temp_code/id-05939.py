from collections import defaultdict
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456802, 1623456810]
log_entries = [
    {'type': 'IO_READ', 'duration_ms': 12, 'size_kb': 512},
    {'type': 'CPU_BURST', 'duration_ms': 45, 'util': 0.88},
    {'type': 'IO_WRITE', 'duration_ms': 8, 'size_kb': 256},
    {'type': 'CPU_BURST', 'duration_ms': 67, 'util': 0.94},
    {'type': 'IO_READ', 'duration_ms': 15, 'size_kb': 1024}
]

# Irrelevant auxiliary mapping (distraction)
status_codes = {200: 'OK', 404: 'Not Found', 500: 'Server Error'}
error_counter = defaultdict(int)
error_counter[404] += 1  # Dead code path

# System state with multiple components (mix of relevant and irrelevant fields)
system_state = {
    'cpu_cores': 8,
    'memory_gb': 32,
    'disk_queue_depth': 4,
    'network_latency_ms': 12.4,
    'thermal_throttle': False,
    'io_priority': 'high',
    'uptime_seconds': 3600
}

# Decoy function that is defined but not used in critical path
def analyze_failures(logs):
    failure_count = 0
    for entry in logs:
        if entry.get('error'):
            failure_count += 1
    return failure_count

# Secondary distraction: unused performance model
performance_model = lambda x: math.exp(-0.1 * x) if x > 0 else 1.0
baseline_score = performance_model(5)

# Data aggregator with red herring counters
counter = defaultdict(int)
size_accumulator = 0
irrelevant_sum = 0

for entry in log_entries:
    e_type = entry['type']
    counter[e_type] += 1
    if 'size_kb' in entry:
        size_accumulator += entry['size_kb']
    # Misleading accumulation
    if 'util' in entry:
        irrelevant_sum += entry['util'] * 100

# Spurious transformation chain (not affecting final result)
transformed = list(map(lambda x: x * 1.5, timestamps))
normalized = [t - timestamps[0] for t in transformed]
filtered = [n for n in normalized if n > 10]

# Core diagnostic logic buried among distractions
def calculate_response_index(entries, state):
    cpu_bursts = [e for e in entries if e['type'] == 'CPU_BURST']
    io_events = [e for e in entries if 'IO_' in e['type']]
    
    avg_cpu_duration = sum(e['duration_ms'] for e in cpu_bursts) / len(cpu_bursts) if cpu_bursts else 0
    total_io_size = sum(e['size_kb'] for e in io_events)
    
    # Complex but ultimately irrelevant adjustment
    thermal_factor = 0.9 if state['thermal_throttle'] else 1.0
    
    # Key metric: weighted responsiveness index
    responsiveness = (avg_cpu_duration * 0.6) + (total_io_size * 0.001 * 0.4)
    
    # Distractor: unused branch with complex logic
    if state['disk_queue_depth'] > 5:
        responsiveness *= 1.2
    elif state['network_latency_ms'] > 20:
        temp_adjust = 0
        for i in range(3):
            temp_adjust += math.sin(i)
        responsiveness -= temp_adjust
    
    return responsiveness

# Another decoy: advanced statistical check (never called)
def compute_entropy(data_list):
    from collections import Counter
    import math
    counts = Counter(data_list)
    total = len(data_list)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Real processing function - answer depends on this
def process_metrics(entries, state):
    # Extract durations for all event types
    durations = [e['duration_ms'] for e in entries]
    duration_stats = {
        'min': min(durations),
        'max': max(durations),
        'sum': sum(durations)
    }
    
    # Compute derived diagnostic value
    raw_diagnostic = duration_stats['sum'] * state['cpu_cores']
    
    # Apply conditional bit manipulation based on IO pattern
    io_read_count = counter['IO_READ']  # Uses outer-scope counter
    if io_read_count >= 2:
        # Bitwise twist: shift and XOR to obscure calculation
        raw_diagnostic = (raw_diagnostic << 1) ^ 0xAAAA
    else:
        raw_diagnostic = (raw_diagnostic >> 1) + 0x5555
    
    # Final adjustment using string-based key lookup (meaningful use of string method)
    keys = ['diagnostic', 'health', 'status']
    mode_key = ''.join([k for k in keys if k.startswith('diag')]).upper()
    adjustment_map = {'DIAGNOSTIC': 3, 'HEALTH': 2, 'STATUS': 1}
    adjustment = adjustment_map.get(mode_key, 1)
    
    final_value = raw_diagnostic - adjustment * 17
    
    # Dead code block - misleading intermediate print
    if False:
        debug_dump = f"Metrics: {duration_stats}, State: {state['memory_gb']}GB"
        print(debug_dump)
    
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_state)

# Print required output
print(f"Result: {final_diagnostic}")