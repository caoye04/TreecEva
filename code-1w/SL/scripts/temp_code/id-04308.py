def analyze_system_load(base_load, threshold=75):
    peak_loads = [base_load + i * 12 for i in range(4) if (base_load + i * 12) > threshold]
    adjusted_loads = [x * 0.9 for x in peak_loads]
    return sum(adjusted_loads) if adjusted_loads else base_load


def compute_bandwidth_efficiency(packets, errors):
    total_bits = packets * 1500
    retransmitted = errors * 300
    overhead = total_bits * 0.05
    net_throughput = total_bits - retransmitted - overhead
    efficiency = net_throughput / total_bits if total_bits > 0 else 0
    return round(efficiency, 4)


def generate_diagnostics(code_map):
    diagnostics = {}
    for key, val in code_map.items():
        if val % 3 == 0 and val % 5 != 0:
            diagnostics[key] = 'STATUS_PENDING'
        elif val % 5 == 0:
            diagnostics[key] = 'STATUS_RESOLVED'
        else:
            diagnostics[key] = 'STATUS_ACTIVE'
    return diagnostics

# Irrelevant helper (dead path)
def deprecated_calculator(x, y):
    return (x ** 2 + y ** 2) ** 0.5

# Unused constant cluster (distractor)
MAX_BUFFER_SIZE = 65536
RETRY_LIMIT = 3
TIMEOUT_GRACE_PERIOD = 120
DEFAULT_PRIORITY = 'MEDIUM'

# Simulated sensor readings (partially relevant)
sensor_readings = {
    'node_a': 88,
    'node_b': 67,
    'node_c': 91,
    'node_d': 73
}

# Misleading aggregation (red herring)
avg_reading = sum(sensor_readings.values()) / len(sensor_readings)
high_load_nodes = [k for k, v in sensor_readings.items() if v > 80]

# Core data transformation chain
raw_metrics = [
    {'id': 'A', 'load': 88, 'packets': 120, 'errors': 4},
    {'id': 'B', 'load': 67, 'packets': 95, 'errors': 12},
    {'id': 'C', 'load': 91, 'packets': 200, 'errors': 7},
    {'id': 'D', 'load': 73, 'packets': 130, 'errors': 5}
]

# Distractor list comprehension with no downstream use
stale_flags = [m['id'] for m in raw_metrics if m['packets'] < 100 and m['load'] < 70]

# Key processing pipeline
metric_set = set()
for entry in raw_metrics:
    load_score = analyze_system_load(entry['load'])
    bw_efficiency = compute_bandwidth_efficiency(entry['packets'], entry['errors'])
    composite = int((load_score * 0.6) + (bw_efficiency * 100 * 0.4))
    metric_set.add(composite)

# Unused dictionary operation (decoy)
diag_map = {i: chr(65+i) for i in range(len(metric_set))}
sorted_pairs = sorted(diag_map.items(), key=lambda x: x[0], reverse=True)

# Conditional branch with misleading elif chain
if len(metric_set) > 3:
    scaling_factor = 1.1
elif sum(metric_set) / len(metric_set) > 85:
    scaling_factor = 0.95
else:
    scaling_factor = 1.0  # This will actually be used

# Critical execution point
final_score = evaluate_performance(metric_set)

# Primary function with nested logic and distractors
def evaluate_performance(metrics):
    baseline = 70
    adjustment = 0
    
    # Bit manipulation red herring
    binary_flag = 0b1010
    mask = 0b1111
    masked = binary_flag & mask
    
    # Set operations (core relevance)
    high_performers = {m for m in metrics if m > baseline}
    low_performers = metrics - high_performers
    
    # Conditional adjustments with short-circuiting
    if high_performers and len(high_performers) >= 2 and not (len(low_performers) > 2):
        adjustment += 12
    elif len(low_performers) == 0:
        adjustment += 5
    else:
        adjustment -= 3
    
    # Modular arithmetic component
    total_mod = sum(m % 11 for m in metrics)
    
    # Complex expression with distractor variables
    temp_offset = TIMEOUT_GRACE_PERIOD * 0.01  # unused but looks important
    debug_trace = []  # dead collection
    
    # Final computation (answer depends only on this)
    result = len(high_performers) * 17 + total_mod + adjustment
    
    return result

# Print required output
print(f"Result: {final_score}")