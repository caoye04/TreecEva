def analyze_efficiency(metrics):
    baseline = sum(metrics) / len(metrics)
    adjusted_metrics = [x for x in metrics if x > baseline]
    efficiency_ratio = len(adjusted_metrics) / len(metrics)
    return efficiency_ratio


def calculate_volatility(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    volatility_index = variance ** 0.5
    fake_adjustment = (variance + 1) * 0.5  # Distractor
    another_unused = [x * 2 for x in data if x < mean_val]  # Dead code path
    return volatility_index


def evaluate_risk_level(values, threshold=0.7):
    sorted_vals = sorted(values, reverse=True)
    top_quartile = sorted_vals[:len(sorted_vals)//4]
    avg_top = sum(top_quartile) / len(top_quartile)
    risk_flag = avg_top > threshold
    safety_buffer = 100 - avg_top * 10  # Irrelevant computation
    return 'high' if risk_flag else 'low'


def merge_indicators(efficiency, volatility, risk_profile):
    score_map = {'high': 30, 'medium': 20, 'low': 10}
    base_score = efficiency * 50
    adjustment = volatility * -15
    risk_bonus = score_map.get(risk_profile, 0)
    temp_result = base_score + adjustment  # Semi-relevant
    final_rating = temp_result + risk_bonus
    outlier_check = final_rating > 60
    penalty = 5 if outlier_check else 0
    return final_rating - penalty

# Main execution block
raw_data = [0.8, 0.6, 0.9, 0.7, 0.85, 0.65, 0.75, 0.95]
duplicate_data = raw_data.copy()
processed_set = set(duplicate_data)
filtered_slice = list(processed_set)[1:-1]
efficiency = analyze_efficiency(filtered_slice)
volatility = calculate_volatility(raw_data)
risk_category = evaluate_risk_level(raw_data)

productivity = efficiency * 100
risk_exposure = volatility * 10

# Key statement
final_score = evaluate_performance(productivity, risk_exposure)

# Helper function used above
def evaluate_performance(output, hazard):
    performance_band = 'high' if output > 75 else 'medium' if output > 60 else 'low'
    normalized_hazard = min(hazard, 10)
    deduction = normalized_hazard * 2
    base_value = {'high': 90, 'medium': 70, 'low': 50}[performance_band]
    intermediate_calc = base_value - deduction  # Relevant but not final
    cushion = 5.0  # Unused buffer
    scaling_factor = 1.0  # Distractor
    trend_analysis = [x * output for x in [0.1, 0.2]]  # Irrelevant list comprehension
    final_score_local = intermediate_calc * 0.95  # Final transformation
    return int(final_score_local)

print(f"Result: {final_score}")