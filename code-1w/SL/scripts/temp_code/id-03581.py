def analyze_efficiency(values, threshold=0.75):
    weighted_sum = 0
    scaling_factor = 1.2
    temp_adjustment = 0.0
    for i, val in enumerate(values):
        if i % 2 == 0:
            weighted_sum += val * scaling_factor
        else:
            weighted_sum += val * (scaling_factor * 0.8)
    normalized = weighted_sum / len(values)
    return normalized > threshold


def calculate_risk_index(metrics):
    base_risk = sum([m ** 0.5 for m in metrics if m > 0])
    adjustment = 0.0
    for j in range(len(metrics)):
        if metrics[j] < 0:
            adjustment -= metrics[j]
    return base_risk + adjustment


def evaluate_performance(output_levels, risk):
    baseline = 100
    penalty = 0
    boost = 0
    
    # Simulate performance tiers
    for level in output_levels:
        if level > 80:
            boost += 15
        elif level > 60:
            boost += 5
        else:
            penalty += 10
    
    adjusted_base = baseline + boost - penalty
    
    # Apply risk adjustment
    if risk > 20:
        adjusted_base *= 0.8
    elif risk < 10:
        adjusted_base *= 1.1
    
    # Irrelevant tracking variables
    status_log = []
    for idx, lvl in enumerate(output_levels):
        status_log.append(f"Day {idx}: {'High' if lvl > 70 else 'Normal'}")
    
    # Unused intermediate calculations
    avg_level = sum(output_levels) / len(output_levels)
    variance_proxy = sum((x - avg_level) ** 2 for x in output_levels) / len(output_levels)
    stability_score = 100 - variance_proxy

    return int(adjusted_base)

# Main execution
productivity = [85, 73, 90, 64, 77]
risk_metrics = [25, 18, 30, -5, 12]

is_efficient = analyze_efficiency(productivity, threshold=0.7)
risk_factor = calculate_risk_index(risk_metrics)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")