from itertools import groupby

def analyze_efficiency(metrics):
    adjusted = []
    baseline = sum(metrics) / len(metrics)
    for val in metrics:
        if val > baseline:
            adjusted.append(val * 1.1)
        else:
            adjusted.append(val * 0.95)
    return adjusted

def compute_stability_index(data):
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    avg_diff = sum(diffs) / len(diffs)
    stability = 1 / (1 + avg_diff)
    
    # Distractor: irrelevant string processing
    status_labels = ['high', 'medium', 'low']
    coded = ''.join([label.capitalize() for label in status_labels])
    code_point_sum = sum([ord(c) for c in coded if c.isalpha()])  # Unused
    
    return stability

def evaluate_performance(output, volatility):
    efficiency = output * 0.8
    penalty = volatility ** 2 * 10
    score = efficiency - penalty
    
    # Additional distractor logic
    temp_result = []
    for i in range(3):
        temp_result.append(efficiency + penalty * i)
    temp_sum = sum(temp_result)  # Not used
    
    # More distractions with string and grouping
    raw_sequence = 'aabbbcccc'
    grouped = [(k, len(list(g))) for k, g in groupby(raw_sequence)]
    group_total = sum([count for _, count in grouped])  # Irrelevant to final result
    
    return int(score)

# Main execution
productivity_data = [85, 90, 87, 92, 88]

# Apply efficiency analysis
processed_metrics = analyze_efficiency(productivity_data)
total_flow = sum(processed_metrics)

# Compute derived values
average_flow = total_flow / len(processed_metrics)
fluctuation = [abs(processed_metrics[i] - processed_metrics[i-1]) for i in range(1, len(processed_metrics))]
mean_fluctuation = sum(fluctuation) / len(fluctuation)
risk_factor = 1 / (1 + mean_fluctuation)

# Evaluate performance
final_score = evaluate_performance(average_flow, risk_factor)

# Print result
print(f"Result: {final_score}")