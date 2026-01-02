from collections import defaultdict, Counter

# Simulated system telemetry data
technical_metrics = [120, 85, 90, 110, 95, 100, 90]
latency_data = [50, 60, 55, 65, 70, 58, 62]
error_flags = [False, True, False, False, True, False, False]

def analyze_trends(data, weight=1.0):
    trend = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend += weight
        elif data[i] < data[i-1]:
            trend -= weight * 0.5
    return trend

def filter_outliers(values):
    mean_val = sum(values) / len(values)
    return [v for v in values if abs(v - mean_val) <= 15]

def calculate_stability_index(latencies):
    sorted_latencies = sorted(latencies)
    median_latency = sorted_latencies[len(sorted_latencies) // 2]
    deviation_score = sum(abs(l - median_latency) for l in latencies) / len(latencies)
    return round(100 - deviation_score, 2)

def assess_error_impact(flags):
    error_count = sum(1 for f in flags if f)
    severity = error_count * 10
    return severity

# Irrelevant preprocessing: red herring function
def compute_network_efficiency(packets, acks):
    efficiency = 0
    for p, a in zip(packets, acks):
        if a > 0:
            efficiency += a / p
    return efficiency * 100

# Unused but plausible decoy variables
packet_log = [100, 95, 105, 90, 110]
acknowledgments = [98, 90, 100, 85, 108]
phantom_baseline = compute_network_efficiency(packet_log, acknowledgments)

# Core logic disguised among distractions
def evaluate_performance(metrics, base):
    # Step 1: Filter metrics
    filtered = filter_outliers(metrics)
    
    # Step 2: Compute weighted trend
    trend_score = analyze_trends(filtered, weight=1.2)
    
    # Step 3: Stability component
    stability = calculate_stability_index(latency_data)
    
    # Step 4: Error penalty
    error_penalty = assess_error_impact(error_flags)
    
    # Step 5: Aggregate score before normalization
    raw_score = sum(filtered) + trend_score + stability - error_penalty
    
    # Step 6: Normalize against baseline with offset
    normalized = (raw_score - base) / base
    
    # Step 7: Apply non-linear boost
    boosted = normalized * (1 + normalized / 10)
    
    # Step 8: Final adjustment using bit manipulation (obscure but valid)
    adjusted = int(boosted * 100) ^ 0x5A  # XOR with hex constant for minor variation
    
    return adjusted

# Distractor block: unused dictionary aggregation
diagnostic_summary = defaultdict(list)
for i, val in enumerate(technical_metrics):
    diagnostic_summary['metrics'].append(val)
    diagnostic_summary['flagged'].append(error_flags[i])

counter_report = Counter()
for flag in error_flags:
    counter_report['errors' if flag else 'clean'] += 1

# Another red herring: list comprehension with no side effect
[latency * 2 for latency in latency_data if latency < 60]

# Key baseline derived from initial data
baseline = sum(technical_metrics[:3]) / 3  # Average of first three metrics

# Critical execution point
final_score = evaluate_performance(technical_metrics, baseline)

# Result output
print(f"Result: {final_score}")