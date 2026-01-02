def analyze_trends(data, threshold=0.5):
    trends = [1 if x > threshold else -1 for x in data]
    return sum(trends)


def compute_bias(values):
    # Irrelevant helper function (dead code path)
    return sum(v ** 0.5 for v in values if v > 0) / len(values)


def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    adjustment_factor = 0.9
    temp_result = []
    
    for i, metric in enumerate(metrics):
        if metric < 0.2:
            continue  # Skip low performers
        elif metric > 0.8:
            bonus = 1.5
            temp_result.append(metric * 1.1)
        else:
            bonus = 1.0
            temp_result.append(metric)
        
        # Distractor computation with intermediate variables
        noise = (i + 1) * 0.01
        adjusted_metric = metric * adjustment_factor + noise
        weighted_sum += adjusted_metric * weights[i] * bonus
    
    # Real answer depends only on filtered weighted sum with bonuses
    outlier_check = list(filter(lambda x: x > 0.7, temp_result))
    stability_score = len(outlier_check) * 0.05
    
    final_score = int(weighted_sum * 100) + int(stability_score * 10)
    
    # Unused but plausible-looking variables to increase cognitive load
    avg_temp = sum(temp_result) / len(temp_result) if temp_result else 0
    decay_correction = sum([w / (i + 1) for i, w in enumerate(weights)])
    
    return final_score

# Main execution
raw_data = [0.1, 0.3, 0.85, 0.72, 0.91]
config_weights = [0.1, 0.2, 0.3, 0.25, 0.15]

# Trigger irrelevant analysis
_ = analyze_trends([x ** 2 for x in raw_data], threshold=0.4)

# Key statement
final_score = evaluate_performance(raw_data, config_weights)

print(f"Target result: {final_score}")