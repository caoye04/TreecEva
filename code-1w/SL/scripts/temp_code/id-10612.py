from itertools import combinations

# Simulate system performance metrics under varying load conditions
def generate_metrics(base_load, stress_factor):
    metrics = {}
    temp_data = []
    for i in range(1, 6):
        load = base_load * (1 + i * 0.1)
        throughput = (100 - abs(load - 50)) ** 1.1
        latency = 1000 / (throughput + 1) if throughput > 0 else 1000
        efficiency = throughput / (latency / 10)
        temp_data.append((load, throughput, latency, efficiency))
    
    # Add dummy aggregation (not used later but adds distraction)
    avg_latency = sum(item[2] for item in temp_data) / len(temp_data)
    peak_throughput = max(item[1] for item in temp_data)
    
    # Actual metric of interest
    metrics['efficiency_trend'] = [item[3] for item in temp_data]
    metrics['stability_ratio'] = (peak_throughput / avg_latency) * 0.1
    metrics['variation'] = sum(
        abs(temp_data[i][3] - temp_data[i-1][3]) 
        for i in range(1, len(temp_data))
    )
    return metrics

def analyze_variation(patterns):
    # Irrelevant pattern analyzer (dead-end function)
    count = 0
    for c in combinations(patterns, 3):
        if sum(c) % 2 == 0:
            count += 1
    return count  # Never used

def validate_stability(ratio, threshold=0.5):
    # Distractor validation that isn't actually critical
    if ratio > threshold:
        status = "stable"
    else:
        status = "unstable"
    confidence = 0.8 if status == "stable" else 0.3
    return status, confidence

def calculate_risk_adjustment(variation, efficiency_list):
    adjustment = 0
    for i, e in enumerate(efficiency_list):
        if i % 2 == 0:
            adjustment += e * 0.05
        else:
            adjustment -= variation * 0.01
    # Some red herring logic
    if adjustment < 0:
        adjustment = abs(adjustment) * 0.5
    return adjustment

def evaluate_performance(metrics, baseline):
    efficiency_trend = metrics['efficiency_trend']
    stability_ratio = metrics['stability_ratio']
    variation = metrics['variation']
    
    # Distraction: unused intermediate calculation
    trend_growth = sum(
        1 for i in range(1, len(efficiency_trend)) 
        if efficiency_trend[i] > efficiency_trend[i-1]
    )
    decay_periods = 5 - trend_growth
    
    # Core scoring logic
    base_score = sum(efficiency_trend) / len(efficiency_trend)
    stability_bonus = stability_ratio * 0.2
    risk_adjustment = calculate_risk_adjustment(variation, efficiency_trend)
    
    # Final computation chain
    raw_score = base_score + stability_bonus - (variation * 0.05)
    adjusted_score = raw_score + risk_adjustment
    
    # Normalize against baseline with damping
    final_score = (adjusted_score / baseline) * 100
    
    # Unused health check
    health_flag = 1 if final_score > 60 and stability_ratio > 0.4 else 0
    
    return final_score

# Main execution flow
baseline = 45.0
metrics = generate_metrics(base_load=40, stress_factor=1.8)

# Irrelevant combinatorial analysis
patterns = [1, 0, 1, 1, 0]
analyze_variation(patterns)  # No effect on result

# Key statement
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")