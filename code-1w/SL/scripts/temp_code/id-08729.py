def analyze_trends(values):
    trend_scores = [1 if values[i] < values[i+1] else -1 for i in range(len(values)-1)]
    return sum(trend_scores)

metric_data = [23, 45, 38, 47, 52, 49, 61]

# Irrelevant transformation (distractor)
transformed = ''.join([chr(97 + (x % 26)) for x in metric_data])

baseline = 40
above_baseline_count = len([x for x in metric_data if x > baseline])

def adjust_value(val, factor):
    if val < 50:
        return val * (1 + factor / 100)
    else:
        return val * (1 - factor / 100)

adjusted_metrics = [adjust_value(x, 5) for x in metric_data]

# Dead code path (misleading)
if len(transformed) > 100:
    dummy_result = sum(ord(c) for c in transformed)
else:
    pass  # No effect

rolling_averages = []
for i in range(len(adjusted_metrics) - 2):
    avg = (adjusted_metrics[i] + adjusted_metrics[i+1] + adjusted_metrics[i+2]) / 3
    rolling_averages.append(avg)

# Secondary analysis with partial relevance
volatility_index = sum(abs(rolling_averages[i+1] - rolling_averages[i]) for i in range(len(rolling_averages)-1))

# Core logic disguised among distractions
trend_strength = analyze_trends(metric_data)
efficiency_ratio = above_baseline_count / len(metric_data)

# Key computational step combining multiple factors
raw_score = trend_strength * efficiency_ratio * 100

# Final adjustment using list comprehension (relevant but obscured)
correction_factors = [0.95 if x > 50 else 1.05 for x in metric_data]
net_correction = sum(correction_factors[:len(rolling_averages)]) / len(rolling_averages) if rolling_averages else 1.0

final_score = int(raw_score * net_correction)

print(f"Result: {final_score}")