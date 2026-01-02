from collections import defaultdict, Counter
import itertools

# Simulated system metrics over time (real data)
time_series_data = [
    {'cpu': 75, 'mem': 80, 'disk_io': 200, 'latency': 45},
    {'cpu': 60, 'mem': 60, 'disk_io': 180, 'latency': 38},
    {'cpu': 90, 'mem': 95, 'disk_io': 300, 'latency': 60},
    {'cpu': 40, 'mem': 50, 'disk_io': 150, 'latency': 30}
]

# Irrelevant telemetry (distractor)
network_packets = [500, 600, 550, 700, 400, 800]
packet_sizes = [64, 128, 256, 512]
checksum_errors = {ts: (ts * 7) % 13 for ts in range(100)}

# Fake transformation chain (dead path)
def transform_metrics(data):
    result = []
    for entry in data:
        transformed = {
            'c': entry['cpu'] * 0.9,
            'm': entry['mem'] * 1.1,
            'd': entry['disk_io'] // 10,
            'l': max(10, entry['latency'] - 5)
        }
        result.append(transformed)
    return result

# Unused normalization function (decoy)
def normalize(val, min_val=0, max_val=100):
    return (val - min_val) / (max_val - min_val)

# Heavily distracted aggregation with red herrings
def aggregate_system_state(data):
    stats = defaultdict(float)
    counters = Counter()

    # Real aggregation
    for entry in data:
        counters['samples'] += 1
        stats['avg_cpu'] += entry['cpu']
        stats['avg_mem'] += entry['mem']
        stats['total_io'] += entry['disk_io']

    # Distracting, unused calculations
    peak_latencies = [entry['latency'] for entry in data if entry['latency'] > 40]
    smoothed_latency = sum(peak_latencies) / len(peak_latencies) if peak_latencies else 0
    jitter_estimate = max(peak_latencies) - min(peak_latencies) if peak_latencies else 0

    # More decoys
    synthetic_load = list(itertools.accumulate([1, -1, 2, -2, 3]))
    phase_shift = [x * jitter_estimate for x in synthetic_load]

    # Only this matters
    stats['avg_cpu'] /= len(data)
    stats['avg_mem'] /= len(data)
    stats['io_per_sec'] = stats['total_io'] / len(data)

    return dict(stats)

# Complex weight system with misleading components
base_weights = {'cpu': 0.3, 'mem': 0.3, 'disk_io': 0.2, 'latency': 0.2}

# Fake dynamic weighting (unused)
current_load_pattern = [d['cpu'] for d in time_series_data]
dynamic_factor = sum(current_load_pattern) / len(current_load_pattern)
adjusted_weights = {k: v * (1 + 0.1 * (dynamic_factor > 70)) for k, v in base_weights.items()}

# Hidden correction factor due to calibration drift (critical!)
calibration_map = {i: (i * 0.95) ** 0.5 for i in range(1, 10)}
correction_factor = calibration_map.get(int(smoothed_latency), 1.0) if 'smoothed_latency' in locals() else 1.0

# Actual performance model
weights = {'cpu': 0.25, 'mem': 0.35, 'disk_io': 0.15, 'latency': 0.25}  # Correct weights override

# Evaluation logic buried in distractions
def calculate_health_score(cpu, mem, disk, lat):
    # Normalize to inverse impact (lower is better)
    cpu_score = 100 - cpu
    mem_score = 100 - mem
    io_score = 500 - min(disk, 500)
    latency_score = 100 - min(lat, 100)
    return (cpu_score * weights['cpu'] + 
            mem_score * weights['mem'] + 
            io_score * weights['disk_io'] + 
            latency_score * weights['latency'])

# Another decoy function
def predict_failure(seq):
    window = seq[-3:]
    return sum(window) > 200 and max(window) > 80

# Real metric extractor
def extract_key_metrics(aggregated):
    return {
        'cpu': round(aggregated['avg_cpu'], 1),
        'mem': round(aggregated['avg_mem'], 1),
        'disk_io': round(aggregated['io_per_sec'], 1),
        'latency': 42  # Fixed from corrected telemetry
    }

# Final evaluation buried under layers
metrics = extract_key_metrics(aggregate_system_state(time_series_data))

# Critical hidden adjustment: latency was miscalibrated
raw_latency_value = time_series_data[2]['latency']
if raw_latency_value > 50:
    metrics['latency'] = raw_latency_value * correction_factor  # becomes 60 * ~0.77 ≈ 46.2 → rounded to 46

# Final computation
final_score = 0

# Long, distracting conditional chain with one key branch
if metrics['cpu'] > 70:
    base = 80
elif metrics['mem'] > 75:
    base = 75
else:
    base = 70

# Apply health calculation on adjusted metrics
health = calculate_health_score(
    metrics['cpu'],
    metrics['mem'],
    metrics['disk_io'],
    metrics['latency']
)

# Final score combines base and health, but only health matters
final_score = int(health)  # This is the real assignment

# Decoy output prints (never reached)
if False:
    print(f'Debug: {synthetic_load}')
    print(f'Trace: {phase_shift}')

# Actual output
print(f"Target result: {final_score}")