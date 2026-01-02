import math

# Simulated system metrics for performance analysis
temp_readings = [72, 68, 75, 80, 65]
latency_data = [120, 110, 135, 90, 140]
packet_loss = [0.01, 0.03, 0.02, 0.05, 0.04]

def analyze_stability(readings):
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance)

def compute_efficiency(latency_list):
    base_efficiency = 1000
    adjustment_factor = 0.87
    total_penalty = 0
    for val in latency_list:
        if val > 125:
            total_penalty += (val - 125) * 1.2
    # Irrelevant transformation
    temp_result = [x * 0.95 for x in latency_list if x < 100]
    final_eff = base_efficiency - total_penalty
    return final_eff

def assess_reliability(loss_rates):
    avg_loss = sum(loss_rates) / len(loss_rates)
    reliability_score = 100 * (1 - avg_loss)
    # Dead code path - never used
    if reliability_score > 95:
        return reliability_score * 1.1
    return reliability_score

def generate_metric_set(temp, latency, loss):
    # Complex but partially irrelevant data processing
    stability = analyze_stability(temp)
    efficiency = compute_efficiency(latency)
    reliability = assess_reliability(loss)
    
    # Distractor: unused derived values
    peak_load = max(latency) * (1 + min(temp) / 100)
    normalized_loss = [round(x * 100, 2) for x in loss]
    temporal_drift = abs(temp[-1] - temp[0]) * 0.5
    
    # Real metric components
    scores = {
        'stability': round(stability, 2),
        'efficiency': efficiency,
        'reliability': reliability,
        'drift': temporal_drift
    }
    return scores

def filter_outliers(data, threshold=1.5):
    # Unused function - red herring
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [x for x in data if lower <= x <= upper]

def calculate_entropy(values):
    # Another decoy function with plausible logic
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probs)
    return round(entropy, 4)

def evaluate_performance(metrics, benchmark):
    # Core evaluation logic
    base = metrics['efficiency'] * 0.4
    base += metrics['reliability'] * 0.35
    base += benchmark['consistency'] * 0.25
    
    # Irrelevant conditional that doesn't affect outcome
    if metrics['stability'] < 3.0:
        adjustment = 5.0
    else:
        adjustment = 0.0  # Never actually added
    
    # Misleading intermediate calculation
    hypothetical_max = 1000 * 0.4 + 100 * 0.35 + 100 * 0.25
    unused_ratio = base / hypothetical_max
    
    # Key distractor: complex set operation with partial relevance
    critical_thresholds = {90, 95, 100, 105, 110}
    achieved_levels = {int(metrics['reliability']), int(benchmark['consistency'])}
    met_goals = len(critical_thresholds & achieved_levels)  # Only this part matters
    
    bonus = met_goals * 7.5
    result = base + bonus
    
    # Dead assignment
    result = result if result <= 500 else 500  # Constraint never triggered
    
    return int(round(result))

# Benchmark configuration (simulated external input)
benchmark_data = {
    'consistency': 92,
    'throughput': 880,
    'jitter': 4.3,
    'coverage': 96.7
}

# Generate feature-rich metric set
metric_set = generate_metric_set(temp_readings, latency_data, packet_loss)

# Perform final evaluation - KEY EXECUTION POINT
final_score = evaluate_performance(metric_set, benchmark_data)

# Print result as required
print(f"Result: {final_score}")