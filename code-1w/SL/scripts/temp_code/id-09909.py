from collections import defaultdict, Counter

# Simulated system performance metrics with irrelevant and relevant data
def collect_diagnostics():
    diagnostics = {}
    diagnostics['cpu_load'] = [0.78, 0.82, 0.75, 0.91]
    diagnostics['mem_usage'] = [0.64, 0.71, 0.78, 0.83]
    diagnostics['disk_iops'] = [120, 115, 130, 125]  # Irrelevant metric
    diagnostics['network_latency_ms'] = [23, 45, 30, 35]
    diagnostics['temp_cores'] = [67, 70, 68, 72]  # Red herring
    return diagnostics

def normalize_series(data):
    # Dummy normalization function (not used in final calculation)
    mean_val = sum(data) / len(data)
    return [round((x - mean_val) / mean_val, 3) for x in data]

def extract_trend(signal):
    # Misleading trend analysis
    diff = [signal[i+1] - signal[i] for i in range(len(signal)-1)]
    return sum(diff) / len(diff)

def calculate_stability_index(seq):
    # Unused stability metric - dead code path
    variance = sum((x - sum(seq)/len(seq))**2 for x in seq) / len(seq)
    return round(1 / (1 + variance), 3)

def filter_outliers(data_list, threshold=2.0):
    # Outlier filtering - looks important but unused
    mean_val = sum(data_list) / len(data_list)
    stdev = (sum((x - mean_val)**2 for x in data_list) / len(data_list)) ** 0.5
    return [x for x in data_list if abs(x - mean_val) <= threshold * stdev]

def smooth_signal(signal):
    # Smoothing function that's never called
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append(round((signal[i-1] + signal[i] + signal[i+1]) / 3, 3))
    smoothed.append(signal[-1])
    return smoothed

def analyze_pattern(seq):
    # Another decoy function analyzing patterns
    counter = Counter()
    for i in range(len(seq) - 1):
        if seq[i+1] > seq[i]:
            counter['increase'] += 1
        elif seq[i+1] < seq[i]:
            counter['decrease'] += 1
    return dict(counter)

def compute_weighted_average(values, weights):
    # Core arithmetic operation used in final result
    total_weight = sum(weights)
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight if total_weight != 0 else 0

def infer_operational_mode(cpu, memory):
    # Complex conditional logic - appears critical but not used
    if cpu > 0.85 and memory > 0.8:
        return "CRITICAL"
    elif cpu > 0.75 or memory > 0.75:
        return "WARNING"
    else:
        return "STABLE"

def evaluate_performance(metrics, importance_weights):
    # Main evaluation logic buried among distractions
    recent_cpu = metrics['cpu_load'][-1]
    avg_memory = sum(metrics['mem_usage']) / len(metrics['mem_usage'])
    latency_sample = metrics['network_latency_ms'][1]  # Pick specific index
    
    # Normalize latency to a 0-1 scale (inverse: lower latency = higher score)
    normalized_latency = 1 - (latency_sample / 100)  # Assume max expected is 100ms
    
    # Relevance check: only cpu, memory, and latency are used
    raw_scores = [
        1 - recent_cpu,           # CPU: lower usage = better
        1 - avg_memory,           # Memory: lower = better
        normalized_latency        # Latency: lower = better
    ]
    
    # Apply weighting scheme
    weighted_score = compute_weighted_average(raw_scores, importance_weights)
    
    # Scale to 0-100 point system
    final_score = round(weighted_score * 100, 4)
    
    # Introduce misleading secondary transformation (unused)
    adjusted_for_temp = final_score * (1 - (metrics['temp_cores'][-1] - 60) / 100)
    
    return final_score

# --- Execution Flow ---
data_log = collect_diagnostics()

# Extract subsets for processing
primary_metrics = {
    'cpu_load': data_log['cpu_load'],
    'mem_usage': data_log['mem_usage'],
    'network_latency_ms': data_log['network_latency_ms']
}

# Add irrelevant transformations
trends = {}
for key, series in primary_metrics.items():
    trends[key + '_trend'] = extract_trend(series)

diag_summary = defaultdict(int)
diag_summary['total_entries'] = sum(len(v) for v in data_log.values())

cpu_pattern = analyze_pattern(data_log['cpu_load'])

# Weight assignment - crucial but obscured
weights = [0.4, 0.35, 0.25]  # CPU, Memory, Latency importance

# Critical execution point
final_score = evaluate_performance(primary_metrics, weights)

# Print result as required
print(f"Result: {final_score}")