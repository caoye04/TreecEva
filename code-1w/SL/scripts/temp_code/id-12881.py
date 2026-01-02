def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = {k: v / max(metrics.values()) for k, v in metrics.items()}
    exceeded = set()
    for metric, value in metrics.items():
        if value > thresholds.get(metric, 0):
            exceeded.add(metric)
    
    # Semi-relevant filtering
    significant = {k: v for k, v in metrics.items() if v > 50}
    
    # Core logic begins
    high_priority_count = len(exceeded.intersection(['latency', 'error_rate']))
    
    temp_debug = sum(significant.values())  # unused later, mild distractor
    
    base_score = 0
    if 'throughput' in exceeded:
        base_score += 25
    if 'memory_usage' in exceeded:
        base_score -= 10
    
    # Bitwise adjustment based on presence of multiple issues
    flag_code = 0
    for m in ['latency', 'error_rate', 'cpu_load']:
        if m in exceeded:
            flag_code |= (1 << list(['latency', 'error_rate', 'cpu_load']).index(m))
    
    # Extra computation that doesn't affect final score directly
    parity_check = bin(flag_code).count('1') % 2
    debug_snapshot = {'flag': flag_code, 'parity': parity_check}  # dead storage
    
    # Scoring adjustment using XOR-based rule
    adjustment = flag_code ^ 3  # arbitrary pattern
    if adjustment > 5:
        base_score += 15
    
    avg_significant = sum(significant.values()) / len(significant) if significant else 0
    if avg_significant > 75:
        base_score += 20
    
    # Final decision via helper
    def calculate_final_score(score, count, avg):
        modifier = 1.0
        if count >= 2:
            modifier *= 1.2
        if avg > 80:
            modifier *= 1.1
        return int(score * modifier)
    
    final_score = calculate_final_score(base_score, high_priority_count, avg_significant)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
metrics_data = {
    'latency': 85,
    'error_rate': 45,
    'throughput': 95,
    'memory_usage': 110,
    'cpu_load': 65
}
thresholds_config = {
    'latency': 80,
    'error_rate': 50,
    'throughput': 90,
    'memory_usage': 100,
    'cpu_load': 70
}

result = analyze_performance(metrics_data, thresholds_config)