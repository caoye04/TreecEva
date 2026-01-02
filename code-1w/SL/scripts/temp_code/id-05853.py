def evaluate_performance(data, limits):
    baseline = 0
    adjustment = 0
    penalty = 0
    bonus = 0
    temp_result = 0
    
    # Irrelevant preprocessing: normalize unused fields
    normalized = {k: v / max(data.values()) for k, v in data.items()}
    scaled = {k: int(v * 100) for k, v in normalized.items()}
    
    # Real logic begins
    compliance_count = 0
    for key, value in data.items():
        threshold = limits.get(key, 0)
        if value >= threshold:
            compliance_count += 1
            adjustment += (value - threshold) // 10
        else:
            penalty += (threshold - value) * 2
    
    # Distractor: complex but unused bitwise calculation
    mask = 0b101010
    masked_values = [v ^ mask & 0b1111 for v in data.values()]
    entropy_estimate = sum((v & 3) for v in masked_values)  # Unused
    
    # Conditional expression used
    stability = 'high' if compliance_count >= 3 else 'low'
    bonus = 50 if stability == 'high' and adjustment > 10 else 20
    
    # Secondary loop with early break
    audit_phases = ['initial', 'review', 'final']
    for phase in audit_phases:
        if phase == 'review':
            temp_result += adjustment * 2
        elif phase == 'final':
            temp_result -= penalty
            break  # Early break to mislead control flow analysis
    
    # Final computation
    base_score = sum(data.values()) // len(data)
    final_score = base_score + bonus + temp_result - penalty // 4
    
    return final_score

# Main execution
metric_data = {'throughput': 85, 'latency': 45, 'reliability': 90, 'bandwidth': 60}
thresholds = {'throughput': 70, 'latency': 50, 'reliability': 80, 'bandwidth': 55}

baseline_calc = sum(metric_data.values()) / len(metric_data)  # Red herring
interim = [x * 0.1 for x in metric_data.values()]  # Dead code path

final_score = evaluate_performance(metric_data, thresholds)
print(f"Result: {final_score}")