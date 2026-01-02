def evaluate_performance(metrics, weights):
    # Normalize metrics to a 0-1 scale
    normalized = {k: (v - 50) / 50 for k, v in metrics.items() if v > 40}
    
    # Irrelevant computation: tracking 'peaks' that isn't used later
    peaks = [v for v in metrics.values() if v > 85]
    peak_count = len(peaks) * 1.5  # Not used in final logic

    # Weighted aggregation with conditional boosts
    base_score = sum(normalized[k] * weights[k] for k in normalized)
    
    # Apply bonus if all metrics exceed threshold
    excellence_bonus = 10 if all(v > 75 for v in metrics.values()) else 0
    
    # Simulate experience adjustment using tuple unpacking (some distraction)
    exp_factor, _ = (1.2, 'years') if metrics.get('experience', 0) > 60 else (1.0, 'none')
    adjusted_score = base_score * exp_factor + excellence_bonus
    
    # Additional distracting logic: string-based flag check
    status_str = ''.join([k[:1].upper() for k in metrics.keys()])
    multiplier_flag = 1.1 if 'E' in status_str and 'P' in status_str else 1.0
    
    # Final scoring with misleading intermediate
    temp_result = adjusted_score * multiplier_flag
    noise_offset = sum([i for i in range(len(peaks))]) * 0.1  # Minor noise, not impactful
    final_score = int(temp_result - noise_offset + 0.5)  # Rounded to nearest integer
    
    return final_score

# Main execution
metrics_data = {
    'accuracy': 92,
    'speed': 78,
    'consistency': 88,
    'experience': 65,
    'adaptability': 90
}

weights = {
    'accuracy': 0.3,
    'speed': 0.2,
    'consistency': 0.2,
    'experience': 0.15,
    'adaptability': 0.15
}

# Key statement
final_score = evaluate_performance(metrics_data, weights)
print(f"Result: {final_score}")