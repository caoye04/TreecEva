def evaluate_performance(metrics, threshold):
    # Initialize various tracking variables (some are distractions)
    total_points = 0
    bonus_awarded = False
    debug_log = []
    temp_adjustment = 0
    
    # Distractor: Precompute irrelevant stats
    avg_latency = sum(metrics.get('latency', [0])) / len(metrics.get('latency', [1])) if metrics.get('latency') else 0
    peak_memory = max(metrics.get('memory_usage', [100]))
    
    # Real logic begins: score based on throughput and error rate
    throughput = metrics.get('throughput', 0)
    error_rate = metrics.get('error_rate', 0.0)
    stability_factor = metrics.get('stability', 1.0)

    # Conditional expression for base points
    base_points = 50 if throughput >= threshold else 25
    
    # Bitwise flag check for 'high_performance' mode (XOR used to toggle logic)
    mode_flags = metrics.get('flags', 0)
    high_perf_mode = (mode_flags & 0b100) != 0
    secure_mode = (mode_flags & 0b010) != 0
    debug_mode = (mode_flags & 0b001) != 0
    
    # XOR-based anomaly detection in operational modes
    mode_anomaly = high_perf_mode ^ secure_mode ^ debug_mode
    if mode_anomaly:
        temp_adjustment -= 5

    # Use dictionary operations to map performance levels
    grade_map = {0: 'F', 1: 'D', 2: 'C', 3: 'B', 4: 'A', 5: 'S'}
    performance_grade = min(int(throughput // 20), 5)
    grade_key = performance_grade if performance_grade in grade_map else 0
    letter = grade_map.get(grade_key, 'F')
    
    # Add bonus points conditionally using nested conditionals
    if throughput > threshold * 1.3 and error_rate < 0.05:
        if stability_factor > 0.95:
            bonus_awarded = True
            total_points += 30
        elif stability_factor > 0.85:
            total_points += 15
    elif throughput > threshold:
        total_points += 10

    # Apply base points and adjustments
    total_points += base_points
    total_points += temp_adjustment
    
    # Final adjustment based on grade and mode (irrelevant debug_mode check as distractor)
    if letter in ['S', 'A'] and not debug_mode:
        total_points += 10
    
    # Dead code path - never reached due to fixed conditions above (distractor)
    if peak_memory > 1000 and False:  
        total_points -= 20

    # Key assignment statement
    final_score = int(total_points * stability_factor)

    return final_score

# Main execution
metric_data = {
    'throughput': 85,
    'error_rate': 0.03,
    'stability': 0.96,
    'flags': 0b110,  # high_perf_mode and secure_mode active
    'latency': [120, 115, 130],
    'memory_usage': [450, 470]
}
base_threshold = 70

# Execute and print result
final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")