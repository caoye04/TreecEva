import itertools

# Simulated system performance metrics from various subsystems
def collect_diagnostics():
    return {
        'latency': [120, 145, 130, 155, 138],
        'throughput': [880, 850, 900, 870, 890],
        'error_rate': [0.002, 0.003, 0.001, 0.004, 0.002],
        'cpu_load': [78, 82, 75, 85, 79],
        'memory_usage': [65, 67, 64, 68, 66]
    }

# Irrelevant health check (red herring)
def system_health_check():
    return {chr(i): (i % 13) * 0.77 for i in range(97, 105)}  # Decoy data

# Misleading preprocessing function that's not actually used
def preprocess_logs(raw_logs):
    transformed = []
    for entry in raw_logs:
        transformed.append({
            'timestamp': entry.get('ts', 0) // 1000,
            'severity': min(entry.get('level', 1), 5),
            'checksum': entry.get('data', '').__hash__() % 1000
        })
    return transformed

# Core evaluation logic
def evaluate_performance(metrics, weights):
    
    # Extract relevant time-series data
    latency_series = metrics['latency']
    throughput_series = metrics['throughput']
    error_series = metrics['error_rate']
    
    # Compute base indicators (some are distractions)
    avg_latency = sum(latency_series) / len(latency_series)
    peak_throughput = max(throughput_series)
    total_errors = sum(error_series) * 1000  # per 1000 requests
    stability_score = 0
    
    # Spurious loop with no effect (distractor)
    for _ in range(3):
        temp = [x ** 0.5 for x in metrics['cpu_load']]
        stability_score += sum(temp) % 17  # This gets discarded later

    # Real computation begins: normalize and weight key factors
    normalized_latency = max(0, (150 - avg_latency) / 150)  # lower latency → higher score
    normalized_throughput = peak_throughput / 1000
    error_penalty = min(total_errors * 2, 1.0)

    # Weighted aggregation using lambda-based dynamic adjustment
    adjuster = lambda x, w: round(x * w, 4)
    
    # Apply weights (provided externally)
    components = [
        ('latency', normalized_latency, weights[0]),
        ('throughput', normalized_throughput, weights[1]),
        ('errors', 1 - error_penalty, weights[2])
    ]
    
    weighted_sum = 0
    for name, value, weight in components:
        if name == 'errors' and total_errors > 5:
            continue  # conditional skip branch (not triggered here)
        contribution = adjuster(value, weight)
        weighted_sum += contribution
    
    # Additional logic using itertools to create illusion of complexity
    combos = list(itertools.combinations([1.0, 0.8, 0.6], 2))
    bonus_factor = 1.0
    for c in combos:
        if abs(c[0] - c[1]) < 0.3:
            bonus_factor *= 0.95  # Not impactful in this case

    # Final nonlinear transformation
    raw_score = weighted_sum * 85  # Base out of 85
    final_score = int(raw_score + (bonus_factor * 15))  # Cap at ~100
    
    # Dead code path (never reached due to logic above)
    if final_score > 120:
        final_score = 100  # Clamping (unreachable)
    
    return final_score

# Auxiliary function that looks important but isn't used
def generate_audit_trace(data_map):
    trace = []
    for k, v in data_map.items():
        if isinstance(v, list):
            trace.append(f"{k}:{sum(v) % 100}")
    return '|'.join(trace)

# --- Main execution ---
if __name__ == "__main__":
    # Collect real data
    telemetry = collect_diagnostics()
    
    # Irrelevant audit log (distraction)
    logs = [
        {'ts': 1678886400000, 'level': 3, 'data': 'init'},
        {'ts': 1678886460000, 'level': 1, 'data': 'ping'}
    ]
    processed_logs = preprocess_logs(logs)  # Result unused
    
    # Health check result ignored
    health_data = system_health_check()
    
    # Define weighting scheme (business logic)
    weights = [0.4, 0.5, 0.1]  # Emphasis on throughput and latency
    
    # Evaluate system performance
    final_score = evaluate_performance(telemetry, weights)
    
    # Output target result
    print(f"Result: {final_score}")