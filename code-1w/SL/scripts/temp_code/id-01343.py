import math

# Simulated system health monitoring with distractors
def collect_telemetry():
    return {
        'cpu_load': [0.78, 0.82, 0.91, 0.65, 0.77],
        'mem_usage': [0.64, 0.71, 0.79, 0.85, 0.68],
        'disk_io': [120, 145, 130, 155, 138],
        'net_latency_ms': [23, 45, 31, 29, 36]
    }

def deprecated_normalize(data_list):
    # Unused function - red herring
    return [x / max(data_list) for x in data_list]

def rolling_average(values, window=3):
    if len(values) < window:
        return values[:]
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def bit_twiddle_severity(level):
    # Distractor: looks important but used only once insignificantly
    level = level ^ 7
    level = (level << 2) & 15
    return level | 3

def calculate_stability_index(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return round(100 * (1 - math.sqrt(variance) / (max(readings) - min(readings) + 0.01)), 2)

def filter_outliers(data_seq, threshold=1.5):
    q1 = sorted(data_seq)[len(data_seq)//4]
    q3 = sorted(data_seq)[3*len(data_seq)//4]
    iqr = q3 - q1
    low_bound = q1 - threshold * iqr
    high_bound = q3 + threshold * iqr
    return [x for x in data_seq if low_bound <= x <= high_bound]

def assess_risk_category(value, boundaries):
    for limit, category in sorted(boundaries.items()):
        if value <= limit:
            return category
    return "critical"

def transform_metrics(raw_data):
    # Irrelevant transformation path
    transformed = {}
    for k, v in raw_data.items():
        if 'cpu' in k:
            transformed['processor'] = sum(v) / len(v)
        elif 'mem' in k:
            transformed['memory'] = rolling_average(v)[-1] if v else 0
        elif 'disk' in k:
            transformed['storage'] = sum(v) / len(v)
        elif 'net' in k:
            transformed['latency'] = calculate_stability_index(v)
    return transformed

def compute_fallback_heuristic(telemetry_snapshot):
    # Dead code path - never actually used in final calculation
    base = telemetry_snapshot.get('cpu_load', [])
    if not base:
        return 0
    weighted = sum(i * val for i, val in enumerate(base, 1))
    return weighted / len(base)

def evaluate_component_health(metric_value, ref_list, weight):
    rank_pos = sorted(ref_list + [metric_value]).index(metric_value) + 1
    percentile = rank_pos / len(ref_list)
    return percentile * weight

def analyze_performance(metrics, config_thresholds):
    # Core logic embedded within noise
    cpu_val = metrics.get('processor', 0)
    mem_val = metrics.get('memory', 0)
    latency_stab = metrics.get('latency', 50)

    # Real contribution to answer
    score_components = [
        evaluate_component_health(cpu_val, [0.5, 0.6, 0.7, 0.8, 0.9], 0.4),
        evaluate_component_health(mem_val, [0.55, 0.65, 0.72, 0.78, 0.88], 0.35),
        evaluate_component_health(latency_stab, [30, 40, 50, 60, 70], 0.25)
    ]
    
    raw_score = sum(score_components) * 100
    
    # Misleading adjustment
    temp_adj = bit_twiddle_severity(int(raw_score % 10))
    adjusted_score = raw_score - temp_adj  # Slight real effect but obscured
    
    # Final clamping and rounding
    final_score = max(0, min(100, round(adjusted_score, 1)))
    
    # Unused diagnostic output
    diagnostics = {"stages": ["raw", "adj", "final"], "values": [raw_score, adjusted_score, final_score]}
    
    return final_score

# Irrelevant global constants
MAX_RETRIES = 7
TIMEOUT_BUFFER = 1.25
REDACTED_KEYS = ['auth', 'secret', 'token']

# Main execution flow
if __name__ == "__main__":
    # Collect real data
    sensor_data = collect_telemetry()
    
    # Apply filtering (distractor: some paths not fully used)
    filtered_cpu = filter_outliers(sensor_data['cpu_load'])
    filtered_mem = filter_outliers(sensor_data['mem_usage'])
    
    # Generate transformed metrics (used in analysis)
    processed_metrics = transform_metrics({
        'cpu_load': filtered_cpu,
        'mem_usage': filtered_mem,
        'disk_io': sensor_data['disk_io'],
        'net_latency_ms': sensor_data['net_latency_ms']
    })
    
    # Threshold configuration (only 'latency_critical' is unused)
    thresholds = {
        'overload': 0.85,
        'warning': 0.70,
        'normal': 0.50,
        'latency_critical': 50
    }
    
    # Execute key statement
    final_score = analyze_performance(processed_metrics, thresholds)
    
    # Additional unused computation
    projected_load = lambda x: x * 1.07
    projection_chain = [projected_load(final_score)]
    for _ in range(2):
        projection_chain.append(projected_load(projection_chain[-1]))
    
    # Print result as required
    print(f"Result: {final_score}")