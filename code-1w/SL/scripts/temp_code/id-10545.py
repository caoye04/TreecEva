def analyze_efficiency(metrics):
    base_efficiency = sum(metrics) / len(metrics)
    adjustment = 0
    if base_efficiency > 75:
        adjustment = 10
    elif base_efficiency > 60:
        adjustment = 5
    else:
        adjustment = -5
    
    # Distractor: Irrelevant computation on variance
    variance = sum((x - base_efficiency) ** 2 for x in metrics) / len(metrics)
    normalized_variance = variance / base_efficiency if base_efficiency != 0 else 0
    
    return base_efficiency + adjustment

# Simulate system health score (irrelevant to final result)
def compute_health_score(temps):
    avg_temp = sum(temps) / len(temps)
    health = 100 - abs(avg_temp - 70) * 0.5
    return int(health) if health > 80 else 80

# Core logic with mixed operations
def evaluate_performance(output_levels, risk):
    threshold_set = {x for x in output_levels if x > 50}
    penalty = 0
    
    if len(threshold_set) >= 3:
        bonus = 20
    else:
        bonus = 5
    
    # Bitwise masking for 'risk' categorization (only top 3 bits matter)
    masked_risk = (risk & 0b111000) >> 3
    
    # Conditional expression based on set membership and risk level
    multiplier = 1.5 if masked_risk < 4 and (90 in threshold_set) else 1.0
    
    # Secondary distractor calculation (unused)
    temp_analysis = [x * 1.1 for x in output_levels]
    filtered_temps = [t for t in temp_analysis if t > 60]
    avg_filtered = sum(filtered_temps) / len(filtered_temps) if filtered_temps else 0
    
    raw_score = sum(output_levels) + bonus
    final_value = raw_score * multiplier
    
    # Final adjustment using conditional expression
    final_value = final_value - 10 if masked_risk >= 6 else final_value + 5
    
    return int(final_value)

# Main execution
productivity = [85, 92, 78, 90, 88]
risk_data = 0b111010  # Binary for 58
system_temps = [68, 72, 75, 69]

# Irrelevant pre-computations
efficiency_rating = analyze_efficiency(productivity)
system_health = compute_health_score(system_temps)

# Key statement
final_score = evaluate_performance(productivity, risk_data)

print(f"Result: {final_score}")