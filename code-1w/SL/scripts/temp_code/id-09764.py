from collections import defaultdict, Counter

# Simulated system telemetry data
telemetry_logs = [
    'CPU_TEMP: 75, FAN_SPEED: 2000, POWER_DRAW: 65',
    'CPU_TEMP: 80, FAN_SPEED: 2200, POWER_DRAW: 70',
    'CPU_TEMP: 77, FAN_SPEED: 2150, POWER_DRAW: 68',
    'CPU_TEMP: 85, FAN_SPEED: 2400, POWER_DRAW: 75',
    'CPU_TEMP: 69, FAN_SPEED: 1800, POWER_DRAW: 60'
]

# Parse logs into structured metrics
def parse_logs(logs):
    parsed = []
    for log in logs:
        entries = log.split(', ')
        record = {}
        for entry in entries:
            key, value = entry.split(': ')
            record[key] = int(value)
        parsed.append(record)
    return parsed

# Extract specific metric time series
def extract_metric(data, metric_key):
    return [entry[metric_key] for entry in data if metric_key in entry]

# Misleading auxiliary function (dead path)
def calculate_efficiency_index(values):
    peak = max(values)
    avg = sum(values) / len(values)
    return (avg / peak) * 100 if peak else 0

# Real processing begins here
telemetry_data = parse_logs(telemetry_logs)
temps = extract_metric(telemetry_data, 'CPU_TEMP')
fan_speeds = extract_metric(telemetry_data, 'FAN_SPEED')
power_usage = extract_metric(telemetry_data, 'POWER_DRAW')

# Distractor: unused transformation chain
decayed_temps = [t * (0.9 ** i) for i, t in enumerate(reversed(temps))]
spike_count = sum(1 for t in temps if t > 75)

# Benchmark thresholds (reference only - not used in final calculation)
thresh_high_temp = 80
thresh_high_power = 70

# Weighted scoring system initialization
benchmark_weights = defaultdict(float)
benchmark_weights['stability'] = 0.4
benchmark_weights['efficiency'] = 0.3
benchmark_weights['consistency'] = 0.3

# Performance metrics computation
metrics = {}

# Metric 1: Temperature stability (inverse of variance)
mean_temp = sum(temps) / len(temps)
variance = sum((t - mean_temp) ** 2 for t in temps) / len(temps)
metrics['stability'] = 100 - (variance * 2)  # Higher variance → lower score

# Metric 2: Efficiency ratio (power per fan speed unit)
efficiency_ratio = sum(power_usage) / sum(fan_speeds) * 1000
metrics['efficiency'] = 100 - abs(65 - efficiency_ratio)  # Target optimal at 65

# Metric 3: Consistency (using entropy-like measure via Counter)
counts = Counter(temps)
consistency_score = 0
for _, count in counts.items():
    p = count / len(temps)
    consistency_score += p * p
metrics['consistency'] = 1 - consistency_score  # Lower repetition → higher score

# Red herring: complex but unused correlation analysis
correlation = 0
for i in range(len(temps) - 1):
    temp_delta = temps[i+1] - temps[i]
    fan_delta = fan_speeds[i+1] - fan_speeds[i]
    correlation += temp_delta * fan_delta

# Final performance evaluation
def evaluate_performance(met, weights):
    total = 0.0
    for key in met:
        if key in weights:
            total += met[key] * weights[key]
    adjustment = (sum(power_usage) / len(power_usage)) * 0.1
    return int(total - adjustment)

# Key statement
final_score = evaluate_performance(metrics, benchmark_weights)

# Output result
print(f"Result: {final_score}")