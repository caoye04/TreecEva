def evaluate_performance(data):
    base_score = 0
    bonus_multiplier = 1.5
    penalty_factor = 0.9
    temp_result = 0
    intermediate_values = []
    
    for key, value in data.items():
        if 'response_time' in key:
            base_score += max(10 - value // 10, 0)
        elif 'error_rate' in key:
            base_score -= min(value * 5, 20)
        elif 'throughput' in key:
            temp_result += value // 5
            intermediate_values.append(temp_result)
    
    # Distractor: irrelevant computation with side storage
    stats_summary = {}
    stats_summary['count'] = len(intermediate_values)
    stats_summary['sum_temp'] = sum(intermediate_values)
    adjustment = len(intermediate_values) > 0 and stats_summary['sum_temp'] > 50
    
    # Real path: throughput contributes only if meets threshold
    throughput_bonus = 10 if temp_result >= 25 else 0
    
    # Another distractor: bitwise check that doesn't affect outcome
    flag_check = (base_score & 1) ^ 1  # parity flip, unused
    debug_flag = base_score + throughput_bonus > 40
    
    # Final score calculation - depends only on base_score and throughput_bonus
    final_score = base_score + throughput_bonus
    
    # Additional red herring: unused conditional reassignment
    if debug_flag and adjustment:
        final_score += 5  # never reached due to logic
    
    return final_score

# Data input
metric_data = {
    'response_time_avg': 35,
    'response_time_peak': 80,
    'error_rate_network': 3,
    'error_rate_storage': 4,
    'throughput_rps': 135,
    'throughput_burst': 120,
    'latency_percentile': 45  # unused key
}

final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")