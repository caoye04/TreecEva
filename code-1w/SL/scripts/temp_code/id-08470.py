from itertools import combinations

# Simulate system performance metrics under varying load conditions
def analyze_workload_efficiency(requests_log, threshold=100):
    high_load_periods = 0
    total_utilization = 0.0
    peak_moment = -1
    dummy_counter = 0

    for i, req_count in enumerate(requests_log):
        if req_count > threshold:
            high_load_periods += 1
            total_utilization += req_count * 0.01
        if req_count > peak_moment:
            peak_moment = req_count
        
        # Distractor: irrelevant combinatorial counting
        dummy_counter += len(list(combinations(range(i + 1), 2))) if i >= 2 else 0

    avg_load = sum(requests_log) / len(requests_log)
    return high_load_periods, total_utilization, avg_load

# Evaluate data integrity across transmission cycles
def verify_data_consistency(transmissions):
    error_flags = 0
    correction_cycles = 0
    total_xor = 0
    
    for data_chunk in transmissions:
        chunk_value = int(data_chunk, 2)
        parity = bin(chunk_value).count('1') % 2
        if parity != 0:
            error_flags += 1
            correction_cycles += 1
        total_xor ^= chunk_value  # Bitwise tracking (semi-relevant)
    
    consistency_rate = (len(transmissions) - error_flags) / len(transmissions)
    return consistency_rate, total_xor

# Main evaluation logic
def evaluate_performance(metrics, weights):
    score_components = []
    
    # Component 1: Efficiency weight
    efficiency_data = metrics['efficiency']
    raw_efficiency_score = (efficiency_data[0] * 10) + (efficiency_data[2] * 2)
    adjusted_efficiency = raw_efficiency_score * weights[0]
    score_components.append(adjusted_efficiency)
    
    # Component 2: Consistency weight
    consistency_rate = metrics['consistency'][0]
    reliability_bonus = 5 if consistency_rate > 0.8 else 0  # Threshold bonus
    raw_consistency_score = consistency_rate * 100 + reliability_bonus
    score_components.append(raw_consistency_score * weights[1])
    
    # Component 3: Security factor (based on XOR fingerprint)
    security_base = metrics['consistency'][1]
    security_mask = 0xFF
    masked_security = (security_base & security_mask) % 25
    score_components.append(masked_security * weights[2])
    
    # Irrelevant intermediate transformation
    temp_vals = [x * 1.05 for x in score_components if x > 10]
    temp_vals = [t - 1 for t in temp_vals]  # Dead adjustment, not used
    
    final_score = sum(score_components) // 1  # Integer aggregation
    return final_score

# Input data
requests_log = [89, 105, 130, 95, 110, 140, 90, 120, 115, 100]
transmissions = ['110101', '110100', '111100', '110001', '110111',
                  '100100', '110101', '111111', '110000', '110100']

# Extract low-level metrics
efficiency_metrics = analyze_workload_efficiency(requests_log)
consistency_metrics = verify_data_consistency(transmissions)

# Package for evaluation
metrics = {
    'efficiency': efficiency_metrics,
    'consistency': consistency_metrics
}
weights = [0.3, 0.5, 0.2]  # Weight distribution across criteria

# Critical execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")